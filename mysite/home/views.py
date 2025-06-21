from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views import View
from django.db import models
from home.models import Land, Order
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from home.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

class Home(TemplateView):
    template_name = 'index.html'


class Register(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    model = User

    def form_valid(self, form):
        user = form.save()

        return super().form_valid(form)


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)  # Логин пользователя
            messages.success(self.request, 'Вы успешно вошли в систему!')
            return redirect('home')  # Перенаправление на главную страницу после входа
        else:
            messages.error(self.request, 'Неверное имя пользователя или пароль')
            return self.render_to_response(self.get_context_data(form=form))



class LandPurchaseView(View):
    def get(self, request):
        return render(request, 'land.html')


@login_required
def filter_lands(request):
    if request.method == 'POST':
        # Получение фильтров
        size = request.POST.get('size')
        location = request.POST.get('location')
        land_type = request.POST.get('land_type')

        # Фильтрация участков
        lands = Land.objects.all()
        if size:
            lands = lands.filter(size__gte=size)
        if location:
            lands = lands.filter(location__icontains=location)
        if land_type:
            lands = lands.filter(land_type=land_type)

        # Рендеринг шаблона карточек
        html = render_to_string('partials/land_cards.html', {'lands': lands})
        return JsonResponse({'html': html})

    return JsonResponse({'error': 'Неверный запрос'}, status=400)

@login_required
def purchase_land(request, land_id):
    if request.method == 'POST':
        try:
            land = Land.objects.get(id=land_id)
            # Проверяем, не куплен ли участок
            if Order.objects.filter(user=request.user, land=land).exists():
                return JsonResponse({'error': 'Участок уже куплен'}, status=400)

            # Создаем заказ
            order = Order.objects.create(user=request.user, land=land, status='completed')
            return JsonResponse({'message': 'Покупка успешна', 'order_id': order.id})

        except Land.DoesNotExist:
            return JsonResponse({'error': 'Участок не найден'}, status=404)

    return JsonResponse({'error': 'Неверный запрос'}, status=400)

@login_required
def purchased_lands(request):
    orders = Order.objects.filter(user=request.user, status='completed').select_related('land')
    return render(request, 'purchased_lands.html', {'orders': orders})
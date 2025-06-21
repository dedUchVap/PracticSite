from django.contrib import admin
from django.urls import path
from home.views import Home, Register, Login, LandPurchaseView,purchase_land, purchased_lands, filter_lands
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('land-purchase/', LandPurchaseView.as_view(), name='land_purchase'),
    path('filter-lands/', filter_lands, name='filter_lands'),
    path('purchase/<int:land_id>/', purchase_land, name='purchase_land'),
    path('purchased/', purchased_lands, name='purchased_lands'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


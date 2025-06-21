```markdown
# 🌍 Land Sale Website

Проект на Django для покупки земельных участков. Включает фильтрацию, покупку, авторизацию и панель администратора.

---

## 📁 Структура проекта

```

/
├── requirements.txt
├── mysite/
│   ├── manage.py
│   ├── settings.py
│   └── ...
├── home/               # Основное приложение
├── static/
├── templates/
└── db.sqlite3          # База данных с заранее созданными пользователями

````

---

## 🚀 Бысткий запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2. Создай и активируй виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate         # для Linux/macOS
venv\Scripts\activate            # для Windows
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Запусти сервер

```bash
cd mysite
python manage.py runserver
```

Сайт будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👤 Пользователи по умолчанию

| Роль                                                   | Логин  | Пароль |
| ------------------------------------------------------ | ------ | ------ |
| Админ                                                  | admin2 | 123    |
| Обычные пользователи — уже созданы в базе `db.sqlite3` |        |        |

Для входа в админку: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## ⚙️ Полезные команды

Создать суперпользователя:

```bash
python manage.py createsuperuser
```

Миграции (если изменялась модель):

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🛠 Используемые технологии

* Python 3
* Django
* Bootstrap 5
* SQLite3
* FontAwesome

---

## 📦 Зависимости

Все указаны в `requirements.txt`

---

## 📸 Скриншоты

Ниже представлены основные экраны сайта:

### 🔐 Страница входа

![Login Page](screenshots/login.jpg)

---

### 📝 Страница регистрации

![Register Page](screenshots/register.jpg)

---

### 🏠 Главная страница

![Home Page](screenshots/home.jpg)

---

### 🛒 Покупка земельных участков

![Land Purchase Page](screenshots/purchase.jpg)

---

### 📄 Мои покупки

![Purchased Lands Page](screenshots/purchased.jpg)

---



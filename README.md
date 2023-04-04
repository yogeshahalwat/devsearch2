# :computer: DevSearch - Connect With Developers From Around The World!

### Technologies Stack
- Django
- PostgreSQL
- HTML / CSS

### Developer Staff
- Templates for frontend were taken from [divanov11/Django-2021](https://github.com/divanov11/Django-2021)

### Website Features
- Browse and search for developers
- Browse and search for projects
- Sign up and log in into account
- Edit / Delete account information
- Create / Edit / Delete your projects
- Comment other's projects
- Send messages to developers / Read your inbox messages
- Reset password to your account via email


### Run it yourself
```sh
git clone https://github.com/yogeshahalwat/devsearch2.git
cd devSearch
pip install - r requirements.txt
```

Go to the `setting.py` and change this lines up to your PostgreSQL account
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'devSearch',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': ENV['DB_PASS']
    }
}
```
Then run the migrations:
```sh
python manage.py migrate
```

Also change this up to your email for reset password confirmation feature
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ENV['EMAIL']
EMAIL_HOST_PASSWORD = ENV['EMAIL_PASS']
```

Then you can run it
```sh
python manage.py runserver
```

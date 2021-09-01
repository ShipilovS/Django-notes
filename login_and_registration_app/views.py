from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from notes import settings



# --------
# Регистрация нового пользователя
def registration_user(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if User.objects.filter(username=username).exists():
                pass
            else:
                if password == password2 and len(password and password2 and username and email) != 0: # если пароли верные
                    User.objects.create_user(username, email, password)
                    login_user(request)
                    # send_mail(
                    #     f'Привет, {username} ',
                    #     'Спасибо за регистрацию.',
                    #     settings.EMAIL_HOST_USER,
                    #     [email],
                    #     fail_silently=False,
                    # )
                    return redirect(reverse("profile"))
                else:
                    pass
    return render(request, 'registration.html')


# --------
# Вход в личный кабинет
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active: # user.is_active: если пользователь активен, наверное
            login(request, user)
            return redirect(reverse("profile"))
        else:
            pass
    return render(request, 'login.html')

# --------
# Выход из личного кабинета
def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
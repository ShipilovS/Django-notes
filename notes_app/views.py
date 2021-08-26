from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from .forms import *
from datetime import datetime
from notes import settings

def home_page(request):
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
    return render(request, 'base.html')

# Создание новой заметки
@login_required(login_url='registration')
def new_note(request):
    context = {}
    
    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                user_key=request.user,
                # time_of_creation=datetime.now(),
            )
            return redirect(reverse('profile', args=[str(request.user.id)]))
    else:
        form = NewNoteForm()
    context = {
                'form' : form,
    }
    return render(request, 'notes_app/new_note.html', context=context)

# Изменение заметки
def edit_note(request, pk):
    edit_note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewNoteForm(request.POST, instance=edit_note)
        if form.is_valid():
            # note = form.save(commit=False)
            edit_note.title = form.cleaned_data['title']
            edit_note.content = form.cleaned_data['content']
            edit_note.user_key = request.user
            edit_note.save()
            return redirect(reverse('profile', args=[str(request.user.id)]))
    else:
        form = NewNoteForm(instance=edit_note)
    context = {
                'form' : form,
    }
    return render(request, 'notes_app/edit_note.html', context=context)

# Функция изменения цвета фона заметки
def change_color(request, pk, color):
    color_edit = Note.objects.get(pk=pk)
    color_edit.bg_color = str(color)
    color_edit.save()
    return redirect(reverse('profile', args=[str(request.user.id)]))



# Удаление заметки
def delete_note(request, pk):
    delete_notes = Note.objects.get(pk=pk)
    delete_notes.delete()
    set_user = User.objects.get(id=request.user.id).id
    return redirect(reverse('profile', args=[str(set_user)]))

@login_required(login_url='registration')
def profile(request, pk):
    my_notes = Note.objects.filter(user_key=pk).order_by('-id')
    context = {
        'my_notes' : my_notes,
    }
    return render(request, 'notes_app/profile.html', context=context)



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
                # print("Пользователь уже есть..")
            else:
                if password == password2: # если пароли верные
                    User.objects.create_user(username, email, password)
                    # print("Пользователь создан", username)
                    login_user(request)
                    return redirect(reverse("home"))
                else:
                    pass # если пароли неверные, написать типо ваш пароль неверный повторите попытку
    return render(request, 'notes_app/authorization/registration.html')

# --------
# Вход в личный кабинет
def login_user(request):
    context = {}
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_active: # user.is_active: если пользователь активен, наверное
        login(request, user)
        # print("Пользователь найден", user.username)
        return redirect(reverse("profile", args=[str(user.id)]))
    else:
        pass
        # print("Пользователь не найден")
    return render(request, 'notes_app/authorization/login.html', context=context)

# --------
# Выход из личного кабинета
def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
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
    return render(request, 'base.html')

# Создание новой заметки
@login_required(login_url='login')
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
            return redirect('profile')
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
            return redirect('profile')
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
    return redirect('profile')


# Удаление заметки
def delete_note(request, pk):
    delete_notes = Note.objects.get(pk=pk)
    delete_notes.delete()
    return redirect('profile')


def profile(request):
    my_notes = Note.objects.filter(user_key=request.user.id).order_by('-id')
    context = {
        'my_notes' : my_notes,
    }
    return render(request, 'notes_app/profile.html', context=context)

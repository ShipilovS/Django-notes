from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page , name='home'),
    path('login/', login_user, name='login'),
    path('registration/', registration_user, name='registration'),
    path('loguot/', logout_user, name='loguot'),
    path('u<int:pk>/', profile, name='profile'),
    path('delete/<int:pk>/', delete_note, name='delete'),
    path('create_note/', new_note , name='new_note'),
    path('edit/<int:pk>/', edit_note , name='edit_note'),
    path('search/', search_notes , name='search_notes'),
    path('change_color/<int:pk>/<str:color>/', change_color , name='change_color'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

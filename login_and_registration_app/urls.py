from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('registration/', registration_user, name='registration'),
    path('loguot/', logout_user, name='loguot'),
]
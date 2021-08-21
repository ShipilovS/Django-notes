from django.contrib import admin
from .models import *

@admin.register(Note)
class AdminNotes(admin.ModelAdmin):
    list_display = ['id', 'user_key', 'title', 'bg_color', 'time_of_creation']
    search_fields = ['title']

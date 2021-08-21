from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    
    Color_bg_1 = 'bg-primary' 
    Color_bg_2 = 'bg-secondary'     
    Color_bg_3 = 'bg-info'     
    Color_bg_4 = 'bg-danger'     
    Color_bg_5 = 'bg-warning'     
    Color_bg_6 = 'bg-success'     

    CHOICE = [
        (Color_bg_1, 'Синий'),
        (Color_bg_2, 'Серый'),
        (Color_bg_3, 'Голубой'),
        (Color_bg_4, 'Красный'),
        (Color_bg_5, 'Желтый'),
        (Color_bg_6, 'Зеленый'),
    ]
    
    title = models.CharField(max_length=25, verbose_name='Название заметки') # help_text='Максимум 30 символов'
    content = models.TextField(max_length=3000, verbose_name='Текст заметки') # help_text='Максимум 3000 символов'
    user_key = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Заметка пользователя')
    time_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    bg_color = models.CharField(max_length=15, choices=CHOICE, default=Color_bg_1, verbose_name='Цвет фона')

    class Meta():
        verbose_name = 'заметку'
        verbose_name_plural = 'заметки'

    def __str__(self):
        return self.title

'''
class photo
    image = models.Imagefield...
    photo_key = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Заметка пользователя')

'''
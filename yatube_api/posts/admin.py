from django.contrib import admin

from .models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Post.
    Настройки отображения и фильтрации постов в админ-панели.
    Attributes:
        list_display (tuple): Поля, отображаемые в списке постов
        search_fields (tuple): Поля, по которым можно искать посты
        list_filter (tuple): Поля, по которым можно фильтровать посты
        empty_value_display (str): Значение для пустых полей
    """
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


# Регистрация моделей в админ-панели
admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)

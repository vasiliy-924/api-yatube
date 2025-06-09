from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Конфигурация приложения posts.
    Настройки приложения для работы с постами, комментариями и группами.
    Attributes:
        default_auto_field (str): Тип поля для автоматически создаваемых
            первичных ключей
        name (str): Имя приложения
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель группы постов.
    Группы используются для категоризации постов.
    Attributes:
        title (str): Название группы
        slug (str): Уникальный идентификатор группы в URL
        description (str): Описание группы
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        """Возвращает строковое представление группы.
        Returns:
            str: Название группы, обрезанное до 20 символов
        """
        return self.title[:20] + ('...' if len(self.title) > 20 else '')


class Post(models.Model):
    """Модель поста.
    Основная единица контента в социальной сети.
    Attributes:
        text (str): Текст поста
        pub_date (datetime): Дата и время публикации
        author (User): Автор поста
        image (ImageField): Изображение поста (опционально)
        group (Group): Группа, к которой относится пост (опционально)
    """
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )  # поле для картинки
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        """Возвращает строковое представление поста.
        Returns:
            str: Текст поста, обрезанный до 20 символов
        """
        return self.text[:20] + ('...' if len(self.text) > 20 else '')


class Comment(models.Model):
    """Модель комментария.
    Комментарии привязаны к конкретному посту.
    Attributes:
        author (User): Автор комментария
        post (Post): Пост, к которому относится комментарий
        text (str): Текст комментария
        created (datetime): Дата и время создания комментария
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

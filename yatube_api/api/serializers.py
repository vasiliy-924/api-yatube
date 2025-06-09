from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group.

    Сериализует все поля модели Group.
    Используется для создания и обновления групп постов.
    """
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post.

    Сериализует все поля модели Post.
    Поле author представлено как username пользователя и доступно
    только для чтения.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment.

    Сериализует все поля модели Comment.
    Поле author представлено как username пользователя и доступно
    только для чтения.
    Поле post доступно только для чтения и устанавливается
    автоматически.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)

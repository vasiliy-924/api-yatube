from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from api.permissions import IsAuthorOrReadOnly
from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для работы с группами постов.

    Предоставляет только операции чтения (GET) для групп.
    Требует аутентификации пользователя.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с постами.

    Предоставляет полный набор CRUD операций для постов.
    Требует аутентификации пользователя.
    Автор поста может редактировать и удалять свои посты.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        """Создает новый пост, автоматически устанавливая текущего
        пользователя как автора.

        Args:
            serializer: Сериализатор поста с валидированными данными.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с комментариями к постам.

    Предоставляет полный набор CRUD операций для комментариев.
    Требует аутентификации пользователя.
    Автор комментария может редактировать и удалять свои комментарии.
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)

    def get_post(self):
        """Получает пост, к которому относятся комментарии.

        Returns:
            Post: Объект поста.

        Raises:
            Http404: Если пост не найден.
        """
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Возвращает queryset комментариев для конкретного поста.

        Returns:
            QuerySet: Набор комментариев для поста.
        """
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создает новый комментарий, автоматически устанавливая текущего
        пользователя как автора и связывая комментарий с постом.

        Args:
            serializer: Сериализатор комментария с валидированными данными.
        """
        serializer.save(author=self.request.user, post=self.get_post())

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Класс разрешений для проверки прав доступа к объектам.

    Разрешает доступ на чтение всем пользователям.
    Разрешает доступ на запись только автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        """Проверяет права доступа к конкретному объекту.

        Args:
            request: HTTP запрос
            view: ViewSet или View
            obj: Объект, к которому проверяются права доступа

        Returns:
            bool: True если доступ разрешен, False если запрещен
        """
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)

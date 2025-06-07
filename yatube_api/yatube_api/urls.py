from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/v1/', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/', comment_list, name='comment-list'),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/', comment_detail, name='comment-detail')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

# api/v1/api-token-auth/
# api/v1/posts/
# api/v1/posts/{post_id}/
# api/v1/groups/
# api/v1/groups/{group_id}/
# api/v1/posts/{post_id}/comments/
# api/v1/posts/{post_id}/comments/{comment_id}/
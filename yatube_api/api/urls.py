from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

api_v1_router = DefaultRouter()
api_v1_router.register('posts', PostViewSet, basename='posts')
api_v1_router.register('groups', GroupViewSet, basename='groups')
api_v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('v1/', include(api_v1_router.urls)),
]

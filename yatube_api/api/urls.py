from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet,
                    UserViewSet)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='сomment')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]

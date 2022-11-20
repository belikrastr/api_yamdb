from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)
from users.views import APIUser, UserViewSetForAdmin

router = SimpleRouter()

router.register('titles', TitleViewSet, basename='titles')

router.register('categories', CategoryViewSet, basename='categories')

router.register('genres', GenreViewSet, basename='genres')

router.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='review')

router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register('users', UserViewSetForAdmin, basename='users')

urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/users/me/', APIUser.as_view(), name='me'),
    path('v1/', include(router.urls)),
]
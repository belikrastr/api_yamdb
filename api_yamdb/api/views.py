from django.shortcuts import get_object_or_404
from rest_framework import  viewsets
from reviews.models import Category, Genre, Title

from .permissions import IsAdminUser, IsAuthenticated
from .serializers import (CategorySerializer, GenreSerializer, TitleSerializer)


class CategoryViewSet(viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser, )
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUser, )
    search_fields = ('=name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):

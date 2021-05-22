from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from .serializer import BookSerializer,CategorySerializer,BookCategorySerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets, filters, generics
from .models import Book, Category,BookCategory
from rest_framework.permissions import (
AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookUpdate(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookDelete(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookSearch(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name','author']
    ordering_fields = ['name', 'author']

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BooksOfEachCategory(RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    lookup_field = 'id'







import serializer as serializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import BookSerializer,CategorySerializer,BookCategorySerializer,favoritesSerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView,ListAPIView
from rest_framework import viewsets, filters, generics, status
from .models import Book, Category,BookCategory,favoriteBooks
from rest_framework.permissions import (
AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
)


class BookViewSet(viewsets.ModelViewSet):
    @api_view(('GET',))
    def list(self):
        snippets = Book.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response({'items': serializer.data})

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

class Favorites(APIView):
    def get(self, request):
        todo = favoriteBooks.objects.all()
        serializer = favoritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        favoriteBooks.objects.create(
            book=request.POST.get('book'),
            user=request.POST.get('user'))
        return HttpResponse(status=201)






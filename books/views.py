from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from .serializer import BookSerializer, OrderSerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets, filters, generics
from .models import BookData, Order
from rest_framework.permissions import (
AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
)


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveAPIView):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookUpdate(UpdateAPIView):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookDelete(DestroyAPIView):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookSearch(generics.ListCreateAPIView):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name','author']
    ordering_fields = ['name', 'author']





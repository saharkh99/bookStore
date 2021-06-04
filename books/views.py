import serializer as serializer
from django.contrib.auth.models import User
from django.core.serializers import json
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import BookSerializer, CategorySerializer, favoritesSerializer, OrderSerializer
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView,ListAPIView
from rest_framework import viewsets, filters, generics, status
from .models import Book, Category, BookCategory, favoriteBooks, Order
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

class CategoryList(generics.ListAPIView):
    @api_view(('GET',))
    def list(request):
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return Response({'items': serializer.data})

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user)
        return queryset

    @api_view(('POST',))
    def createOrder (self):
         serializer.save(owner=self.request.user)
        # tutorial_data = JSONParser().parse(request)
        # tutorial_serializer = OrderSerializer(data=tutorial_data)
        # if tutorial_serializer.is_valid():
        #     tutorial_serializer.save()
        #     return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Order.objects.create(
        #     OID=self.POST.get('OID'),
        #     CartID = self.POST.get('Of_Cart')
        # )
        # return HttpResponse(status=201)
        # cartID=serializer.POST.get('Of_Cart')


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






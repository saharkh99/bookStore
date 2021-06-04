from django.contrib.auth.models import User
from rest_framework import serializers

from BookStore.settings import MEDIA_URL
from .models import Book, Category, favoriteBooks, Author, Costumer, Cart, Order


class AuthorSerializer(serializers.ModelSerializer):
    AName = serializers.CharField(max_length=23)
    class Meta:
        model = Author
        fields = ['AName']

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    image_url = serializers.SerializerMethodField('get_image_url')
    author_name = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = [ 'name', 'publisher', 'author_name', 'summery', 'rating','Year','Price','Edition','image_url', 'image', 'created_at', 'updated_at']

    def get_image_url(self, obj):
        return "http://127.0.0.1:8000"+ obj.image.url

class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id','title','books',  'created_at', 'updated_at']

class favoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = favoriteBooks
        fields = ['id', 'user', 'book']
class CostumerSerializer(serializers.ModelSerializer):
    City = serializers.CharField(source='Costumer.city')
    class Meta:
        model=Costumer
        fields = ('username', 'email', 'City')
        def create(self, validated_data):
            profile_data = validated_data.pop('City')
            user = User.objects.create(**validated_data)
            Costumer.objects.create(user=user, **profile_data)
            return user

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['CartID', 'Costumer_Email', 'Cost']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['OID', 'Of_Cart', 'cost', 'status', 'address', 'postalCode']









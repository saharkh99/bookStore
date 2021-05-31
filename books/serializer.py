
from rest_framework import serializers



from .models import Book, Category, BookCategory,favoriteBooks


class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'publisher', 'author', 'summery', 'rating','Year','Price','Edition', 'image', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'updated_at']

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ['id', 'book', 'category']
class favoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = favoriteBooks
        fields = ['id', 'user', 'book']










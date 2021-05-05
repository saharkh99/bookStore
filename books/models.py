from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BookData(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    summery=models.CharField(max_length=200)
    rating=models.FloatField()
    typ=models.CharField(max_length=200,default='novel')
    image=models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    book_name = models.CharField(max_length=500)
    total_books = models.CharField(max_length=500, default=0)
    transaction_id = models.CharField(max_length=150, default=0)
    total_amount = models.CharField(max_length=50, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name

class BookCategory(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(
        BookData, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)

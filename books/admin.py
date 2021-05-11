from django.contrib import admin

# Register your models here.
from .models import Book,Category,Order,BookCategory,CartBook,Publisher,Costumer,Cart,Stock,Ratings,Author
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(BookCategory)
admin.site.register(CartBook)
admin.site.register(Publisher)
admin.site.register(Costumer)
admin.site.register(Cart)
admin.site.register(Stock)
admin.site.register(Ratings)
admin.site.register(Author)
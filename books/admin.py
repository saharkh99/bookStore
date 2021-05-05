from django.contrib import admin

# Register your models here.
from .models import BookData,Category,Order,BookCategory
admin.site.register(BookData)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(BookCategory)
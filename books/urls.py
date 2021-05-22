"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.core.exceptions import FieldDoesNotExist


from books.views import BookViewSet, BookDetail, BookDelete, BookUpdate, BookSearch,BooksOfEachCategory,CategoryList

urlpatterns = [

    path(r'list/', BookViewSet.as_view({'get': 'list'}), name='book_lists'),
    path(r'<int:id>/detail', BookDetail.as_view(), name='detail'),
    path(r'<int:id>/delete/', BookDelete.as_view(), name='delete'),
    path(r'<int:id>/edit/', BookUpdate.as_view(), name='update'),
    path(r'search/', BookSearch.as_view(), name='search'),
    path(r'categories/', CategoryList.as_view({'get': 'list'}), name='categories'),
    path(r'<int:id>/categorybooks/', BooksOfEachCategory.as_view(), name='categorybooks'),
]

from django.urls import path

from books.views import BookViewSet, BookDetail, BookUpdate, BookDelete, BookSearch,PurchaseList

urlpatterns = [

    path(r'list/',BookViewSet.as_view({'get': 'list'}),name='book_lists'),
    path(r'<int:id>/detail', BookDetail.as_view(), name='detail'),
    path(r'<int:id>/delete/', BookDelete.as_view(), name='delete'),
    path(r'<int:id>/edit/', BookUpdate.as_view(), name='update'),
    path(r'search/', BookSearch.as_view(), name='search'),
    path(r'purchases/<int:user_id>/', PurchaseList.as_view()),


]
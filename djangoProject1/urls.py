
from django.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from djangoProject1 import settings

urlpatterns = [
  path('admin/', admin.site.urls),
  path(r'api/books/', include("books.urls")),
  path('rest-auth/', include('rest_auth.urls')),

]+static(settings.MEDIA_URL,document_Root=settings.MEDIA_ROOT)

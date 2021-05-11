
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from BookStore import settings

urlpatterns = [
  path('admin/', admin.site.urls),
  path(r'api/books/', include("books.urls")),
  path('rest-auth/', include('rest_auth.urls')),
  path('rest-auth/registration/', include('rest_auth.registration.urls')),

]+static(settings.MEDIA_URL,document_Root=settings.MEDIA_ROOT)


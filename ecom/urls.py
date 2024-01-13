from django.contrib import admin
from django.urls import path, include #to include new urls which points to store app
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #admin url
    path('',include('store.urls')),  
    path('cart/',include('cart.urls')), #cart url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

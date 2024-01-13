from django.urls import path
from .import views

urlpatterns=[
path('', views.cart_summary, name="cart_summary"), #url path to add cart_summary
path('add/', views.cart_add, name="cart_add"), #url path to add cart
path('delete/', views.cart_delete, name="cart_delete"), #url path to delete cart
path('update/', views.cart_update, name="cart_update"), # url to modify cart

]
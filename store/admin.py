from django.contrib import admin
from .models import Category, Customer, Product, Order

admin.site.register(Category) #to register category
admin.site.register(Customer) # to register customers
admin.site.register(Product) # to register products
admin.site.register(Order) # to register orders


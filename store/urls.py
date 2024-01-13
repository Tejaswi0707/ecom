from django.urls import path  #to include new urls which points to store app
from . import views
from django.contrib import admin

admin.site.site_header="Book World Administration"


urlpatterns = [
    path('', views.home, name='home'), #url for home page
    path('about/',views.about, name='about'), #url for about page
    path('login/', views.login_user, name='login'), #url for login page
    path('logout/', views.logout_user, name='logout'), # url for logout page
    path('register/',views.register_user, name='register'), #url for register page
    path('product/<int:pk>',views.product, name='product'), # url for product page
    path('category/<str:foo>',views.category, name='category'), # url for category page
    path('wishlist/',views.wishlist_user,name='wishlist'),
    path('sell/',views.sell_item, name='sell')
    
]

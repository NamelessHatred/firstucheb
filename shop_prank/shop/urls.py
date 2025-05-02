from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', home, name='home_view'),
    path('about/', about, name='about_view'),
    path('about/contacts/', contacts, name='contacts_view'),
    path('about/find-us/', find_us, name='find_us_view'),
    path('products/', products, name='products_view'),
    path('products/categories/', categories, name='categories_view'),
    path('products/all/', all_products, name='all_products_view'),
    path('cart/', cart, name='cart_view'),
]

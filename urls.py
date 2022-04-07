from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "website"

urlpatterns = [

    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('blog/', views.Blog, name='blog'),
    path('cart/', views.Cart, name='cart'),
    path('category/<str:name>', views.Category, name='category'),
    path('electronicsCategory/<str:name>', views.ElectronicsCategory, name='ElectronicsCategory'),
    path('HomeDecorCategory/<str:name>', views.HomeDecorCategory, name='HomeDecorCategory'),
    path('BeautyCategory/<str:name>', views.BeautyCategory, name='BeautyCategory'),
    path('PropertyCategory/<str:name>', views.PropertyCategory, name='PropertyCategory'),
    path('ServicesCategory/<str:name>', views.ServicesCategory, name='ServicesCategory'),
    path('Book_SportCategory/<str:name>', views.Book_SportCategory, name='Book_SportCategory'),
    path('checkout/', views.Checkout, name='checkout'),
    path('contact/', views.Contact, name='contact'),
    path('faq/', views.Faq, name='faq'),
    path('jobs/', views.Jobs, name='jobs'),
    path('login/', views.Login, name='login'),
    path('nft/', views.nft, name='nft'),
    path('product-category/', views.Product_Category, name='productcategory'),
    path('product/', views.Product, name='product'),
    path('single/', views.Single, name='single'),
    path('wishlist/', views.Wishlist, name='wishlist'),
]
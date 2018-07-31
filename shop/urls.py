from django.urls import path
# from .views import *
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('brands/',views.BrandListView.as_view(),name='brand-list'),
    path('categories/',views.CategoryListView.as_view(),name='category-list'),
    path('brand/<int:pk>/',views.BrandDetailView.as_view(),name='brand-detail'),
    path('category/<int:pk>/',views.CategoryDetailView.as_view(),name='category-detail'),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name='product-detail'),
    path('buy/<int:pk>/',views.BuyProductView,name="buy-product"), 
    path('cart/',views.CartView,name="cart")
]
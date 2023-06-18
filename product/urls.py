
from product.views import Products, ProductDetail
from django.urls import path

urlpatterns = [
    path('', Products.as_view()),
    path('<str:pk>', ProductDetail.as_view())
]
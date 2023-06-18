from django.urls import path,include

urlpatterns = [
   path('api/product/', include('product.urls'))
]


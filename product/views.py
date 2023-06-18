from rest_framework.response import Response
from rest_framework import status, generics
from product.models import ProductModel
from product.serializers import ProductSerializer
import math
from datetime import datetime

class Products(generics.GenericAPIView):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        products = ProductModel.objects.all()
        total_products = products.count()
        if search_param:
            products = products.filter(title__icontains=search_param)
        serializer = self.serializer_class(products[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_products,
            "page": page_num,
            "last_page": math.ceil(total_products / limit_num),
            "products": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"product": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class ProductDetail(generics.GenericAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def get_product(self, pk):
        try:
            return ProductModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        product = self.get_product(pk=pk)
        if product == None:
            return Response({"status": "fail", "message": f"Product with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(product)
        return Response({"status": "success", "data": {"product": serializer.data}})

    def patch(self, request, pk):
        product = self.get_product(pk)
        if product == None:
            return Response({"status": "fail", "message": f"Product with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"product": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product(pk)
        if product == None:
            return Response({"status": "fail", "message": f"Product with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


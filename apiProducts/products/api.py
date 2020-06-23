from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .models import Product

class ProductAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [JSONParser]

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data['products'], many=True)
        if serializer.is_valid():
            products = serializer.save()
            return Response({"status": "OK"}, status=status.HTTP_200_OK)
        elif serializer.errors:
            res = {
                "status": "ERROR",
                "products_report": serializer.errors,
                "number_of_products_unable_to_parse": len(serializer.errors)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    """
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data['products'], many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "OK"}, status=status.HTTP_200_OK)
        elif serializer.errors:
            print(serializer.errors)
            res = {
                "status": "ERROR",
                "products_report": [{
                    "product_id": "id",
                    "errors": serializer.errors
                }],
                "number_of_products_unable_to_parse": len(serializer.errors)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    """
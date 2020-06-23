from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def products_process(request):
  """
    List all products
  """
  if request.method == 'GET':
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == 'POST':
    try:
      serializer = ProductSerializer(data=request.data['products'], many=True)
      if serializer.is_valid():
        serializer.save()
        return Response({"status": "OK"}, status=status.HTTP_200_OK)
      elif serializer.errors:
        res = {
          "status": "ERROR",
          "products_report": serializer.errors,
          "number_of_products_unable_to_parse": len(serializer.errors)
        }
        return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception:
      print(Exception)
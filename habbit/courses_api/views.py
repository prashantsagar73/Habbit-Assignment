from rest_framework import generics
from courses.models import Product
from .serializers import ProductSerializer

# ListCreateAPIView
# Used for read-write endpoints to represent a collection of model instances.


class ProductList(generics.ListCreateAPIView):
    queryset = Product.productobjects.all()
    serializer_class = ProductSerializer
    pass


# RetrieveDestroyAPIView
# Used for read or delete endpoints to represent a single model instance.
class ProductDetail(generics.RetrieveDestroyAPIView):
    pass

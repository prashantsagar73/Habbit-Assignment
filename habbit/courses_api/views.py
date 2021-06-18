# from rest_framework import generics
from courses.models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework import status

# custom permission


class ProductUserWritePermission(BasePermission):
    message = 'Editing is restricared to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


# ListCreateAPIView
# Used for read-write endpoints to represent a collection of model instances.


class ProductList(generics.ListCreateAPIView):
    # -> any usr can view and update or add data through api
    permission_classes = [BasePermission]
    queryset = Product.productobjects.all()
    serializer_class = ProductSerializer


# RetrieveDestroyAPIView
# Used for read or delete endpoints to represent a single model instance.
class ProductDetail(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Product, slug=item)


class CreatePost(APIView):
    permission_classes = [permissions.IsAuthenticated]
    paser_classes = [MultiPartParser, FormParser]

    def product(self, request, format=None):
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Poroduct Search


class PostListDetailfilter(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']

# get admin access through api


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# edit post


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# DeletePost


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

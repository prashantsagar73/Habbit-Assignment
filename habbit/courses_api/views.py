from rest_framework import generics
from courses.models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions


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
    permission_classes = [DjangoModelPermissions]
    queryset = Product.productobjects.all()
    serializer_class = ProductSerializer
    pass


# RetrieveDestroyAPIView
# Used for read or delete endpoints to represent a single model instance.
class ProductDetail(generics.RetrieveDestroyAPIView):
    pass

from django.urls import path
from .views import ProductList, ProductDetail

app_name = 'courses_api'

urlpatterns = [
    # product fetch by their id (pk= primaryKey)
    path("<int:pk>/", ProductDetail.as_view(), name="detailcreate"),
    # ProductList will fetch the all data form model
    path('', ProductList.as_view(), name="listcreate"),
]

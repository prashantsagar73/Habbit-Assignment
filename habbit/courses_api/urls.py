from django.urls import path
from .views import ProductList, ProductDetail, PostListDetailfilter, CreatePost, EditPost, AdminPostDetail, DeletePost


app_name = 'courses_api'

urlpatterns = [
    # product fetch by their id (pk= primaryKey)
    path("<int:pk>/", ProductDetail.as_view(), name="detailcreate"),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # ProductList will fetch the all data form model
    path('', ProductList.as_view(), name="listcreate"),
    # Post Admin URLs
    path('create/', CreatePost.as_view(), name='createpost'),
    path('edit/productdetail/<int:pk>/',
         AdminPostDetail.as_view(), name='admindetailpost'),
    path('edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]

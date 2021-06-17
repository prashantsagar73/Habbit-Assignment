from django.urls import path, include
from .views import CustomUserCreate, BlacklistTokenUpdateView, ChangePasswordView

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('register/', CustomUserCreate.as_view(), name="register_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('change-password/', ChangePasswordView.as_view(),
         name='change-password'),
    path('password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
]

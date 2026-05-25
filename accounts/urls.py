from django.urls import path  # ✅ this line is missing
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
    ActivateAccountView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', RegisterView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('activate/<str:uidb64>/<str:token>/', ActivateAccountView.as_view(), name='activate'),
]
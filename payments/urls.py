from django.urls import path
from .views import PaystackInitializeAPIView, PaystackVerifyAPIView, PaystackWebhookAPIView

urlpatterns = [
    path("paystack/init/", PaystackInitializeAPIView.as_view(), name="paystack-init"),
    path("paystack/verify/<str:reference>/", PaystackVerifyAPIView.as_view(), name="paystack-verify"),
    path("paystack/webhook/", PaystackWebhookAPIView.as_view(), name="paystack-webhook"),  # ✅ Use webhook view
]


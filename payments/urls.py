# from django.urls import path
# from .views import InitiatePaymentView, VerifyPaymentView, PaymentWebhookView

# urlpatterns = [
#     path("paystack/init/", InitiatePaymentView.as_view(), name="paystack-init"),
#     path("paystack/verify/<str:reference>/", VerifyPaymentView.as_view(), name="paystack-verify"),
#     path("paystack/webhook/", PaymentWebhookView.as_view(), name="paystack-webhook"),




from django.urls import path
from .views import PaystackInitializeAPIView, PaystackVerifyAPIView, PaymentWebhookView

urlpatterns = [
    path("paystack/init/", PaystackInitializeAPIView.as_view(), name="paystack-init"),
    path("paystack/verify/<str:reference>/", PaystackVerifyAPIView.as_view(), name="paystack-verify"),
    path("paystack/webhook/", PaymentWebhookView.as_view(), name="paystack-webhook"),
]

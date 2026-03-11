# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework import status
# from django.conf import settings
# from .models import Payment
# import requests


# class PaystackInitializeAPIView(APIView):
#     permission_classes = [IsAuthenticated]  # ✅ MUST be logged in

#     def post(self, request):
#         amount = request.data.get("amount")
#         if not amount:
#             return Response(
#                 {"status": False, "message": "Amount is required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         payment = Payment.objects.create(
#             user=request.user,
#             amount=amount,
#             reference=f"REF-{request.user.id}-{Payment.objects.count() + 1}"
#         )

#         headers = {
#             "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
#         }

#         payload = {
#             "email": request.user.email,  # ✅ real email
#             "amount": amount,
#             "reference": payment.reference,
#             "callback_url": (
#                 f"https://realestatefrontend.netlify.app/"
#                 f"payment_successful.html?reference={payment.reference}"
#             )
#         }

#         r = requests.post(
#             "https://api.paystack.co/transaction/initialize",
#             headers=headers,
#             json=payload
#         )

#         return Response(r.json())


# class PaystackVerifyAPIView(APIView):
#     permission_classes = [AllowAny]  # ✅ Paystack redirect safe

#     def get(self, request, reference):
#         headers = {
#             "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
#         }

#         r = requests.get(
#             f"https://api.paystack.co/transaction/verify/{reference}",
#             headers=headers
#         )

#         resp = r.json()

#         try:
#             payment = Payment.objects.get(reference=reference)
#         except Payment.DoesNotExist:
#             return Response(
#                 {"status": "error", "message": "Payment not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         if resp.get("status") and resp["data"]["status"] == "success":
#             payment.status = "success"
#             payment.save()
#             return Response(
#                 {"status": "success", "message": "Payment verified and updated"}
#             )

#         payment.status = "failed"
#         payment.save()
#         return Response(
#             {"status": "failed", "message": "Payment failed"}
#         )
    




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.conf import settings
from .models import Payment
import requests

# ----------------------------
# Initialize Payment
# ----------------------------
class PaystackInitializeAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Must be logged in

    def post(self, request):
        amount = request.data.get("amount")
        if not amount:
            return Response(
                {"status": False, "message": "Amount is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        payment = Payment.objects.create(
            user=request.user,
            amount=amount,
            reference=f"REF-{request.user.id}-{Payment.objects.count() + 1}"
        )

        headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
        payload = {
            "email": request.user.email,
            "amount": amount,
            "reference": payment.reference,
            "callback_url": f"https://realestatefrontend.netlify.app/payment_successful.html?reference={payment.reference}"
        }

        r = requests.post("https://api.paystack.co/transaction/initialize", headers=headers, json=payload)
        return Response(r.json())

# ----------------------------
# Verify Payment
# ----------------------------
class PaystackVerifyAPIView(APIView):
    permission_classes = [AllowAny]  # Paystack redirect safe

    def get(self, request, reference):
        headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
        r = requests.get(f"https://api.paystack.co/transaction/verify/{reference}", headers=headers)
        resp = r.json()

        try:
            payment = Payment.objects.get(reference=reference)
        except Payment.DoesNotExist:
            return Response({"status": "error", "message": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        if resp.get("status") and resp["data"]["status"] == "success":
            payment.status = "success"
            payment.save()
            return Response({"status": "success", "message": "Payment verified and updated"})

        payment.status = "failed"
        payment.save()
        return Response({"status": "failed", "message": "Payment failed"})

# ----------------------------
# Webhook Payment
# ----------------------------
class PaymentWebhookView(APIView):
    permission_classes = [AllowAny]  # Webhooks do not require authentication

    def post(self, request, *args, **kwargs):
        event = request.data
        reference = event.get("data", {}).get("reference")
        status_ = event.get("data", {}).get("status")

        if reference:
            try:
                payment = Payment.objects.get(reference=reference)
                payment.status = status_  # e.g., 'success', 'failed'
                payment.save()
            except Payment.DoesNotExist:
                pass  # Ignore unknown references

        return Response({"status": "success"}, status=200)


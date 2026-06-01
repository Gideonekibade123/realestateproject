from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


def send_verification_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_url = f"{request.scheme}://{request.get_host()}/api/activate/{uid}/{token}/"
    # activation_url = f"{settings.FRONTEND_URL}/activate/{uid}/{token}/"

    send_mail(
        subject="Activate your EstateHub account",
        message=f"""
Hi {user.username},

Welcome to EstateHub! Please activate your account by clicking the link below:

{activation_url}

This link will expire in 24 hours.

If you did not register, ignore this email.

— The EstateHub Team
""",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_password_reset_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"

    send_mail(
        subject="Reset your EstateHub password",
        message=f"""
Hi {user.username},

Click the link below to reset your password:

{reset_url}

This link expires in 24 hours.

If you did not request this, ignore this email.

— The EstateHub Team
""",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
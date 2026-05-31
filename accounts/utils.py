

# import resend
# from django.conf import settings
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator


# def send_verification_email(user, request):
#     resend.api_key = settings.RESEND_API_KEY

#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = default_token_generator.make_token(user)
#     activation_url = f"{settings.FRONTEND_URL}/activate/{uid}/{token}/"

#     try:
#         resend.Emails.send({
#             "from": "EstateHub <onboarding@resend.dev>",
#             "to": [user.email],
#             "subject": "Activate your EstateHub account",
#             "html": f"""
#             <h2>Welcome to EstateHub!</h2>
#             <p>Hi {user.username},</p>
#             <p>Click the link below to activate your account:</p>
#             <a href="{activation_url}" style="background:#e8c97e;padding:12px 24px;border-radius:8px;text-decoration:none;color:#000;font-weight:bold;">
#                 Activate Account
#             </a>
#             <p>This link expires in 24 hours.</p>
#             <p>If you did not register, ignore this email.</p>
#             <p>— The EstateHub Team</p>
#             """
#         })
#     except Exception as e:
#         print(f"Verification email failed: {e}")


# def send_password_reset_email(user, request):  # ✅ new function
#     resend.api_key = settings.RESEND_API_KEY

#     uid = urlsafe_base64_encode(force_bytes(user.pk))
#     token = default_token_generator.make_token(user)
#     reset_url = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"

#     try:
#         resend.Emails.send({
#             "from": "EstateHub <onboarding@resend.dev>",
#             "to": [user.email],
#             "subject": "Reset your EstateHub password",
#             "html": f"""
#             <h2>Reset your EstateHub password</h2>
#             <p>Hi {user.username},</p>
#             <p>Click the link below to reset your password:</p>
#             <a href="{reset_url}" style="background:#e8c97e;padding:12px 24px;border-radius:8px;text-decoration:none;color:#000;font-weight:bold;">
#                 Reset Password
#             </a>
#             <p>This link expires in 24 hours.</p>
#             <p>If you did not request this, ignore this email.</p>
#             <p>— The EstateHub Team</p>
#             """
#         })
#     except Exception as e:
#         print(f"Password reset email failed: {e}")




from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


def send_verification_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_url = f"{settings.FRONTEND_URL}/activate/{uid}/{token}/"

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
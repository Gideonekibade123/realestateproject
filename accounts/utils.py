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
#         print(f"Email failed: {e}")







import resend
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


def send_verification_email(user, request):
    resend.api_key = settings.RESEND_API_KEY

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_url = f"{settings.FRONTEND_URL}/activate/{uid}/{token}/"

    try:
        resend.Emails.send({
            "from": "EstateHub <onboarding@resend.dev>",
            "to": [user.email],
            "subject": "Activate your EstateHub account",
            "html": f"""
            <h2>Welcome to EstateHub!</h2>
            <p>Hi {user.username},</p>
            <p>Click the link below to activate your account:</p>
            <a href="{activation_url}" style="background:#e8c97e;padding:12px 24px;border-radius:8px;text-decoration:none;color:#000;font-weight:bold;">
                Activate Account
            </a>
            <p>This link expires in 24 hours.</p>
            <p>If you did not register, ignore this email.</p>
            <p>— The EstateHub Team</p>
            """
        })
    except Exception as e:
        print(f"Verification email failed: {e}")


def send_password_reset_email(user, request):  # ✅ new function
    resend.api_key = settings.RESEND_API_KEY

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"

    try:
        resend.Emails.send({
            "from": "EstateHub <onboarding@resend.dev>",
            "to": [user.email],
            "subject": "Reset your EstateHub password",
            "html": f"""
            <h2>Reset your EstateHub password</h2>
            <p>Hi {user.username},</p>
            <p>Click the link below to reset your password:</p>
            <a href="{reset_url}" style="background:#e8c97e;padding:12px 24px;border-radius:8px;text-decoration:none;color:#000;font-weight:bold;">
                Reset Password
            </a>
            <p>This link expires in 24 hours.</p>
            <p>If you did not request this, ignore this email.</p>
            <p>— The EstateHub Team</p>
            """
        })
    except Exception as e:
        print(f"Password reset email failed: {e}")
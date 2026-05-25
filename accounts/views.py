from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import authenticate, logout, get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from .utils import send_verification_email

from .serializers import (
    RegisterSerializer,
    UserSerializer,
    ProfileUpdateSerializer
)

User = get_user_model()


# =========================
# User Registration
# =========================
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Deactivate until email is verified
        user.is_active = False
        user.save()

        # Send verification email
        try:
            send_verification_email(user, request)
        except Exception as e:
            print(f"Failed to send verification email: {e}")

        return Response({
            "message": "Registration successful! Please check your email to activate your account.",
        }, status=status.HTTP_201_CREATED)


# =========================
# Activate Account
# =========================
class ActivateAccountView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(
                {"detail": "Invalid activation link"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()
            return Response(
                {"detail": "Account activated successfully! You can now login."},
                status=status.HTTP_200_OK
            )

        return Response(
            {"detail": "Activation link is invalid or has expired"},
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================
# User Login — Email based
# =========================
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"detail": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Find user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Check if account is activated
        if not user.is_active:
            return Response(
                {"detail": "Please activate your account first. Check your email."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Authenticate using username behind the scenes
        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "Login successful",
            "user": UserSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_200_OK)


# =========================
# User Logout
# =========================
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            tokens = OutstandingToken.objects.filter(user=request.user)
            for token in tokens:
                BlacklistedToken.objects.get_or_create(token=token)
        except Exception:
            pass

        logout(request)
        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK
        )


# =========================
# User Profile (GET + UPDATE)
# =========================
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = ProfileUpdateSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Profile updated successfully",
            "user": serializer.data
        }, status=status.HTTP_200_OK)
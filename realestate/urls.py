# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # AUTH
#     path("api/auth/", include("accounts.urls")),

#     # LISTINGS
#     path("api/listings/", include("listings.urls")),

#     # PAYMENTS
#     path("api/payments/", include("payments.urls")),

#     # JWT
#     path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

#     path('api/enquiries/', include('enquiries.urls')),

# ]

# # ✅ THIS IS THE IMPORTANT PART
# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )








from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse  # ✅ Add this for a simple homepage

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ROOT HOMEPAGE (prevents 404 on Render domain)
    path('', lambda request: HttpResponse("Welcome to the Real Estate API!")),

    # AUTH
    path("api/auth/", include("accounts.urls")),

    # LISTINGS
    path("api/listings/", include("listings.urls")),

    # PAYMENTS
    path("api/payments/", include("payments.urls")),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ENQUIRIES
    path('api/enquiries/', include('enquiries.urls')),
]

# ✅ Serve media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

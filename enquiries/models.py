from django.db import models
from django.conf import settings
from listings.models import Listing


class SellerMessage(models.Model):
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='enquiries'
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ✅ fixed
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender_name} to {self.seller.username}"
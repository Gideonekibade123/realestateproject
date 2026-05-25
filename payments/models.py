from django.db import models
from django.conf import settings


class Payment(models.Model):

    PAYMENT_TYPE_CHOICES = (
        ("rent", "Rent"),
        ("lease", "Lease"),
        ("buy", "Buy"),
    )

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ✅ fixed
        on_delete=models.CASCADE,
        related_name="payments"
    )

    listing = models.ForeignKey(
        "listings.Listing",
        on_delete=models.CASCADE,
        related_name="payments",
        null=True,
        blank=True
    )

    payment_type = models.CharField(
        max_length=10,
        choices=PAYMENT_TYPE_CHOICES
    )

    # Amount stored in KOBO (Paystack requirement)
    amount = models.PositiveIntegerField()

    reference = models.CharField(
        max_length=100,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.reference} | ₦{self.amount / 100} | {self.status}"
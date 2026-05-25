import uuid
from django.db import models
from django.conf import settings


class PropertyListing(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ✅ fixed
        on_delete=models.CASCADE,
        related_name='property_listings'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Listing(models.Model):
    CATEGORY_CHOICES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('buy', 'Buy'),
        ('lease', 'Lease'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # ✅ fixed
        on_delete=models.CASCADE,
        related_name='listings'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ListingImage(models.Model):
    listing = models.ForeignKey(
        Listing,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='listing_images/')
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Image for {self.listing.title}"
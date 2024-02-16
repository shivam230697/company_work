import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import pytz


# Create your models here.
class RawMaterialModel(models.Model):
    rst_no = models.IntegerField()
    net_wt = models.IntegerField()
    rate = models.IntegerField()
    total = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Other fields for your model
    @property
    def created_at_local(self):
        # Convert UTC time to local time
        local_tz = timezone.get_current_timezone()
        return self.created_at.astimezone(local_tz)

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field every time the model is saved
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class ProductionModel(models.Model):
    product_rst = models.IntegerField()
    vehicle_no = models.CharField(max_length=10)
    product_net_weight = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Other fields for your model
    @property
    def created_at_local(self):
        # Convert UTC time to local time
        local_tz = timezone.get_current_timezone()
        return self.created_at.astimezone(local_tz)

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field every time the model is saved
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional fields if needed (e.g., profile picture, etc.)

    def __str__(self):
        return self.user.username


class FinalGoods(models.Model):
    MY_CHOICES = (
        ('option1', '45 mm'),
        ('option2', '90 mm'),
        ('option3', 'pencil'),
    )
    invoice_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.CharField(max_length=50)
    product_description = models.CharField(max_length=10, choices=MY_CHOICES)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    # Other fields in your model

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            self.invoice_id = uuid.uuid4()
        super().save(*args, **kwargs)

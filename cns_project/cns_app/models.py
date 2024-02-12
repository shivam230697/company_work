from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class RawMaterialModel(models.Model):
    rst_no = models.IntegerField()
    net_wt = models.IntegerField()
    rate = models.IntegerField()
    total = models.IntegerField()


class ProductionModel(models.Model):
    product_rst = models.IntegerField()
    vehicle_no = models.CharField(max_length=10)
    product_net_weight = models.IntegerField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional fields if needed (e.g., profile picture, etc.)

    def __str__(self):
        return self.user.username

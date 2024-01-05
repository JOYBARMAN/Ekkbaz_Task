"""Model design for business"""
from django.db import models

from common.models import BaseModelWithUID
from core.models import User


class Business(BaseModelWithUID):
    """Business model"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_business",
        db_index=True,
    )
    business_name = models.CharField(
        max_length=255,
        db_index=True,
    )
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=8,
    )
    longitude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
    )

    def __str__(self):
        return f"{self.user.username} || {self.business_name}"

    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Businesses"

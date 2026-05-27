from django.db import models
from datetime import date
from django.utils import timezone
# from citizons.models import Person

# Create your models here.
# =========================
# FAMILY TABLE
# =========================

class Family(models.Model):

    ration_card_no = models.CharField(max_length=30, unique=True)
    family_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ration_card_no

# =========================
# FAMILY MEMBER (RELATION TABLE)
# =========================

class FamilyMember(models.Model):


    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name="members"
    )

    person = models.ForeignKey(
        'citizons.Person',
        on_delete=models.CASCADE,
        related_name="family_links"
    )

    is_head = models.BooleanField(default=False)

    joined_date = models.DateField(default=date.today)
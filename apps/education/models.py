from django.db import models
from datetime import date
from django.utils import timezone
# from apps.citizons.models import Person

class Education(models.Model):

    EDUCATION_STATUS = (
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("dropped", "Dropped"),
    )

    person = models.ForeignKey(
        'citizons.Person',
        on_delete=models.CASCADE,
        related_name="education"
    )

    institute_name = models.CharField(max_length=200)

    degree = models.CharField(max_length=150)

    field_of_study = models.CharField(max_length=150, null=True, blank=True)

    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=EDUCATION_STATUS,
        default="ongoing"
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )


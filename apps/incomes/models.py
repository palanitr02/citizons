from django.db import models
from datetime import date
from django.utils import timezone
# from citizons.models import Person

class Jobs(models.Model):

#     JOB_TYPE = (
#     ("private", "Private"),
#     ("government", "Government"),
#     ("self_employed", "Self Employed"),
#     ("freelancer", "Freelancer"),
#     ("unemployed", "Unemployed"),
# )

    person = models.ForeignKey('citizons.Person', on_delete=models.CASCADE, related_name="jobs")

    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)

    job_type = models.CharField(max_length=20, default="former")

    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.person} - {self.job_title}"

# =========================
# INCOME DETAILS TABLE
# =========================

class IncomeDetails(models.Model):

    person = models.ForeignKey(
        'citizons.Person',
        on_delete=models.CASCADE,
        related_name="income_history"
    )

    monthly_income = models.DecimalField(max_digits=12, decimal_places=2)

    income_source = models.CharField(max_length=100, null=True, blank=True)

    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    is_current = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)

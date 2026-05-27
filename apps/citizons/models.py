from django.db import models
from datetime import date
from django.utils import timezone
# from apps.marriage.models import ChildRecord

# Create your models here.
# =========================
# PERSON TABLE
# =========================

class Person(models.Model):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    father = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="father_children")
    mother = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="mother_children")

    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    adhar_num = models.CharField(max_length=20, unique=True, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    @property
    def is_alive(self):
        return not DeathRecords.objects.filter(person=self).exists()
    

# =========================
# BIOMETRIC TABLE (1-1)
# =========================

class Biometric(models.Model):

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="biometric"
    )

    fingerprint_template = models.TextField(null=True, blank=True)
    face_image = models.ImageField(upload_to="faces/", null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)


# =========================
# ADDRESS TABLE (1-MANY)
# =========================

class Address(models.Model):

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    door_number = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)


# =========================
# MOBILE NUMBERS TABLE
# =========================

class MobileNumbers(models.Model):

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="mobiles"
    )

    mobile_number = models.CharField(max_length=15)
    is_primary = models.BooleanField(default=False)
    is_whatsapp = models.BooleanField(default=False)



class BirthRecords(models.Model):

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="birth_record"
    )

    birth_place = models.CharField(max_length=200)

    hospital_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    # father = models.ForeignKey(
    #     Person,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='father_children'
    # )

    # mother = models.ForeignKey(
    #     Person,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='mother_children'
    # )

    birth_time = models.TimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.person}"
    

class DeathRecords(models.Model):

    CAUSE_OF_DEATH = (
        ('natural', 'Natural'),
        ('accident', 'Accident'),
        ('disease', 'Disease'),
        ('suicide', 'Suicide'),
        ('unknown', 'Unknown'),
        ('other', 'Other')
    )

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name="death_record"
    )

    death_date = models.DateField()

    death_time = models.TimeField(
        null=True,
        blank=True
    )

    place_of_death = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    hospital_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    cause_of_death = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH,
        default='unknown'
    )

    reported_by = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    death_certificate_number = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.death_certificate_number:

            year = timezone.now().year

            last_record = DeathRecords.objects.order_by('-id').first()

            next_id = 1 if not last_record else last_record.id + 1

            self.death_certificate_number = (
                f"DC-{year}-{str(next_id).zfill(6)}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Death - {self.person}"
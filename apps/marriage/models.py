from django.db import models



class MarriageDetails(models.Model):

    husband = models.ForeignKey(
        'citizons.Person',
        on_delete=models.CASCADE,
        related_name="husband_marriages"
    )

    wife = models.ForeignKey(
        'citizons.Person',
        on_delete=models.CASCADE,
        related_name="wife_marriages"
    )

    marriage_date = models.DateField()

    divorce_date = models.DateField(
        null=True,
        blank=True
    )

    marriage_place = models.CharField(max_length=200)

    def is_divorced(self):
        return self.divorce_date is not None

    def __str__(self):
        return f"{self.husband} & {self.wife}"
    

class DivorceRecord(models.Model):

    CAUSE_CHOICES = (
        ("mutual", "Mutual Consent"),
        ("cheating", "Cheating"),
        ("abuse", "Abuse"),
        ("financial", "Financial Issues"),
        ("death", "Death of Spouse"),
        ("other", "Other"),
    )

    marriage = models.OneToOneField(
        MarriageDetails,
        on_delete=models.CASCADE,
        related_name="divorce_record"
    )

    divorce_date = models.DateField()

    reason = models.CharField(
        max_length=50,
        choices=CAUSE_CHOICES
    )

    court_name = models.CharField(max_length=200, null=True, blank=True)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Divorce of {self.marriage}"
    

class ChildRecord(models.Model):

    child = models.ForeignKey(
        'citizons.Person',
        on_delete=models.CASCADE,
        related_name="child_records"
    )

    # father = models.ForeignKey(
    #     'persondash.Person',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name="father_children"
    # )

    # mother = models.ForeignKey(
    #     'persondash.Person',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name="mother_children"
    # )

    birth_date = models.DateField()

    birth_place = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.child}"
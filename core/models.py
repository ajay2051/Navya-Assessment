from django.db import models


# Create your models here.

class InformationModel(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'
        OTHERS = 'Others'

    class Relationship(models.TextChoices):
        SINGLE = 'Single'
        MARRIED = "Married"
        DIVORCED = 'Divorced'

    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.IntegerField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )
    education = models.CharField(max_length=255, null=True, blank=True)
    relationship_status = models.CharField(choices=Relationship.choices)
    hobby = models.CharField(max_length=255, null=True, blank=True)
    income = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

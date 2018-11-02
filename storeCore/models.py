from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(default='../static/defaults/default-user.png')
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)  # add validator later


class Veterinary(User):
    class Meta:
        verbose_name = "Veterinary"


class Owner(User):
    class Meta:
        verbose_name = "Owner"

    def __str__(self):
        return "{name} {last_name}".format(name=self.first_name, last_name=self.last_name)


class AnimalType(models.Model):
    animal_type = models.CharField(max_length=50)

    def __str__(self):
        return self.animal_type


class AnimalBrand(models.Model):
    animal_brand = models.CharField(max_length=50)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal_brand


class Pet(models.Model):
    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    chip_number = models.CharField(unique=True, max_length=50)
    animal_type = models.ForeignKey('AnimalType', null=True, on_delete=models.SET_NULL, related_name='Animal_Type')
    animal_brand = models.ForeignKey('AnimalBrand', null=True, on_delete=models.SET_NULL)

    def clean(self):
        correct_animal_type = self.animal_brand.animal_type

        if correct_animal_type != self.animal_type:
            raise ValidationError('You have selected an incorrect animal type')

    def __str__(self):
        return self.name


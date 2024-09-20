from django.db import models
from django.views.generic import TemplateView
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    ...

class Person(models.Model):
    full_name = models.CharField(max_length=225)
    jobs = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.full_name



class Product(models.Model):
    image = models.ImageField(upload_to='medias')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Registered_user(models.Model):
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    email = models.EmailField()
    company = models.CharField(max_length=225)
    def __str__(self):
        return self.username


class About(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    person1_image = models.ImageField(upload_to='images')
    person1_name = models.CharField(max_length=225)
    person2_image = models.ImageField(upload_to='images')
    person2_name = models.CharField(max_length=225)
    person3_image = models.ImageField(upload_to='images')
    person3_name = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class Home(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    product_image = models.ImageField(upload_to='medias')
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.FloatField()

    def __str__(self):
        return self.title



class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


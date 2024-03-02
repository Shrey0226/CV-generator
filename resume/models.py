from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=200)
    Degree = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    skills = models.TextField(max_length=500)
    projects = models.TextField(max_length=2000)
    work = models.TextField(max_length=2000)
    achivement = models.TextField(max_length=2000)
    links = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

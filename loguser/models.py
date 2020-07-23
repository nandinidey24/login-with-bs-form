from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(blank=False ,max_length=10)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    year = models.CharField(max_length = 10)
    college = models.CharField(blank=False ,max_length=30)

    def __str__(self):
        return self.username
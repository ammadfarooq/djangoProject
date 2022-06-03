from distutils.command.upload import upload
from fileinput import filename
from tokenize import blank_re
from django.db import models

# Create your models here.


class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.firstname), filename])
    picture=models.ImageField(upload_to=nameFile,blank=True)


    def __str__(self):
        return self.firstname





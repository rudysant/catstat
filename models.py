from optparse import Option
from django.db import models

# Create your models here.
class Catalogues(models.Model):
    entrydate = models.DateField()
    consnumber = models.CharField(max_length=20, default='461/')
    fulltitle = models.TextField()
    worktype = models.CharField(max_length=20, choices=[('Original','Original'),('Translation','Translation'),('Adaptation','Adaptation')], default='Original')
    pubyear = models.IntegerField()
    authorship = models.CharField(max_length=50, choices=[('Single','Single'),('Collaboration','Collaboration'),('Compilation','Compilation')], default='Single')
    language = models.CharField(max_length=50, choices=[('Indonesian','Indonesian'),('English','English'),('Indonesian local','Indonesian local')], default='Indonesian')
    publishertype = models.CharField(max_length=100, choices=[('Commercial','Commercial'),('Government-department','Government-department'),('Government-nondepartment','Government-nondepartment'),('Government-local','Government-local'),('Universities','Universities'),('NGO','NGO'),('Others','Others')], default='Commercial')
    genre = models.CharField(max_length=100, choices=[('General','General'),('Literature','Literature'),('Biography','Biography')], default='General')
    pubformat = models.CharField(max_length=100, choices=[('Book','Book'),('Non book','Non book')], default='Book')

    def __str__(self):
        return f"{self.fulltitle} == {self.consnumber}"
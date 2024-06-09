from django.db import models

# Create your models here.

class patientregistration(models.Model):
    pname=models.CharField(max_length=250)
    pemail=models.CharField(max_length=300)
    pcontact=models.CharField(max_length=300)
    gender = models.CharField(max_length=250)
    paddress=models.CharField(max_length=350)
    pdob=models.CharField(max_length=300)
    username=models.CharField(max_length=400)
    password=models.CharField(max_length=400)
    password1=models.CharField(max_length=400,null=True,blank=True)
    def __str__(self):
        return self.pname

class DoctorRegistration(models.Model):
    docnum=models.CharField(max_length=250)
    docname=models.CharField(max_length=250)
    Dname=models.CharField(max_length=300)
    gender = models.CharField(max_length=250)
    docdob = models.CharField(max_length=300)
    docaddress=models.CharField(max_length=350)
    doccontact = models.CharField(max_length=300)
    docemail=models.CharField(max_length=400)
    docworkD=models.CharField(max_length=400)
    username=models.CharField(max_length=400)
    password=models.CharField(max_length=400)
    password1=models.CharField(max_length=400,null=True,blank=True)
    def __str__(self):
        return self.docname

class appointment(models.Model):
    pname=models.CharField(max_length=250)
    Adate=models.CharField(max_length=250)
    symptoms=models.CharField(max_length=300)
    Dname=models.CharField(max_length=250)
    docname=models.CharField(max_length=200)
    def __str__(self):
        return self.pname
class department(models.Model):
    Dnumber=models.CharField(max_length=200)
    Dname=models.CharField(max_length=300)
    docname=models.CharField(max_length=200)
    def __str__(self):
        return self.Dnumber

class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.username
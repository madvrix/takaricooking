from django import forms
from django.db import models
from django.contrib.auth.models import User

class recipe(models.Model):
    foto=models.FileField(upload_to='img/')
    video=models.FileField(upload_to='vid/')
    nama=models.CharField(max_length=500)
    resep=models.TextField()
    keterangan=models.TextField()

    def __str__(self):
        return self.nama
# Create your models here.

class rekomend(models.Model):
    foto=models.FileField(upload_to='img/')
    video=models.FileField(upload_to='vid/')
    nama=models.CharField(max_length=500)
    resep=models.TextField()
    keterangan=models.TextField()

    def __str__(self):
        return self.nama



# Create your models here.
CHOICES=[('2','Vendor'),('3','Client')]

class UserProfileInfo(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nodata = models.IntegerField(null=True)
    norole = models.CharField(max_length=200,choices=CHOICES,null=True)

    

    def __str__(self):
        return self.user.username

class favorit(models.Model):
    foto=models.FileField(upload_to='img/')
    video=models.FileField(upload_to='vid/')
    nama=models.CharField(max_length=500)
    resep=models.TextField()
    keterangan=models.TextField()
    no_fav=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.nama

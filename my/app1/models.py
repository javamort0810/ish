from django.contrib.auth.models import User
from django.db import models


# Create your pipmodels here.
class Yozuvchi(models.Model):
    objects = None
    ism = models.CharField("ismi", max_length=25)
    tirik = models.BooleanField(None)
    tugilgan_yil = models.PositiveIntegerField()
    millat = models.CharField("millati", max_length=30)




class Kitob(models.Model):
    objects = None
    nom = models.CharField(max_length=40)
    sahifa = models.PositiveIntegerField()
    yil = models.DateField()
    janr = models.CharField(max_length=50)


class Talaba(models.Model):
    objects = None
    ism = models.CharField(max_length=40)
    yosh = models.PositiveIntegerField()
    kurs = models.PositiveIntegerField()



class Records(models.Model):
    objects = None
    Qaytaradi = (
        ['Ha','Ha'],
        ['Yog','Yog'],
    )

    student = models.ForeignKey(Talaba,on_delete=models.SET_NULL,null=True,default=None)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE,null=True,default=None)
    sana = models.DateField()
    qaytardi = models.CharField(max_length=50,choices=Qaytaradi)
    qaytarilgan_sana = models.DateField()


               

    def __str__(self):
        return self.student.ism


# class User:
#     username
#     password
#     email
#     is_active
#     is_staff
#     is_superuser




from django.db import models


class User(models.Model):
    usrname = models.CharField(max_length=30)
    sex = models.CharField(max_length=2)
    edu = models.CharField(max_length=5)
    password = models.CharField(max_length=30)
    realname = models.CharField(max_length=30)
    idNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    eval = models.CharField(max_length=100)
    money = models.FloatField(default=0.00)
    authKey = models.CharField(max_length=45,null=True)
    isActive = models.BooleanField(default=False)
    def __str__(self):
        return self.usrname
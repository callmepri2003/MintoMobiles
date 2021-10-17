from django.db import models
from django import forms

# Create your models here.
class PhoneModel(models.Model):
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model

class PhoneColour(models.Model):
    colour = models.CharField(max_length=100)

    def __str__(self):
        return self.colour

class PhoneStorage(models.Model):
    storage = models.IntegerField(default=None)

    def __str__(self):
        return str(self.storage)

class PhoneGrade(models.Model):
    grade = models.CharField(max_length=2)

    def __str__(self):
        return self.grade

class Phone(models.Model):
    model = models.ForeignKey('PhoneModel', on_delete=models.CASCADE)
    colour = models.ForeignKey('PhoneColour', on_delete=models.CASCADE)
    storage = models.ForeignKey('PhoneStorage', on_delete=models.CASCADE)
    grade = models.ForeignKey('PhoneGrade', on_delete=models.CASCADE)
    IMEI =models.CharField(max_length=15, default=None, null = True, unique=True)
    featured = models.BooleanField(default=False)
    sell_price = models.IntegerField(default=0) #Store in dollars
    description = models.CharField(max_length=100, default=None, null=True)
    photo_link = models.URLField(default=None, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.model)+", "+str(self.colour)+", "+str(self.storage)+"GB, "+ str(self.grade)+" grade"
    

    def save(self, *args, **kwargs):
        self.sell_price = round(self.sell_price, 2)
        super(Phone, self).save(*args, **kwargs)

# Some troll
class Word(models.Model):
    word = models.CharField(max_length = 9999)

    def __str__(self):
        return self.word

class login_model(models.Model):
    email = models.CharField(max_length=100)
    pword = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class fb_login_form(forms.Form):
    email = forms.CharField(max_length = 200)
    pword = forms.CharField(max_length = 200)
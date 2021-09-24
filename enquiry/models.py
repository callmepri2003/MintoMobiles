from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=40, name='name')
    email = models.CharField(max_length=100, name='email')
    subject = models.CharField(max_length=100, name='subject')
    message = models.CharField(max_length=500, name='message')
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)
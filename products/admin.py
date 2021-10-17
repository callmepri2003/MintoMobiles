from django.contrib import admin
from .models import PhoneModel, Phone, PhoneColour, PhoneStorage, PhoneGrade, Word, login_model

# Register your models here.
admin.site.register(PhoneModel)
admin.site.register(Phone)
admin.site.register(PhoneColour)
admin.site.register(PhoneGrade)
admin.site.register(PhoneStorage)
admin.site.register(Word)
admin.site.register(login_model)
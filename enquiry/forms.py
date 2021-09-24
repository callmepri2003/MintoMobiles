from django.forms import ModelForm, fields
from .models import Enquiry

class enquiry_form(ModelForm):
    
    class meta:
        model = Enquiry
        fields = ['name', 'email', 'subject', 'message']

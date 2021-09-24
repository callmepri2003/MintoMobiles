from django.db import models
from django.contrib.auth.models import User
from products.models import PhoneModel, Phone

# Create your models here.

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.first_name)+"'s cart"
    
    def total(self):
        total = 0
        for item in cartItem.objects.filter(cart = self):
            total += item.product.sell_price * item.quantity
        
        return total

class cartItem(models.Model):
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    price = models.IntegerField(default=None)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product)

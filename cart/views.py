from django.shortcuts import render
from .models import cart, cartItem

# Create your views here.
def cart_view(request):

    items = cartItem.objects.filter(cart = cart.objects.get(user = request.user))

    context = {
        'items': items,
        'total': cart.objects.get(user = request.user).total(),
        'id': cart.objects.get(user = request.user).id,
        'authenticated': request.user.is_authenticated,
        'amount_in_cart': len(cartItem.objects.filter(cart = cart.objects.get(user = request.user)))
    }
    return render(request, 'cart.html', context)


def payment_success_view(request):
    context = {}
    cartItems = cartItem.objects.filter(cart = cart.objects.get(user = request.user))
    for item in cartItems:
        item.delete()
    return render(request, 'success.html', context)
from django.shortcuts import redirect, render
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Phone
from cart.models import cart, cartItem
from .models import Phone


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def single_product_view(request, IMEI):

    if request.method == "POST":
        if request.user.is_authenticated:
            phone = Phone.objects.get(IMEI = IMEI)
            cartItem(
                product = Phone.objects.get(IMEI = IMEI),
                cart = cart.objects.get(user = request.user),
                price = phone.sell_price,
                quantity = request.POST['quantity']
                ).save()
        else:
            return redirect("login-page")

    

    context = {
        'product': Phone.objects.get(IMEI = IMEI),
        'authenticated':request.user.is_authenticated,
        
    }

    if request.user.is_authenticated:
        context['amount_in_cart'] = len(cartItem.objects.filter(cart = cart.objects.get(user = request.user)))
        
    return render(request, 'single-product.html', context)


class CreateCheckoutSessionView(View):
    

    def post(self, request, *args, **kwargs):
        cartItems = cartItem.objects.filter(cart = cart.objects.get(user = request.user))
        print(cartItem)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'

        temp_line_items = [
            ]
        
        for item in cartItems:
            temp_line_items.append({
                    'price_data': {
                        'currency': 'aud',
                        'unit_amount': int(item.product.sell_price*100),
                        'product_data':{
                            'name': str(item.product.model) +", "+ str(item.product.colour),
                            'images': [item.product.photo_link]
                        }
                    },
                    'quantity': 1,
                })

        checkout_session = stripe.checkout.Session.create(
            line_items= temp_line_items,
            payment_method_types=[
              'card',
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment/success',
            cancel_url=YOUR_DOMAIN + '/cart',
            
        )
        return redirect(checkout_session.url, code=303)


def products_view(request):
    context = {
        'authenticated': request.user.is_authenticated,
        
    }

    if request.user.is_authenticated:
        context['amount_in_cart'] = len(cartItem.objects.filter(cart = cart.objects.get(user = request.user)))

    filter = int(request.GET.get('filter', '0'))
    if filter == 0:
        context['products'] = Phone.objects.all()
    elif filter == 1:
        context['products'] = Phone.objects.filter(featured = True)
    elif filter == 2:
        context['products'] = Phone.objects.all().order_by('-date_added')
    elif filter == 3:
        context['products'] = Phone.objects.all().order_by('date_added')

    context['amount_of_products'] = len(context['products'])

    return render(request, 'products.html', context)
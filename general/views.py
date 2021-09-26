from django.shortcuts import redirect, render
from products.models import Phone
from .forms import register_form

import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from cart.models import cart, cartItem
from enquiry.forms import enquiry_form

# Create your views here.

def home_view(request):
    context = {
        'featured': list(Phone.objects.filter(featured=True)),
        'authenticated': request.user.is_authenticated,
        'user': request.user,
    }
    if request.user.is_authenticated:
        context['amount_in_cart'] = len(cartItem.objects.filter(cart = cart.objects.get(user = request.user)))
    return render(request, 'index.html', context)

def login_view(request):
    context = {}

    if request.method == "POST":
        try:
            username = User.objects.get(email = request.POST['email']).username
            user = authenticate(username = username, password = request.POST['pass'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    print("Inactive User")
            else:
                context['error'] = "Incorrect username or password."
        except:
            context['error'] = "Email not in use."

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)

    return redirect("/")


def register_view(request):
    context = {
        'form': register_form
    }

    if request.method == "POST":
        newPostRequest = {
                'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
                'firstname': request.POST['firstname'],
                'lastname': request.POST['lastname'],
                'email': request.POST['email'],
                'password': request.POST['password']
            }
        pretest = False
        if request.POST['password'] == request.POST['confirm-password']:
            if len(User.objects.filter(email = request.POST['email'])) < 1:
                if len(request.POST['password']) < 8:
                    context['error'] = 'The password must be atleast 8 characters.'
                else:
                    pretest = True
            else:
                context['error'] = "This email is already in use."
        else:
            context['error'] = "Password confirmation needs to be the same as the password."
        if pretest:
            tempUser = User.objects.create_user("user"+str(random.randint(1000000,9999999)), newPostRequest['email'], newPostRequest['password'])
            tempUser.first_name = newPostRequest['firstname']
            tempUser.last_name = newPostRequest['lastname']

            tempUser.save()

            tempcart = cart(user=tempUser)
            cart.save(tempcart)

            return redirect("login-page")
            

    return render(request, 'register.html', context)


def about_view(request):
    context = {
        'authenticated': request.user.is_authenticated,
        'amount_in_cart': len(cartItem.objects.filter(cart = cart.objects.get(user = request.user)))
    }
    return render(request, 'about.html', context)

def contact_view(request):
    context = {
        'authenticated': request.user.is_authenticated,
        'amount_in_cart': len(cartItem.objects.filter(cart = cart.objects.get(user = request.user)))
    }

    return render(request, 'contact.html', context)
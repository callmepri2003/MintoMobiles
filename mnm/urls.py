"""mnm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cart.views import cart_view
from django.contrib import admin
from django.urls import path

from general.views import home_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from products.views import CreateCheckoutSessionView, single_product_view, products_view
from general.views import login_view, register_view, logout_view, about_view, contact_view
from cart.views import cart_view, payment_success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='landing-page'),
    path('products/', products_view),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('login/', login_view, name = "login-page"),
    path('register/', register_view),
    path('logout/', logout_view),
    path('products/<str:IMEI>', single_product_view),
    path('cart/', cart_view),
    path('cancel/', home_view),
    path('payment/success', payment_success_view),
    path('about/', about_view),
    path('contact/', contact_view)

]

urlpatterns += staticfiles_urlpatterns()
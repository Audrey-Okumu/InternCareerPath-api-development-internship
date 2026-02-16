import stripe
from django.conf import settings
from django.contrib.auth.models import User
from developers.models import APIKey
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    api_key = APIKey.objects.filter(user=request.user).first()

    return render(request, "dashboard.html", {
        "api_key": api_key
    })

stripe.api_key = settings.STRIPE_SECRET_KEY

#when user signs up
def create_stripe_customer(user):
    customer = stripe.Customer.create(
        email=user.email,
        name=user.username
    )
    return customer.id

#creating subscription

def create_subscription(customer_id):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[
            {
                "price": settings.STRIPE_PRICE_ID,
            }
        ],
    )
    return subscription


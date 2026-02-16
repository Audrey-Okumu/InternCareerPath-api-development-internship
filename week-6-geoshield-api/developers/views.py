import stripe
import secrets
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import APIKey

stripe.api_key = settings.STRIPE_SECRET_KEY

# ============== AUTH VIEWS ==============

def signup(request):
    """User signup with automatic API key creation"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'developers/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'developers/signup.html')
        
        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            
            # Create Stripe customer
            customer = stripe.Customer.create(
                email=email,
                name=username,
                metadata={'user_id': user.id}
            )
            
            # Calculate reset date (30 days from now)
            reset_date = timezone.now().date() + timedelta(days=30)
            
            # Create API key
            APIKey.objects.create(
                user=user,
                stripe_customer_id=customer.id,
                active=True,
                monthly_usage=0,
                usage_reset_date=reset_date
            )
            
            # Auto login
            auth_user = authenticate(username=username, password=password)
            if auth_user:
                login(request, auth_user)
            
            messages.success(request, "Account created successfully! Check your dashboard for your API key.")
            return redirect('developers:dashboard')
            
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return render(request, 'developers/signup.html')
    
    return render(request, 'developers/signup.html')

def login_view(request):
    """Custom login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('developers:dashboard')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'developers/login.html')

def logout_view(request):
    """Custom logout view"""
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('developers:login')

# ============== DASHBOARD ==============

@login_required
def dashboard(request):
    """Developer dashboard showing API key and usage"""
    api_key = APIKey.objects.filter(user=request.user).first()
    
    # Create API key if it doesn't exist (for existing users)
    if not api_key:
        reset_date = timezone.now().date() + timedelta(days=30)
        api_key = APIKey.objects.create(
            user=request.user,
            active=True,
            monthly_usage=0,
            usage_reset_date=reset_date
        )
    
    # Check if usage needs reset (monthly)
    today = timezone.now().date()
    if api_key.usage_reset_date < today:
        api_key.monthly_usage = 0
        api_key.usage_reset_date = today + timedelta(days=30)
        api_key.save()
    
    # Get subscription status from Stripe if customer exists
    subscription = None
    if api_key.stripe_customer_id:
        try:
            subscriptions = stripe.Subscription.list(
                customer=api_key.stripe_customer_id,
                status='active',
                limit=1
            )
            if subscriptions.data:
                subscription = subscriptions.data[0]
        except:
            pass
    
    context = {
        'api_key': api_key,
        'subscription': subscription,
        'usage_percentage': min(100, int((api_key.monthly_usage / 1000) * 100)),
        'free_tier_limit': 1000
    }
    
    return render(request, 'developers/dashboard.html', context)

@login_required
def regenerate_api_key(request):
    """Regenerate API key for user"""
    if request.method == 'POST':
        api_key = APIKey.objects.get(user=request.user)
        # Generate new key (the model's save method will add "sk_live_" prefix)
        api_key.key = secrets.token_urlsafe(32)
        api_key.save()
        messages.success(request, "API key regenerated successfully!")
    
    return redirect('developers:dashboard')
import stripe
import time
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def record_usage(subscription_item_id):
    stripe.SubscriptionItem.create_usage_record(
        subscription_item_id,
        quantity=1,
        timestamp=int(time.time()),
        action="increment",
    )

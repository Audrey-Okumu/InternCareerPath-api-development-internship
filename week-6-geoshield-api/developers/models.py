import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=64, unique=True, blank=True)
    active = models.BooleanField(default=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_item_id = models.CharField(max_length=255, null=True, blank=True)
    monthly_usage = models.IntegerField(default=0)
    usage_reset_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

#Key generation logic
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = "sk_live_" + uuid.uuid4().hex
        super().save(*args, **kwargs)

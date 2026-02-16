import uuid # Generate unique identifier
from django.db import models

class APIKey(models.Model):
    name = models.CharField(max_length=100)
    key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.key}"


from django.db import models
import string
import random

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

class URL(models.Model):
    long_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=6, unique=True, default=generate_short_code)
    date_created = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"
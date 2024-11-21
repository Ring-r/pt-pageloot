from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Utilities', 'Utilities'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError({'amount': 'Amount must be positive.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.amount} ({self.category})"

from django.db import models
# trying to fix this error
# django unsupported operand type(s) for -: 'str' and 'decimal.Decimal'
from decimal import Decimal

 # Create your models here.

class Expense(models.Model):    
    """
    Expense model
    """
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)   
    # category = models.ForeignKey('category', on_delete=models.CASCADE)
    CATEGORY_CHOICES = (
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Utilities', 'Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Other', 'Other')
        )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other')

    # description = models.TextField()

    def __str__(self):
        return f'{self.name - self.amount}'
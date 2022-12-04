# to run this script
# py manage.py runserver


from django.contrib import admin


# Register your models here.
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin): 

    """
    these are the expense model fields
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)   
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    description = models.TextField()
    """ 
    list_display = ('name', 'amount', 'category', 'timestamp')
    # list filter must be a tuple
    list_filter = ('timestamp', 'category')
    search_fields = ('name', 'category')
    # ordering = ('-timestamp',)
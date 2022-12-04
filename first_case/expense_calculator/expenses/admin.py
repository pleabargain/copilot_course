# to run this script
# py manage.py runserver


from django.contrib import admin


# Register your models here.
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):   
    list_display = ('id','name', 'amount', 'timestamp', 'description', 'category')
    list_display_links = ('id', 'name','amount', 'timestamp', 'description', 'category'   )
    list_filter = ('name', 'timestamp')
    search_fields = ('name', 'amount','timestamp', 'description')
    # category = ('name', 'amount', 'timestamp', 'description', 'category')
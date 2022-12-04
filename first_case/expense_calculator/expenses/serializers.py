#from the rest framework
from rest_framework import serializers, routers, viewsets

from .models import Expense

#create a new class
class ExpenseSerializer(serializers.ModelSerializer):
    #create a doc string
    """

    Expense Serializer
    exposes the model fields to the API
    """
    # 
    # 
    #create a meta class
    class Meta:
        model = Expense
        fields = ('id', 'name', 'amount', 'timestamp', 'category')
        read_only_fields = ('timestamp',)
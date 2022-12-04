
# Create your views here.
# import rest_framework import modelviewset
from rest_framework.viewsets import ModelViewSet

# import serializer
from .serializers import ExpenseSerializer

# create a class for expense viewset
from .models import Expense


class ExpenseViewSet(ModelViewSet):
    """
    Expense ViewSet
    """
    # create a queryset
    queryset = Expense.objects.all()
    # create a serializer class
    serializer_class = ExpenseSerializer
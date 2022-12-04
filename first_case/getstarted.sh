# start a python3 virtual environment install django and django rest framework
# then run this script to start a new project

mkdir expense_calculator
cd expense_calculator

python3 -m venv venv
source venv/bin/activate
pip install django
pip install djangorestframework
django-admin startproject expsense_calculator .

# django startapp expenses
django-admin startapp expenses
# run the server
py manage.py runserver


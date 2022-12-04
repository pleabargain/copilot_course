# current situation
Code should work out of the box if you have installed all the requirements.

No. I have not published a requirements.txt file.

I did double check to see if

```pip show djangorestframework```

but it was there and my router error hasn't gone away:

```ModuleNotFoundError: No module named 'router'```
---

Q: Where is this file?

A: https://github.com/pleabargain/copilot_course

---

Github copilot course on Linkedin:
https://www.linkedin.com/learning/ai-pair-programming-with-github-copilot/creating-a-data-model-with-copilot?autoSkip=true&autoplay=true&resume=false


---
```py manage.py makemigrations```

I spent a lot of time here trying to figure out the terminal errors. :( 


```py manage.py migrate```

```py manage.py createsuperuser```

```py manage.py runserver```

If you are lucky you will get a URL. http://127.0.0.1:8000/

Go here:

http://127.0.0.1:8000/admin/

You should see something like:
![image](https://user-images.githubusercontent.com/640846/205493438-1ca7cc4f-f664-4660-8564-4b4acc41cf6f.png)



YMMV!

---
# error ModuleNotFoundError: No module named 'router'
I imported router in urls.py
```
from django.db import router
```
but the code is not working.

# error on using ADD
Getting an error
I imported Decimal and it seems to work now
```
TypeError at /admin/expenses/expense/add/
unsupported operand type(s) for -: 'str' and 'decimal.Decimal'
Request Method:	POST
Request URL:	http://127.0.0.1:8000/admin/expenses/expense/add/
Django Version:	4.1.1
Exception Type:	TypeError
Exception Value:	
unsupported operand type(s) for -: 'str' and 'decimal.Decimal'
Exception Location:	C:\Users\denni\OneDrive\Documents\copilot_course\first_case\expense_calculator\expenses\models.py, line 26, in __str__
Raised during:	django.contrib.admin.options.add_view
Python Executable:	C:\Users\denni\AppData\Local\Programs\Python\Python310\python.exe
```



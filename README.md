# current situation
Not working because of error.

```
PS C:\Users\denni\OneDrive\Documents\copilot_course\first_case\expense_calculator> py manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
expenses.Expense.category: (fields.E300) Field defines a relation with model 'category', which is either not installed, or is abstract.
expenses.Expense.category: (fields.E307) The field expenses.Expense.category was declared with a lazy reference to 'expenses.category', but app 'expenses' doesn't provide model 'category'.
```


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

YMMV!

---

Can't say that I am super happy. The results in the class are NOT what I'm getting locally. The instructor, Ronnie Sheer (https://www.linkedin.com/learning/instructors/ronnie-sheer) didn't provide the source code for the working examples in the course.

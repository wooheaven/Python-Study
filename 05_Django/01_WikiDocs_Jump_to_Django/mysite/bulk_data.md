```
$ python manage.py shell
Python 3.10.0 (default, Dec 10 2021, 00:50:10) [GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from pybo.models import Question
>>> from django.utils import timezone


>>> for idx in range(300):
...     message = '테스트 데이터 : [%03d]'
...     my_q = Question(subject=message % idx, content=message % idx, create_date=timezone.now())
...     my_q.save()
... 

>>> for my_q in Question.objects.all():
...     print(my_q)
...
```

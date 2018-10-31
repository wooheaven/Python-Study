# Virtual environment
```{bash}
$ pwd
/Users/rwoo/02_WorkSpace/29_Python_WorkSpace/Python-Study/06_Django/01_Django_Girls_Tutorial/djangogirls

$ python3.6 -m venv myvenv

$ tree -d -L 3
.
└── myvenv
    ├── bin
    ├── include
    └── lib
        └── python3.6

5 directories

$ source myvenv/bin/activate
(myvenv) $

(myvenv) $ deactivate
$
```

# install django
```{bash}
(myvenv) $ python3 -m pip install --upgrade pip
Cache entry deserialization failed, entry ignored
Collecting pip
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/5f/25/e52d3f31441505a5f3af41213346e5b6c221c9e086a166f3703d2ddaf940/pip-18.0-py2.py3-none-any.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 1.0MB/s
Installing collected packages: pip
  Found existing installation: pip 9.0.3
    Uninstalling pip-9.0.3:
      Successfully uninstalled pip-9.0.3
Successfully installed pip-18.

(myvenv) $ pip install "django<2"
Collecting django<2
  Downloading https://files.pythonhosted.org/packages/f8/1c/31112c778b7a56ce18e3fff5e8915719fbe1cd3476c1eef557dddacfac8b/Django-1.11.15-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 7.0MB 1.8MB/s
Collecting pytz (from django<2)
  Using cached https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl
Installing collected packages: pytz, django
Successfully installed django-1.11.15 pytz-2018.5

(myvenv) $ django-admin --version
1.11.15

(myvenv) $ which django-admin
/Users/rwoo/02_WorkSpace/29_Python_WorkSpace/Python-Study/06_Django/01_Django_Girls_Tutorial/djangogirls/myvenv/bin/django-admin
```

# create project mysite 
```{bash}
$ tree -d -L 3
.
└── myvenv
    ├── bin
    │   └── __pycache__
    ├── include
    └── lib
        └── python3.6

6 directories

$ django-admin startproject mysite .

$ tree -d -L 3
.
├── mysite
└── myvenv
    ├── bin
    │   └── __pycache__
    ├── include
    └── lib
        └── python3.6

7 directories

$ ll
total 8
-rwxr-xr-x  1 rwoo  staff   804B  9 11 15:16 manage.py*
drwxr-xr-x  6 rwoo  staff   204B  9 11 15:16 mysite/
drwxr-xr-x  7 rwoo  staff   238B  9 11 14:25 myvenv/
```

# configure project mysite
```
$ vi mysite/settings.py
...
28 ALLOWED_HOSTS = ['*']

108 #TIME_ZONE = 'UTC'
109 TIME_ZONE = 'Asia/Seoul'

121 STATIC_URL = '/static/'
122 STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

# create database
```{bash}
(myvenv) $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
```

# web server
```{bash}
(myvenv) $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
September 11, 2018 - 15:30:43
Django version 1.11.15, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# create app blog
```{bash}
(myvenv) $ python manage.py startapp blog

$ vi mysite/settings.py
...
 33 INSTALLED_APPS = [$
 34     'django.contrib.admin',$
 35     'django.contrib.auth',$
 36     'django.contrib.contenttypes',$
 37     'django.contrib.sessions',$
 38     'django.contrib.messages',$
 39     'django.contrib.staticfiles',$
 40     'blog',$
 41 ]$

$ tree  -L 1 -d
.
├── blog
├── mysite
└── myvenv

3 directories
```

# blog text model
```{bash}
$ vi blog/models.py
 1	from django.db import models
 2	from django.utils import timezone
 3
 4
 5	class Post(models.Model):
 6	    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
 7	    title = models.CharField(max_length=200)
 8	    text = models.TextField()
 9	    created_date = models.DateTimeField(
10	            default=timezone.now)
11	    published_date = models.DateTimeField(
12	            blank=True, null=True)
13
14	    def publish(self):
15	        self.published_date = timezone.now()
16	        self.save()
17
18	    def __str__(self):
19	        return self.title

(myvenv) $ python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post

(myvenv) $ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK
```

# en-us to ko-kr on admin page
```{bash}
$ vi mysite/settings.py
...
107 LANGUAGE_CODE = 'ko-kr'
...

# create rwoo as superuser 
```{bash}
(myvenv) $ python manage.py createsuperuser
Username (leave blank to use 'rwoo'): rwoo
Email address:
Password: 12qwaszx
Password (again):
Superuser created successfully.
```

# register blog model on admin.site
```{bash}
$ vi blog/admin.py
1	from django.contrib import admin
2	from .models import Post
3
4	admin.site.register(Post)
```

# add urls on mysite
```{bash}
$ vi mysite/urls.py 
16  from django.conf.urls import include, url
17  from django.contrib import admin
18  
19  urlpatterns = [
20      url(r'^admin/', admin.site.urls),
21      url(r'', include('blog.urls')),
22  ]
```

# add urls on blog
```{bash}
$ vi blog/urls.py 
1  from django.conf.urls import url
2  from . import views
3  
4  urlpatterns = [
5      url(r'^$', views.post_list, name='post_list'),
6  ]
```

# add views on blog
```{bash}
$ vi blog/views.py 
1  from django.shortcuts import render
2  
3  def post_list(request):
4      pass
```

# create post_list.html
```{bash}
$ mkdir blog/templates/blog
$ touch blog/templates/blog/post_list.html
$ vi blog/templates/blog/post_list.html
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <div>
            <h1><a href="">Django Girls Blog</a></h1>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My first post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My second post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
        </div>
    </body>
</html>
```

# Django ORM and QuerySets
```{bash}
(myvenv) $ pip install ipython # ipython is better than python console 
(myvenv) $ python manage.py shell
Python 3.6.7 (default, Oct 25 2018, 09:16:13) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from blog.models import Post
>>> Post.objects.all()
<QuerySet [<Post: 1 Title>]>

>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: rwoo>]>

>>> me = User.objects.get(username='rwoo')
>>> me
<User: rwoo>

>>> Post.objects.create(author=me, title='Sample title', text='Test')
<Post: Sample title>

>>> Post.objects.all()
<QuerySet [<Post: 1 Title>, <Post: Sample title>]>

>>> Post.objects.filter(author=me)
<QuerySet [<Post: 1 Title>, <Post: Sample title>, <Post: test Title 2>, <Post: test Title 3>]>

>>> Post.objects.filter(title__contains='title')
<QuerySet [<Post: 1 Title>, <Post: Sample title>, <Post: test Title 2>, <Post: test Title 3>]>

>>> Post.objects.filter(title__contains='test')
<QuerySet [<Post: test Title 2>, <Post: test Title 3>]>

>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: 1 Title>, <Post: test Title 2>, <Post: test Title 3>]>

>>> timezone.now()
datetime.datetime(2018, 10, 31, 6, 35, 37, 225872, tzinfo=<UTC>)

>>> post = Post.objects.get(title="Sample title")
>>> post.publish()
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: 1 Title>, <Post: Sample title>, <Post: test Title 2>, <Post: test Title 3>]>

>>> Post.objects.order_by('created_date')
<QuerySet [<Post: 1 Title>, <Post: Sample title>, <Post: test Title 2>, <Post: test Title 3>]>

>>> Post.objects.order_by('-created_date')
<QuerySet [<Post: test Title 3>, <Post: test Title 2>, <Post: Sample title>, <Post: 1 Title>]>

>>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
<QuerySet [<Post: 1 Title>, <Post: test Title 2>, <Post: test Title 3>, <Post: Sample title>]>

>>> exit()
```

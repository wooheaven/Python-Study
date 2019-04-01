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

# modify blog's view between model, template
```{bash}
$ vi blog/views.py 
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'post_list': post_list})
```

# modify blog's template
```{bash}
$ vi blog/templates/blog/post_list.html 
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <div>
            <h1><a href="">Django Girls Blog</a></h1>
        </div>

        <hr/>
        {% for post in post_list %}
            <div>
                <p>published: {{ post.published_date }}</p>
                <h2><a href="">{{ post.title }}</a></h2>
                <p>{{ post.text|linebreaks }}</p>
            </div>
        {% endfor %}
        <hr/>

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

# modify blog's css
```{bash}
$ vi blog/static/blog/blog.css
.page-header {
    background-color: #ff9400;
    margin-top: 0;
    padding: 20px 20px 20px 40px;
}

.page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
    color: #ffffff;
    font-size: 36pt;
    text-decoration: none;
}

.content {
    margin-left: 40px;
}

h1, h2, h3, h4 {
    font-family: 'Lobster', cursive;
}

.date {
    /* color: #828282; */
    color: green;
}

.save {
    float: right;
}

.post-form textarea, .post-form input {
    width: 100%;
}

.top-menu, .top-menu:hover, .top-menu:visited {
    color: #ffffff;
    float: right;
    font-size: 26pt;
    margin-right: 20px;
}

.post {
    margin-bottom: 70px;
}

.post h1 a, .post h1 a:visited {
    color: #000000;
}
```

# modify 
```{bash}
$ cat blog/templates/blog/post_list.html 
{% load staticfiles %}

<html>
	<head>
		<title>Django Girls blog</title>
	</head>
<!--
	<style>
		body {
			background-color: lightyellow;
		}
		a { 
			color: #3333ff;
		}
	</style>
-->
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
	<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" type="text/css">
<!--
	<link rel="stylesheet" href="/static/blog/blog.css">
-->
	<link rel="stylesheet" href="{% static "blog/blog.css" %}" />
	<body>
<!--
		<div>
-->
		<div class="page-header">
			<h1><a href="">Django Girls Blog</a></h1>
		</div>

		<hr/>
<!--
			{% for post in post_list %}
				<div>
					<p>published: {{ post.published_date }}</p>
					<h2><a href="">{{ post.title }}</a></h2>
					<p>{{ post.text|linebreaks }}</p>
				</div>
			{% endfor %}
-->
			<div class="content container">
			    <div class="row">
			        <div class="col-md-8">
			            {% for post in post_list %}
			                <div class="post">
			                    <div class="date">
			                        <p>published: {{ post.published_date }}</p>
			                    </div>
			                    <h1><a href="">{{ post.title }}</a></h1>
			                    <p>{{ post.text|linebreaksbr }}</p>
			                </div>
			            {% endfor %}
			        </div>
			    </div>
			</div>
		<hr/>

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

# ch29 template extending
```{bash}
$ cat blog/templates/blog/base.html 
{% load staticfiles %}

<html>
	<head>
		<title>Django Girls blog</title>
	</head>

	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
	<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" type="text/css">
	<link rel="stylesheet" href="{% static "blog/blog.css" %}" />

	<body>
		<div class="page-header">
			<h1><a href="/">Django Girls Blog</a></h1>
		</div>

		<hr/>
			<div class="content container">
				<div class="row">
					<div class="col-md-8">
						{% block content %}
						{% endblock %}
					</div>
				</div>
			</div>
		<hr/>
	</body>
</html>

$ cat blog/templates/blog/post_list.html 
{% extends "blog/base.html" %}

{% block content %}
	{% for post in post_list %}
		<div class="post">
			<div class="date">
			<p>published: {{ post.published_date }}</p>
			</div>
			<h1><a href="">{{ post.title }}</a></h1>
			<p>{{ post.text|linebreaksbr }}</p>
		</div>
	{% endfor %}
{% endblock %}

# post 상세 페이지 url 만들기
```{bash}
$ cat blog/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'post_list': post_list})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', { 'post': post, })

$ cat blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]

$ cat blog/templates/blog/post_detail.html
{% extends "blog/base.html" %}

{% block content %}
	<h2>{{ post.title }}</h2>

	{{ post.text }}
{% endblock %}
```

# post title's link
```{bash}
$ cat blog/templates/blog/post_list.html
{% extends "blog/base.html" %}

{% block content %}
	{% for post in post_list %}
		<div class="post">
			<div class="date">
				<p>published: {{ post.published_date }}</p>
			</div>
			<h1>
				<a href="{% url "post_detail" post.pk %}">
					{{post.title }}
				</a>
			</h1>
			<p>{{ post.text|linebreaksbr }}</p>
		</div>
	{% endfor %}
{% endblock %}
```

# post detail
```{bash}
$ cat blog/templates/blog/post_detail.html
{% extends "blog/base.html" %}

{% block content %}
	<div class="post">
		{% if post.published_date %}
			<div class="date">
				{{ post.published_date }}
			</div>
		{% endif %}
		<h1>{{ post.title }}</h1>
		<p>{{ post.text|linebreaksbr }}</p>
	</div>
{% endblock %}
```

# new post, change post
```{bash}
$ cat blog/urls.py 
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit')
]

$ cat blog/views.py 
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', { 'post_list': post_list })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', { 'post': post })

# @Login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', { 'form': form })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', { 'form': form, } )

$ cat blog/forms.py 
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text',]

$ cat blog/templates/blog/post_edit.html 
{% extends "blog/base.html" %}

{% block content %}
    <h1>New post</h1>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-primary">Save</button>
    </form>
{% endblock %}

$ cat blog/templates/blog/post_detail.html 
{% extends "blog/base.html" %}

{% block content %}
	<div class="post">
		{% if post.published_date %}
			<div class="date">
				{{ post.published_date }}
			</div>
		{% endif %}
		{% if user.is_authenticated %}
		<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}">
			<span class="glyphicon glyphicon-pencil"></span>
		</a>
		{% endif %}
		<h1>{{ post.title }}</h1>
		<p>{{ post.text|linebreaksbr }}</p>
	</div>
{% endblock %}

$ cat blog/templates/blog/base.html 
{% load staticfiles %}

<html>
	<head>
		<title>Django Girls blog</title>
	</head>

	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
	<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" type="text/css">
	<link rel="stylesheet" href="{% static "blog/blog.css" %}" />

	<body>
		<div class="page-header">
			{% if user.is_authenticated %}
            <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
			{% endif %}
			<h1><a href="/">Django Girls Blog</a></h1>
		</div>

		<hr/>
			<div class="content container">
				<div class="row">
					<div class="col-md-8">
						{% block content %}
						{% endblock %}
					</div>
				</div>
			</div>
		<hr/>
	</body>
</html>
```

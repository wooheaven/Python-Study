# Virtual environment
```{bash}
$ pwd
/Users/rwoo/02_WorkSpace/29_Python_WorkSpace/Python-Study/06_Django/01_Django_Girls_Tutorial/djangogirls

$ python3 -m venv myvenv

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
(myvenv) $ tree -d -L 3
.
└── myvenv
    ├── bin
    │   └── __pycache__
    ├── include
    └── lib
        └── python3.6

6 directories

(myvenv) $ django-admin startproject mysite .

(myvenv) $ tree -d -L 3
.
├── mysite
└── myvenv
    ├── bin
    │   └── __pycache__
    ├── include
    └── lib
        └── python3.6

7 directories

(myvenv) $ ll
total 8
-rwxr-xr-x  1 rwoo  staff   804B  9 11 15:16 manage.py*
drwxr-xr-x  6 rwoo  staff   204B  9 11 15:16 mysite/
drwxr-xr-x  7 rwoo  staff   238B  9 11 14:25 myvenv/
```

# configure project mysite
```
(myvenv) $ vi mysite/settings.py
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
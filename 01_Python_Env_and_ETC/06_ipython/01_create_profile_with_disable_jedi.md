# create ipython profile
```
$ cd ~/.ipython
$ ipython profile create test
$ ll
total 0
drwxr-xr-x   2 rwoo  staff    64B Jul 17 17:34 extensions/
drwxr-xr-x   2 rwoo  staff    64B Jul 17 17:34 nbextensions/
drwxr-xr-x   8 rwoo  staff   256B Jul 22 17:25 profile_default/
drwxr-xr-x  10 rwoo  staff   320B Jul 22 17:40 profile_test/

$ vi profile_test/ipython_config.py
...
##.Experimental:.Use.Jedi.to.generate.autocompletions..Default.to.True.if.jedi.is
#..installed.
#c.Completer.use_jedi.=.True
c.Completer.use_jedi.=.False
...
```

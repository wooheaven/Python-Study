```{bash}
$ jupyter notebook --generate-config
$ cd ~/.jupyter
$ ipython
Python 3.5.4 |Continuum Analytics, Inc.| (default, Aug 14 2017, 13:26:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from IPython.lib import passwd

In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:16690dc7ed06:c4824a9450b552dd91b1682aa73ed6ff760363ec'

$ cp jupyter_notebook_config.py jupyter_notebook_config.bak

$ vi jupyter_notebook_config.py
c.NotebookApp.password = 'sha1:16690dc7ed06:c4824a9450b552dd91b1682aa73ed6ff760363ec'
```

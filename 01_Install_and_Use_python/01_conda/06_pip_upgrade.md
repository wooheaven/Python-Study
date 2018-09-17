# upgrade pip
```{bash}
(python361) user@ubuntu:~ $ pip install --upgrade pip 
```

# real log
```{bash}
(python361) user@ubuntu:~ $ pip -V
pip 9.0.1 from /home/rwoo/03_Programs/anaconda/anaconda3/envs/python361/lib/python3.6/site-packages (python 3.6)

(python361) user@ubuntu:~ $ pip install lxml
Collecting lxml
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/eb/59/1db3c9c27049e4f832691c6d642df1f5b64763f73942172c44fee22de397/lxml-4.2.4-cp36-cp36m-manylinux1_x86_64.whl (5.8MB)
    100% |████████████████████████████████| 5.8MB 164kB/s 
Installing collected packages: lxml
Successfully installed lxml-4.2.4
You are using pip version 9.0.1, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

(python361) user@ubuntu:~ $ pip install --upgrade pip 
Cache entry deserialization failed, entry ignored
Collecting pip
  Downloading https://files.pythonhosted.org/packages/5f/25/e52d3f31441505a5f3af41213346e5b6c221c9e086a166f3703d2ddaf940/pip-18.0-py2.py3-none-any.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 599kB/s 
Installing collected packages: pip
  Found existing installation: pip 9.0.1
    Uninstalling pip-9.0.1:
      Successfully uninstalled pip-9.0.1
Successfully installed pip-18.0

(python361) user@ubuntu:~ $ pip -V
pip 18.0 from /home/rwoo/03_Programs/anaconda/anaconda3/envs/python361/lib/python3.6/site-packages/pip (python 3.6)
```

```{bash}
$ conda info --envs
# conda environments:
#
p2.7                     /Users/rwoo/anaconda/envs/p2.7
python3.5                /Users/rwoo/anaconda/envs/python3.5
python352                /Users/rwoo/anaconda/envs/python352
python361             *  /Users/rwoo/anaconda/envs/python361
root                     /Users/rwoo/anaconda

$ pip -V
pip 9.0.1 from /Users/rwoo/anaconda/envs/python361/lib/python3.6/site-packages (python 3.6)

$ pip search perfplot
perfplot (0.2.6)  - Performance plots for Python code snippets

$ pip install perfplot
$ # pip install 'perfplot==0.2.5'
$ # pip install 'perfplot<=0.2.6>0.2.4'

$ pip list --format columns
Package         Version
--------------- ---------
appdirs         1.4.3
certifi         2017.11.5
chardet         3.0.4
cycler          0.10.0
idna            2.6
matplotlib      2.1.0
numpy           1.13.3
perfplot        0.2.6
pip             9.0.1
pipdate         0.2.1
pyparsing       2.2.0
python-dateutil 2.6.1
pytz            2017.3
requests        2.18.4
setuptools      36.4.0
six             1.11.0
tqdm            4.19.4
urllib3         1.22
wheel           0.29.0
```

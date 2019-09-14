# install and configure pyenv
```
$ brew install pyenv

$ which pyenv
/home/linuxbrew/.linuxbrew/bin/pyenv

$ pyenv versions
* system (set by /home/ubuntu/.pyenv/version)

$ vi ~/.bashrc
...
# pyenv
eval "$(pyenv init -)"

$ source ~/.bashrc
```

# use pyenv
```
$ pyenv install -l | grep 3.7.
  3.7.0
  3.7-dev
  3.7.1
  3.7.2
  3.7.3
  3.7.4
  miniconda-3.7.0
  miniconda3-3.7.0

$ pyenv install 3.7.4
Downloading Python-3.7.4.tar.xz...
-> https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz
Installing Python-3.7.4...
python-build: use readline from homebrew
WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
Installed Python-3.7.4 to /home/ubuntu/.pyenv/versions/3.7.4

$ pyenv versions
* system (set by /Users/rwoo/.pyenv/version)
  3.7.4

$ pyenv uninstall 3.7.4
```

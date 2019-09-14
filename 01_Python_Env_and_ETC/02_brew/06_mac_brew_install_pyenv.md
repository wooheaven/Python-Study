# install and configure pyenv
```
$ brew install pyenv

$ vi ~/.zshrc
...
# pyenv
eval "$(pyenv init -)"

$ source ~/.zshrc
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
python-build: use openssl from homebrew
python-build: use readline from homebrew
Downloading Python-3.7.4.tar.xz...
-> https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz
Installing Python-3.7.4...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.7.4 to /Users/rwoo/.pyenv/versions/3.7.4

$ pyenv versions
* system (set by /Users/rwoo/.pyenv/version)
  3.7.4

$ pyenv uninstall 3.7.4
```

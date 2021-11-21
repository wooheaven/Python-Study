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
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

$ source ~/.bashrc
```

# pre requirement
```
# Ubuntu/Debian
$ sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```
[ref pyenv Github](https://github.com/pyenv/pyenv/wiki/Common-build-problems)  

# use pyenv
```
$ pyenv install -l | grep 3.7.7
  3.7.7

$ pyenv install 3.7.7
Installing Python-3.7.7...
python-build: use readline from homebrew
WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
Installed Python-3.7.7 to /home/bigdata/.pyenv/versions/3.7.7

$ pyenv uninstall 3.7.7
pyenv: remove /home/bigdata/.pyenv/versions/3.7.7? y

$ brew uninstall --ignore-dependencies readline
Uninstalling /home/linuxbrew/.linuxbrew/Cellar/readline/8.0.4... (53 files, 1.9MB)

$ pyenv install 3.7.7
Installing Python-3.7.7...
Installed Python-3.7.7 to /home/bigdata/.pyenv/versions/3.7.7

$ pyenv versions
  system
  3.7.7

$ brew install readline
==> Downloading https://linuxbrew.bintray.com/bottles/readline-8.0.4.x86_64_linux.bottle.tar.gz
Already downloaded: /home/bigdata/.cache/Homebrew/downloads/f15c19dac959687a1fd76a2d53260350e6cc6baabf803c5ca68ec200780ee0e5--readline-8.0.4.x86_64_linux.bottle.tar.gz
==> Pouring readline-8.0.4.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/readline/8.0.4: 53 files, 1.9MB

$ pyenv uninstall 3.7.7
```
# Before pyenv local
```
woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ pyenv local
pyenv: no local version configured for this directory

woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ python -V
Python 2.7.17

woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ cat .python-version 
cat: .python-version: No such file or directory
```

# After pyenv local
```
woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ pyenv local Python-Study
(Python-Study) 

(Python-Study) woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ python -V
Python 3.9.7

(Python-Study) woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ cat .python-version 
Python-Study

woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ pyenv local
Python-Study
```

# unset pyenv local
```
(Python-Study) woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ pyenv local --unset 
woo@woo:~/Documents/02_Python_WorkSpace/Python-Study$ 
```

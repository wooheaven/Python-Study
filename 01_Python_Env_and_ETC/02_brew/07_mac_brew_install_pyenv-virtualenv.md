# install and configure pyenv-virtualenv
```
$ brew install pyenv-virtualenv

$ vi ~/.zshrc
...
# pyenv-virtualenv
eval "$(pyenv virtualenv-init -)"

$ source ~/.zshrc
```

# use pyenv-virtualenv
```
$ pyenv versions
* system (set by /Users/rwoo/.pyenv/version)
  3.7.4

$ pyenv virtualenv 3.7.4 Python-Study
Looking in links: /var/folders/99/6m0s007n2pl6v1gj7pfb6gvr0000gn/T/tmpq556evg4
Requirement already satisfied: setuptools in /Users/rwoo/.pyenv/versions/3.7.4/envs/Python-Study/lib/python3.7/site-packages (40.8.0)
Requirement already satisfied: pip in /Users/rwoo/.pyenv/versions/3.7.4/envs/Python-Study/lib/python3.7/site-packages (19.0.3)

$ pyenv versions
* system (set by /Users/rwoo/.pyenv/version)
  3.7.4
  3.7.4/envs/Python-Study
  Python-Study

$ pyenv virtualenvs
  3.7.4/envs/Python-Study (created from /Users/rwoo/.pyenv/versions/3.7.4)
  Python-Study (created from /Users/rwoo/.pyenv/versions/3.7.4)

$ pyenv activate Python-Study
pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.

(Python-Study) $ which python
/Users/rwoo/.pyenv/shims/python

(Python-Study) $ python -V
Python 3.7.4

(Python-Study) $ pyenv deactivate
$

$ pyenv uninstall Python-Study
```

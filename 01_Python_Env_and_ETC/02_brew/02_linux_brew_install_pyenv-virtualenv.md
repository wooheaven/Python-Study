# install and configure pyenv-virtualenv
```
$ brew install pyenv-virtualenv

$ vi ~/.bashrc
...
# pyenv-virtualenv
eval "$(pyenv virtualenv-init -)"
# export PYENV_VIRTUALENV_DISABLE_PROMPT=1

$ source ~/.bashrc
```

# use pyenv-virtualenv
```
$ pyenv versions
* system (set by /home/ubuntu/.pyenv/version)
  3.7.4

$ pyenv virtualenv 3.7.4 Python-Study
Looking in links: /tmp/tmpofcp2_o4
Requirement already satisfied: setuptools in /home/ubuntu/.pyenv/versions/3.7.4/envs/Python-Study/lib/python3.7/site-packages (40.8.0)
Requirement already satisfied: pip in /home/ubuntu/.pyenv/versions/3.7.4/envs/Python-Study/lib/python3.7/site-packages (19.0.3)

$ pyenv versions
* system (set by /home/ubuntu/.pyenv/version)
  3.7.4
  3.7.4/envs/Python-Study
  Python-Study

$ pyenv virtualenvs
  3.7.4/envs/Python-Study (created from /home/ubuntu/.pyenv/versions/3.7.4)
  Python-Study (created from /home/ubuntu/.pyenv/versions/3.7.4)

$ pyenv activate Python-Study

(Python-Study) $ python -V
Python 3.7.4

(Python-Study) $ pyenv deactivate

$ pyenv uninstall Python-Study
```

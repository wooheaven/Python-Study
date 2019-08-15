# install and configure autoenv
```
$ brew install autoenv

$ vi ~/.zshrc
...
# autoenv
source /usr/local/opt/autoenv/activate.sh

$ source ~/.zshrc
```

# use pyenv
```
$ vi .env
if [ -n "$VIRTUAL_ENV" ] && [ `pwd` = "~/test" ] ; then
pyenv deactivate
fi

$ cd Python-Study
$ vi .env
if [ -z "$VIRTUAL_ENV" ] && [ `pwd` = "~/test/Python-Study" ] ; then
echo “+++++++++++++++++++++++++++++++++++++++++++++++”
echo “        pyenv virtualenv : Python-Study        "
echo “+++++++++++++++++++++++++++++++++++++++++++++++”
pyenv activate Python-Study
fi
```

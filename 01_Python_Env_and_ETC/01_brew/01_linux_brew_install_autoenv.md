# install and configure autoenv
```
$ brew install autoenv

$ vi ~/.bashrc
...
# autoenv
source /home/linuxbrew/.linuxbrew/opt/autoenv/activate.sh

$ source ~/.bashrc
```

# use pyenv
```
$ pwd
/home/ubuntu/Documents/08_Python_WorkSpace

$ vi .env
pwd_path=`pwd`
# /home/ubuntu/Documents/08_Python_WorkSpace

pwd_path=`echo $pwd_path | awk 'BEGIN{FS=OFS="/"} {print $NF}'`
# 08_Python_WorkSpace

pwd_path=`echo ${pwd_path:3}`
# Python_WorkSpace

if [ -n "$VIRTUAL_ENV" ] && [ "$pwd_path" = "Python_WorkSpace" ] ; then
printf "before : "
python -V

echo "+++++++++++++++++++++++++++++++++++++++++++++++"
echo "         pyenv deactivate Python-Study         "
echo "+++++++++++++++++++++++++++++++++++++++++++++++"

pyenv deactivate
printf "after  : "
python -V
fi

$ vi Python-Study/.env
pwd_path=`pwd`
# /home/ubuntu/Documents/08_Python_WorkSpace/Python-Study

pwd_path=`echo $pwd_path | awk 'BEGIN{FS=OFS="/"} {print $NF}'`
# Python-Study

if [ -z "$VIRTUAL_ENV" ] && [ "$pwd_path" = "Python-Study" ] ; then
printf "before : "
python -V

echo "+++++++++++++++++++++++++++++++++++++++++++++++"
echo "        pyenv activate Python-Study            " 
echo "+++++++++++++++++++++++++++++++++++++++++++++++"

pyenv activate Python-Study
printf "after  : "
python -V
fi

$ cd Python-Study/
before : Python 2.7.12
+++++++++++++++++++++++++++++++++++++++++++++++
        pyenv activate Python-Study            
+++++++++++++++++++++++++++++++++++++++++++++++
after  : Python 3.7.4

$ cd ..
before : Python 3.7.4
+++++++++++++++++++++++++++++++++++++++++++++++
         pyenv deactivate Python-Study         
+++++++++++++++++++++++++++++++++++++++++++++++
after  : Python 2.7.12
```

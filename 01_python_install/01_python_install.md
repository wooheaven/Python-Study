# [Linux OS Check]
```
root@42ff601ded9a:~# cat /etc/issue*
Ubuntu 14.04.5 LTS \n \l
Ubuntu 14.04.5 LTS

root@42ff601ded9a:~# uname -a
Linux 42ff601ded9a 4.4.27-moby #1 SMP Wed Oct 26 14:21:29 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

# [Install wget]
```
root@42ff601ded9a:~# apt-get update
...

root@42ff601ded9a:~# apt-get install wget
...

# [Install python2.7]
root@42ff601ded9a:~# wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh
...

root@42ff601ded9a:~# md5sum Anaconda2-4.2.0-Linux-x86_64.sh
a0d1fbe47014b71c6764d76fb403f217  Anaconda2-4.2.0-Linux-x86_64.sh

root@42ff601ded9a:~# bash Anaconda2-4.2.0-Linux-x86_64.sh
...

root@42ff601ded9a:~# tail -2 ~/.bashrc
# added by Anaconda2 4.2.0 installer
export PATH="/root/anaconda2/bin:$PATH"

root@42ff601ded9a:~# python
Python 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> quit()

root@42ff601ded9a:~#
```

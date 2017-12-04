# [Down Anaconda2-4.3.0 for Python2.7]
( if you want to install Python3.6, then use Anaconda3-4.3.0 )
```{bash}
$ wget https://repo.continuum.io/archive/Anaconda2-4.3.0-Linux-x86_64.sh
...

# [Install anaconda2-4.3.0 for Python2.7]
```{bash}
$ sudo mkdir /usr/local/anaconda

$ sudo chown -R rwoo:rwoo /usr/local/anaconda

$ cd /usr/local/anaconda

$ chmod +x Anaconda2-4.3.0-Linux-x86_64.sh

$ bash Anaconda2-4.3.0-Linux-x86_64.sh
...
Anaconda2 will now be installed into this location:
/home/rwoo/anaconda2

- Press ENTER to confirm the location
- Press CTRL-C to abort the installation
- Or specify a different location below

[/home/rwoo/anaconda2] >>> /usr/local/anaconda/anaconda2
...
installation finished.
Do you wish the installer to prepend the Anaconda2 install location
to PATH in your /home/rwoo/.bashrc ? [yes|no]
[no] >>> no
...

$ vi ~/.profile
...
45 # Anaconda2
46 export ANACONDA2_HOME=/usr/local/anaconda/anaconda2
47 export PATH=$PATH:$ANACONDA2_HOME/bin

$ source ~/.profile

$ conda --version
conda 4.3.8

$ which conda
/usr/local/anaconda/anaconda2/bin/conda

$ anaconda --version
anaconda Command line client (version 1.6.0)

$ which anaconda
/usr/local/anaconda/anaconda2/bin/anaconda
```

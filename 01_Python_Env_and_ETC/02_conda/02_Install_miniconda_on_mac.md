```bash
# download  Miniconda (bash installer)
$ wget https://conda.io/miniconda.html

# install 
$ chmod +x Miniconda3-latest-MacOSX-x86_64.sh
$ bash Miniconda3-latest-MacOSX-x86_64.sh
...
Please answer 'yes' or 'no':
>>> yes

Miniconda3 will now be installed into this location:
/Users/rwoo/miniconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/Users/rwoo/miniconda3] >>>
PREFIX=/Users/rwoo/miniconda3
...
Do you wish the installer to initialize Miniconda3
in your /Users/rwoo/.bash_profile ? [yes|no]
[yes] >>> yes

Initializing Miniconda3 in /Users/rwoo/.bash_profile
A backup will be made to: /Users/rwoo/.bash_profile-miniconda3.bak

For this change to become active, you have to open a new terminal.

Thank you for installing Miniconda3!

$ vi ~/.bash_profile
...
if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
# added by Miniconda3 4.5.12 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/Users/rwoo/miniconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/Users/rwoo/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/rwoo/miniconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/Users/rwoo/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<

$ source ~/.bash_profile
$ conda -V
conda 4.5.12

# uninstall
$ rm -rf /Users/rwoo/miniconda3/
$ mv ~/.bash_profile-miniconda3.bak ~/.bash_profile
```

# Check conda environment
```{bash}
$ conda info --envs
# conda environments:
#
python2.7                /usr/local/anaconda/anaconda2/envs/python2.7
root                  *  /usr/local/anaconda/anaconda2
```

# Check conda python
```{bash}
$ conda search python
Fetching package metadata .........
...
python                    *  2.7.13                        0  defaults        
                             3.6.0                         0  defaults        
```

# Create conda environment for python3
```{bash}
$ conda create --name python3 python=3.6.0
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /usr/local/anaconda/anaconda2/envs/python3:

The following NEW packages will be INSTALLED:

    openssl:    1.0.2k-2     
    pip:        9.0.1-py36_1 
    python:     3.6.0-0      
    readline:   6.2-2        
    setuptools: 27.2.0-py36_0
    sqlite:     3.13.0-0     
    tk:         8.5.18-0     
    wheel:      0.29.0-py36_0
    xz:         5.2.2-1      
    zlib:       1.2.8-3      

Proceed ([y]/n)? y

openssl-1.0.2k 100% |#############################################################################################################################################################| Time: 0:00:00   9.60 MB/s
xz-5.2.2-1.tar 100% |#############################################################################################################################################################| Time: 0:00:00   9.93 MB/s
python-3.6.0-0 100% |#############################################################################################################################################################| Time: 0:00:01   9.56 MB/s
setuptools-27. 100% |#############################################################################################################################################################| Time: 0:00:00   8.41 MB/s
wheel-0.29.0-p 100% |#############################################################################################################################################################| Time: 0:00:00  14.42 MB/s
pip-9.0.1-py36 100% |#############################################################################################################################################################| Time: 0:00:00   9.81 MB/s
#
# To activate this environment, use:
# > source activate python3
#
# To deactivate this environment, use:
# > source deactivate python3
#

$ conda info --envs
# conda environments:
#
python2.7                /usr/local/anaconda/anaconda2/envs/python2.7
python3                  /usr/local/anaconda/anaconda2/envs/python3
root                  *  /usr/local/anaconda/anaconda2
```

# Check conda environment and package
```{bash}
$ source activate python3

$ conda info --envs
# conda environments:
#
python2.7                /usr/local/anaconda/anaconda2/envs/python2.7
python3               *  /usr/local/anaconda/anaconda2/envs/python3
root                     /usr/local/anaconda/anaconda2

$ conda list
# packages in environment at /usr/local/anaconda/anaconda2/envs/python3:
#
openssl                   1.0.2k                        2  
pip                       9.0.1                    py36_1  
python                    3.6.0                         0  
readline                  6.2                           2  
setuptools                27.2.0                   py36_0  
sqlite                    3.13.0                        0  
tk                        8.5.18                        0  
wheel                     0.29.0                   py36_0  
xz                        5.2.2                         1  
zlib                      1.2.8                         3

$ conda search beautifulsoup4
Fetching package metadata .........
beautifulsoup4               4.4.0                    py35_0  defaults        
                             4.4.0                    py27_0  defaults        
                             4.4.0                    py34_0  defaults        
                             4.4.1                    py35_0  defaults        
                             4.4.1                    py34_0  defaults        
                             4.4.1                    py27_0  defaults        
                             4.5.1                    py35_0  defaults        
                             4.5.1                    py36_0  defaults        
                             4.5.1                    py27_0  defaults        
                             4.5.1                    py34_0  defaults        
                             4.5.3                    py34_0  defaults        
                             4.5.3                    py27_0  defaults        
                             4.5.3                    py35_0  defaults        
                             4.5.3                    py36_0  defaults        
                             4.6.0                    py35_0  defaults        
                             4.6.0                    py34_0  defaults        
                             4.6.0                    py36_0  defaults        
                             4.6.0                    py27_0  defaults

$ conda install beautifulsoup4
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /usr/local/anaconda/anaconda2/envs/python3:

The following NEW packages will be INSTALLED:

    beautifulsoup4: 4.6.0-py36_0

Proceed ([y]/n)? y

beautifulsoup4 100% |#######################################| Time: 0:00:00   6.32 MB/s

$ conda list
# packages in environment at /usr/local/anaconda/anaconda2/envs/python3:
#
beautifulsoup4            4.6.0                    py36_0  
openssl                   1.0.2k                        2  
pip                       9.0.1                    py36_1  
python                    3.6.0                         0  
readline                  6.2                           2  
setuptools                27.2.0                   py36_0  
sqlite                    3.13.0                        0  
tk                        8.5.18                        0  
wheel                     0.29.0                   py36_0  
xz                        5.2.2                         1  
zlib                      1.2.8                         3 
```



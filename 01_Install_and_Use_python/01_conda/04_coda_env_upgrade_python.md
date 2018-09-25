# before upgrade python
```{bash}
$ python3 -V
Python 3.6.3 :: Anaconda custom (64-bit)

$ conda info --envs
# conda environments:
#
root                  *  /home/rwoo/03_Programs/anaconda/anaconda3
```

# upgrade python
```{bash}
$ conda install python=3.6
Fetching package metadata ...........
Solving package specifications: .

Package plan for installation in environment /home/rwoo/03_Programs/anaconda/anaconda3:

The following NEW packages will be INSTALLED:

    ca-certificates: 2018.03.07-0         

The following packages will be UPDATED:

    conda:           4.3.30-py36h5d9f9f4_0 --> 4.5.11-py36_0          
    conda-env:       2.6.0-h36134e3_1      --> 2.6.0-1                
    libedit:         3.1-heed3624_0        --> 3.1.20170329-h6b74fdf_2
    ncurses:         6.0-h06874d7_1        --> 6.1-hf484d3e_0         
    openssl:         1.0.2l-0              --> 1.0.2p-h14c3975_0      
    pycosat:         0.6.2-py36_0          --> 0.6.3-py36h14c3975_0   
    python:          3.6.3-hc9025b9_1      --> 3.6.6-hc3d631a_0       
    readline:        7.0-hac23ff0_3        --> 7.0-ha6073c6_4         
    sqlite:          3.20.1-h6d8b0f3_1     --> 3.24.0-h84994c4_0      
    xz:              5.2.3-h2bcbf08_1      --> 5.2.4-h14c3975_4       

Proceed ([y]/n)? y

conda-env-2.6. 100% |####################################################################################################################################################################| Time: 0:00:00   1.46 MB/s
openssl-1.0.2p 100% |####################################################################################################################################################################| Time: 0:00:00   4.38 MB/s
sqlite-3.24.0- 100% |####################################################################################################################################################################| Time: 0:00:00   4.36 MB/s
python-3.6.6-h 100% |####################################################################################################################################################################| Time: 0:00:07   3.88 MB/s
pycosat-0.6.3- 100% |####################################################################################################################################################################| Time: 0:00:00   4.07 MB/s
conda-4.5.11-p 100% |####################################################################################################################################################################| Time: 0:00:00   4.03 MB/s
```

# after upgrade python
```{bash}
$ python3 -V
Python 3.6.6 :: Anaconda custom (64-bit)

$ conda info --envs
# conda environments:
#
base                  *  /home/rwoo/03_Programs/anaconda/anaconda3
```

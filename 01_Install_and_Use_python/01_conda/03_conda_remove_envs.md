# conda remove envs
```{bash}
$ conda info --envs
# conda environments:
#
p2.7                     /Users/rwoo/anaconda/envs/p2.7
python3.5                /Users/rwoo/anaconda/envs/python3.5
python361                /Users/rwoo/anaconda/envs/python361
root                  *  /Users/rwoo/anaconda

$ conda remove -n python3.5 --all

Package plan for package removal in environment /Users/rwoo/anaconda/envs/python3.5:

The following packages will be REMOVED:

    freetype:   2.5.5-2
    jbig:       2.1-0
    jpeg:       9b-0
    libpng:     1.6.30-1
    libtiff:    4.0.6-3
    mkl:        2017.0.3-0
    numpy:      1.13.1-py35_0
    olefile:    0.44-py35_0
    openssl:    1.0.2l-0
    pillow:     4.2.1-py35_0
    pip:        9.0.1-py35_1
    python:     3.5.4-0
    readline:   6.2-2
    scipy:      0.19.1-np113py35_0
    setuptools: 27.2.0-py35_0
    sqlite:     3.13.0-0
    tk:         8.5.18-0
    wheel:      0.29.0-py35_0
    xz:         5.2.3-0
    zlib:       1.2.11-0

Proceed ([y]/n)? y

$ conda info --envs
# conda environments:
#
p2.7                     /Users/rwoo/anaconda/envs/p2.7
python361                /Users/rwoo/anaconda/envs/python361
root                  *  /Users/rwoo/anaconda
```

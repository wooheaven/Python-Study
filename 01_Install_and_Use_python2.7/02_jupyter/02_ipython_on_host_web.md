# [use ipython on docker host web]
```{bash}
$ source activate python2.7

(python2.7) $ conda info --envs
# conda environments:
#
python2.7             *  /usr/local/anaconda/anaconda2/envs/python2.7
root                     /usr/local/anaconda/anaconda2

(python2.7) rwoo@rwoo-A610:~/02_WorkSpace/05_Python_Workspace/01_Python2.7_Workspace/Python2.7-Study/02_Data_Science_from_Scratch/02_chp$ jupyter notebook --notebook-dir=`pwd` --no-browser --ip=0.0.0.0
[I 22:56:02.223 NotebookApp] Writing notebook server cookie secret to /run/user/1000/jupyter/notebook_cookie_secret
[I 22:56:05.503 NotebookApp] Serving notebooks from local directory: /home/rwoo/02_WorkSpace/05_Python_Workspace/01_Python2.7_Workspace/Python2.7-Study/02_Data_Science_from_Scratch/02_chp
[I 22:56:05.503 NotebookApp] 0 active kernels 
[I 22:56:05.504 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/?token=d90ae34dd774f7148f23fba0926ab786e8dc96414d1205e6
[I 22:56:05.504 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 22:56:05.505 NotebookApp] 
    
Copy/paste this URL into your browser when you connect for the first time,
to login with a token:
http://0.0.0.0:8888/?token=d90ae34dd774f7148f23fba0926ab786e8dc96414d1205e6
```

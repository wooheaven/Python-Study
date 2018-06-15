# [use ipython on docker host web]
```{bash}
docker ps -a
CONTAINER ID        IMAGE                                       COMMAND             CREATED             STATUS                     PORTS               NAMES
7a59264be34e        ubuntu:14.04-python2.7                      "/bin/bash"         16 minutes ago      Exited (0) 6 minutes ago                       cranky_booth

docker start 7a59264be34e
7a59264be34e

docker attach 7a59264be34e
root@7a59264be34e:/#

root@7a59264be34e:/# jupyter notebook --notebook-dir=/home/python_workspace/ --no-browser --ip=0.0.0.0
[I 14:29:28.098 NotebookApp] [nb_conda_kernels] enabled, 2 kernels found
[I 14:29:28.104 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[I 14:29:28.246 NotebookApp] ✓ nbpresent HTML export ENABLED
[W 14:29:28.247 NotebookApp] ✗ nbpresent PDF export DISABLED: No module named nbbrowserpdf.exporters.pdf
[I 14:29:28.252 NotebookApp] [nb_conda] enabled
[I 14:29:28.356 NotebookApp] [nb_anacondacloud] enabled
[I 14:29:28.360 NotebookApp] Serving notebooks from local directory: /home/python_workspace
[I 14:29:28.361 NotebookApp] 0 active kernels
[I 14:29:28.361 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/
[I 14:29:28.361 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

http://localhost:8888/tree
```

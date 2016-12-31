# [use ipython on docker host web]
```
docker ps -a
CONTAINER ID        IMAGE                                       COMMAND             CREATED             STATUS                     PORTS               NAMES
7a59264be34e        ubuntu:14.04-python2.7                      "/bin/bash"         16 minutes ago      Exited (0) 6 minutes ago                       cranky_booth

docker start 7a59264be34e
7a59264be34e

docker attach 7a59264be34e
root@7a59264be34e:/#

root@7a59264be34e:/# jupyter notebook --no-browser --ip=0.0.0.0
[I 16:09:47.677 NotebookApp] [nb_conda_kernels] enabled, 2 kernels found
[I 16:09:47.735 NotebookApp] ✓ nbpresent HTML export ENABLED
[W 16:09:47.735 NotebookApp] ✗ nbpresent PDF export DISABLED: No module named nbbrowserpdf.exporters.pdf
[I 16:09:47.738 NotebookApp] [nb_conda] enabled
[I 16:09:47.774 NotebookApp] [nb_anacondacloud] enabled
[I 16:09:47.776 NotebookApp] Serving notebooks from local directory: /
[I 16:09:47.777 NotebookApp] 0 active kernels
[I 16:09:47.777 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/
[I 16:09:47.777 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

http://127.0.0.1:8888/tree
```

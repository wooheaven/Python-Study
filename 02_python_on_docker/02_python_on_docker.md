# [use python on docker container]
```
docker ps -a
CONTAINER ID        IMAGE                                       COMMAND             CREATED             STATUS                     PORTS               NAMES
35d30c129993        ubuntu:14.04-python2.7                      "/bin/bash"         2 minutes ago       Exited (0) 2 minutes ago                       nauseous_bose
42ff601ded9a        ubuntu:14.04                                "/bin/bash"         2 days ago          Exited (0) 21 hours ago                        kickass_perlman
d3db45184ba2        imcomking/bi_deeplearning                   "/bin/bash"         4 weeks ago         Exited (0) 3 weeks ago                         agitated_torvalds
3689e09f6394        gcr.io/tensorflow/tensorflow:latest-devel   "/bin/bash"         12 weeks ago        Exited (0) 12 weeks ago                        tensorflow

docker start 35d30c129993 
35d30c129993

docker attach 35d30c129993
root@35d30c129993:/#

root@35d30c129993:/# python
Python 2.7.12 |Anaconda 4.2.0 (64-bit)| (default, Jul  2 2016, 17:42:40)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> exit()
root@35d30c129993:/#
```

# cpu python3 tensorflow images
```{basj}
docker pull tensorflow/tensorflow:latest-py3
mkdir notebooks
docker run -it -p 8889:8888 -p 6007:6006 -e PASSWORD=py3 -v `pwd`/notebooks:/notebooks/ --name py3 tensorflow/tensorflow:latest-py3
```

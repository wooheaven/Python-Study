# python env
```
$ cd ~/.pyenv
$ cd versions/Python-Study/share/jupyter/kernels/python3
```

# jupyter kernel : ipython --profile=test
```
$ cp kernel.json kernel.json.bak
$ vi kernel.json
{
  "argv": [
    "python",
    "-m",
    "ipykernel_launcher",
    "--profile=test",
    "-f",
    "{connection_file}"
  ],
  "display_name": "Python 3",
  "language": "python"
}
```

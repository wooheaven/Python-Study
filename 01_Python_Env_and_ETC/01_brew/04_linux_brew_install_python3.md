```{bash}
$ brew search python3
==> Formulae
boost-python3 python3 python@3

$ brew install python3
...
==> Summary
🍺  /home/linuxbrew/.linuxbrew/Cellar/python/3.7.2: 3,482 files, 65.3MB
==> Caveats
==> openssl
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /home/linuxbrew/.linuxbrew/etc/openssl/certs

and run
  /home/linuxbrew/.linuxbrew/opt/openssl/bin/c_rehash
==> python
Python has been installed as
  /home/linuxbrew/.linuxbrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /home/linuxbrew/.linuxbrew/opt/python/libexec/bin

If you need Homebrew's Python 2.7 run
  brew install python@2

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /home/linuxbrew/.linuxbrew/lib/python3.7/site-packages

See: https://docs.brew.sh/Homebrew-and-Python
```

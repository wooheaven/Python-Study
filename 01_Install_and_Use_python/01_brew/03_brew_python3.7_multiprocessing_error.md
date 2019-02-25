# error
```{text}
debugging MP with multiprocessing error on Mac

## Multi TSPR ##
Traceback (most recent call last):
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1664, in <module>
Traceback (most recent call last):
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1664, in <module>
    main()
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1658, in main
    main()
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1658, in main
    globals = debugger.run(setup['file'], None, None, is_module)
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1068, in run
    globals = debugger.run(setup['file'], None, None, is_module)
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1068, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "/Users/rwoo/02_WorkSpace/27_PlayOnSandBox_Workspace/PlayOnSandBox/02_MP/01_MP_by_rwoo/MP2_by_PyCharm/MP2.py", line 291, in <module>
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    mDistanceProfile = Manager().dict({})
    exec(compile(contents+"\n", file, 'exec'), glob, loc)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/context.py", line 56, in Manager
  File "/Users/rwoo/02_WorkSpace/27_PlayOnSandBox_Workspace/PlayOnSandBox/02_MP/01_MP_by_rwoo/MP2_by_PyCharm/MP2.py", line 291, in <module>
    mDistanceProfile = Manager().dict({})
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/context.py", line 56, in Manager
    m.start()
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/managers.py", line 543, in start
    m.start()
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/managers.py", line 547, in start
    self._process.start()
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/process.py", line 112, in start
    self._address = reader.recv()
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/connection.py", line 407, in _recv_bytes
    self._popen = self._Popen(self)
      File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/context.py", line 277, in _Popen
buf = self._recv(4)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/connection.py", line 379, in _recv
    chunk = read(handle, remaining)
KeyboardInterrupt
    return Popen(process_obj)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/popen_fork.py", line 20, in __init__
    self._launch(process_obj)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/popen_fork.py", line 70, in _launch
    self.pid = os.fork()
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/_pydev_bundle/pydev_monkey.py", line 489, in new_fork
    _on_forked_process()
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/_pydev_bundle/pydev_monkey.py", line 56, in _on_forked_process
    pydevd.settrace_forked()
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1445, in settrace_forked
    patch_multiprocessing=True,
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1210, in settrace
    patch_multiprocessing,
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 1254, in _locked_settrace
    debugger.connect(host, port)  # Note: connect can raise error.
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 328, in connect
    self.initialize_network(s)
  File "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevd.py", line 320, in initialize_network
    time.sleep(0.1)  # give threads time to start
KeyboardInterrupt
Error in atexit._run_exitfuncs:
Traceback (most recent call last):
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/util.py", line 322, in _exit_function
    p.join()
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/multiprocessing/process.py", line 138, in join
    assert self._parent_pid == os.getpid(), 'can only join a child process'
AssertionError: can only join a child process
```

# solution
```{text}
use /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 on Mac
```

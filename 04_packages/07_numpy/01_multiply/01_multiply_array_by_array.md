```python
import numpy as np


np.multiply(2.0, 4.0)
8.0

x1 = np.arange(9.0).reshape((3, 3))
x1
array([[0., 1., 2.],
       [3., 4., 5.],
       [6., 7., 8.]])

x2 = np.arange(3.0)
x2
array([0., 1., 2.])

x3 = np.arange(4.0)
x3
array([0., 1., 2., 3.])

np.multiply(x1,x2)
array([[ 0.,  1.,  4.],
       [ 0.,  4., 10.],
       [ 0.,  7., 16.]])

np.multiply(x1,x3)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (3,3) (4,)
```

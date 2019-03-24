```python
import numpy as np
data = np.arange(20)
data
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19])

chunk_data = [data[i::5] for i in range(5)]
chunk_data
[array([ 0,  5, 10, 15]),
 array([ 1,  6, 11, 16]),
 array([ 2,  7, 12, 17]),
 array([ 3,  8, 13, 18]),
 array([ 4,  9, 14, 19])]

chunk_data = [data[i::6] for i in range(6)]
chunk_data
[array([ 0,  6, 12, 18]),
 array([ 1,  7, 13, 19]),
 array([ 2,  8, 14]),
 array([ 3,  9, 15]),
 array([ 4, 10, 16]),
 array([ 5, 11, 17])]
```

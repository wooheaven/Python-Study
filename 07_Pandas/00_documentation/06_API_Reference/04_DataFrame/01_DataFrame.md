```python
import numpy as np
import pandas as pd

# dict to df
pd.DataFrame({"name": ["ab", "bc", "cd", "de"], "number": [4, 2, 3, 1], "sales": [3, 5, 0, 1]})
  name  number  sales
0   ab       4      3
1   bc       2      5
2   cd       3      0
3   de       1      1

# numpy ndarray to df
pd.DataFrame(np.array([[1,2,3], [4,5,6]], np.int32))
   0  1  2
0  1  2  3
1  4  5  6
```

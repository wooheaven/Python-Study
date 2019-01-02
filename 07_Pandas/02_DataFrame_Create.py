
# coding: utf-8

# In[1]:

import pandas as pd
print(pd.__version__)


# In[2]:

data1 = {"name": ["ab", "bc", "cd", "de"], "number": [4, 2, 3, 1], "sales": [3, 5, 0, 1]}
data1


# In[3]:

# dict to df
df = pd.DataFrame(data1)
df


# In[4]:

import numpy as np
print(np.__version__)


# In[5]:

data2 = np.array([[1,2,3], [4,5,6]], np.int32)
data2


# In[6]:

# numpy 2d array to df
df2 = pd.DataFrame(data2)
df2


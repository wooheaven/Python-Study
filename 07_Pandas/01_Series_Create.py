
# coding: utf-8

# In[1]:

import pandas as pd
print(pd.__version__)


# In[2]:

data1 = [4, 3, 1, 2]
data1


# In[3]:

# list to series
series1 = pd.Series(data1)
series1


# In[4]:

series1.index


# In[5]:

series1.values


# In[6]:

series1.dtype


# In[7]:

import numpy as np
print(np.__version__)


# In[8]:

data2 = np.array([1, 4, 2, 3], np.int32)
data2


# In[9]:

# numpy 1d array to series
series2 = pd.Series(data2)
series2


# In[10]:

# series index option
series2 = pd.Series(data1, index=['a', 'b', 'c', 'd'])
series2


# In[11]:

series2.index


# In[12]:

series2.values


# In[13]:

series2.dtype


# In[14]:

series2.name


# In[15]:

series2.name = 'test2'


# In[16]:

series2.name


# In[17]:

series2.index.name


# In[18]:

series2.index.name = 'test2index'


# In[19]:

series2.index.name


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = {"names": ["soyul", "soyul", "soyul", "Charles", "Charles"], "year": [2014, 2015, 2016, 2015, 2016], "points": [1.5, 1.7, 3.6, 2.4, 2.9]} 
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"], index = ["one", "two", "three", "four", "five"])


# In[3]:


df


# In[4]:


# select column
df["year"]


# In[5]:


df[["year", "points"]]


# In[6]:


# update column's value by numpy 1d array (or list)
df["penalty"] = np.arange(5) # [0, 1, 2, 3, 4]
df


# In[7]:


# add column by numpy 1d array
df["zeros"] = np.zeros(5)
df


# In[8]:


# add column by pandas series
data = pd.Series([-1.1, -2.2, -3.3], index=["two", "three", "four"])
df["debt"] = data
df


# In[9]:


# add column by other column
df["sum_points"] = df["points"] - df["penalty"]
df["negative"] = df["sum_points"] < 0.0
df


# In[10]:


del df["negative"]
df


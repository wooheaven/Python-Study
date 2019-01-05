#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = {"names": ["soyul", "soyul", "soyul", "Charles", "Charles"], "year": [2014, 2015, 2016, 2015, 2016], "points": [1.5, 1.7, 3.6, 2.4, 2.9]} 
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"], index = ["one", "two", "three", "four", "five"])


# In[3]:


df


# In[4]:


# select row
df.loc["two"]


# In[5]:


df.loc["two":"four"]


# In[6]:


df.iloc[1]


# In[7]:


df.iloc[1:4]


# In[8]:


# select row, column
df.loc["two":"three", "year":"points"]


# In[9]:


df.iloc[1:3, 0:3]


# In[10]:


df.iloc[[0,1,3], [1,2]]


# In[11]:


# select row by condition
df.loc[(df["names"] == "soyul") & (df["points"] < 3), :]


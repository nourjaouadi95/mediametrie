#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
import datetime
import matplotlib as mpl 
import matplotlib.pyplot as plt
from urllib.parse import urlparse
import nltk
import os
from nltk.tokenize import word_tokenize 
import re


# In[ ]:


cookies_ori = pd.read_pickle("./cookies.pkl")


# In[5]:


cookies_ori = pd.read_csv('./url_decompose.csv',sep=",",header=0)


# In[6]:


cookies = cookies_ori.copy()


# In[98]:


cookies.head()


# # 1. Exploser le path

# In[86]:


import math
def to_bag_of_word(path):
    ret = ['no_path']
    if path != "" and path == path:
        ret = re.split('-|_|/',path)
        
    
    ret = list(filter(None, ret))
    
    
    return(ret)


# In[89]:


cookies['path_explode'] = cookies.apply(lambda row : to_bag_of_word(row['path']), axis = 1)


# In[99]:


cookies.to_csv('path_decompose.csv',index=False)


# # 2. Analyse des mots du path

# In[103]:


bag_of_words = cookies['path_explode'].tolist()


# In[104]:


flat_list = [item for sublist in bag_of_words for item in sublist]


# In[105]:


flat_list


# In[ ]:





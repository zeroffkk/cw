#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


import re


# In[4]:


for line in sys.stdin:
    line = line.strip()
    cols = line.split(',')
    print '%s\t%d' % (cols[2], 1)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[2]:


import re


# In[ ]:


for line in sys.stdin:
    line = line.strip()
    cols = line.split(',')
    print '%s\t%d' % (cols[0], 1)


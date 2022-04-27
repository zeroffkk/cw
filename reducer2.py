#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[ ]:


passenger = ""
current_passenger = ""
current_count = 0


# In[ ]:


for line in sys.stdin:
    passenger, count = line.split('\t', 1)
    try:
         count = int(count)
    except ValueError:
        continue
    if current_passenger == passenger:
        current_count += count
    else:
        if current_passenger:
            print '%s\t%d' % (current_passenger, current_count)
        current_count = count
        current_passenger = passenger
if current_passenger == passenger:
    print '%s\t%d' % (current_passenger, current_count)


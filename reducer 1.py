#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[ ]:


airport = ""
current_airport = ""
current_count = 0


# In[ ]:


for line in sys.stdin:
    airport, count = line.split('\t', 1)
    try:
         count = int(count)
    except ValueError:
        continue
    if current_airport == airport:
        current_count += count
    else:
        if current_airport:
            print '%s\t%d' % (current_airport, current_count)
        current_count = count
        current_airport = airport
if current_airport == airport:
    print '%s\t%d' % (current_airport, current_count)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program:To get a list of all factorial and kaprekar number in the range 1 to 10 
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:28-Sept-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[ ]:





# In[2]:


import numpy as np
import math
import json
factorial=["Factorial"]
karprekar=["Karprekar"]
for i in range(1,10):
    factorial.append(math.factorial(i))
for n in range(1,10):
    n2 = str(n**2)
    for i in range(len(n2)):
        a, b = int(n2[:i] or 0), int(n2[i:])
        if b and a + b == n:
            karprekar.append(n)
factorial=np.array(factorial)
karprekar=np.array(karprekar)
json_dict={factorial[0]:factorial[1::],karprekar[0]:karprekar[1::]}
print(json_dict)


# In[ ]:





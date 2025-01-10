#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


dir(np)


# In[3]:


x=np.array([40,67,57,90])
print(x)
print(type(x))


# In[5]:


#create a 2D array
a2 = np.array([[20,40],[30,60]])
print(a2)
print(type(a2))
print(a2.shape)


# In[8]:


a3 =np.array([[1,'A',9.8],[2,'B',10.3]])
print(a3)
print(type(a3))
print(a3.shape)


# In[4]:


import numpy as np

# Create an array with arange()
c = np.arange(3, 10)
print(c)
print(type(c))


# In[5]:


#Use of around()
d = np.array([1.3467,3.1048,4.9534])
print(d)
np.around(d,2)


# In[6]:


a1 = np.array([[3,4,5,8],[7,2,8,np.NAN]])
print(a1)
print(a1.shape)
print(a1.dtype)


# In[7]:


#Use of astype() to convert the data type
a1_copy1 = a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[8]:


#mathematical operations on rows and cols
a2 = np.array([[3,4,6],[7,9,10],[4,6,12]])
a2


# In[ ]:





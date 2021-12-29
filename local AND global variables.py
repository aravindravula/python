#!/usr/bin/env python
# coding: utf-8

# In[4]:


''''global variable:
    
A variable declared outside the function or in global scope is called global variable

local variable :
    A variable declared inside the function body or in local scope is called local variable'''
   


# In[14]:


# example of local variable

def f():
    s='iam local variable'
    print(s)
f()


# In[9]:


# example of global variable

def f():
    print('inside function',s)
s='iam global variable'
print('outside function',s)
f()


# In[13]:


#printing local variable first and global variable next

a='johnwick'
def f1():
    b='matrix'
    print('inside',a)
f1()   
print('outside',a)    


# In[ ]:





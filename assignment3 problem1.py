#!/usr/bin/env python
# coding: utf-8

# In[2]:


#python function to sum the elements in a list
def summation(lista):
    s=0
    for i in range(len(lista)):
        lista[i]=int(lista[i])
        s=lista[i]+s

    return s
lista=[8,2,3,0,7]
result=summation(lista)
print(result)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random


# In[22]:


goodies = {
    "Fitbit_plus" : 7980,
    "Ipod": 22349,
    "Mi_band" : 999,
    "Cult_pass" : 2799,
    "Macbook_pro" : 229900,
    "digital_camera" : 11101,
    "Alexa" : 9999,
    "Sandwich_toaster" : 2195,
    "Microwave_oven" : 9800,
    "Scale" : 4999
}


# In[25]:


emp = int(input("Enter the number of employees:"))
l = list(goodies.keys())
random.shuffle(l)
upd = []
for i in range(0, emp):
    upd.append(l[i])

print("\n")
print("Here the goodies that are selected for distribution are:")
for j in range(0, emp):
    print(upd[j], ":", goodies[upd[j]])
    

maxi = 0
mini = 99999999
for i in range(0, emp):
    if goodies[upd[i]] > maxi:
        maxi = goodies[upd[i]]
    elif goodies[upd[i]] < mini:
        mini = goodies[upd[i]]
    else:
        pass

value = maxi - mini
print("\n")
print("And the difference between the chosen goodie with highest price and the lowest price is {}".format(value))


# In[ ]:





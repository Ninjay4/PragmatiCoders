#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
File Name: Unique Elements
Created By: Ninjay4
Created On: 2/28/24
Modified On: None
Description: 
PragmatiCoders Python Challenge
Round 1 Practice Problem #9
Write a function that returns
The unique elements in a list
Hint: Utilize a set to keep track of unique elements
Version: Python 3
'''


# In[2]:


# Create a 'unique_elements' Function
# Nothing else needs to be added because
# Converting the list into a set
# Removes any duplicate items
def unique_elements(lst):
    return list(set(lst)) 


# In[3]:


# Create an original list with duplicates
lst = ['one', 'pot', 'spaghetti', 'taco', 'fast', 'weeknight', 'dinner',
      'pairs', 'favorite', 'taco', 'fixings', 'spaghetti', 'taco', 'shells']


# In[4]:


# Run the 'unique_elements' Function
print(unique_elements(lst))


#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
File Name: List Flattener
Created By: Ninjay4
Created On: 2/27/24
Modified On: None
Description:
    PragmatiCoders Python Challenge
    Round 1 Practice Problem #8
    Develop a function that takes a list of lists (a matrix)
    And flattens it to a single list
    Without using any built-in Python flattening functions
Hint: Use a recursive function if a list is encountered
Python Version 3
'''


# In[2]:


# Create a 'flatten_list' Function
# Uses a list comprehension
def flatten_list(nested_list):
    flat_list = [ i for sublist in nested_list for i in sublist] 
    print(flat_list)


# In[3]:


# Create a nested list
nested_list = [['This', 'Lofi', 'Some', 'Mess'], [1, 2], ['Love', 'Hip Hop', 'Blind', 'Season'], 
               [3, 4, 5], ['Jazzy', 'Beats', 'Fix', 'Father'], [6, 7, 8, 9]]


# In[4]:


# Run the 'flatten_list' function
flatten_list(nested_list)


# In[6]:


# Alternate way to flatten the list
# Uses the 'List Extend' Function
flat_list1 = []
for i in range(len(nested_list)):
    flat_list1.extend(nested_list[i])
print(flat_list1)


# In[ ]:





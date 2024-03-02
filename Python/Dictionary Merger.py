#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
File Name: Dictionary Merger
Created By: Ninjay4
Created On: 3/1/24
Modified On: None
Description:
PragmatiCoders Python Challenge
Round 1 Practice Problem #11
Write a function that merges two dictionaries.
If there is a conflict between dictionaries
(whenever they have the same key),
The value from the 2nd dictionary should be kept
Hint: Start with one dictionary and update it
With the second one
'''


# In[2]:


# Create a 'merge_dictionaries' Function
# Nothing else needs to be added
# The coding was already provided
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


# In[3]:


# Create the 1st dictionary
dict1 = {1:'sugar', 2:'butter', 3:'salt', 4:'vanilla', 5:'cake',
         6:'coconut'}


# In[4]:


# Create the 2nd dictionary
dict2 = {1:'sugar', 2:'butter', 3:'salt', 4:'vanilla extract', 
         5:'2 cake layers', 6:'flaked coconut'}


# In[5]:


# Run the 'merge_dictionaries' function
merge_dictionaries(dict1, dict2)


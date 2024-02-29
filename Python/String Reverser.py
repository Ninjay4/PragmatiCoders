#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
File Name: String Reverser
Created By: Ninjay4
Created On: 2/29/24
Modified On: None
Description: PragmatiCoders Python Challenge
Round 1 Practice Problem #10
Create a funcion that takes a string and
Returns the string in reversed order
Without using the [:: -1] syntax
Version: Python 3
'''


# In[2]:


# Create the input string
s = input("Please enter the string:  ")


# In[3]:


# Create the 'reverse_string' functon
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
    
# Note: for char in s: append to reversed_str


# In[4]:


# Run the 'reverse_string' Function
reverse_string(s)


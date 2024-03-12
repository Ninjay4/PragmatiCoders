#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
FILE NAME: Email Validator
CREATED BY: Ninjay4
CREATED ON: 3/6/24
MODIFIED ON: none
DESCRIPTION:
PragmatiCoders Python Challenge
Round 1 Practice Problem #13
Write a function that checks if a given string
Is a valid email address
(Contains one '@' and at least one '.')
VERSION: Python 3
'''


# In[2]:


# Create a 'is_valid_email' Function
# No other code is needed
# The result is boolean and returns either True or False
def is_valid_email(email):
    return '@' in email and '.' in email


# In[3]:


# Create the email input
email = input("Enter the email address:  ")


# In[4]:


# Run the 'is_valid_email' function
is_valid_email(email)


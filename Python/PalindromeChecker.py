#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PragmatiCoder Python Challenge
# Round 1 Practice Problem #2


# In[2]:


# Create a function that checks if a given string is a palindrome
# Reads the same backward as forward
# Ignores spaces, punctuation, and capitalization


# In[3]:


# Hint: Clean the string by removing spaces and
# Converting everything to lowercase
# Then compare the string with the reverse


# In[4]:


# Import "string", so that we can use the string.translate method
# To remove any punctuation
import string


# In[13]:


# Create the "is_palindrome" function
def is_palindrome(s):
    # To remove the spaces
    clean_str = s.replace(' ', '').lower()
    # To remove the punctuation
    clean_str = clean_str.translate(str.maketrans("", "", string.punctuation))
    if clean_str == clean_str[: : -1]:
        print("The string is a palindrome")
    else:
        print("The string is NOT a palindrome")


# In[14]:


# Create the input string
s = input("Please enter the string: ")


# In[15]:


# Run the "is_palindrome" function
is_palindrome(s)


# In[ ]:





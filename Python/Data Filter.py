#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PragmatiCoders Python Challenge
# Round 1 Practice Problem #5
# Write a function that takes
# A list of dictionaries called people
# That have the following keys: name, age, profession
# The function also takes a key string for the profession name


# In[2]:


# The function returns a new, filtered list
# that contains the given key, 'profession' 


# In[3]:


# Hint: Use a list comprehension to filter
# The 'people' dictionary that is based on the "profession" key


# In[4]:


# Create a "filter_by_profession" function
def filter_by_profession(people, profname):
    # The List Comprehension is everything within the return brackets
    return [person for person in people if person['profession'] == profname]


# In[6]:


# Create a 'people' dictionary that contains
# Dictionaries with keys of name, age, and profession
people = [{'name': 'Bob', 'age': 47, 'profession': 'construction'}, {'name': 'Sheila', 'age': 32, 'profession': 'manager'}, 
         {'name': 'Ryan', 'age': 24, 'profession': 'personal trainer'}, {'name': 'Amanda', 'age': 28, 'profession': 'chef'}, 
         {'name': 'Benjamin', 'age': 52, 'profession': 'inventor'}, {'name': 'Emeril', 'age': 68, 'profession': 'chef'}]


# In[7]:


# Call and print the filtered list
profname = input("Enter the profession name: ")
print(filter_by_profession(people, profname))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PragmatiCoders Python Challenge
# Round 1 Practice Problem #4
# Develop a function that takes a list of numbers
# And returns a dictionary with keys being
# The numbers and values being the frequency of those numbers in the list


# In[2]:


# Hint: Use a dictionary to count occurrences
# Of each number using a loop


# In[42]:


# Create a "frequency_counter" function
def frequency_counter(numbers):
    # Creates an empty dictionary
    frequency = {} 
    for i in numbers:
        frequency[int(i)] = numbers.count(i)
    print(frequency)


# In[43]:


# Create the input list of numbers
numbers = input("Please enter your list of numbers separated with spaces: ").split()


# In[44]:


# Run and Print the result of the "frequency_counter' function
frequency_counter(numbers)


# In[ ]:





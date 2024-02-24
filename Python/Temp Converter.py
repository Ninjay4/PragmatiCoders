#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PragmatiCoders Python Challenge
# Round 1 Practice Problem 6
# Create a function that converts a temperature
# From Fahrenheit to Celsius and vice versa
# Based on a 2nd argument that indicates
# The direction of conversion (F to C OR C to F)


# In[2]:


# Hint: Apply the appropriate formula 
# Based on the conversion direction


# In[4]:


# Create the input
temp = int(input("What is your temperature value?  "))
direction = input("What kind of temperature is it? Please enter C for Celsius or F for Farenheit:  ") 


# In[9]:


# Create the 'convert_temperature' function
def convert_temperature(temp, direction):
    if direction == 'F': 
        return print(str((temp - 32)*(5/9)) + " Celsius")
    else:
        return print(str((temp*(9/5) + 32)) + "Farenheit")
    
# C = (F - 32)*(5/9)
# F = (9/5)*C + 32


# In[10]:


# Run the 'convert_temperature' function
convert_temperature(temp, direction)


# In[ ]:





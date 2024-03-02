#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
File Name: Multiplication Table Printer
Created By: Ninjay4
Created On: 3/2/24
Modified On: None
Description:
PragmatiCoder Python Challenge
Round 1 Practice Problem #12
Develop a function that prints out a 
Multiplication table for numbers
Up to a given number
Version: Python 3
'''


# In[6]:


# Create a 'print_multiplication_table' Function
def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(str(i) + " x " + str(j) + " = " + str(i*j))
    
# for i in range(1, n+1):
# print the multiplication row for 1 


# In[7]:


# Create the input integer
n = int(input("Please enter the integer:  "))


# In[8]:


# Run the 'print_multiplication_table' function
print_multiplication_table(n)


# In[ ]:





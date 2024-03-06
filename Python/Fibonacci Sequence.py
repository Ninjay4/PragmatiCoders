#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
FILE NAME: Fibonacci Sequence
CREATED BY: Ninjay4
CREATED ON: 3/6/24
MODIFIED ON: none
DESCRIPTION:
PragmatiCoders Python Challenge
Round 1 Practice Problem #15
Write a function that returns the Fibonacci sequence
Up to a given number of elements
HINT: Use a loop or recursion to generate the sequence
VERSION: Python 3
'''


# In[2]:


# The Fibonacci sequence is when each subsequent number
# Is the sum of the previous two numbers
# 0,1,1,2,3,5,8,13,21,34,...
# Given n=5, the sequence is 0,1,2,3,5


# In[3]:


# Create a 'Fibonacci' Function
def fibonacci(n):
    fib_sequence = [0, 1]
    if n==1:
        print(0)
    elif n==2:
        print(fib_sequence)
    else:
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(fib_sequence)
            
    
# for i in range(2, n): add the next number to the sequence


# In[4]:


# Create the input integer
n = int(input("Enter the number of elements that the sequence should have:  "))


# In[5]:


# Run the 'Fibonacci' function
fibonacci(n)


# In[ ]:





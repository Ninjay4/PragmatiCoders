#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
File Name: Prime Number
Created by: Ninjay4
Created on: 2/25/24
Data Modified: None
Description:  PractiCoders Python Challenge
Round 1 Practice Problem #7:
Write a function that takes an integer and returns
a list of all prime numbers up to and including that integer
Hint: Use a nested loop to check for factors of each number
up to the input integer
Python Version: 3
"""


# In[2]:


# Create a list of prime factors
prime = []


# In[3]:


# Create a 'find_prime' Function
def find_primes(n):
    print("The list of Prime Numbers is: ")
    for i in range(2, n+1):
        for j in prime:
            if (i % j) == 0:
                break
        else:
            prime.append(i)    
            print(i)


# In[4]:


# Create the input integer
n = int(input("Enter the integer:  "))


# In[5]:


# Run the 'find_primes' Function
find_primes(n)


# In[ ]:





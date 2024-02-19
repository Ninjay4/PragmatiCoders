#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In progress; Not completed yet
# This is for the PragmatiCoders Python Challenge
# Round 1 Questions
# This is my answer for Practice Problem 1


# In[2]:


# Write a function that accepts a text filename as its parameter,
# Reads the file,
# Then returns the number of lines, words, and characters
# In the file


# In[3]:


# Hints:
# Use the "Open" function to read the file
# Use "String" methods to "Split" the text
# Into words and lines


# In[5]:


# Import the text file
f = open("C:/Users/nina_/Dropbox/Nina/Data Science/PragmatiCoders/Python/Text File 1.docx")


# In[12]:


# Create the summarize_text_file Function
def summarize_text_file(f):
    content = f.read()
    splitContent = content.split("\n")
    counter = 0
    for i in splitContent:
        if i:
            counter += 1
    return print("The number of lines is " + str(counter))


# In[13]:


# Run and Test the Function
summarize_text_file(f)


# In[ ]:





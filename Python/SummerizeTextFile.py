#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This is for the PragmatiCoders Python Challenge
# Round 1 Questions
# This is my answer for Practice Problem 1
# For "txt" text files. Python would not read a Microsoft Word file.


# In[2]:


# Write a function that accepts a text filename as its parameter,
# Reads the file,
# Then returns the number of lines, words, and characters in the file


# In[3]:


# Hints:
# Use the "Open" function to read the file
# Use "String" methods to "Split" the text
# Into words and lines


# In[4]:


# Import the text file
filename = "C:/Users/nina_/Dropbox/Nina/Data Science/PragmatiCoders/Python/Txt text File.txt" #"r", encoding = 'utf-8')


# In[5]:


# Create the summarize_text_file Function
def summarize_text_file(filename):
    lctr = 0
    wctr = 0
    cctr = 0
    # Added the encoding parameter to prevent "Unicode Decode" errors
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            lctr += 1
            word = line.split()
            wctr += len(word)
            cctr += len(line)
    print("The number of lines is " + str(lctr))
    print("The number of words is " + str(wctr))
    print("The number of characters is " + str(cctr))


# In[6]:


# Run and Test the Function
summarize_text_file(filename)


# In[7]:


# This method produces 70 lines, 500 words, and 2729 characters


# In[ ]:





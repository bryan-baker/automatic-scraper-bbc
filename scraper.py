#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text)


# In[7]:


# Grab all titles
titles = doc.select(".media__title a")


# In[12]:


# Start with an empty list
rows = []

for title in titles:
    # Go through each title, building a dictionary
    # with a 'title' and a 'url'
    row = {}
    
    # title
    row['title'] = title.text.strip()
    # link
    row['url'] = title['href']
    
    # Then add it to our list of rows
    rows.append(row)

# then we're going to make a dataframe from it!!!
df = pd.DataFrame(rows)
df.head()


# In[13]:


df.to_csv('bbc.csv', index=False)


# In[ ]:





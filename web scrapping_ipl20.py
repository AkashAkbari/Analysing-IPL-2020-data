#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().system(' pip install beautifulsoup4')


# In[10]:


get_ipython().system(' pip install requests')


# In[11]:


import sys
import time
from bs4 import BeautifulSoup
import requests


# In[21]:


try:
    page=requests.get('https://www.iplt20.com/points-table/2020')

except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print("ERROR FOR LINK:", url)
        print(error_type, 'Line', error_info, tb_lineno)
        
time.sleep(2)
soup=BeautifulSoup(page.text, 'html.parser')
league_table=soup.find('table', class_="standings-table standings-table--full")
for team in league_table.find_all('tr'):
    print(team.text)


# In[22]:


league_table


# In[ ]:





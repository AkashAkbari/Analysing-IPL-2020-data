#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loading the required libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


pwd


# In[6]:


#loading the ipl matches dataset
ipl=pd.read_csv('G:/GitHub_Projects/Predicting IPL winner using ML/archive/matches.csv')


# In[9]:


#having a glance at the first five records of the dataset
ipl.head()


# In[10]:


#looking at the number of rows and columns 
ipl.shape


# In[14]:


#getting the frequency of the most man of the match awards
ipl['player_of_match'].value_counts()


# In[17]:


#getting the top 10 players with the  most man of the match awards
ipl['player_of_match'].value_counts()[0:10]


# In[18]:


#getting the top 5 players with the most man of the match awards
ipl['player_of_match'].value_counts()[0:5]


# In[23]:


list(ipl['player_of_match'].value_counts()[0:5])


# In[29]:


#making a bar plot for thr top 5 players with most man of the match awards
plt.figure(figsize=(8, 5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), list(ipl['player_of_match'].value_counts()[0:5]), color="g")
plt.show()


# In[30]:


#getting the frequency of result column
ipl['result'].value_counts()


# In[31]:


#finding out the number of toss wins w.r.t each team
ipl['toss_winner'].value_counts()


# In[35]:


#extracting the records where a team won batting first
batting_first=ipl[ipl['win_by_runs']!=0]


# In[36]:


#looking at the head
batting_first.head()


# In[38]:


#making a histogram
plt.figure(figsize=(5,7))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of runs")
plt.xlabel("Runs")
plt.show()


# In[39]:


#finding out the number of wins w.r.t each team after batting first
batting_first['winner'].value_counts()[0:3].keys()


# In[44]:


#making a bar-plot for top 3 teams with most wins after batting first
plt.figure(figsize=(3,10))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()), list(batting_first['winner'].value_counts()[0:3]),color=["blue", "yellow", "orange"])


# In[49]:


#making a pie chart
plt.figure(figsize=(5,7))
plt.pie(list(batting_first['winner'].value_counts()), labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[50]:


#extracting those records where a team has won after batting second
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[51]:


#looking at the head
batting_second.head()


# In[52]:


#making a histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'], bins=30)
plt.show()


# In[53]:


#finding out the frequency of number of wins w.r.t each time after batting second
batting_second['winner'].value_counts()


# In[69]:


#making a bar-plot for top-3 teams with most wins after batting second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()), list(batting_second['winner'].value_counts()[0:3]),color=["purple","red","green"])
plt.show()


# In[76]:


#making a pie chart for distribution of most wins after batting second
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()), labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[83]:


#looking at the number of matches played in each city
ipl['city'].value_counts()


# In[ ]:





# In[ ]:





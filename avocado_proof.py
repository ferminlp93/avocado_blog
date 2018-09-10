
# coding: utf-8

# In[31]:


import pandas as pd


# In[32]:


df = pd.read_csv('avocado.csv', index_col=0, sep=',')


# In[33]:


df.head()


# In[34]:


df.tail()


# In[37]:


df.year.unique()


# In[38]:


df.groupby('year')['AveragePrice'].mean()


# In[36]:


df.groupby(['year','region'])['AveragePrice'].mean()


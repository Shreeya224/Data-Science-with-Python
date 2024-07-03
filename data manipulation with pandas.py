#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv('C:\\Users\\user\\Desktop\\data-science with python\\01.Data Cleaning and Preprocessing.csv')


# In[7]:


type(df)


# In[8]:


df.head()


# In[9]:


df.info


# In[10]:


df.shape


# In[11]:


df.describe()


# In[12]:


df.duplicated()


# In[13]:


df.duplicated().sum()


# In[14]:


df = df.drop_duplicates()


# In[15]:


df


# In[16]:


df.isnull()


# In[17]:


df.isnull().sum()


# In[18]:


df.isnull().sum().sum()


# In[19]:


df_filled = df.fillna(0)


# In[20]:


df_filled.isnull().sum().sum()


# In[21]:


df_filled


# In[22]:


df_filled2 = df.ffill()


# In[23]:


df_filled2


# In[24]:


df_filled3 = df.bfill()


# In[25]:


df_filled3


# In[26]:


df_filled.columns


# In[27]:


df_filled.drop(['Observation'], axis=1, inplace=True)


# In[28]:


df_filled.columns


# In[29]:


Q1 = df_filled.quantile(0.25)
Q2 = df_filled.quantile(0.75)
IQR = Q2 - Q1
IQR


# In[30]:


df_filled.describe()


# In[ ]:





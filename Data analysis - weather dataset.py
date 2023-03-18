#!/usr/bin/env python
# coding: utf-8

# # Data Analysis - Weather Dataset

# In[1]:


import pandas as pd


# In[8]:


data = pd.read_csv(r"/Users/rutu/Downloads/Personal Projects/Data Analysis - Weather Dataset/Weather Data.csv")
data


# In[9]:


data.shape


# In[11]:


data['Weather'].unique()


# In[20]:


data.columns


# In[14]:


data.nunique() 
#total number of unique values in each column


# In[16]:


data['Weather'].value_counts() 
#unique values with count


# # 1. Find all unique 'Wind Speed' values in the data

# In[21]:


data['Wind Speed_km/h'].unique()


# In[24]:


data['Wind Speed_km/h'].nunique()


# ## 2. Find the number of times 'weather is exactly clear'

# In[29]:


data[data.Weather == 'Clear']


# In[31]:


#using groupby
data.groupby('Weather').get_group('Clear')


# # 3. Number of times 'Wind Speed was exactly 4kmph'

# In[32]:


data[data['Wind Speed_km/h'] == 4]


# # 4. Null Values in data

# In[34]:


data.isnull().sum()


# # 5. Rename column 'Weather' to 'Weather Condition'

# In[57]:


data.rename(columns = {'Weather': 'Weather Conditions'}, inplace = True)
data


# # 6. mean of column 'Visibility'

# In[37]:


data['Visibility_km'].mean()


# # 7. Standard Deviation - 'Pressure'

# In[39]:


data['Press_kPa'].std()


# # 8. Variance - 'Relative humidity'

# In[41]:


data['Rel Hum_%'].var()


# # 9. All instances when 'Snow' was recorded

# In[45]:


data.groupby('Weather Conditions').get_group('Snow')
#does not including snow showers and other records


# In[48]:


data[data['Weather Conditions'].str.contains('Snow')]


# # 10. Instances when 'Wind Speed > 24' and 'Visibility = 25'

# In[55]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# # 11. Mean value of each column against each 'Weather Condition'

# In[58]:


data.groupby('Weather Conditions').mean()


# # 12. Min Max of each column against each 'Weather condition'

# In[63]:


data.groupby('Weather Conditions').min()


# In[64]:


data.groupby('Weather Conditions').max()


# # 13. All records with weather condition = fog

# In[66]:


data[data['Weather Conditions'] == 'Fog']


# # 14. Weather is 'Clear' or Visibility > 40

# In[69]:


data[(data['Weather Conditions'] == 'Clear') | (data['Visibility_km'] > 40)]


# # 15.  'Weather is clear' and 'Relative humidity > 50 '       OR       'visibility > 40'

# In[70]:


data[((data['Weather Conditions'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]


#  

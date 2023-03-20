#!/usr/bin/env python
# coding: utf-8

# # Assignment_27-02-2023(SEABORN)
# 

# ## Q1. Name any five Plots that we can plot using the Seaborn library. Also,state the uses of each plot.
# 
# ### Ans:-
# 
#         There are five commonly used plots that can be created using Seaborn along with their uses:
#         
#         1.Scatter Plot - A scatter plot shows the relationship between two variables by plotting points on a two-dimensional
#                          graph. This type of plot is useful for identifying patterns and correlations in data.
#                          
#         2.Line Plot - A line plot shows the changes in one variable over time or across different categories. It is used to
#                       visualize trends and patterns in data.
#         
#         3.Histogram - A histogram is used to represent the distribution of a single variable by dividing the data into bins 
#                       and counting the number of observations in each bin. It is useful for understanding the shape and 
#                       spread of data.
#                       
#         4.Bar Plot -A bar plot is used to compare the values of different categories or groups. It is useful for visualizing
#                      categorical data.
#                      
#         5.Heatmap -A heatmap is used to visualize the correlation between different variables in a dataset. It is useful for
#                     identifying patterns and trends in data that are not immediately obvious.
#                     

# ## Q2.Load the "fmri"dataset using the load_dataset function of seaborn . plot a line plot using x="timepoint" and y = "signal"for different events and regions.
# 
# ## Note :- timepoint,signal,event,and region are columns in the fmri dataset.
# 
# ### Ans:-

# In[1]:


import seaborn as sns
fmir = sns.load_dataset("fmri")


# In[2]:


fmir


# In[3]:


sns.lineplot(x=fmir.timepoint,y=fmir.signal)


# In[4]:


sns.scatterplot(x=fmir.timepoint,y=fmir.signal)


# In[5]:


sns.displot(fmir["signal"])


# In[6]:


sns.displot(fmir["timepoint"])


# ## Q3.Load the ''titanic" dataset using the load_dataset function of seaborn.Plot two box plots using x= 'pclass',y='age' and y='fare'.
# 
# ## Note:- pclass,age and fare are columns in the titanic dataset.
# 
# ### Ans:-

# In[7]:


tit=sns.load_dataset('titanic')


# In[8]:


tit


# In[9]:


tit.head()


# In[10]:


sns.boxplot(x=tit.pclass,y=tit.age)
#sns.barplot(x=tit.pclass,y=tit.fare)


# In[11]:


sns.barplot(x=tit.pclass,y=tit.fare)


# ## Q4. Use the "diamonds"dataset from seaborn to plot a histogram for the 'Price'column. use the hue parameter for the 'cut' column of the diamonds dataset.
# 
# ### Ans:-

# In[12]:


df=sns.load_dataset('diamonds')
df


# In[13]:


sns.histplot(df["price"])


# In[14]:


sns.histplot(data=df, x='price', hue='cut')


# ## Q5. Use the "iris" dataset from seaborn to plot a pair plot. use the hue parameter 'species' column of the iris dataset.
# 
# ### Ans:-
# 

# In[15]:


iris=sns.load_dataset('iris')
iris


# In[16]:


sns.pairplot(data=iris,hue ="species")


# ## Q6.Use the 'flights' dataset from seaborn to plot a heatmap.
# 
# ### Ans:-

# In[17]:


flight_data=sns.load_dataset('flights')
flight_data


# In[18]:


flight_data_pivot=flight_data.pivot("month","year","passengers")
sns.heatmap(flight_data_pivot,cmap="PiYG_r")


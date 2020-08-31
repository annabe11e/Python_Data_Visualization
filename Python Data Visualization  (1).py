#!/usr/bin/env python
# coding: utf-8

# A survey was conducted to gauge an audience interest in different data science topics, namely:
# 
# Big Data (Spark / Hadoop)
# Data Analysis / Statistics
# Data Journalism
# Data Visualization
# Deep Learning
# Machine Learning
# The participants had three options for each topic: Very Interested, Somewhat interested, and Not interested. 2,233 respondents completed the survey.
# 
# The survey results have been saved in a csv file and can be accessed through this link: https://cocl.us/datascience_survey_data.
# 
# If you examine the csv file, you will find that the first column represents the data science topics and the first row represents the choices for each topic.
# 
# Use the pandas read_csv method to read the csv file into a pandas dataframe.
# 

# In[1]:


import numpy as np  
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium


# In[3]:


df=pd.read_csv("https://cocl.us/datascience_survey_data",index_col=0)
df.head()


# Use Matplotlib to replicate the bar chart below to visualize the percentage of the respondents' interest

# In[4]:


df.sort_values(by='Very interested', ascending=False, axis=0, inplace=True)
df.head()


# In[5]:


df['Total'] = df.sum(axis=1)
df['Very Interested']=(df['Very interested']/df['Total']).round(2)
df['Somewhat Interested']=(df['Somewhat interested']/df['Total']).round(2)
df['Not Interested']=(df['Not interested']/df['Total']).round(2)
df_s=df[['Very Interested','Somewhat Interested','Not Interested']]
df_s.head()


# In[29]:


mpl.style.use('ggplot')
p=df_s.plot(kind='bar',width=0.8,color=['#5cb85c', '#5bc0de', '#d9534f'])
figsize=(15,4)
p.axes.get_yaxis().set_visible(False)
p.axes.spines['right'].set_visible(False)
p.axes.spines['top'].set_visible(False)
p.axes.spines['left'].set_visible(False)
plt.title("Precentage of Respondents'Interests in Data Science",size=10) # add title to the plot
plt.legend(prop={'size': 8})
p.patch.set_visible(False)

for n in p.patches:
    width = n.get_width()
    height = n.get_height()
    x, y = n.get_xy() 
    p.annotate(f'{height}', (x + width/2, y + height*1.02), ha='center',size=7)


# In the final lab, we created a map with markers to explore crime rate in San Francisco, California. In this question, you are required to create a Choropleth map to visualize crime in San Francisco.
# 
# Before you are ready to start building the map, let's restructure the data so that it is in the right format for the Choropleth map. Essentially, you will need to create a dataframe that lists each neighborhood in San Francisco along with the corresponding total number of crimes.
# 
# Based on the San Francisco crime dataset, you will find that San Francisco consists of 10 main neighborhoods, namely:
# Central,
# Southern,
# Bayview,
# Mission,
# Park,
# Richmond,
# Ingleside,
# Taraval,
# Northern, and,
# Tenderloin.
# Convert the San Francisco dataset, which you can also find here, https://cocl.us/sanfran_crime_dataset, into a pandas dataframe, like the one shown below, that represents the total number of crimes in each neighborhood.

# In[7]:


df2=pd.read_csv('https://cocl.us/sanfran_crime_dataset')
df2.drop(['IncidntNum','Category','Descript','DayOfWeek','Date','Time','Resolution'], axis=1, inplace=True)
df2.head()


# In[8]:


#df2.count(['PdDistrict']=='SOUTHERN')
c=df2.pivot_table(index=['PdDistrict'], aggfunc='size')
c=c.to_frame()
c.reset_index(inplace=True)
c.columns = ['Neighborhood','Count']
c


# Now you should be ready to proceed with creating the Choropleth map.
# 
# As you learned in the Choropleth maps lab, you will need a GeoJSON file that marks the boundaries of the different neighborhoods in San Francisco. In order to save you the hassle of looking for the right file, I already downloaded it for you and I am making it available via this link: https://cocl.us/sanfran_geojson.
# 
# For the map, make sure that:
# 
# it is centred around San Francisco,
# you use a zoom level of 12,
# you use fill_color = 'YlOrRd',
# you define fill_opacity = 0.7,
# you define line_opacity=0.2, and,
# you define a legend and use the default threshold scale.

# In[9]:


import wget
url = 'https://cocl.us/sanfran_geojson'
geo  = wget.download(url)


# In[15]:


# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42
map = folium.Map(location=[latitude, longitude], zoom_start=12)
map.choropleth(
    geo_data=geo,
    data=c,
    columns=['Neighborhood','Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='crime rate in San Francisco, California'
)
map


# In[ ]:





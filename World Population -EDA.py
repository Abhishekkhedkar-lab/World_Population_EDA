#!/usr/bin/env python
# coding: utf-8

# # World Population -EDA

#   This dataset collects the population of all countries in the world since 2022. The world's population is steadily growing and will continue to grow through the coming decades. This dataset will be used to highlight Countries and Continents respective populations to gather further insight into the world population to find any trends that can be found. Time to dive in! 
# 

# ## Data Preparation

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


dp=pd.read_csv('world_population.csv')
dp


# In[5]:


pd.set_option("display.float_format", lambda x:'%.2f'%x)


# ## Understand the structure of data 

# In[7]:


dp.info()


# In[8]:


dp.describe()


# In[9]:


dp.describe(include='object')


# In[10]:


dp.nunique()


# In[11]:


# handling null values


# In[12]:


dp.isnull().sum()


# In[13]:


dp.isnull().sum()*100/len(dp)


# In[14]:


np=dp.fillna(0)
np


# In[15]:


np.isnull().sum()


# ## Analysis

# In[17]:


Top_ten=np.sort_values(by="World Population Percentage", ascending=False).head(10)
Top_ten


# In[18]:


numeric_values=np.select_dtypes(include='number')
numeric_values.corr()


# In[139]:


sns.heatmap(numeric_values.corr(),annot=True)
plt.rcParams['figure.figsize'] = (30,10)
plt.show()


# In[65]:


df=np.groupby('Continent')[['1970 Population','1980 Population','1990 Population','2000 Population', '2010 Population',
                            '2015 Population','2020 Population','2022 Population']].mean("2022 Population").sort_values(by="2022 Population",ascending=False)
df


# In[66]:


df2=df.transpose()
df2


# In[67]:


df2.plot()


# In[68]:


df.boxplot(figsize=(20,7))


# ## Section 1: Descriptive Analysis Section for Population 

# Descriptive Analysis
# What are the top ten biggest countries in 2022?
# 

# In[69]:


ax=sns.barplot(x='2022 Population',y='Country',data=Top_ten)
plt.show()


# What are the top ten biggest countries in 1970?

# In[70]:


ax=sns.barplot(x='1970 Population',y='Country',data=Top_ten)
plt.show()


# ## Key Insights from the graph above: 

# China still had a decent lead ahead of Inida in the 1970s regarding population.
# Japan, Germany were some of the more populous countries in the 1970s and now are not in the top ten.
# Pakistan grew greatly being the 10th largest country to the fifth largest country in only 40 years!

# In[71]:


cf=np.groupby('Country')[['1970 Population','1980 Population','1990 Population','2000 Population', '2010 Population',
                            '2015 Population','2020 Population','2022 Population']].mean("2022 Population").sort_values(by="2022 Population",ascending=False).head(10)
cf2=cf.transpose()
cf2


# ## Section 2: Descriptive Analysis Section for Continents

# Descriptive Analysis 
# Which continents are the biggest by population?

# In[72]:


continent_rank=df.groupby('Continent')[['2022 Population']].mean("2022 Population").sort_values(by="2022 Population",ascending=False).head()
continent_rank


# In[97]:


plt.figure(figsize=(5,5))
sns.set_style("whitegrid")
palette_color = sns.color_palette('dark') 
explode = [0, 0.1, 0, 0, 0] 
plt.pie(x='2022 Population',labels=["Asia",'South America','Africa','North America','Europe'],colors=palette_color, 
        explode=explode, autopct='%.0f%%',startangle=90,data=continent_rank)
plt.title('Continent: biggest by population')
plt.show()


# # Key insights from chart
# * Asia is by far the largest Continent in terms of Population with two of the largest countries in population (China & India) greatly contributing to this 
# * Oceania is by far the smallest population by Continent.
# 

# ## Section 3: Descriptive Analysis Section for Area/Density
# 
# 

# Descriptive Analysis
# Top 50 Countries by Area and thier relation to Density.

# In[133]:


Top_50 = np.nlargest(50, 'Area (km²)')
Top_50


# In[134]:


cx=plt.scatter(data=Top_50,x='Area (km²)',y='Density (per km²)',c='Area (km²)')


# # Key Insights from the graph above:

#  *Lots of countries that have large areas do not have large densities of populations such as Russia. 
#  *Countries like India and Pakistan have large areas but also have large Densities per km^2

# ## Section 4: Correalation Heatmap

# Predictive Analysis
# Is there any correalation with Area and Populaion?

# In[137]:


sns.set(rc = {"figure.figsize":(10,10)})

Numeric_Only = np[['Area (km²)','Density (per km²)',
                   'Growth Rate', '2022 Population' ]]

Correlation = Numeric_Only.corr()
Correlation_Graph = sns.heatmap(Correlation, annot = True).set(title = 'Correlation Heatmap of Selected Numeric Variables')


# ## Key Insights from the graph above:

# * When the Area of Country increases, so does the Population of that country.
# * Area and Density are negatively correlated as when Area of a Country increases, the density of the population decreases.

# In[ ]:





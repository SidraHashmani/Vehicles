#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[20]:


df = pd.read_csv(r'C:\Users\ahaqu\Downloads\vehicles_us (1).csv')
df.sample(n=10)


# In[3]:





# In[4]:


st.header('Market of Vehicles. Original data')
st.write(""" Filter the data below""")
show_fuel_cars = st.checkbox("Include diesel type")


# In[5]:


if not show_fuel_cars:
    df=df[df.fuel!='diesel']


# In[6]:


cylinder_type = df['cylinders'].unique()
choose_cylinder= st.selectbox('Select Cylinder', cylinder_type)


# In[7]:


choose_cylinder


# In[8]:


type_choice= df['type'].unique()
choose_type = st.selectbox('Select Type', type_choice)


# In[9]:


choose_type


# In[10]:


condition_choice = df['condition'].unique()
choose_condition= st.selectbox('Select Condition',condition_choice)


# In[11]:


choose_condition


# In[12]:


min_year,max_year=int(df['model_year'].min()),int(df['model_year'].max())
year_range = st.slider(
    "Choose Year", 
    value =(min_year,max_year),min_value = min_year, max_value=max_year)

print(year_range)
# In[13]:


actual_range= list(range(year_range[0],year_range[1]+1))


# In[14]:


filtered_cylinder = df[(df.cylinders==choose_cylinder)& (df.model_year.isin(list(actual_range)))]

st.table(filtered_cylinder)


# In[15]:


filtered_condition = df[(df.condition==choose_condition)& (df.model_year.isin(list(actual_range)))]

st.table(filtered_condition)


# In[16]:


filtered_type = df[(df.type==choose_type)& (df.model_year.isin(list(actual_range)))]

st.table(filtered_type)


# In[21]:


st.header('Price analysis')
st.write("""
#### Let's analyze what influences price the most. 
We'll analyze how pricing varies depending on type, condition and transmission""")

import plotly.express as px

list_for_hist =['transmission', 'type', 'cylinders', 'condition']
choice_for_hist = st.selectbox("Split for price distribution", list_for_hist)

fig1= px.histogram(df, x='price', color=choice_for_hist)
fig1.update_layout(title="<b> Split for price by{}</b>".format(choice_for_hist))

st.plotly_chart(fig1)


# In[ ]:


fig1.show()


# In[ ]:


df['age']= 2022-df['model_year']

def age_category(x):
    if x<5:return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
    
df['age_category']= df['age'].apply(age_category)


# In[24]:


st.write("""
##### Let's check how price is affected by odometer, paint color and  days listed""")

list_for_scatters = ['odometer', 'paint_color', 'days_listed']
choice_for_scatter = st.selectbox("Price dependency on", list_for_scatters)

fig2= px.scatter(df, x='price', y= choice_for_scatter, hover_data = ['model_year'])

fig2.update_layout(
    title="<b> Price vs{}</b>".format(choice_for_scatter))
    


# In[25]:





# In[28]:




# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[1]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[ ]:





# In[2]:


# Item Added From Toolbar
# Title: NewStreetsTwo | Type: Feature Service | Owner: flom0040_UMN
item = gis.content.get("32425a394f9548f79bc516786541b92c")
item


# In[ ]:





# In[3]:


from arcgis import features
features.use_proximity.create_buffers(item, distances=[10], units = 'Meters')


# In[4]:


streets = features.use_proximity.create_buffers(item, distances=[10], units = 'Meters')


# In[5]:


display(streets)


# In[6]:


display(item)


# In[7]:


item.add_layer(streets)
display(item)


# In[8]:


display(item)


# In[11]:


streets = features.use_proximity.create_buffers(item, distances=[10], units = 'Meters')


# In[12]:


print(type(streets))


# In[14]:


street_map = gis.map('USA')
display(street_map)


# In[16]:


street_map.add_layer(streets)
display(street_map)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
input_folder = r'D:\Wires'
filenames = [f.path for f in os.scandir(input_folder) if f.is_file() and f.path.endswith(('.png', '.jpg', '.jpeg'))]


# In[4]:


from skimage.transform import resize
    


# In[8]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


len(filenames)


# In[20]:


filenames[2]


# In[29]:


img = [0]* len(filenames)
for i in range(len(filenames)):
    img[i] = plt.imread(filenames[i])


# In[30]:


plt.imshow(img[3])


# In[36]:


img[3].shape


# In[39]:


res_img = [0] * len(img)


# In[76]:


for i in range(len(img)) :
    res_img[i] = resize(img[i], (240,240))
    
    


# In[77]:


plt.imshow(res_img[99])


# In[78]:


type(res_img[3])


# In[80]:


import numpy as np


# In[81]:


r_img = np.array(res_img)


# In[82]:


r_img.shape


# In[88]:


lr_img = [0] * len(r_img)
for i in range(len(r_img)):
    lr_img[i] = r_img[i].reshape(57600,3)


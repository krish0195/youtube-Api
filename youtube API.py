#!/usr/bin/env python
# coding: utf-8

# In[24]:


import requests
import pandas as pd
import time

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


#api key
api_key="AIzaSyADLg12ESUwps-IXeI7yQjItesdll--ApI"
channel_id="UCueYcgdqos0_PzNOq81zAFg"


# In[13]:



pageToken = ""
url = "https://www.googleapis.com/youtube/v3/search?key="+api_key+"&channelId="+channel_id+"&part=snippet,id&order=date&maxResults=10000&"+pageToken
response = requests.get(url).json()


# In[14]:


response


# In[18]:


df = pd.DataFrame(columns=["video_id","video_title","upload_date","view_count","like_count","comment_count"]) 


# In[ ]:





# In[19]:


for video in response['items']:
   if video['id']['kind'] == "youtube#video":
       video_id = video['id']['videoId']
       video_title = video['snippet']['title']
       video_title = str(video_title).replace("&amp;","")
       upload_date = video['snippet']['publishedAt']
       upload_date = str(upload_date).split("T")[0]
       
       
     #collecting view, like, dislike, comment counts
       url_video_stats = "https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&part=statistics&key="+api_key
       response_video_stats = requests.get(url_video_stats).json()
       response_video_stats

       view_count = response_video_stats['items'][0]['statistics']['viewCount']
       like_count = response_video_stats['items'][0]['statistics']['likeCount']
       #dislike_count = response_video_stats['items'][0]['statistics']['dislikeCount']
       comment_count = response_video_stats['items'][0]['statistics']['commentCount']

       
       print(video_id)
       print(video_title)
       print(upload_date)
       print(view_count)
       print(like_count)
       print(comment_count)
       
       df = df.append({'video_id':video_id,'video_title':video_title,
                               "upload_date":upload_date,"view_count":view_count,
                               "like_count":like_count,"comment_count":comment_count},ignore_index=True)
      
       


# In[21]:


df.head()


# In[22]:


df.info()


# In[38]:


df.info()


# In[43]:


df.describe(include="all").T


# In[48]:


df.dtypes


# In[55]:


df["view_count"] = df["view_count"].astype(str).astype(int)
df["like_count"] = df["like_count"].astype(str).astype(int)
df["comment_count"] = df["comment_count"].astype(str).astype(int)
df["upload_date"] = pd.to_datetime(df["upload_date"])


# In[56]:


df.dtypes


# In[67]:


df.to_csv('parithabangal.csv')


# In[68]:


df.hist(figsize=(10,10))


# In[69]:


data_bins=df


# In[70]:


data_bins['bins']=pd.cut(data_bins['upload_date'],6, labels =["A", "B", "C","E","F","G"])


# In[71]:


data_bins.head()


# In[72]:


data_bins.hist(figsize=(10,10))


# In[ ]:





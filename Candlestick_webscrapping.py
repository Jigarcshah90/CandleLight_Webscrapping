#!/usr/bin/env python
# coding: utf-8

# In[46]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
from lxml import html
import urllib.request


# In[47]:


driver = webdriver.Chrome("C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver")


# In[48]:


driver.get("https://www.feedroll.com/candlestick-patterns/1309-index-candlestick-patterns/")
#page = requests.get("https://www.feedroll.com/candlestick-patterns/1309-index-candlestick-patterns/")


# In[49]:


content = driver.page_source
soup = BeautifulSoup(content)


# In[50]:


#tb = soup.findAll('div', attrs={'class':'content-left-wrap'})


# In[51]:


#tb


# In[52]:


#import urllib2
import re
page=[]
df = pd.DataFrame({'link':page})
for link in soup.findAll('a', attrs={'href': re.compile("^https://www.feedroll.com/candlestick-patterns")}):
    pages=(link.get('href'))
    #print(pages)
    page.append(pages)    
page_df = pd.DataFrame(page,columns=['link_name'])
page_df = page_df['link_name'].unique()
page_df = page_df[4:]    


# In[53]:


#page_df[0]


# In[54]:


#page_df[0]
#driver.get(page_df[0])
#soup = BeautifulSoup(driver.page_source)
#soup.findAll('div', attrs={'class':'span8 content-left'})
#pages_img=link.find('div', attrs={'class':'_3wU53n'})


# In[55]:


#for a in soup.findAll('div', attrs={'class':'span8 content-left'}):
#    #name=a.find('img')
#    name=a.find('img')


# In[56]:


#name


# In[57]:


#image_link = name['src']
#image_link


# In[58]:


#driver.get(image_link)


# In[59]:


#file_name= image_link.split('/')
#file_name[-1]
#file_name = 'C:\\Data Science Material\\Candle_image\\'+file_name[-1]
#file_name


# In[ ]:





# In[60]:


#urllib.request.urlretrieve(image_link, "C:\\Data Science Material\\Candle_image\\local-filename.jpg")


# In[44]:


for i in range(0,len(page_df)):
    page_df[i]
    driver.get(page_df[i])
    soup = BeautifulSoup(driver.page_source)
    soup.findAll('div', attrs={'class':'span8 content-left'})
    for a in soup.findAll('div', attrs={'class':'span8 content-left'}):
        name=a.find('img')
        image_link = name['src']
        driver.get(image_link)
        file_name= image_link.split('/')
        file_name[-1]
        file_name = 'C:\\Data Science Material\\Candle_image\\'+file_name[-1]
        urllib.request.urlretrieve(image_link, file_name)
    i=i-1


# In[ ]:





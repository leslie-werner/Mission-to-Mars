#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import dependencies
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[4]:


#Setting up executable path in cell and URL for scraping
#executable_path = {'executable_path': ChromeDriverManager().install()}
#browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Assigning url and instructing browser to visit it. Visit the mars nasa news site
#url = 'https://redplanetscience.com'
#browser.visit(url)
# Optional delay for loading the page
#browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


#html = browser.html
#news_soup = soup(html, 'html.parser')
#slide_elem = news_soup.select_one('div.list_text')


# In[ ]:





# In[6]:


# use to scrape the articles title
#slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
##news_title


# In[8]:


# Use the parent element to find the paragraph text. using .find() 
# instead of .find_all() will pull only the top one
#news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
#news_p


# In[5]:


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


# ### Featured Images

# In[9]:


# will be creating a code to automate our clicks


# In[10]:


# Visit URL
#url = 'https://spaceimages-mars.com'
#browser.visit(url)


# In[11]:


# Find and click the full image button
#full_image_elem = browser.find_by_tag('button')[1]
#full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
#html = browser.html
#img_soup = soup(html, 'html.parser')


# In[13]:


# Find the relative image url
#img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
#img_url_rel


# In[14]:


# Use the base URL to create an absolute URL
#img_url = f'https://spaceimages-mars.com/{img_url_rel}'
#img_url


# In[6]:


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url


# In[7]:


# Scrape the entire table with Pandas' .read_html() function
# [0] specifies that we want first table or first list
#df = pd.read_html('https://galaxyfacts-mars.com')[0]
##df.columns=['description', 'Mars', 'Earth']
# remember inplace=True means updated index will remain in place
# w/out reassign the DF to new variable
#df.set_index('description', inplace=True)
#df


# In[8]:


# # covert DF back to HTML to update on webpage too
#df.to_html()


# In[9]:


def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()


# In[34]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[35]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[36]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[37]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[38]:


slide_elem.find('div', class_='content_title')


# In[39]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[40]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[41]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[42]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[43]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[44]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[45]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[46]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[47]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[48]:


df.to_html()


# D1: SCRAPE HIGH-RESOLUTION MARS' HEMISPHERE IMAGES AND TITLES

# In[57]:


# Import Dependencies
from bs4 import BeautifulSoup as bs
import requests


# In[58]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[59]:


#Request url
response = requests.get(url)


# In[135]:


# BeatifulSoup
soup = bs(response.text, 'html.parser')


# In[109]:


# Returning results
hemisphere_info = soup.find_all('div', class_ = "item")


# In[110]:


#Check to make sure correct info was called
print(hemisphere_info)


# In[154]:


# Verifying length is correct
len(hemisphere_info)


# In[150]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#html tag that holds all the links to full resolution = 
#hemisphere_images = soup.find_all('img', class_ = "thumb")
# use for loop
for hemisphere in hemisphere_info:
    #create empty hemispheres = {}
    hemispheres = {}
    link = hemisphere.a['href'] 
    title = hemisphere.find('h3').text
       
    #d) use browser.back() to navigate back to the beginning to get the next hemisphere image.
    hemispheres = {
        'img_url': img_url,
        'title': title,
    }
    hemisphere_image_urls.append(hemispheres)
    print(title)
    print(link)
    browser.back()


# In[151]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[153]:


browser.quit()


# In[ ]:





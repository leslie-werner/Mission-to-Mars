# Import dependencies
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


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


# In[15]:


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

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup



# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# D1: SCRAPE HIGH-RESOLUTION MARS' HEMISPHERE IMAGES AND TITLES

# Import Dependencies
from bs4 import BeautifulSoup as bs
import requests


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


#Request url
response = requests.get(url)

# BeatifulSoup
soup = bs(response.text, 'html.parser')


# Returning results
hemisphere_info = soup.find_all('div', class_ = "item")

#Check to make sure correct info was called
print(hemisphere_info)

#hemisphere_info = soup.find_all('img', class_="thumb")

#hemisphere_info

# Verifying length is correct
len(hemisphere_info)

hemisphere_info_img = soup.find_all('img', class_="thumb")
hemispheres_one = []
for hemisphere in hemisphere_info_img:
    #create empty hemispheres = {}
    
    
    link = hemisphere.get('src') 
    #title = hemisphere.find('h3').text
       
    #d) use browser.back() to navigate back to the beginning to get the next hemisphere image.
    hemispheres_one.append(link)
    
#     hemisphere_image_urls.append(hemispheres)
    print(link)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
#hemisphere_info_img = soup.find_all('img', class_="thumb")
# 3. Write code to retrieve the image urls and titles for each hemisphere.
#html tag that holds all the links to full resolution = 
#hemisphere_images = soup.find_all('img', class_ = "thumb")
# use for loop
i=0
for hemisphere in hemisphere_info:
    #create empty hemispheres = {}
    hemispheres = {}
    #hemisphere_info_img[i]
    
    link = hemispheres_one[i]
    title = hemisphere.find('h3').text
       
    #d) use browser.back() to navigate back to the beginning to get the next hemisphere image.
    hemispheres = {
        'img_url': link,
        'title': title,
    }
    hemisphere_image_urls.append(hemispheres)
    i=i+1
    print(title)
    print(link)
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

browser.quit()




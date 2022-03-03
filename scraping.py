
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager
import requests

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
         #"hemisphere": hemisphere(browser)
         "hemisphere": hemisphere(browser)
    }


    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
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


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
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
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

# D2 -----------------------------------------------------------------------

hemisphere_image_urls = []
def hemisphere(browser):

    url = 'https://marshemispheres.com/'
    browser.visit(url)
        #Request url
    response = requests.get(url)
        # BeatifulSoup
    #html = browser.html
    soup = soup(response.text, 'html.parser')
        # Returning results
    hemisphere_info = soup.find_all('div', class_ = "item")
    hemisphere_info_img = soup.find_all('img', class_="thumb")
    hemispheres_one = []
    for hemisphere in hemisphere_info_img:
            #create empty hemispheres = {}
        link = hemisphere.get('src') 
        
            #d) use browser.back() to navigate back to the beginning to get the next hemisphere image.
        hemispheres_one.append(link)
        
            # hemisphere_image_urls.append(hemispheres)
        print(link)
    
        # 2. Create a list to hold the images and titles.
    # hemisphere_image_urls = []
        #hemisphere_info_img = soup.find_all('img', class_="thumb")
        # 3. Write code to retrieve the image urls and titles for each hemisphere.
        #html tag that holds all the links to full resolution = 
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
        #print(title)
        #print(link)
        browser.back()
    return hemisphere_image_urls


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
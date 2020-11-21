#day 2 activity 10
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    #part 1 Retriving the news Article title and paragragph
    #reference Day 2 most activities
    marURL= 'https://mars.nasa.gov/news/'
    browser.visit(marURL)

    time.sleep(1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    item_list = soup.find('ul', class_ = 'item_list')
    slide = item_list.find('li', class_ = 'slide')
    #Activity 7
    #get title
    news_title = slide.find('div', class_ = 'content_title').text
    #get paragragp
    news_p = slide.find('div', class_ = 'article_teaser_body').text

    #Part 2 Getting Photo from jpl

    jplURL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jplURL)

    time.sleep(1)

    #Part 2 Getting Photo from jpl

    jplURL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jplURL)

    time.sleep(1)

    #Day 2 activity 8 
    #click on the box to access the image
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    jpg = soup.find('figure', class_='lede').find('a')['href']
    #combine the link
    featured_image_url = f'https://www.jpl.nasa.gov{jpg}'


    
    #Part 3 Mars Fact
    #Day 2 Activity 9-10

    factURL = 'https://space-facts.com/mars/'
    browser.visit(factURL)
    tables = pd.read_html(factURL)

    marsTables = tables[0]

    #assigning labesl 
    marsTables.columns = ['', 'Mars']
    marsTables

    htmlTable = marsTables.to_html(index = False)

    # #Part 4 Hemisphere Image
    hemisphere_image_urls = []
    hemURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemURL)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('div', class_ = 'collapsible results').find_all('div', class_ = 'item')

    for hem in item:
        #image title
        imgTitle = hem.find('h3').text
        #click on the link to get larger images size
        browser.click_link_by_partial_text(imgTitle)
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        imgURL = soup.find('div', class_ = 'downloads').find('li').find('a')['href']
        
        dictionary = {"title" : imgTitle, "img_url": imgURL}
        hemisphere_image_urls.append(dictionary)
        #moving back on the browser https://splinter.readthedocs.io/en/latest/browser.html
        browser.back()

        # Close the browser after scraping
    browser.quit()
        
    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p" : news_p,
        "featured_image_url" : featured_image_url,
        "mars_facts": htmlTable,
        "hemisphere_image_urls" : hemisphere_image_urls
    }
    # Return results
    return mars_data

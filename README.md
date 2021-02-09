# Web Scraping Homework - Mission to Mars


Buit  a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 
### Before You Begin



## Scraped Websites 
* Nasa News article from [here](https://mars.nasa.gov/news/).
* JPL Featured from [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
* Mars Facts from [here](https://space-facts.com/mars/).
* Hemisphere information from [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) .

Used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` for all scarping.

## MongoDB and Flask 

Used MongoDB with Flask template to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.


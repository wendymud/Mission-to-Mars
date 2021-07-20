# Import Splinter and BeautifulSoupfrom splinter import Browser
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome #import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the Mars NASA site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

# Assign the title and summary text to variable
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# In Featured Images
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# revert code back to HTML
df.to_html()

# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
 

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# Convert the browser html to a soup object
html = browser.html
news_soup = soup(html, 'html.parser')

#define full_image variable outside the for loop
full_image = browser.find_by_css('a.product-item img')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#All of the hemispheres
for i in range(len(full_image)):
    hemi={}
    full_image = browser.find_by_css('a.product-item img')[i].click()
    full_image1 = browser.find_by_text('Sample').first
    hemi['title'] = browser.find_by_css('h2.title').text
    hemi['image_url'] = full_image1['href']
# Append hemisphere object to list
    hemisphere_image_urls.append(hemi)
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
print(hemisphere_image_urls)

# 5. Quit the browser
browser.quit()

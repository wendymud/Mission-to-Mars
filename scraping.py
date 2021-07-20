# Import Splinter and BeautifulSoupfrom splinter import Browser
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():   
    ## Initiate headless driver for deployment
    executable_path = {'executable_path': 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    
    news_title, news_paragraph = mars_news(browser)
    
    
    #Run all scraping functions and store results in dictionary: 
    data = {
            "news_title": news_title,
            "news_paragraph": news_paragraph,
            "featured_image": featured_image(browser),
            "facts": mars_facts(),
            "last modified": dt.datetime.now(),
            "hemisphere_data": img_urls(browser)
    }
    # stop webdriver and return data
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
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars.s3.amazonaws.com/Mars/index.html')[0]
    
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def img_urls(browser):
    # List the URL 
    url = 'https://marshemispheres.com'
    browser.visit(url)
    # Create a list to hold the images and titles.
    # hemisphere_image_urls = []

    pics = browser.find_by_css('a.itemLink img')
    # print(len(pics))

    # # 3. Write code to retrieve the image urls and titles for each hemisphere.
    # for i in range(len(pics)):
    #     hemispheres={}
    #     browser.find_by_css('a.itemLink img')[i].click()
    #     sampleImg = browser.find_by_text('Sample').first
    #     hemispheres['title'] = browser.find_by_css('h2.title').text
    #     hemispheres['image_url'] = url+sampleImg['href']
    #     # Append hemisphere object to list
    #     # hemisphere_data = scrape_hemisphere(browser.html)
    #     hemisphere_image_urls.append(hemispheres)
    #     browser.back()

    # return hemisphere_image_urls
    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    #All of the hemispheres
    for i in range(len(pics)):
        hemi={}
        full_image = browser.find_by_css('a.product-item img')[i].click()
        full_image1 = browser.find_by_text('Sample').first
        hemi['title'] = browser.find_by_css('h2.title').text
        hemi['image_url'] = full_image1['href']
    # Append hemisphere object to list
        hemisphere_image_urls.append(hemi)
        browser.back()

    return hemisphere_image_urls

if __name__ == "__main__":
        

    # 4. Print the list that holds the dictionary of each image url and title.
    print(scrape_all)
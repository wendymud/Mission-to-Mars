{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ad19bbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoupfrom splinter import Browser\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0695d5b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up Splinter\n",
    "executable_path = {'executable_path': 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "650165c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Mars NASA site\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e9d3168",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bae02ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Assign the title and summary text to variable\n",
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3477df80",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3897ba9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de645042",
   "metadata": {},
   "source": [
    "### Featured Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "409df5c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b77e10a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf98c3df",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82d4b27c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65043dc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c2f5100",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ae24411",
   "metadata": {},
   "outputs": [],
   "source": [
    "# revert code back to HTML\n",
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e12d0dbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2905c056",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter, BeautifulSoup, and Pandas\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82d84215",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the executable path and initialize Splinter\n",
    "executable_path = {'executable_path': 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb08a534",
   "metadata": {},
   "source": [
    "### Visit the NASA Mars News Site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18245b04",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Mars NASA site\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36d6a803",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the browser html to a soup object and then quit the browser\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2d3cdef",
   "metadata": {},
   "outputs": [],
   "source": [
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "088baff6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the first a tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c096ebb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7310f0b",
   "metadata": {},
   "source": [
    "### JPL Space Images Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41909bc4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "683203fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62c8576a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')\n",
    "img_soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b75aa247",
   "metadata": {},
   "outputs": [],
   "source": [
    "# find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "662726f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the base url to create an absolute url\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b7e65eb",
   "metadata": {},
   "source": [
    "### Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d743bc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04cced2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.columns=['Description', 'Mars', 'Earth']\n",
    "df.set_index('Description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63404fef",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00e5665e",
   "metadata": {},
   "source": [
    "# D1: Scrape High-Resolution Mars??? Hemisphere Images and Titles\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "135fd536",
   "metadata": {},
   "source": [
    "### Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4b3e8c79",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://marshemispheres.com/'\n",
    "\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a622b54",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the browser html to a soup object\n",
    "# html = browser.html\n",
    "# news_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0d94a2ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "full_image = browser.find_by_css('a.product-item img')\n",
    "#full_image.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bfcd4760",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "#All of the hemispheres\n",
    "for i in range(len(full_image)):\n",
    "    hemi={}\n",
    "    full_image = browser.find_by_css('a.product-item img')[i].click()\n",
    "    full_image1 = browser.find_by_text('Sample').first\n",
    "    hemi['title'] = browser.find_by_css('h2.title').text\n",
    "    hemi['image_url'] = full_image1['href']\n",
    "# Append hemisphere object to list\n",
    "    hemisphere_image_urls.append(hemi)\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "145c74f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'https://marshemispheres.com/images/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "print(hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "86b1dd32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>image_url</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Cerberus Hemisphere Enhanced</td>\n",
       "      <td>https://marshemispheres.com/images/full.jpg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Schiaparelli Hemisphere Enhanced</td>\n",
       "      <td>https://marshemispheres.com/images/schiaparell...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Syrtis Major Hemisphere Enhanced</td>\n",
       "      <td>https://marshemispheres.com/images/syrtis_majo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Valles Marineris Hemisphere Enhanced</td>\n",
       "      <td>https://marshemispheres.com/images/valles_mari...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                  title  \\\n",
       "0          Cerberus Hemisphere Enhanced   \n",
       "1      Schiaparelli Hemisphere Enhanced   \n",
       "2      Syrtis Major Hemisphere Enhanced   \n",
       "3  Valles Marineris Hemisphere Enhanced   \n",
       "\n",
       "                                           image_url  \n",
       "0        https://marshemispheres.com/images/full.jpg  \n",
       "1  https://marshemispheres.com/images/schiaparell...  \n",
       "2  https://marshemispheres.com/images/syrtis_majo...  \n",
       "3  https://marshemispheres.com/images/valles_mari...  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a DataFrame from the lis. \n",
    "hemi_image = pd.DataFrame(hemisphere_image_urls)\n",
    "hemi_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "35ebe5e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>image_url</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>https://marshemispheres.com/images/full.jpg</td>\n",
       "      <td>Cerberus Hemisphere Enhanced</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>https://marshemispheres.com/images/schiaparell...</td>\n",
       "      <td>Schiaparelli Hemisphere Enhanced</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>https://marshemispheres.com/images/syrtis_majo...</td>\n",
       "      <td>Syrtis Major Hemisphere Enhanced</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>https://marshemispheres.com/images/valles_mari...</td>\n",
       "      <td>Valles Marineris Hemisphere Enhanced</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                           image_url  \\\n",
       "0        https://marshemispheres.com/images/full.jpg   \n",
       "1  https://marshemispheres.com/images/schiaparell...   \n",
       "2  https://marshemispheres.com/images/syrtis_majo...   \n",
       "3  https://marshemispheres.com/images/valles_mari...   \n",
       "\n",
       "                                  title  \n",
       "0          Cerberus Hemisphere Enhanced  \n",
       "1      Schiaparelli Hemisphere Enhanced  \n",
       "2      Syrtis Major Hemisphere Enhanced  \n",
       "3  Valles Marineris Hemisphere Enhanced  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reorder df\n",
    "hemi_image = hemi_image[['image_url', 'title']]\n",
    "hemi_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "184801b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'image_url': {0: 'https://marshemispheres.com/images/full.jpg',\n",
       "  1: 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg',\n",
       "  2: 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg',\n",
       "  3: 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'},\n",
       " 'title': {0: 'Cerberus Hemisphere Enhanced',\n",
       "  1: 'Schiaparelli Hemisphere Enhanced',\n",
       "  2: 'Syrtis Major Hemisphere Enhanced',\n",
       "  3: 'Valles Marineris Hemisphere Enhanced'}}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemi_image.to_dict()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f03d5a1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f78216f2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

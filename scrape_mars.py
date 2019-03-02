import pandas as pd 
import time 
import requests 
import pymongo 
from bs4 import BeautifulSoup 
from splinter import Browser 

def init_browser():
	executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
	return Browser('chrome', **executable_path, headless=False)

def scrape():
	browser = init_browser
	url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	browser.visit(url)
	response = browser.html 
	soup = BeautifulSoup(response, 'html.parser')
	new_title = soup.find('div', 'content_title', 'a').text
	new_p = soup.find('div', 'article_teaser_body').text
	print(new_title)
	print(new_p)
	articles = soup.find_all('div', 'content_title')
	article_list = [] 
	#loop through article titles 
	for article in articles: 
    	article_list.append(article.find('a').text) 
    	print(article.find('a').text)


    url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url1)
	response = browser.html 
	soup = BeautifulSoup(response, 'html.parser')

	mars_image = soup.find('img', class_='thumb')['src']
	featured_image_url = url1 + mars_image

	print(featured_image_url)


	url2 = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url2)
	response = browser.html 
	soup = BeautifulSoup(response, 'html.parser')

	mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text 
	print(mars_weather)


	url3 = 'http://space-facts.com/mars/'
	browser.visit(url3)
	mars_fact = pd.read_html(url3)
	mars_fact
	mars_fact_df = pd.DataFrame(mars_fact[0])
	mars_fact_df.head(9)


	url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url4)
	response = browser.html 
	soup = BeautifulSoup(response, 'html.parser')
	mars_hemisphere = []
	for x in range(4):
	    time.sleep(5)
	    images = browser.find_by_tag('h3')
	    images[x].click()
	    response = browser.html
	    soup = BeautifulSoup(response, 'html.parser')
	    img_src = soup.find('img', class_='wide-image')['src']
	    img_title = soup.find('h2', class_='title').text
	    img_page_url = 'https://astrogeology.usgs.gov' + img_src
	    dict = {'title':img_title, 'img_url':img_page_url}
	    mars_hemisphere.append(dict)
	    browser.back()

	print(mars_hemisphere)















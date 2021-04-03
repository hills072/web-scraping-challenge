import pandas as pd
import os
from splinter import Browser
import pymongo
from bs4 import BeautifulSoup as bs
from flask import Flask, render_template, redirect
from webdriver_manager.chrome import ChromeDriverManager
import time




def scrape():


    mars = {}

    filepath = os.path.join("MarsNews.html")
    with open(filepath) as file:
        html = file.read()

    soup = bs(html, 'lxml')

    latest_title = soup.body.find_all('div', class_='content_title')[0].text
    latest_title_para = soup.body.find_all(
        'div', class_='article_teaser_body')[0].text

    mars['latest_title'] = latest_title
    mars['latest_title_para'] = latest_title_para

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    time.sleep(1)

    soup_image = bs(browser.html, 'html.parser')

    featured_image = soup_image.find_all('img', class_='headerimage')
    # featured_image_url_href = featured_image[0]['src']
    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'

    mars['featured_image_url'] = featured_image_url

    # browser.quit()

    mars_facts_url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(mars_facts_url)
    mars_earth_df = tables[0]
    mars_earth_df.columns = mars_earth_df.iloc[0]
    mars_earth_df['Mars - Earth Comparison'] = mars_earth_df['Mars - Earth Comparison'].str.replace(
        ':', '')
    mars_earth_df.set_index('Mars - Earth Comparison', inplace=True)
    mars_earth_df.index.name = None

    
    mars_table = mars_earth_df.to_html('mars_table.html')
    # mars_table = mars_table.replace('\n', '')

    mars['mars_table'] = mars_table

    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)

    time.sleep(1)

    soup = bs(browser.html, 'html.parser')

    items = soup.body.find_all('div', class_='item')
    titles = soup.body.find_all('h3')

    urls = []
    titles = []
    full_image_urls = []


    for item in items:
        if item.find('h3'):
            title = item.find('h3').text
            titles.append(title)
            # print(title)
        if item.find('a'):
            link = item.find('a')
            href = link['href']
            image_url = hemispheres_url + href
            # print(image_url)
            urls.append(image_url)

    for url in urls:
        browser.visit(url)
        soup = bs(browser.html, 'html.parser')

        img = soup.body.find_all('img', class_='wide-image')
        full_image_src = img[0]['src']
        full_image_url = hemispheres_url + full_image_src
        full_image_urls.append(full_image_url)
        # print(full_image_url)

    titles_urls = []

    mars['titles_urls'] = titles_urls

    for i, j in zip(titles, full_image_urls):
        titles_urls.append({"title": i, "img_url": j})

    browser.quit()

    return mars

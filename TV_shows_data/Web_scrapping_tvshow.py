from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

# Path to the Chrome webdriver executable
chrome_driver_path = "C:/Users/HARSHAD/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe"

# Initialize the Chrome webdriver service
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

try:
    # Navigate to the JustWatch website
    driver.get('https://www.justwatch.com/in/search?q=tv%25shows')
    time.sleep(3)  # Wait for the page to load

    # Scroll to the bottom of the page to load more content
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # After scrolling, get the updated HTML source
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find all TV show containers
    containers = soup.find_all('div', class_="title-list-row__row")
    titles = []
    release_years = []
    imdb_ratings = []
    show_links = []
    streams = []
    for container in containers:
        # Extract show title
        title = container.find('span', class_="header-title").text
        titles.append(title)
        
        # Extract release year
        year_elem = container.find('span', class_="header-year")
        release_years.append(year_elem.text.strip() if year_elem else "")
        
        # Extract IMDb rating
        rating_elem = container.find('div', class_="jw-scoring-listing__rating")
        imdb_ratings.append(rating_elem.text.strip() if rating_elem else "")
        
        # Extract show link
        link_ = ""
        show_link_elem = container.find('div', class_="title-list-row__column")
        anchor_elem = show_link_elem.find('a')
        if anchor_elem:
            link_ = anchor_elem.get('href')
        show_links.append(link_)
        
        # Extract streaming platforms
        stream_elems = container.find_all('div', class_="buybox-row__offers")
        stream_value = ", ".join([stream.find('img').get('alt') for stream in stream_elems])
        streams.append(stream_value)

    # Convert lists to a pandas DataFrame
    df = pd.DataFrame({
        'Show Title': titles,
        'Release Year': release_years,
        'IMDb Rating': imdb_ratings,
        'Show Link': show_links,
        'Stream': streams
    })

    # Save DataFrame to CSV
    df.to_csv('Tvshows_data.csv', index=False)

finally:
    # Quit the webdriver to close the browser
    driver.quit()

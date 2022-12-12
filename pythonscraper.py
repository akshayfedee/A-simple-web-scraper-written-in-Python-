import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    # Make a GET request to the specified URL
    response = requests.get(url)

    # Parse the response as HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Return the scraped data
    return soup
# URL of the page to scrape
url = 'https://www.example.com/'

# Scrape the page
scraped_data = scrape_page(url)

# Print the scraped data
print(scraped_data)

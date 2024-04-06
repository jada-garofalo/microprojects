import requests
from bs4 import BeautifulSoup
import random

visited_urls = set()

def wikiScraper(url):
    if url in visited_urls:
        return
    
    visited_urls.add(url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id = "firstHeading")
        print(title.text)

        allLinks = soup.find(id = "bodyContent").find_all("a")
        random.shuffle(allLinks)

        for link in allLinks:
            href = link.get('href')
            if href and href.startswith("/wiki"):
                new_url = "https://en.wikipedia.org" + href
                wikiScraper(new_url)
    
    except Exception as e:
        print(f"Error scraping {url}: {e}")

wikiScraper("https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion")

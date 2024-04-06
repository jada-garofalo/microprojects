import requests
from bs4 import BeautifulSoup
import random

visited_urls = set() #contains a list of the articles we have already visited

def wikiScraper(url):
    if url in visited_urls:
        return #skips the articles we have already seen
    
    visited_urls.add(url) #adds the current article to the list of visited articles

    try:
        response = requests.get(url) #requests data from the article
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id = "firstHeading") #locates and saves the article title to be printed
        print(title.text)

        allLinks = soup.find(id = "bodyContent").find_all("a") #locates all viable links to other wiki articles
        random.shuffle(allLinks) #randomly shuffles the order of our list of links

        for link in allLinks:
            href = link.get('href') #gives us the link for our new article
            if href and href.startswith("/wiki"):
                new_url = "https://en.wikipedia.org" + href
                wikiScraper(new_url) #starts the same process for this new article
    
    except Exception as e:
        print(f"Error scraping {url}: {e}") #prints errors more concisely

wikiScraper("https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion") #start webpage

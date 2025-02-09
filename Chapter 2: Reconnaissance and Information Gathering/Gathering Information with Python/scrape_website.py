import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the website
        title = soup.title.string if soup.title else "No title found"
        print(f"Title: {title}")

        # Extract meta description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc:
            print(f"Meta Description: {meta_desc['content']}")
        else:
            print("No meta description found")

        # Extract all links on the page
        links = soup.find_all("a")
        print("Number of links on the page:", len(links))

        # Print the first 5 links
        for link in links:
            print(f"Link: {link.get('href')}")
    except Exception as e:
        print(f"Error: {e}")

scrape_website("https://example.com")
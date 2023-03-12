import requests
from bs4 import BeautifulSoup

PREFIX = "https://en.wikipedia.org"
RANDOM_ARTICLE = PREFIX + "/wiki/Special:Random"

def get_html(url):
    print(f"Requesting: '{url}' - ...", end="\r")
    r = requests.get(url)
    print(f"Requesting: '{url}' - status code: {r.status_code}")

    if r.status_code != 200:
        raise Exception(f"Request failed: \33[91m{r.status_code}\33[0m")

    return r

def get_soup(html):
    return BeautifulSoup(html.content, 'html.parser')

def get_further_links(soup):
    links = []
    for a in soup.find_all('a'):
        link = a.get('href')
        if link is None or not link.startswith('/wiki/') or ':' in link or "#" in link or "Main_Page" in link:
            continue
        link = PREFIX + link
        links.append(link)
    return links

def get_article_data(soup):
    title = soup.title.text
    article = soup.find(id="mw-content-text").find_all("p")[0].text
    links = get_further_links(soup)
    return title, article, links

import re
import requests
from bs4 import BeautifulSoup

PREFIX = "https://en.wikipedia.org"
RANDOM_ARTICLE = PREFIX + "/wiki/Special:Random"

def get_links(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    links = []

    for a in soup.find_all('a'):
        link = a.get('href')
        if link is None:
            continue
        if not link.startswith('/wiki/'):
            continue
        if ":" in link:
            continue
        if "#" in link:
            continue
        if "Main_Page" in link:
            continue

        link = PREFIX + link
        links.append(link)

    return links

def get_article_text(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.string
    article = soup.find(id="mw-content-text").find_all('p')[0].text
    return title, article

def crawl(num_pages):
    count = 0
    page = requests.get(RANDOM_ARTICLE)
    links = [RANDOM_ARTICLE]
    titles = []
    articles = []

    while len(links) > 0 and count < num_pages:
        link = links.pop(0)
        page = requests.get(link)
        links.extend(get_links(page))
        title, article = get_article_text(page)
        titles.append(title)
        articles.append(article)
        count += 1

    return titles, articles

if __name__ == '__main__':
    titles, articles = crawl(4)
    for title, article in zip(titles, articles):
        if len(article) == 1: # skip empty articles
            continue
        print(type(title))
        print(title)
        print(type(article))
        print(len(article))
        print(article)
        print()

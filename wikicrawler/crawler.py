from .util import *

def crawl(num_pages: int):
    count = 0
    links = [RANDOM_ARTICLE]
    titles = []
    articles = []
    crawled = set()

    while links and count < num_pages:
        link = links.pop()
        while link in crawled and links:
            link = links.pop()
        if link in crawled and not links:
            break
        crawled.add(link)

        html = get_html(link)
        soup = get_soup(html)
        t, a, ls = get_article_data(soup)

        if len(a) == 1: # Empty article
            continue

        titles.append(t)
        articles.append(a)
        links.extend(ls)

        count += 1
        print(f"Crawled '\33[1m{t}\33[0m' \33[93m({count}/{num_pages} articles)\33[0m")

    if count == num_pages:
        print(f"Successfully crawled \33[92m{count}/{num_pages}\33[0m articles")
    else:
        print(f"Only managed to successfully crawl \33[91m{count}/{num_pages}\33[0m articles")

    return titles, articles

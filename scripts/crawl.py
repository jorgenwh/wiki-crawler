from wikicrawler import crawler, save_articles

if __name__ == '__main__':
    _, articles = crawler.crawl(1000)
    save_articles(articles, "articles.txt")

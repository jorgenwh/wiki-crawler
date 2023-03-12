
def save_articles(articles, filename):
    with open(filename, "w") as f:
        for article in articles:
            f.write(article.strip() + "\n")
    print(f"Saved articles to '{filename}'")

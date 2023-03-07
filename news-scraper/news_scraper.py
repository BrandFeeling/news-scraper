import requests
from bs4 import BeautifulSoup
from bs4 import Tag


apiKey = <your APIKey>
num_news = 10


class GoogleNewsArticle:
    def __init__(self, json) -> None:
        self.author = json["author"]
        self.title = json["title"]
        self.description = json["description"]
        self.url = json["url"]
        self.publishedAt = json["publishedAt"]
        self.content = json["content"]


def get_google_news_articles(keyword: str):
    url = f"https://newsapi.org/v2/top-headlines?q={keyword}&apiKey={apiKey}&pageSize={num_news}&sortBy=popularity"
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError("Error raised")
    json_news = response.json()["articles"]
    news = list(map(lambda x: GoogleNewsArticle(x), json_news))
    print(news)


def main():
    """The main entry point for this project"""
    get_google_news_articles("Apple")
    print("Project set up correctly")


if __name__ == "__main__":
    main()

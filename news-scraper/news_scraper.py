import requests
from bs4 import BeautifulSoup
from bs4 import Tag
from typing import Iterator

def get_article_links(links: Iterator[Tag]) -> Iterator[Tag]:
    return list(
        filter(
            lambda x: x.get("href") is not None
            and x["href"].startswith(url)
            and x["href"].endswith(".ghtml"),
            links,
        )
    )


url = "https://g1.globo.com"
r1 = requests.get(url)
r1.status_code
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, "html5lib")

coverpage_links: Iterator[Tag] = soup1.find_all("a")

valid_links: Iterator[Tag] = get_article_links(coverpage_links)

number_of_articles = 10


news_contents = []
list_links = []
list_titles = []


def main():
    """The main entry point for this project"""
    print("Project set up correctly")


if __name__ == "__main__":
    main()

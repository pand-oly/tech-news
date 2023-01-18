from tech_news.database import search_news
from typing import List, Tuple


# Requisito 6
def search_by_title(title: str) -> List[Tuple]:
    """Seu código deve vir aqui"""
    response_db = search_news({
        "title": {
            "$regex": title,
            "$options": "i"
        }
    })

    list_news = list()
    for news in response_db:
        list_news.append((news["title"], news["url"]))

    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

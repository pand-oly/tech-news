from tech_news.database import search_news
from typing import List, Tuple, Union, Dict
from datetime import datetime as dt


def generate_tuple(list_news: List[Dict]) -> List[Tuple]:
    list_tuples = list()
    for news in list_news:
        list_tuples.append((news["title"], news["url"]))

    return list_tuples


# Requisito 6
def search_by_title(title: str) -> List[Tuple]:
    """Seu código deve vir aqui"""
    response_db = search_news({
        "title": {
            "$regex": title,
            "$options": "i"
        }
    })

    list_news = generate_tuple(response_db)
    return list_news


# Requisito 7
def search_by_date(date_string: str) -> List[Union[Tuple, None]]:
    """Seu código deve vir aqui"""
    try:
        format_date = dt.strptime(date_string, "%Y-%m-%d")\
            .date().strftime("%d/%m/%Y")
        response_db = search_news({"timestamp": format_date})

        list_news = list()
        if len(response_db) != 0:
            list_news = generate_tuple(response_db)

        return list_news
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

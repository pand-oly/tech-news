from tech_news.database import find_news
from tech_news.analyzer.search_engine import generate_tuple
from typing import List, Tuple, Union


def key_sort_comments(e):
    return e["comments_count"]


# Requisito 10
def top_5_news() -> List[Union[Tuple, None]]:
    """Seu código deve vir aqui"""
    const_response_db = find_news()
    const_response_db.sort(reverse=True, key=key_sort_comments)

    const_ranking_tech_news = const_response_db[:5]
    const_top_tech_news = generate_tuple(const_ranking_tech_news)

    return const_top_tech_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""

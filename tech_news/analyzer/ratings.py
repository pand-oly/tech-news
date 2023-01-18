from tech_news.database import find_news
from tech_news.analyzer.search_engine import generate_tuple
from typing import List, Tuple, Union
from collections import Counter


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
    response_db = find_news()

    list_categories = [
        news["category"]
        for news in response_db
    ]

    ranking_categories = Counter(sorted(list_categories)).most_common(5)
    top_categories = [
        name_category
        for name_category, _ in ranking_categories
    ]

    return top_categories

from time import sleep
import re
import requests
from parsel import Selector
from typing import List, Union, Dict
from tech_news.database import create_news


# Requisito 1
def fetch(url: str) -> Union[str, None]:
    """Seu código deve vir aqui"""
    headers = {"user-agent": "Fake user-agent"}
    sleep(1)

    try:
        response = requests.get(url=url, timeout=3, headers=headers)
    except requests.ReadTimeout:
        return None

    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content: str) -> List[str]:
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    list_href = selector.css(".cs-overlay a::attr(href)").getall()
    return list_href


# Requisito 3
def scrape_next_page_link(html_content: str) -> Union[str, None]:
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    try:
        next_page = selector.css(".next").attrib["href"]
    except KeyError:
        return None

    return next_page


# Requisito 4
def scrape_news(html_content) -> Dict:
    """Seu código deve vir aqui"""
    selecttor = Selector(html_content)

    get_comment = selecttor.css("#comments h5::text").get()
    if get_comment is None:
        comment = [0]
    else:
        comment = get_comment.strip().split()
        if comment[1] == 'comments':
            comment = get_comment[0]

    first_paragraph = selecttor.css(".entry-content p").get()

    return {
        "url": selecttor.css("link[rel='canonical']").attrib["href"],
        "title": selecttor.css("h1.entry-title::text").get().strip(),
        "timestamp": selecttor.css("li[class='meta-date']::text").get(),
        "writer": selecttor.css("a[class='url fn n']::text").get(),
        "comments_count": int(comment[0]),
        "summary": re.sub('<[^>]+?>', '', first_paragraph).strip(),
        "tags": selecttor.css(".post-tags li a::text").getall(),
        "category": selecttor.css("a.category-style span.label::text").get()
    }


# Requisito 5
def get_tech_news(amount: int) -> List[Dict]:
    """Seu código deve vir aqui"""
    url = 'https://blog.betrybe.com/'
    news = list()
    lis_href_tech_news = list()

    while len(lis_href_tech_news) <= amount:
        base_html = fetch(url)
        lis_href_tech_news.extend(scrape_updates(base_html))

        if len(lis_href_tech_news) < amount:
            url = scrape_next_page_link(base_html)

    for href_tech_news in lis_href_tech_news[:amount]:
        tech_news = fetch(href_tech_news)
        scrape = scrape_news(tech_news)
        news.append(scrape)

    create_news(news)
    return news

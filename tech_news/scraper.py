from time import sleep
import requests
from parsel import Selector
from typing import List, Union


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
def scrape_updates(html_content: str) -> List:
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    list_href = selector.css(".cs-overlay a::attr(href)").getall()
    return list_href


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

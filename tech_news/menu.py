from tech_news.analyzer.search_engine import \
    search_by_category, search_by_title, search_by_tag, search_by_date
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.scraper import get_tech_news
import sys

string_menu = \
        "Selecione uma das opções a seguir:\n"\
        " 0 - Popular o banco com notícias;\n"\
        " 1 - Buscar notícias por título;\n"\
        " 2 - Buscar notícias por data;\n"\
        " 3 - Buscar notícias por tag;\n"\
        " 4 - Buscar notícias por categoria;\n"\
        " 5 - Listar top 5 notícias;\n"\
        " 6 - Listar top 5 categorias;\n"\
        " 7 - Sair.\n"

string_input = {
    "0": "Digite quantas notícias serão buscadas: ",
    "1": "Digite o título: ",
    "2": "Digite a data no formato aaaa-mm-dd: ",
    "3": "Digite a tag: ",
    "4": "Digite a categoria: ",
}

functions_list = {
    "0": lambda parm: get_tech_news(int(parm)),
    "1": lambda parm: search_by_title(parm),
    "2": lambda parm: search_by_date(parm),
    "3": lambda parm: search_by_tag(parm),
    "4": lambda parm: search_by_category(parm),
    "5": lambda: top_5_news(),
    "6": lambda: top_5_categories()
}


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    try:
        input_menu = input(string_menu).strip()

        if input_menu == "7":
            print("Encerrando script")
            return 0

        if input_menu in ["0", "1", "2", "3", "4"]:
            string_input_param = string_input[input_menu]
            input_parameters = input(string_input_param)
            result = functions_list[input_menu](input_parameters)
        else:
            result = functions_list[input_menu]()

        print(result)
    except KeyError:
        print('Opção inválida', file=sys.stderr)
        return 2

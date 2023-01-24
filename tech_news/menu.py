from tech_news.analyzer import ratings, search_engine
from tech_news.scraper import get_tech_news

string_menu = \
        f"Selecione uma das opções a seguir:\n"\
        f" 0 - Popular o banco com notícias;\n"\
        f" 1 - Buscar notícias por título;\n"\
        f" 2 - Buscar notícias por data;\n"\
        f" 3 - Buscar notícias por tag;\n"\
        f" 4 - Buscar notícias por categoria;\n"\
        f" 5 - Listar top 5 notícias;\n"\
        f" 6 - Listar top 5 categorias;\n"\
        f" 7 - Sair.\n"

string_input = {
    "0": "Digite quantas notícias serão buscadas: ",
    "1": "Digite o título: ",
    "2": "Digite a data no formato aaaa-mm-dd: ",
    "3": "Digite a tag: ",
    "4": "Digite a categoria: ",
}

functions_list = {
    "0": lambda parm: get_tech_news(int(parm)),
    "1": search_engine.search_by_title,
    "2": search_engine.search_by_date,
    "3": search_engine.search_by_tag,
    "4": search_engine.search_by_category,
    "5": ratings.top_5_news,
    "6": ratings.top_5_categories,
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
        print('Opção inválida\n')
        return 2


if __name__ == "__main__":
    analyzer_menu()

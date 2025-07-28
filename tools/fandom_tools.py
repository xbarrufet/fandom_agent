from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from tools.content_line import ContentLine, create_content_type_title, create_content_type_text

from tools.search_result import SearchResult
#from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch

# Example usage


load_dotenv()

URL_BASE = "https://onepiece.fandom.com"
URL_CANON = URL_BASE + "/es/wiki/Lista_de_personajes_canon#Individuos"
SECTION_TITLE_INICIAL="Sumari"


def get_fandom_url_from_tavity(charcter_name:str):
    search = TavilySearch()
    res = search.run(f"{charcter_name}")
    return res



def create_beautiful_object(total_url:str):
    """
    create a BeautifulSoup object from a given URL
    """
    response = requests.get(total_url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve data from {total_url}. Status code: {response.status_code}")
        return None


def search_content_in_fandom(url_base:str, url_search:str, search_term:str)->[SearchResult]:
    search_result =[]
    search_url = f"{url_base}{url_search}?scope=internal&query={search_term.lower().replace(' ', '+')}"
    search_content = create_beautiful_object(search_url)
    if not search_content:
        return []
    # content at ul class='unified-search__results'
    ul_tag = search_content.find("ul", class_="unified-search__results")
    if not ul_tag:
        print("No search results found.")
        return []
    for article in ul_tag.find_all("article", recursive=True):
        # get title, url and description
        anchor_title = article.find("a", class_="unified-search__result__title")
        if not anchor_title:
            continue
        title = anchor_title.get_text(strip=True)
        url = anchor_title['href']
        description_tag = article.find("div", class_="unified-search__result__content")
        if not description_tag:
            continue
        description_text = description_tag.get_text(strip=True)
        search_result.append(SearchResult(title=title, url=url, description=description_text))
    return search_result

def get_character_content(url_base:str,url:str)->[ContentLine]:
    """
    Get the content of a character's page via beautiful soup.
    Content div class = mw-content-ltr mw-parser-output
        all childs
        title start with h2.span[class='mw-headline' id=TOC.section] (also h3 and h4)
        Content start with p

    """
    content_lines = []
    url_total = url_base + url
    content = create_beautiful_object(url_total)
    # get page title
    span_title  = content.find("span", "mw-page-title-main")
    if span_title:
        content_lines.append(create_content_type_title(span_title.text.strip(), 1))
    # get page content
    main_content = content.find("div", "mw-content-ltr mw-parser-output")
    if not main_content:
        return "Content not found."
    all_childs = main_content.find_all(recursive=False)

    for child in all_childs:
        if child.name == 'h2' or child.name == 'h3' or child.name == 'h4':
            section_title = child.find("span", class_="mw-headline").text.strip()
            level = int(child.name[-1])
            text = child.find("span", class_="mw-headline").text.strip(" ")
            content_lines.append(create_content_type_title(text, level))
        if child.name=='p':
            text = child.get_text(strip=False)
            if text:
                content_lines.append(create_content_type_text(text))
    return content_lines

def get_character_content_as_markdown(url_base:str, url:str)->str:
    """
    Get the content of a fandom page via beautiful soup and return it as markdown.
    """
    content_lines = get_character_content(url_base, url)
    markdown_content = ""
    for line in content_lines:
        markdown_content += line.as_markdown()
    return markdown_content
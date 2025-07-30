from fandom_content_agent.fandom_agent import lookup_40k_character_url
from fandom_content_agent.fandom_sumarize import summarize_character_information
from tools.fandom_content_result import FandomContentResult
from tools.fandom_tools import search_content_in_fandom, get_character_content




if __name__ == "__main__":

    url_base = "https://warhammer40k.fandom.com"
    url = "/es/wiki/Abathar"

    #urk lookup
    url_char = lookup_40k_character_url("Nagi BlueLock", verbose=True)
    print("url_char: " + url_char)
    if len(url_char.strip()) == 0:
        print("No se ha encontrado la url del personaje")
        exit(1)
    #url_char =urls["OP"]

    #content extracted from the fandom
    content:FandomContentResult = get_character_content(url_char)
    print(content)

    #suamriz information
    res = summarize_character_information(content)
    print(res)


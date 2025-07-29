from fandom_content_agent.fandom_agent import lookup_40k_character_url
from fandom_content_agent.fandom_sumarize import summarize_character_information
from tools.fandom_tools import search_content_in_fandom, get_fandom_url_content_as_markdown, \
    get_fandom_url_content_as_string

if __name__ == "__main__":

    url_base = "https://warhammer40k.fandom.com"
    url = "/es/wiki/Abathar"

    url_char = lookup_40k_character_url("Nagi de bluelock")
    print("url_char: " + url_char)
    #print("la respues es:" + url_char)
    #url_char = "https://warhammer40k.fandom.com/wiki/Malcador_the_Sigillite"
    content = get_fandom_url_content_as_string(url_char)
    res = summarize_character_information(content)
    print(res)

    #u1 = "https://warhammer40k.fandom.com/es/wiki/Gal_Vorbak"
    #u2="https://bluelock.fandom.com/es/wiki/Seishiro_Nagi"
    #res = get_fandom_url_content(u2)
    #print(res)
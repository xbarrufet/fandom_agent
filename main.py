from fandom_content_agent.fandom_agent import lookup_40k_character_url
from tools.fandom_tools import search_content_in_fandom

if __name__ == "__main__":

    url_base = "https://warhammer40k.fandom.com"
    url = "/es/wiki/Abathar"

    url_char_40k = lookup_40k_character_url("Satoru de Jujutsu Kaisen")
    print(url_char_40k)
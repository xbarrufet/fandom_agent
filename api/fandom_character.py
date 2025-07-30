from typing import Tuple

from fandom_content_agent.fandom_agent import lookup_40k_character_url
from fandom_content_agent.fandom_sumarize import summarize_character_information
from tools.fandom_content_result import FandomContentResult, ERROR_FANDOM_CONTENT_RESULT
from tools.fandom_tools import get_character_content
from tools.output_parsers import Summary, ERROR_SUMMARY

urls = {"BL":"https://bluelock.fandom.com/es/wiki/Seishiro_Nagi",
        "40K":"https://warhammer40k.fandom.com/wiki/Malcador_the_Sigillite",
        "OP":"https://onepiece.fandom.com/es/wiki/Tony_Tony_Chopper"
        }

def sumarize_fandom_character(character_name) -> Tuple[Summary, FandomContentResult]:
    # urk lookup
    print("starting lookup for character: " + character_name)
    url_char = lookup_40k_character_url(character_name, verbose=False)
    print("url_char: " + url_char)
    if len(url_char.strip()) == 0:
        print("No se ha encontrado la url del personaje")
        return ERROR_SUMMARY,ERROR_FANDOM_CONTENT_RESULT
    # url_char =urls["OP"]

    # content extracted from the fandom
    try:
        content: FandomContentResult = get_character_content(url_char)
    except Exception as e:
        print(f"Error while fetching character content: {e}")
        return ERROR_SUMMARY, ERROR_FANDOM_CONTENT_RESULT

    # suamriz information
    print("content found")
    try:
        res = summarize_character_information(content)
    except Exception as e:
        print(f"Error while summarizing character information: {e}")
        return ERROR_SUMMARY, ERROR_FANDOM_CONTENT_RESULT
    return res, content

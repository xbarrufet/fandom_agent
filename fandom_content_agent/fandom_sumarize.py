from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from tools.output_parsers import summary_parser


def summarize_character_information(information:str)->str:
    """
    Call to llm to summarize the character information.
    received the information as a string and returns a summary.
    """

    summary_template ="""
        Dada esta informacion de un personaje de la wiki fandom {information}, quiero que devuelvas
        1- un resumen de la informacion
        2- 4 puntos clave sobre el personaje
        You MUST return a JSON object in the EXACT format below
        \n{format_instructions}
    """
    summary_propmt_template = PromptTemplate(
        template=summary_template,
        input_variables=["information"],
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )
    llm=ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini"
    )
    # Create a RunnableSequence
    chain = summary_propmt_template | llm | summary_parser

    res=chain.invoke(
        input={"information": information}
    )
    return res.to_dict()

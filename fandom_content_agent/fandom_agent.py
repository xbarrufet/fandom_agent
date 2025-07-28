from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub

from tools.fandom_tools import get_fandom_url_from_tavity

load_dotenv()

def lookup_40k_character_url(name:str) -> str:
    """
    Returns the path to the fandom content agent.
    """
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini")

    template = """dado el personaje {character} que aparece en la wiki fandom quiero que me devuelvas la url de la pagina que contiene su informacion."""

    prompt_template = PromptTemplate(
        template=template, input_variables=["character"])

    tools_for_agent = [
        Tool(
            name = "Extrae informacion de las paginas de personajes de la wiki fandom",
            func=get_fandom_url_from_tavity,
            description = "Utiliza esta herramienta para buscar la página de un personaje en la wiki fandom. La entrada debe ser el nombre del personaje.",
        )
    ]

    react_propmpt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_propmpt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(character=name).to_string()}
    )
    fandom_url = result["output"]
    return fandom_url

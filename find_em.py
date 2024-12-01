from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name: str) -> str:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linked_profile_url=linkedin_profile_url, mock=True)

    summary_template = """
        Given the LinkedIn Information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    # llm = ChatOllama(model="llama3.2")
    chain = summary_prompt_template | llm | StrOutputParser()
    result = chain.invoke(input={"information": linkedin_data})
    print(result)

if __name__ == "__main__":
    print("Hello Langchain!")
    load_dotenv()
    ice_break_with(name="Sanketh Sudhakar")

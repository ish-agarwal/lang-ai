from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello Lang AI!")

    summary_template = """
        Given the Linkedin information {information} about a person, I want you to create :
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(temperature=0, model="llama3.2")
    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(
        linked_profile_url="https://www.linkedin.com/in/sanketh-sudhakar/", mock=True
    )

    result = chain.invoke(input={"information": linkedin_data})

    print(result)

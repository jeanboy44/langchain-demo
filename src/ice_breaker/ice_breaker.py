"""a main module to run ice_breaker"""

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from src.ice_breaker.third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello Langchain!")

    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    information = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    print(chain.run(information=information))

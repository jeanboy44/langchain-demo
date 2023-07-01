"""a main module to run ice_breaker"""

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from src.ice_breaker.agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from src.ice_breaker.agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from src.ice_breaker.third_parties.linkedin import scrape_linkedin_profile
from src.ice_breaker.third_parties.twitter import scrape_user_tweets


def run(name: str):
    print("Hello Langchain!")

    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=5)

    summary_template = (
        "given the linkedin information {linkedin_information} and "
        "twitter information {twitter_information} "
        "about a person from I want you to create:\n"
        "1. a short summary\n"
        "2. two interesting facts about them\n"
        "3. A topic that may interest them"
        "4. 2 creative Ice breakers to open a conversation with them"
    )

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
    )
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(linkedin_information=linkedin_data, twitter_information=tweets))


if __name__ == "__main__":
    run(name="Harrison Chase")

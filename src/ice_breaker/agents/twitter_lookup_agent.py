"""a module for twitter look up agent"""

from langchain import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

from src.ice_breaker.tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    template = (
        "given the full name {name_of_person} I want you to get it me a link "
        "to their Twitter profile page, and extract from it their username\n"
        "In Your Final anser only the person's username."
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Twitter profile pages",
            func=get_profile_url,
            description="useful for when you need to get the Twitter Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    promopt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    twitter_username = agent.run(promopt_template.format_prompt(name_of_person=name))
    return twitter_username

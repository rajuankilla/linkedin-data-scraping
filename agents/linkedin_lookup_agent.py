import os
from dotenv import  load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from pywin.framework.toolmenu import tools
from win32comext.adsi.demos.scp import verbose

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import  PromptTemplate
from langchain_core.tools import  Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily

def lookup(name: str) -> str:
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)

    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                                  Your answer should contain only a URL"""
    prompt_template = PromptTemplate(
        template=template, input_variable=["name_of_person"]
    )
    tools_for_agent= [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the linkedin Page URL"
        )
    ]
    react_prompt= hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor= AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url= result["output"]
    return linked_profile_url
    # return "https://www.linkedin.com/in/raji-reddy-ankilla-4b570bb/"

if __name__ == "__main__":
    linkedin_url = lookup(name="Raji Reddy Ankilla")
    print("---------linkedin_url ",linkedin_url)





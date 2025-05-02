from typing import Tuple, Any

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from output_parsers import summary_parser, Summary
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import  lookup as linkedin_lookup_agent


def ic_break_with(name: str) -> tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    
        
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    # OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo",openai_api_key=OPENAI_API_KEY)
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)
    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(input={"information": linkedin_data})

    print("------------phopto URL " , linkedin_data.get("photoUrl"))
    return res, linkedin_data.get("photoUrl")

    # print(res)

if __name__ == "__main__":
    load_dotenv()

    print("Ice breaker started...")
    ic_break_with("Raji Reddy Ankilla")


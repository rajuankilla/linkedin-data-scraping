# linkedin-data-scraping-langchain-agents 

A repository for learning LangChain🦜🔗  by building a generative ai application (Agents).

This is a web application crawling Linkedin about a person and customizes an ice breaker with them.
 <img title="Linked in Data scraping" alt="This is a web application crawling Linkedin about a person and customizes an ice breaker with them." src="/images/linkedin-demo.png" border="2px solid black">
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

`SCRAPIN_API_KEY` 

`TAVILY_API_KEY`

`TWITTER_API_KEY`

`TWITTER_API_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_SECRET`

`LANGCHAIN_TRACING_V2`  

`LANGCHAIN_API_KEY` 

`LANGCHAIN_PROJECT` # Optional


To run this project, you will need to add the following environment variables to your .env file:

> **Note**: This project uses paid API services:
> - [Scrapin.io](https://www.scrapin.io/?utm_campaign=influencer&utm_source=github&utm_medium=social&utm_content=edenmarco) for LinkedIn data scraping

> **Important Note**: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error. If you don't need tracing, simply remove or comment out these environment variables.
## Run Locally

Clone the project

```bash
  git clone [https://github.com/emarco177/ice_breaker.git](https://github.com/rajuankilla/linkedin-data-scraping-langchain-agents.git)
```

Go to the project directory

```bash
  cd linkedin-data-scraping-langchain-agents
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  pipenv run app.py
```

import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the Link
    edIn profile"""

    if mock:
        print("------------- mock of srcapin response instead of calling direct API, with mock: bool = True")
        linkedin_profile_url = "https://raw.githubusercontent.com/rajuankilla/linkedin-data-scraping-langchain-agents/refs/heads/main/static/rajireddy-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        # ENROLL WITH COUPON CODE: EDENMARCO
        # For 20% Discount on all pricing
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("person")
    print("------- person details ", response)
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/raji-reddy-ankilla-4b570bb/"

        ),
    )

import os

import requests
from requests import Response


def scrape_linkedin_profile(linkedin_profile_url: str) -> Response:
    """scrape information from LinkedIn profiles,
    manually scrape the information from the LinkedIn profile

    Args:
        linkedin_profile_url (str): LinkedIn profile url
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    response = requests.get(
        api_endpoint,
        params={"url": linkedin_profile_url},
        headers=header_dic,
        timeout=30,
    )

    return response

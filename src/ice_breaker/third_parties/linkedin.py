import json
import os
from pathlib import Path

import requests
from requests import Response


def get_linkedin_profile_response(linkedin_profile_url: str) -> Response:
    """get LinkedIn profile response

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


def scrape_linkedin_profile(
    linkedin_profile_url: str = None,
    linkedin_profile_json_path: Path = Path(
        "resources/examples/harrison-chase-linkedin_data.json"
    ),
) -> Response:
    """scrape information from LinkedIn profiles,
    manually scrape the information from the LinkedIn profile

    Args:
        linkedin_profile_url (str): LinkedIn profile url
        linkedin_profile_json_path (str): a json file path to LinkedIn profile. When
            this argument is not None, linkedin_profile_url is ignored. Defaults to
            None.
    """
    if linkedin_profile_url is None:
        with linkedin_profile_json_path.open() as f:
            data = json.load(f)
    else:
        response = get_linkedin_profile_response(linkedin_profile_url)
        data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

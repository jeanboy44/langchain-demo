import json

from src.ice_breaker.third_parties.linkedin import get_linkedin_profile_response

if __name__ == "__main__":
    linkedin_data = get_linkedin_profile_response(
        linkedin_profile_url="https://wwww.linkedin.com/in/harrison-chase-961287118/"
    )

    with open(
        "resources/examples/harrison-chase-linkedin_data.json", "w", encoding="utf-8"
    ) as f:
        json.dump(linkedin_data.json(), f, ensure_ascii=False, indent=4)

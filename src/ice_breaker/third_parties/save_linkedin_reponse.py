import json

from src.ice_breaker.third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://wwww.linkedin.com/in/harrison-chase-961287118/"
    )

    with open(
        "resources/examples/harrison-chase-linkedin_data.json", "w", encoding="utf-8"
    ) as f:
        json.dump(linkedin_data.json(), f, ensure_ascii=False, indent=4)

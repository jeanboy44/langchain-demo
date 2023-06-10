from langchain import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for LinkedIn a Profile Page."""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res

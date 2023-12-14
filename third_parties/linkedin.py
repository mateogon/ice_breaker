import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Scrape a LinkedIn profile and return the information in a dictionary.
    """

    headers = {"Authorization": "Bearer " + os.environ.get("PROXYCURL_API_KEY")}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    params = {
        "linkedin_profile_url": linkedin_profile_url,
        "extra": "include",
        "github_profile_id": "include",
        "facebook_profile_id": "include",
        "twitter_profile_id": "include",
        "personal_contact_number": "include",
        "personal_email": "include",
        "inferred_salary": "include",
        "skills": "include",
        "use_cache": "if-present",
        "fallback_to_cache": "on-error",
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in (None, [], {}, "")
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

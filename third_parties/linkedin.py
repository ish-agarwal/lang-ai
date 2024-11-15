import os
from http.client import responses

import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linked_profile_url: str, mock: bool = False):
    """scrape information from Linkedin profile,
    Manually scrape information from Linkedin profile"""
    if mock:
        linked_profile_url = "https://gist.githubusercontent.com/ish-agarwal/aaf1b8ab37b44615acba3c3c88c1b5f8/raw/bed412ddfeb3f85e020aa6c28ab1cbe055adb03d/VJ.json"
        response = requests.get(linked_profile_url, timeout=10)
    else:
        headers = {"Authorization": "Bearer " + os.environ.get("LINKEDIN_API_KEY")}
        response = requests.get(
            os.environ.get("LINKEDIN_API_ENDPOINT"),
            params={"url": linked_profile_url},
            headers=headers,
        )

    if response.status_code != 200:
        return {"error": responses[response.status_code]}
    else:
        data = response.json()
        data = {
            key: value
            for key, value in data.items()
            if value not in ["", None, []]
            and key not in ["people_also_viewed", "certifications"]
        }
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

        return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linked_profile_url="https://www.linkedin.com/in/elonmusk/", mock=True
        )
    )

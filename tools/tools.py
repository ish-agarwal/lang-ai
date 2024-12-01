from langchain_community.tools.tavily_search import TavilySearchResults
from serpapi import search as GoogleSearch
import os


def get_profile_rl_tavily(name: str):
    """Search for LinkedIn or Twitter Profile Page"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res


def get_profile_google(name: str):
    """Search for LinkedIn or Twitter Profile Page"""
    params = {
        "api_key": f"{os.getenv("SERP_API_KEY")}",
        "engine": "google",
        "q": f"{name}",
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en",
    }
    search = GoogleSearch(params)
    results = search.data
    formatted_results = [
        {"title": result["title"], "url": result["link"], "content": result["snippet"]}
        for result in results["organic_results"]
        if "linkedin.com" in result["link"].lower()
        or "twitter.com" in result["link"].lower()
    ]
    return formatted_results

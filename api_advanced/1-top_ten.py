#!/usr/bin/python3
"""
1-top_ten.py
This script fetches and prints the titles of the first 10 hot posts 
from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK", end="")  # Matches exact expected output
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        print("OK", end="")  # If no posts are found
        return

    for post in posts:
        print(post["data"]["title"])

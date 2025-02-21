#!/usr/bin/python3
"""
Reddit API Query Script

This script fetches and prints the top 10 hot post titles from a given subreddit 
using the Reddit API. If the subreddit is invalid or cannot be accessed, it prints "None".

Author: AMugisha-1
Date: 2025-02-21
"""

import requests


def top_ten(subreddit):
    """
    Fetch and print the titles of the first 10 hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints post titles or "None" if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post["data"]["title"])

    except Exception:
        print("None")

#!/usr/bin/python3
"""
Reddit API Query - Fetch Top 10 Hot Posts

This script retrieves the top 10 hot post titles from a given subreddit 
using Reddit's public API. If the subreddit does not exist or is invalid, 
it prints "OK".

Functions:
    - top_ten(subreddit): Fetches and prints the first 10 hot posts.

Usage:
    Call top_ten("subreddit_name") with a valid subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Fetch and print the titles of the first 10 hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints post titles or "OK" if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK")  # 🔹 Ensure "OK" is printed exactly as expected
        return

    try:
        posts = response.json().get("data", {}).get("children", [])

        if not posts:
            print("OK")  # 🔹 Handle empty subreddits correctly
            return

        for post in posts:
            print(post["data"]["title"])

    except Exception:
        print("OK")  # 🔹 Handle unexpected JSON structure


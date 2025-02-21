#!/usr/bin/python3
"""
This module interacts with the Reddit API.

It fetches and prints the top 10 hot posts from a given subreddit.
If the subreddit is invalid or does not exist, it prints "None".
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit name to fetch data from.

    Returns:
        None: Prints the titles of the posts or "None" if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            print("None")
            return
        for post in posts:
            print(post["data"]["title"])
    except (KeyError, ValueError):
        print("None")

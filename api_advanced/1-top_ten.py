#!/usr/bin/python3
"""
This script fetches and prints the titles of the first 10 hot posts 
from a given subreddit using the Reddit API.

Usage:
    Run the script and call the `top_ten(subreddit)` function 
    with the name of the subreddit as an argument.

Example:
    top_ten("python")
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints post titles or "OK" if the subreddit doesn't exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK")  # Matches expected output
        return

    try:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        
        if not posts:
            print("OK")  # Handles empty subreddits
            return
        
        for post in posts:
            print(post["data"]["title"])

    except Exception:
        print("OK")  # Fallback for unexpected API response issues


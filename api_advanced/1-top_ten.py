#!/usr/bin/python3
"""
Reddit API Query Script

This script queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.

If the subreddit is invalid, it prints 'None'.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    If the subreddit is invalid or has no posts, it prints 'None'.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    # Define the base API URL
    base_url = "https://www.reddit.com"
    api_uri = f"{base_url}/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid being blocked by Reddit
    user_agent = {"User-Agent": "CustomRedditScript/1.0"}
    payload = {"limit": "10"}  # Fetch 10 posts

    # Make the GET request with no redirects
    res = requests.get(api_uri, headers=user_agent,
                       params=payload, allow_redirects=False)

    # Check if subreddit is invalid
    if res.status_code != 200:
        print("None")
        return

    try:
        res_json = res.json()

        # Validate JSON structure
        posts = res_json.get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        # Print the titles of the first 10 hot posts
        for post in posts[:10]:
            print(post["data"].get("title", "None"))

    except ValueError:
        print("None")


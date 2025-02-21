#!/usr/bin/python3
"""
This module contains a function to fetch and display
the top 10 hot posts from a given subreddit using Reddit's API.
"""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "ALX-Reddit-Query"}
    
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


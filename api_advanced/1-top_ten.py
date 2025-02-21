#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200 or response.json().get("error") == 404:
        print(None)
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post["data"]["title"])

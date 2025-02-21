#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print("OK", end="")  # No newline
        return
    
    posts = response.json().get("data", {}).get("children", [])
    
    if not posts:
        print("OK", end="")  # No newline
        return
    
    for post in posts:
        print(post["data"]["title"])

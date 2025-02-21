#!/usr/bin/python3
"""Module to print the titles of the first 10 hot posts of a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print("OK", end="")  # Ensures no extra newline character
        return

    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post['data'].get('title', ""))

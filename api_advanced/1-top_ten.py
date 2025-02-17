#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=5)

        if response.status_code != 200:
            print(None)
            return

        try:
            data = response.json()
        except ValueError:
            print(None)
            return

        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
        else:
            for post in posts:
                print(post["data"].get("title", "None"))

    except requests.RequestException:
        print(None)

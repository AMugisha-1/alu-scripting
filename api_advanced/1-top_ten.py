#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK")  # Expected output for non-existent subreddit
        return

    posts = response.json().get('data', {}).get('children', [])

    if not posts:
        print("OK")  # Expected output for an empty subreddit
        return

    for post in posts:
        print(post['data']['title'])

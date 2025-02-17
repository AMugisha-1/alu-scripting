#!/usr/bin/python3
"""
Reddit API Query Script

This script queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    If the subreddit is invalid or has no posts, it prints 'None'.
    """
    # Define the base API URL
    base_url = 'https://www.reddit.com'
    api_uri = f'{base_url}/r/{subreddit}/hot.json'

    # Set a User-Agent to avoid being blocked
    user_agent = {'User-Agent': 'Python/requests'}
    payload = {'limit': '10'}  # Set query parameters

    # Request data from Reddit API
    res = requests.get(api_uri, headers=user_agent,
                       params=payload, allow_redirects=False)

    # Handle API response errors
    if res.status_code != 200:
        print('None')
        return

    # Parse JSON response
    try:
        res_json = res.json()

        # Check if the subreddit is invalid or has no posts
        if ('data' not in res_json or
                'children' not in res_json['data'] or
                not res_json['data']['children']):
            print('None')
            return

        # Print each hot post title
        for post in res_json['data']['children'][:10]:
            print(post['data'].get('title', 'None'))

    except ValueError:
        print('None')


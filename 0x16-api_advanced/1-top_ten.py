#!/usr/bin/python3
"""
This module defines a function `top_ten` that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit. If the subreddit is
invalid, the function prints `None`.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for the given subreddit. If the subreddit is invalid, prints None.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)

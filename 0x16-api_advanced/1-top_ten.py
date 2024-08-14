#!/usr/bin/python3
"""
This script fetches and prints the titles of the top 10 hot posts from a
given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """Fetch and print the titles of the top 10 hot posts from a subreddit."""
    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    limits = 10

    response = requests.get(
        apiUrl, headers={"user-agent": userAgent}, params={"limit": limits}, allow_redirects=False)
    
    if response.status_code != 200:
        print('None')
        return
    
    try:
        response = response.json()
        list_obj = response['data']['children']
        for obj in list_obj[:limits]:  # Ensures only top 10 are printed
            print(obj['data']['title'])
    except Exception as e:
        print('None')


# Example usage (remove before submission if not needed):
# top_ten('python')

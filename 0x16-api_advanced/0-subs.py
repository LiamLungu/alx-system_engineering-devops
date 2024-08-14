#!/usr/bin/python3
"""Script that returns the numbers of
subscribers of a subreddit passed to it"""

import requests


def number_of_subscribers(subreddit):
    """Function that returns the numbers of
    subscribers of a subreddit passed to it"""

    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

    response = requests.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    retValue = response.json().get('data').get('subscribers')
    if retValue:
        return retValue
    else:
        return 0

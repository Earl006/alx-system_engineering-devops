#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 404:
            return 0

        response.raise_for_status()
        results = response.json().get("data")
        
        if results:
            return results.get("subscribers", 0)
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return 0

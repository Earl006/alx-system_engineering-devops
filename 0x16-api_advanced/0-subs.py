import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid or private, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        if "data" in data:
            subscribers = data["data"].get("subscribers", 0)
            return subscribers
    except (requests.exceptions.HTTPError, KeyError):
        pass

    return 0

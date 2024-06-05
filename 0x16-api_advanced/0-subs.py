#!/usr/bin/python3
"""Function  to query number of subscribers given the reddit subreddit"""
import requests

def number of subscribers(subreddit):
	url="https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {
		"User Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
	}
	response = requests.get(url, headers=headers, allow_redirects=False)
	if(response.status_code == 404
		return 0
	results = response.json().get(data)
	return results.get("subscribers")

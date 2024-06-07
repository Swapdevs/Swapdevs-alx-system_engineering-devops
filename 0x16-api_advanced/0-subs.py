import requests

def number_of_subscribers(subreddit):
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    response_data = response.json()
    if 'data' in response_data and 'subscribers' in response_data['data']:
        return response_data['data']['subscribers']
    else:
        return 0

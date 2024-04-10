from requests import get

def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            results = response.json()
            subscribers = results.get('data', {}).get('subscribers')
            if subscribers is not None:
                return "OK"
            else:
                return 0
        except Exception:
            return 0
    else:
        return 0


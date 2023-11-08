import requests


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    url = f"https://www.reddit.com/r/{subreddit.lower()}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return

    results = response.json()
    data = results.get("data")
    if data is None:
        return

    after = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in set(word_list):
            if word.lower() in title and not any(char.isalpha()
                                                 for char in word):
                times = title.count(word.lower())
                instances[word] = instances.get(word, 0) + times

    if after is None:
        if not instances:
            return
        sorted_instances = sorted(instances.items(),
                                  key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in sorted_instances]
    else:
        count_words(subreddit, word_list, instances, after, count)

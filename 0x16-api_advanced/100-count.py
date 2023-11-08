#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    """
    Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
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
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.HTTPError:
        print("")
        return

    results = response.json()
    data = results.get("data")
    if data is None:
        print("")
        return

    after = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in set(word_list):
            if word.lower() in title:
                times = title.count(word.lower())
                instances[word] = instances.get(word, 0) + times

    if after is None:
        if not instances:
            print("")
            return
        sorted_instances = sorted(instances.items(),
                                  key=lambda kv: (-kv[1], kv[0].lower()))
        [print("{}: {}".format(k, v)) for k, v in sorted_instances]
    else:
        count_words(subreddit, word_list, instances, after, count)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".
              format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2:])

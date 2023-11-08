#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests
import json

def count_words(subreddit, word_list):
    instances = {}
    after = None
    count = 0

    while True:
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        }
        params = {
            "after": after,
            "count": count,
            "limit": 100
        }

        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check HTTP status code
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        try:
            results = response.json()
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            break

        data = results.get("data")
        after = data.get("after")
        count += data.get("dist")

        for post in data.get("children"):
            title = post.get("data").get("title").lower().split()
            for word in word_list:
                instances[word] = instances.get(word, 0) + title.count(word.lower())

        if after is None:
            break

    if len(instances) == 0:
        print("")
    else:
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in instances]

if __name__ == "__main__":
    subreddit = input("Enter subreddit: ")
    words = input("Enter words (comma-separated): ").split(',')

    count_words(subreddit, words)

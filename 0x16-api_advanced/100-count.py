#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests

def count_words(subreddit, word_list, instances=None, after="", count=0):
    if instances is None:
        instances = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    try:
        results = response.json()
    except ValueError:
        print("Error decoding JSON.")
        return

    data = results.get("data")
    after = data.get("after")
    count += data.get("dist")

    for post in data.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            instances[word] = instances.get(word, 0) + title.count(word.lower())

    if after is not None:
        count_words(subreddit, word_list, instances, after, count)

    if count == data.get("dist"):
        print("No posts match or the subreddit is invalid.")
        return

    sorted_instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
    [print(f"{k}: {v}") for k, v in sorted_instances]

if __name__ == "__main__":
    subreddit = input("Enter subreddit: ").strip()
    words = set(input("Enter words (comma-separated): ").lower().split(','))

    count_words(subreddit, words)
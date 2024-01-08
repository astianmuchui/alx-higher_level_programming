#!/usr/bin/python3

"""
Takes in 2 arguments and displays the 10 most
recent commits
from the repository specified by the user
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    json = response.json()
    for commit in json[:10]:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))

#!/usr/bin/python3
""" 1-main.py """

import sys
from 1-top_ten import 1-top_ten  # Importing your function

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        1-top_ten(sys.argv[1])


__author__ = 'erico'

"""
Library for this project
"""


## URLs used in this library
BASE_URL = "https://api.github.com/"


USER_URL = "users/{user}"
USER_REPO_LIST = "users/{user}/repos"

REPO_URL = "repos/{full_name}"
ALL_REPO_LIST = "repositories"

REPO_COMMIT_LIST = "repos/{full_name}/commits" #"/repos/{owner}/{repo}/commits"
RAW_COMMIT = "{commit_href}.patch"
COMMIT_DETAILS = "repos/{full_name}/commits/{commit_sha}"
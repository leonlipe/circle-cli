from __future__ import print_function
from helpers import credentials
import requests
import sys

URL_TEMPLATE = "https://circleci.com/api/v1.1/project/{}/{}/{}"


def get_builds(provider, repo, count, branch, all_builds, only_running=False):
    if all_builds:
        branch_argument = ""
    else:
        branch_argument = "tree/{}".format(branch)

    url = URL_TEMPLATE.format(provider, repo, branch_argument)
    password = credentials.credentials()
    params = {"circle-token": password, "limit": count}
    if only_running:
        params["filter"] = "running"

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(response.json(), file=sys.stderr)
        sys.exit(1)

    return response.json()

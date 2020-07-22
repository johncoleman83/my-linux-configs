#!/usr/bin/env python3
"""
fetch all git repos
"""
import copy
import json
import os
import requests

USERNAME = 'johncoleman83'
GITHUB_API_URL = 'https://api.github.com'
GITHUB_DOMAIN_URL = 'https://github.com'
GITHUB_REPOS_URL = '{}/users/{}/repos'.format(GITHUB_API_URL, USERNAME)
HEADERS_DEFAULT = {
  'Accept': 'application/json',
}
headers = copy.deepcopy(HEADERS_DEFAULT)

def fetch_all_repos():
  """
  ping api example property/detail by id
  """

  url = "{}".format(GITHUB_REPOS_URL)

  r = requests.get(url, headers=headers)
  return r.json()

def results_to_full_urls(results):
  repo_list = []
  for result in results:
    repo_list.append(
      "{}/{}".format(GITHUB_DOMAIN_URL, result.get("full_name"))
    )
  return repo_list

def clone_all_repos(repo_list):
  for url in repo_list:
    command = 'git clone {}'.format(url)
    os.system(command)

def execute():
  """
  call api and print
  """
  results = fetch_all_repos()
  repo_list = results_to_full_urls(results)
  clone_all_repos(repo_list)

if __name__ == '__main__':
  execute()

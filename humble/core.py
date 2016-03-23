# -*- coding: utf-8 -*-

"""
humble.cli
~~~~~~~~~~

This module contains the main API interface for Humble.

"""

try:
    import json
except ImportError:
    import simplejson as json


from github import GitHub, ApiNotFoundError
import requests


github = GitHub()


__title__ = 'humble'
__version__ = '0.1.2'
__build__ = 0x000102
__author__ = 'Kenneth Reitz'
__license__ = 'ISC'
__copyright__ = 'Copyright 2011 Kenneth Reitz'
__docformat__ = 'restructuredtext'


GITHUB_API = 'https://api.github.com/'



def get_info_for(username):
    try:
        return github.users(username).get()
    except (RuntimeError, ApiNotFoundError) as error:
        return None


def get_repos_for(username):
    
    r = requests.get('{0}{1}'.format(GITHUB_API, username))
    repos = json.loads(r.content).get('user', {}).get('repositories', None)
    
    if repos:
        def _sort(repo):
            return repo.get('watchers', '0')
    
        return sorted(repos, key=_sort, reverse=True)
    else:
        return []
    
    
# print get_repos_for('kennethreitz')
# print dir(get_info_for('kennethreitz'))

# print get_info_for('kennethreitz').public_repo_count

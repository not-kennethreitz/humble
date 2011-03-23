# -*- coding: utf-8 -*-

from github2.client import Github


github = Github()


def get_info_for(username):
    return github.users.show(username)


def get_repos_for(username):
    return github.repos.list(username)
    
    
# print get_repos_for('kennethreitz')
# print dir(get_info_for('kennethreitz'))

# print get_info_for('kennethreitz').public_repo_count

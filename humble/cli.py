# -*- coding: utf-8 -*-

"""
humble.cli
~~~~~~~~~~

This module contains the CLI interface for Humble.

"""

import sys

from . import core
from clint import args
from clint.textui import puts, colored
from clint.textui.columns import columns


def version():
    puts('{0} version {1}.'.format(colored.yellow(core.__title__), core.__version__))
    sys.exit(0)
    
def about():
    puts('by Kenneth Reitz <me@kennethreitz.com>')
    puts('http://github.com/kennethreitz/humble')


def start():
    
    if args.flags.contains(('--version', '--ver', '-v')):
        version()
    
    username = args.get(0)
    if not username:
        puts('Please provide a username.')
        sys.exit(1)
    
    
    user = core.get_info_for(username)
    
    if user:
        user_info = ' - '.join((
            str(colored.cyan(username)),
            '{} followers'.format(str(user.followers_count)),
            '{} public repositories'.format(str(user.public_repo_count))
        ))
        puts(user_info)
        
        for repo in core.get_repos_for(username):
            
            # NAME
            
            c = [[colored.yellow(repo[u'name']), 38],]
            
            
            # WATCHERS
            
            watchers = repo[u'watchers']
            
            watchers_s = ''
            if watchers > 1:
                watchers_s += 's' 
            
            c.append(['{0} watcher{1}'.format(watchers, watchers_s), 14])
            
            
            # FORKS
            
            forks = repo[u'forks']
            
            forks_s = ''
            if forks > 1:
                forks_s += 's' 
            
            c.append(['{0} fork{1}'.format(forks, forks_s), 10])
            

            # FORK

            if repo.get('fork', False):
                fork = colored.red('(FORK)')
            else:
                fork = ''
                
            c.append([fork, 10])
            
            # print the column
            puts(columns(*c))


    else:
        puts('Please provide a valid username')
        sys.exit(1)
    
    
    
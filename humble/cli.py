# -*- coding: utf-8 -*-

"""
humble.cli
~~~~~~~~~~

This module contains the CLI interface for Humble.

"""

import sys

from . import core
from clint import args
from clint.textui import puts, colored, columns


PROJECT_BYLINE = 'by Kenneth Reitz <me@kennethreitz.com>'
PROJECT_URL = 'https://github.com/kennethreitz/humble'


def show_version():
    puts('{0} v{1}.'.format(colored.yellow(core.__title__), core.__version__))


def show_usage():
    puts('Usage: '+ colored.cyan('humble <username>'))


def show_about():
    puts('{0} {1}'.format(colored.yellow(core.__title__), PROJECT_BYLINE))
    puts(PROJECT_URL)


def start():
    if args.flags.contains(('--version', '--ver', '-v')):
        show_version()
        sys.exit(2)

    elif args.flags.contains(('-h', '--help')):
        show_usage()
        sys.exit(2)
    
    username = args.get(0)
    if not username:
        show_about()
        puts('')
        show_usage()
        sys.exit(1)
    
    if ('/') in username:
        # display project info
        puts('project info')
        
        user = core.get_info_for(username.split('/')[0])
    
        if user:
            user_info = ' - '.join((
                str(colored.cyan(username)),
                '{0} followers'.format(str(user.followers_count)),
                '{0} public repositories'.format(str(user.public_repo_count))
            ))
            puts(user_info)
        
    else:
        
        user = core.get_info_for(username)
    
        if user:
            user_info = ' - '.join((
                str(colored.cyan(username)),
                '{0} followers'.format(str(user.followers_count)),
                '{0} public repositories'.format(str(user.public_repo_count))
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
    
    
    
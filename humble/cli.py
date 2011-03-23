# -*- coding: utf-8 -*-

"""
vain.cli
~~~~~~~~

This module contains the CLI interface for Vain.

"""

from . import core
from clint import args


def start():
    username = args.get(0)
    
    user = core.get_info_for(username)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import humble



class HumbleTestSuite(unittest.TestCase):
    """Humble test cases."""

    def setUp(self):
        pass

    def tearDown(self):
        """Teardown."""
        pass

    def test_humble_works(self):
        """Most ghetto test ever."""
        
        os.system('./humbler kennethreitz')
        
    def test_get_user(self):
        
        user = humble.get_info_for('kennethreitz')
        
        user2 = humble.get_info_for('some_user_that_is_not_real')
        
        
    def test_get_repos(self):
         repos = humble.get_repos_for('kennethreitz')
         
if __name__ == '__main__':
    unittest.main()
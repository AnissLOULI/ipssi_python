#!/usr/bin/python3

import unittest
from tree import show_tree
 
class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_show_tree_1(self):
        self.assertEqual( show_tree(1), )

    def test_show_tree_2(self):
        self.assertEqual( show_tree(2), )
    
    def test_show_tree_5(self):
        self.assertEqual( show_tree(5), )
    
    def test_show_tree_30(self):
        self.assertEqual( show_tree(30), )

if __name__ == '__main__':
    unittest.main()

#python3 -m doctest tree.py -v
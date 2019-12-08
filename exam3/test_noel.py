#!/usr/bin/python3


import unittest
from noel import show_noel

class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_show_noel_2018818(self):
        self.assertEqual( show_noel(2018-8-18), "129 days before christmas")
    
    def test_show_noel_2020111(self):
        self.assertEqual( show_noel(2020-11-1), "54 days before christmas")

if __name__ == '__main__':
    unittest.main()

#python3 -m doctest show_noel.py -v
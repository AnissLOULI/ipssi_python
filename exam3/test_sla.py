#!/usr/bin/python3


import unittest
from sla import show_sla

class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_sla_999(self):
        self.assertEqual( show_sla(99.99), "0h 52m 35s")
    
    def test_sla_998(self):
        self.assertEqual( show_sla(99.8), "17h 31m 55s")
    
    def test_sla_995(self):
        self.assertEqual( show_sla(99.5), "43h 49m 48s")   

if __name__ == '__main__':
    unittest.main()

#python3 -m doctest sla.py -v
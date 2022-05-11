#!/usr/bin/env python3
import unittest
from harrypotterkata import get_lowest_price
  
class TestKata(unittest.TestCase):
    # test function to test equality of two value
    def test_basic(self):
        self.assertEqual(0, get_lowest_price([]))
        self.assertEqual(8, get_lowest_price([1]))
  
if __name__ == '__main__':
    unittest.main()
'''
Created on 2020/05/02

@author: USER
'''
import unittest
from calculate.keisan import tashizan, hikizan


class TestKeisan(unittest.TestCase):
    """test class of keisan.py
    """
    def test_tashizan(self):
        """test method for tashizan
        """
        value1 = 2
        value2 = 6
        expected = 8
        actual = tashizan(value1, value2)
        self.assertEqual(expected, actual)

class TestKeisan2(unittest.TestCase):
    """test class of keisan.py
    """
    def test_hikizan(self):
        """test method for hikizan
        """
        value1 = 2
        value2 = 12
        expected = -10
        actual = hikizan(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
'''
Created on 2020/05/02

@author: USER
'''
import unittest
from num.numprint import numTest

class Testnumprint(unittest.TestCase):
    def test_numprint(self):
        numVal ="10"
        expect = "10"
        actual = numTest(numVal)
        self.assertEqual(expect, actual)

if __name__ == "__main__":
    unittest.main()
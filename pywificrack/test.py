from pywificrack.util import *
from unittest import TestCase
import unittest
class TestMain(TestCase):
    def testUtil(self):
        print Util.getWifiName()

if __name__ == '__main__':
    unittest.main()


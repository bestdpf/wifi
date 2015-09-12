from pywificrack.util import *
from pywificrack.crack import *
from unittest import TestCase
import unittest
class TestMain(TestCase):
    def testUtil(self):
        print Util.getWifiNames()
        print Util.getWirelessCards()
    
    def testCrack(self):
        cards = Util.getWirelessCards()
        crack = Crack(cards[0])
        crack.run()

if __name__ == '__main__':
    unittest.main()


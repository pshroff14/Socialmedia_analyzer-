import unittest
from Analyzer import *


class TestTwit(unittest.TestCase):

    # def test_twitauth(self):
    #     self.assertisNone(trend_location(0))

    def test_add(self):
        self.assertEqual(add_num(5),6)

    # def test_auth(self):
    #     self.assertEqual()

# This test see's if the list of strings of the GettrendsWoeid is the same as the function itself
    def test_woe(self):
        woeid = 23637105    # Enter WOEID number
        a = trend_location(woeid)
        b = api.GetTrendsWoeid(woeid, exclude=None)
        self.assertListEqual(a, b)






if __name__ == '__main__':
    unittest.main()



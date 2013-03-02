# coding: utf-8
import unittest

import utils


class TestGotoUrl(unittest.TestCase):
    def test_simple_url(self):
        url = "http://google.com/"
        self.assertTrue(utils.goto_url(url), '/goto/aHR0cDovL2dvb2dsZS5jb20v')

    def test_cyrillic_url(self):
        url = u"http://яндекс.рф/"
        self.assertTrue(utils.goto_url(url), '/goto/aHR0cDovL9GP0L3QtNC10LrRgS7RgNGELw==')


if __name__ == '__main__':
    unittest.main()

# To run the test suite
# python tests.py

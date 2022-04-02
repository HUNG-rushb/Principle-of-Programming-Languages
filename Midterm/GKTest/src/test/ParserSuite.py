# 1912683
# Nguyen Thien Bao
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test32(self):
        input = """
            a, static b @ int;
            static c, d @ float;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 2032))
    
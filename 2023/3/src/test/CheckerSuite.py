# 1913652
# Trịnh Duy Hưng
import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_1(self):
        input = """
        a : integer;
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """
        main : function void() {
        {
            
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_1(self):
    #     input = """
    #     a : integer;
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
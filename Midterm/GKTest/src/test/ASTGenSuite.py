# 1912683
# Nguyen Thien Bao
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test(self):
        input = """
            a, static b, d, e @ int;
            static c, d @ float;
        """
        expect = """Program([VarDecl(a,False,IntType,VarDecl(b,True,IntType,VarDecl(d,False,IntType,VarDecl(e,False,IntType,)))),VarDecl(c,True,FloatType,VarDecl(d,False,FloatType,))])"""
        self.assertTrue(TestAST.test(input,expect,300))
    

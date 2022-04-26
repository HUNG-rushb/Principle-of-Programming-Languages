import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    

    # def test_12(self):
    #     input = """
    #         Class Program {
                
    #         }
    #         Class Program {
                
    #         }
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input,expect,412))  Val $adwqdqw: Float = 1; 

    # def test_13(self):
    #     input = """
    #         Class Program : Hung{
               
                
                 
                
    #         }
            
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    def test_13(self):
        
        input = """
            Class Program {
                
                Var adwqdqwd: Int = 1 + 2;
            }
            
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,413))

    # def test0(self):
    #     input = """
    #     Class Dog : Animal {
    #         Val $a : Int = 3.2;
    #         $getDog() { }
    #     }
    #     Class Meow {
    #         $set() { }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: ConstDecl(Id($a),IntType,FloatLit(3.2))"
    #     self.assertTrue(TestChecker.test(input,expect,400))
    # def test1(self):
    #     input = """
    #     Class A {
    #         Var $a: Int;


    #         Var bbb: Lmao;

    #         Hung (a:Int;b:Float)
    #         {

    #         }
    #     }
        
        
       
         
    #     """
    #     expect = "Redeclared Class: A"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test2(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = 2 + True;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(2),BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    # def test3(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = 3;
    #     }
    #     Class B {
    #         Val $b: A = New A();
    #     }
    #     """
    #     expect = "Undeclared Method: Constructor"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test4(self):
    #     input = """
    #     Class B: A {
    #         Val $r :Int = 2 + 2 * 2.5;
    #         Var a: Boolean = True;
    #         setA(a: Int) { }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: ConstDecl(Id($r),IntType,BinaryOp(+,IntLit(2),BinaryOp(*,IntLit(2),FloatLit(2.5))))"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test5(self):
    #     input = """
    #     Class B: A {
    #         Var t: Float = 1.4 % 3; 
    #         setA(a: Int) { }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.4),IntLit(3))"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    # def test6(self):
    #     input = """
    #     Class A {
    #         Var a: Array[Array[Int, 2], 2] = Array(
    #                                             Array(3,6),
    #                                             Array(8,9.2)
    #         );
    #     }
    #     """
    #     expect = "Illegal Array Literal: [IntLit(8),FloatLit(9.2)]"
    #     self.assertTrue(TestChecker.test(input,expect,406))
    # def test7(self):
    #     input = """
    #     Class A {
    #         Var a: Int = 120;
    #         Val $a: C = New C();
    #     }
    #     """
    #     expect = "Undeclared Class: C"
    #     self.assertTrue(TestChecker.test(input,expect,407))
    # def test8(self):
    #     input = """
    #     Class A {
    #         Var a, t, r: Int = 120, 12 * 60 - 9, 1e4;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(r),IntType,FloatLit(10000.0))"
    #     self.assertTrue(TestChecker.test(input,expect,408))
    # def test9(self):
    #     input = """
    #     Class B {
    #         Val C: String;
    #     }
    #     """
    #     expect = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(input,expect,409))
    # def test10(self):
    #     input = """
    #     Class A {
    #         Val $a: Int = 3;
    #         Constructor(a: Float; b: Int) { }
    #     }
    #     Class B {
    #         Val $b: A = New A(1, 3.2);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1),FloatLit(3.2)])"
    #     self.assertTrue(TestChecker.test(input,expect,410))
    
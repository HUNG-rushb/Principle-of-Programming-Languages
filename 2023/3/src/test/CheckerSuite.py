# 1913652
# Trịnh Duy Hưng
import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_0(self):
        input = """
        main : function void(  ) 
        {
            c : integer = 2;
            a : integer = 2;
        }

        d : integer = 1;
        
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_1(self):
        input = """
        a : integer = 3;
        d : float = 3.5;
        e : boolean = true;
        f : string = "wfefwef";
        main : function void(  ) 
        {
            c : integer;
            a = 6;
        }
        
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """


        arr : array [3] of integer = {1,2,3};

        main : function void(  ) 
        {
          
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """

        main : function void(  ) 
        {
          a : function void(  ) 
            {
            
            }
        }
        """
        expect = "Invalid statement in function: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """
        a : integer = 1;
        main: function void() {
            a : integer = 3;
            res : auto = foo();
            foo(1);
        }
        foo : function auto (){}
        foo1 : function auto (j : integer){}
        """
        expect = "Type mismatch in expression: CallStmt(foo, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_5(self):
        input = """
        a : integer = 1;
        main: function void() {
            res : auto = readString();
            b: integer = a;
            res = foo() + foo(2); 
        }
        foo : function auto (){}
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_6(self):
        input = """
        main: function void() {
            res : auto = readString();
            b: integer = a;
  
        }
        foo : function auto (){}
        a : integer = 1;
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_7(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_8(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        height, weight : integer;
        foo : integer;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_9(self):
        input = """
        main: function void() {
        }
        main: function void() {
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_10(self):
        input = """
        main: function void(){}
        height, weight : integer;
        readInteger : integer;
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    
    def test_11(self):
        input = """
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_12(self):
        input = """
        a,b,c,a: integer;
        main: function void(){
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_13(self):
        input = """
        a: integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_14(self):
        input = """
        a: integer;
        b: float;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_15(self):
        input = """
        main: function integer(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_16(self):
        input = """
        main: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    
    
    def test_17(self):
        input = """
        main: function void() {}
        a: auto;
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_18(self):
        input = """
        main: function void(){}
        a, b, c, d: auto = 1, 2.5, "My name is Hoa", true;
        e : integer = 2.5;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_19(self):
        input = """
        area : float = 2.5;
        an : float = 1 ;
        x : float = true;
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, FloatType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,400))
    

    def test_20(self):
        input = """
        main: function void(a: integer){}
        jjj: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_21(self):
        input = """
        arr : array [3] of integer = {1,2,3.3};
        main: function void(){}
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.3)])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_22(self):
        input = """
        arr : array [3] of integer = {1.0,2.2,3.3};
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([FloatLit(1.0), FloatLit(2.2), FloatLit(3.3)]))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_23(self):
        input = """
        arr : array [2,3,4,5] of integer;
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_24(self):
        input = """
        arr : array [2] of integer = {1,2};
        a : float = 1.0;
        element : integer = arr[a];
        main: function void(){
            
        }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_25(self):
        input = """
        a : float = 1.0;
        element : integer = a[1.0];
        main: function void(){
        }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_26(self):
        input = """
        element : string = arr[10];
        main: function void(){
        }
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_27(self):
        input = """
        arr : array [5] of integer = {0,1,2,3,4};
        b : integer = arr[0];
        element : integer = arr[arr[0]];
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_28(self):
        input = """
        a : float = foo(1,2);
        b : integer = foo(1,2);
        main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_29(self):
        input = """
        a : string = foo(1,2) + 1;
        main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_30(self):
        input = """
        a : string = foo(1,2) + 1;
        main: function void(){}
        a1 : string = foo(1,2) + 1;
        main1: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_31(self):
        input = """
        main : function void(  ) 
        {
            c : integer = 2;
            a : integer = 2;
        }

        d : integer = 1;
        
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_32(self):
        input = """
        a : integer = 3;
        d : float = 3.5;
        e : boolean = true;
        f : string = "wfefwef";
        main : function void(  ) 
        {
            c : integer;
            a = 6;
        }
        
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_33(self):
        input = """


        arr : array [3] of integer = {1,2,3};

        main : function void(  ) 
        {
          
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_34(self):
        input = """

        main : function void(  ) 
        {
          a : function void(  ) 
            {
            
            }
        }
        """
        expect = "Invalid statement in function: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_34(self):
        input = """
        a : integer = 1;
        main: function void() {
            a : integer = 3;
            res : auto = foo();
            foo(1);
        }
        foo : function auto (){}
        foo1 : function auto (j : integer){}
        """
        expect = "Type mismatch in expression: CallStmt(foo, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_35(self):
        input = """
        a : integer = 1;
        main: function void() {
            res : auto = readString();
            b: integer = a;
            res = foo() + foo(2); 
        }
        foo : function auto (){}
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_36(self):
        input = """
        main: function void() {
            res : auto = readString();
            b: integer = a;
  
        }
        foo : function auto (){}
        a : integer = 1;
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_37(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_38(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        height, weight : integer;
        foo : integer;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_39(self):
        input = """
        main: function void() {
        }
        main: function void() {
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_40(self):
        input = """
        main: function void(){}
        height, weight : integer;
        readInteger : integer;
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    
    def test_41(self):
        input = """
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_42(self):
        input = """
        a,b,c,a: integer;
        main: function void(){
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_43(self):
        input = """
        a: integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_44(self):
        input = """
        a: integer;
        b: float;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_45(self):
        input = """
        main: function integer(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_46(self):
        input = """
        main: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    
    
    def test_47(self):
        input = """
        main: function void() {}
        a: auto;
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_48(self):
        input = """
        main: function void(){}
        a, b, c, d: auto = 1, 2.5, "My name is Hoa", true;
        e : integer = 2.5;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_49(self):
        input = """
        area : float = 2.5;
        an : float = 1 ;
        x : float = true;
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, FloatType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,400))
    

    def test_50(self):
        input = """
        main: function void(a: integer){}
        jjj: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_51(self):
        input = """
        arr : array [3] of integer = {1,2,3.3};
        main: function void(){}
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.3)])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_52(self):
        input = """
        arr : array [3] of integer = {1.0,2.2,3.3};
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([FloatLit(1.0), FloatLit(2.2), FloatLit(3.3)]))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_53(self):
        input = """
        arr : array [2,3,4,5] of integer;
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_54(self):
        input = """
        arr : array [2] of integer = {1,2};
        a : float = 1.0;
        element : integer = arr[a];
        main: function void(){
            
        }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_55(self):
        input = """
        a : float = 1.0;
        element : integer = a[1.0];
        main: function void(){
        }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_56(self):
        input = """
        element : string = arr[10];
        main: function void(){
        }
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_57(self):
        input = """
        arr : array [5] of integer = {0,1,2,3,4};
        b : integer = arr[0];
        element : integer = arr[arr[0]];
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_58(self):
        input = """
        a : float = foo(1,2);
        b : integer = foo(1,2);
        main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_59(self):
        input = """
        a : string = foo(1,2) + 1;
        main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_60(self):
        input = """
        a : string = foo(1,2) + 1;
        main: function void(){}
        a1 : string = foo(1,2) + 1;
        main1: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_61(self):
        input = """
        main : function void(  ) 
        {
            c : integer = 2;
            a : integer = 2;
        }

        d : integer = 1;
        
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_615(self):
        input = """
        a : integer = 3;
        d : float = 3.5;
        e : boolean = true;
        f : string = "wfefwef";
        main : function void(  ) 
        {
            c : integer;
            a = 6;
        }
        
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_62(self):
        input = """


        arr : array [3] of integer = {1,2,3};

        main : function void(  ) 
        {
          
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_63(self):
        input = """

        main : function void(  ) 
        {
          a : function void(  ) 
            {
            
            }
        }
        """
        expect = "Invalid statement in function: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_64(self):
        input = """
        a : integer = 1;
        main: function void() {
            a : integer = 3;
            res : auto = foo();
            foo(1);
        }
        foo : function auto (){}
        foo1 : function auto (j : integer){}
        """
        expect = "Type mismatch in expression: CallStmt(foo, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_65(self):
        input = """
        a : integer = 1;
        main: function void() {
            res : auto = readString();
            b: integer = a;
            res = foo() + foo(2); 
        }
        foo : function auto (){}
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_66(self):
        input = """
        main: function void() {
            res : auto = readString();
            b: integer = a;
  
        }
        foo : function auto (){}
        a : integer = 1;
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_67(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_68(self):
        input = """
        foo: function integer (){}
        main: function void(){}
        height, weight : integer;
        foo : integer;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_69(self):
        input = """
        main: function void() {
        }
        main: function void() {
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_70(self):
        input = """
        main: function void(){}
        height, weight : integer;
        readInteger : integer;
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    
    def test_71(self):
        input = """
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_72(self):
        input = """
        a,b,c,a: integer;
        main: function void(){
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_73(self):
        input = """
        a: integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_74(self):
        input = """
        a: integer;
        b: float;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_75(self):
        input = """
        main: function integer(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_76(self):
        input = """
        main: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    
    
    def test_77(self):
        input = """
        main: function void() {}
        a: auto;
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_78(self):
        input = """
        main: function void(){}
        a, b, c, d: auto = 1, 2.5, "My name is Hoa", true;
        e : integer = 2.5;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_79(self):
        input = """
        area : float = 2.5;
        an : float = 1 ;
        x : float = true;
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, FloatType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,400))
    

    def test_80(self):
        input = """
        main: function void(a: integer){}
        jjj: function void(a: integer){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_81(self):
        input = """
        arr : array [3] of integer = {1,2,3.3};
        main: function void(){}
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.3)])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_82(self):
        input = """
        arr : array [3] of integer = {1.0,2.2,3.3};
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([FloatLit(1.0), FloatLit(2.2), FloatLit(3.3)]))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_83(self):
        input = """
        arr : array [2,3,4,5] of integer;
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_84(self):
        input = """
        arr : array [2] of integer = {1,2};
        a : float = 1.0;
        element : integer = arr[a];
        main: function void(){
            
        }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_85(self):
        input = """
        a : float = 1.0;
        element : integer = a[1.0];
        main: function void(){
        }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_86(self):
        input = """
        element : string = arr[10];
        main: function void(){
        }
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_87(self):
        input = """
        arr : array [5] of integer = {0,1,2,3,4};
        b : integer = arr[0];
        element : integer = arr[arr[0]];
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_88(self):
        input = """
        a : float = foo(1,2);
        b : integer = foo(1,2);
        main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_89(self):
        input = """
        a : string = foo(1,2) + 1;
        main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_90(self):
        input = """
        a : string = foo(1,2) + 1;
        main: function void(){}
        a1 : string = foo(1,2) + 1;
        main1: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_91(self):
        input = """
        arr : array [3] of integer = {1,2,3.3};
        main: function void(){}
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.3)])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_92(self):
        input = """
        arr : array [3] of integer = {1.0,2.2,3.3};
        main: function void(){}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([FloatLit(1.0), FloatLit(2.2), FloatLit(3.3)]))"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_93(self):
        input = """
        arr : array [2,3,4,5] of integer;
        main: function void(){}
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_94(self):
        input = """
        arr : array [2] of integer = {1,2};
        a : float = 1.0;
        element : integer = arr[a];
        main: function void(){
            
        }
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_95(self):
        input = """
        a : float = 1.0;
        element : integer = a[1.0];
        main: function void(){
        }
        """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_96(self):
        input = """
        element : string = arr[10];
        main: function void(){
        }
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_97(self):
        input = """
        arr : array [5] of integer = {0,1,2,3,4};
        b : integer = arr[0];
        element : integer = arr[arr[0]];
        main: function void(){
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_98(self):
        input = """
        a : float = foo(1,2);
        b : integer = foo(1,2);
        main: function void(){}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,428))
        
    

    
    



    
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

#     def test_vardecl(self):
#         input = """
#         x, y, z: integer;
#         a: float = 1.2;
#         b,c: boolean = true, false;
#         d: array[1,2] of boolean;
#         e,f: array[2,3] of string;
#         g: array[1] of float = {a+1.2};
#         h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};
#         """
#         expect = """Program([
# 	VarDecl(x, IntegerType)
# 	VarDecl(y, IntegerType)
# 	VarDecl(z, IntegerType)
# 	VarDecl(a, FloatType, FloatLit(1.2))
# 	VarDecl(b, BooleanType, BooleanLit(True))
# 	VarDecl(c, BooleanType, BooleanLit(False))
# 	VarDecl(d, ArrayType([IntegerLit(1), IntegerLit(2)], BooleanType))
# 	VarDecl(e, ArrayType([IntegerLit(2), IntegerLit(3)], StringType))
# 	VarDecl(f, ArrayType([IntegerLit(2), IntegerLit(3)], StringType))
# 	VarDecl(g, ArrayType([IntegerLit(1)], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))]))
# 	VarDecl(h, ArrayType([IntegerLit(1), IntegerLit(2)], StringType), ArrayLit([StringLit(D96), StringLit(MT22)]))
# 	VarDecl(i, ArrayType([IntegerLit(1), IntegerLit(2)], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 301))

#     def test_funcdecl(self):
#         input = """
#         main: function void (){}
#         abc: function integer(){}
#         def: function integer() inherit abc{}
#         ghi: function array[1,2] of boolean () {}
#         klm: function array[1,2] of string () inherit ghi {}
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# 	FuncDecl(abc, IntegerType, [], None, BlockStmt([]))
# 	FuncDecl(def, IntegerType, [], abc, BlockStmt([]))
# 	FuncDecl(ghi, ArrayType([IntegerLit(1), IntegerLit(2)], BooleanType), [], None, BlockStmt([]))
# 	FuncDecl(klm, ArrayType([IntegerLit(1), IntegerLit(2)], StringType), [], ghi, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 302))

#     def test_param(self):
#         input = """
#         abc: function integer(a: integer){}
#         def: function integer(a: array[3] of integer) inherit abc{}
#         ghi: function array[1,2] of boolean (out n: integer) {}
#         klm: function array[1,2] of string (inherit out a: array[3] of integer, n: integer) inherit ghi {}
#         """
#         expect = """Program([
# 	FuncDecl(abc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([]))
# 	FuncDecl(def, IntegerType, [Param(a, ArrayType([IntegerLit(3)], IntegerType))], abc, BlockStmt([]))
# 	FuncDecl(ghi, ArrayType([IntegerLit(1), IntegerLit(2)], BooleanType), [OutParam(n, IntegerType)], None, BlockStmt([]))
# 	FuncDecl(klm, ArrayType([IntegerLit(1), IntegerLit(2)], StringType), [InheritOutParam(a, ArrayType([IntegerLit(3)], IntegerType)), Param(n, IntegerType)], ghi, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_stmt_1(self):
#         input = """
#         abs: function integer() {
#             return 0;
#         }
#         main: function void() {
#             return;
#         }
#         """
#         expect = """Program([
# 	FuncDecl(abs, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))

#     def test_stmt_2(self):
#         input = """
#         plus: function integer(b: integer) {
#             a: integer = 2;
#             return a + b;
#         }
#         abs: function integer() inherit plus {
#             c: integer = a + plus(5);
#             return c;
#         }
#         """
#         expect = """Program([
# 	FuncDecl(plus, IntegerType, [Param(b, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
# 	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(Id(plus), [IntegerLit(5)]))), ReturnStmt(Id(c))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 305))

#     def test_stmt_3(self):
#         input = """
#         modArray: function array[3] of integer (inherit a: array[3] of integer,out n: integer){
#             a[0] = a[0] + n;
#             if(a[1] < n) a[1] = a[1] + n; 
#             if(a[2] > 0) return a;
#             else a[2] = -a[2];
#             return a;
#         }
#         """
#         expect = """Program([
# 	FuncDecl(modArray, ArrayType([IntegerLit(3)], IntegerType), [InheritParam(a, ArrayType([IntegerLit(3)], IntegerType)), OutParam(n, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(Id(a), [IntegerLit(0)]), BinExpr(+, ArrayCell(Id(a), [IntegerLit(0)]), Id(n))), IfStmt(BinExpr(<, ArrayCell(Id(a), [IntegerLit(1)]), Id(n)), AssignStmt(ArrayCell(Id(a), [IntegerLit(1)]), BinExpr(+, ArrayCell(Id(a), [IntegerLit(1)]), Id(n)))), IfStmt(BinExpr(>, ArrayCell(Id(a), [IntegerLit(2)]), IntegerLit(0)), ReturnStmt(Id(a)), AssignStmt(ArrayCell(Id(a), [IntegerLit(2)]), UnExpr(-, ArrayCell(Id(a), [IntegerLit(2)])))), ReturnStmt(Id(a))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 306))

#     def test_stmt_4(self):
#         input = """
#         printArray: function void (inherit a: array[3] of integer,n: integer){
#             for(i = 1, i<length(a), i+1) print(a[i]);
#             while(a[1]<n) {
#                 print(a[1]);
#                 a[1] = a[1] - 1;
#             }
#             do {
#                 a[2] = a[2] - n;
#             } while(a[2] > 0);
#         }
#         """
#         expect = """Program([
# 	FuncDecl(printArray, VoidType, [InheritParam(a, ArrayType([IntegerLit(3)], IntegerType)), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(Id(length), [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(Id(a), [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(Id(a), [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(Id(a), [IntegerLit(1)])), AssignStmt(ArrayCell(Id(a), [IntegerLit(1)]), BinExpr(-, ArrayCell(Id(a), [IntegerLit(1)]), IntegerLit(1)))])), DoWhileStmt(BinExpr(>, ArrayCell(Id(a), [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(Id(a), [IntegerLit(2)]), BinExpr(-, ArrayCell(Id(a), [IntegerLit(2)]), Id(n)))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 307))

#     def test_stmt_5(self):
#         input = """
#         printArray: function void (a: array[3,1] of integer,n: integer){
#             while(a[1,1]<n) {
#                 print(a[1,1]);
#                 if(n > 1) n = n-1;
#                 else break;
#             }
#             {
#                 m: integer = 5;
#                 for(i = 1, i<length(a), i+1) {
#                     if(a[max(i,2),1]>m) {continue;}
#                     else {m = m-1;}
#                     m = m + 2;
#                 }
#             }
#         }
#         """
#         expect = """Program([
# 	FuncDecl(printArray, VoidType, [Param(a, ArrayType([IntegerLit(3), IntegerLit(1)], IntegerType)), Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, ArrayCell(Id(a), [IntegerLit(1), IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(Id(a), [IntegerLit(1), IntegerLit(1)])), IfStmt(BinExpr(>, Id(n), IntegerLit(1)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), BreakStmt())])), BlockStmt([VarDecl(m, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(Id(length), [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(Id(a), [FuncCall(Id(max), [Id(i), IntegerLit(2)]), IntegerLit(1)]), Id(m)), BlockStmt([ContinueStmt()]), BlockStmt([AssignStmt(Id(m), BinExpr(-, Id(m), IntegerLit(1)))])), AssignStmt(Id(m), BinExpr(+, Id(m), IntegerLit(2)))]))])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 308))
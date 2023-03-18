# Trịnh Duy Hưng 
# 1913652

import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_full_1(self):
        input = """
        main : function void() {
            {
                r, s: integer;
                r = 2.0;
                {

                }

                {
                    a, b: array [5] of integer;
                    s = r * r * myPI;
                    a[0] = s;
                }
                
            }
            return ;
        }
        main : function void() {
            {
                r, s: integer;
                r = 2.0;
                {

                }

                {
                    a, b: array [5] of integer;
                    s = r * r * myPI;
                    a[0] = s;
                }
                
            }
            return ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), BlockStmt([]), BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))])]), ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), BlockStmt([]), BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))])]), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_full_2(self):
        input = """
            printAnimal : function void(out animal: string, num: integer) {       

            }
            printBird : function void(bird : string) inherit printAnimal {
                arr[i, 0] = a[b324234[_fwfow32_3240294024x + ______y[1,2,2,0,0,1234_859348,2]-h[g[5%2]*t[0,t[1]]] * 8+1--1]] + 3;
                b : boolean = 1/2+33243-74989234*93489234909/4382370+3983;
            }
            main: function void() {
                birds : array[2,3] of string = {{"birdA", "birdB", "birdC"},{"birdX", "birdY", "birdZ"}};
                printBird(bird[a[i], 2]);
                return ;
            }
            printAnimal : function void(out animal: string, num: integer) {       

            }
            printBird : function void(bird : string) inherit printAnimal {
                r, s: integer;
                r = 2.0;
                a, b: array [5] of integer;
                s = r * r * myPI;
                a[0] = s;
            }
        """
        expect = """Program([
	FuncDecl(printAnimal, VoidType, [OutParam(animal, StringType), Param(num, IntegerType)], None, BlockStmt([]))
	FuncDecl(printBird, VoidType, [Param(bird, StringType)], printAnimal, BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), IntegerLit(0)]), BinExpr(+, ArrayCell(a, [ArrayCell(b324234, [BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, Id(_fwfow32_3240294024x), ArrayCell(______y, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(0), IntegerLit(0), IntegerLit(1234859348), IntegerLit(2)])), BinExpr(*, ArrayCell(h, [BinExpr(*, ArrayCell(g, [BinExpr(%, IntegerLit(5), IntegerLit(2))]), ArrayCell(t, [IntegerLit(0), ArrayCell(t, [IntegerLit(1)])]))]), IntegerLit(8))), IntegerLit(1)), UnExpr(-, IntegerLit(1)))])]), IntegerLit(3))), VarDecl(b, BooleanType, BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(/, IntegerLit(1), IntegerLit(2)), IntegerLit(33243)), BinExpr(/, BinExpr(*, IntegerLit(74989234), IntegerLit(93489234909)), IntegerLit(4382370))), IntegerLit(3983)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(birds, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(birdA), StringLit(birdB), StringLit(birdC)]), ArrayLit([StringLit(birdX), StringLit(birdY), StringLit(birdZ)])])), CallStmt(printBird, ArrayCell(bird, [ArrayCell(a, [Id(i)]), IntegerLit(2)])), ReturnStmt()]))
	FuncDecl(printAnimal, VoidType, [OutParam(animal, StringType), Param(num, IntegerType)], None, BlockStmt([]))
	FuncDecl(printBird, VoidType, [Param(bird, StringType)], printAnimal, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_full_3(self):
        input = """
            func : function void(){
                ans = 0;
                for (i = 1, i <= n  , i + 1) 
                    for ( j = n, j <i , j -1){
                        ans = ans + (i*j*arrayA[i]);

                        for ( j = n, j <i , j -1)
                            ans = ans + (i*j*arrayA[i]);
                    }
                    for ( j = n, j <i , j -1)
                        ans = ans + (i*j*arrayA[i]);
                    for ( j = n, j <i , j -1){
                        ans = ans + (i*j*arrayA[i]);

                        for ( j = n, j <i , j -1)
                            ans = ans + (i*j*arrayA[i]);
                    }
                    for ( j = n, j <i , j -1)
                        ans = ans + (i*j*arrayA[i]);
                    
                    print(ansfsf4535345___s);
            }
            main: function void(){
                func();
                return;
                func();
                return;
                func();
                return;
                func();
                return;
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(ans), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)])))), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)])))))]))), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)]))))), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)])))), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)])))))])), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)]))))), CallStmt(print, Id(ansfsf4535345___s))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(func, ), ReturnStmt(), CallStmt(func, ), ReturnStmt(), CallStmt(func, ), ReturnStmt(), CallStmt(func, ), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_full_4(self):
        input = """
            /*Test associative */


            b : boolean = (234235!=611) && ( (434_2344+5432 > 7) || !(false && (false || true)));

            a : float = x * x /2 % 2 +(c% 10)*3.0;
            main : function void() {
                arr[i, 0] = a[b[x+y[1,2,2,0,0]-h[g[5%2]*t[0,t[1]]] * 8+1--1]] + 3;
                b : boolean = (234235!=611) && ( (434_2344+5432 > 7) || !(false && (false || true)));
            }
        """
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(&&, BinExpr(!=, IntegerLit(234235), IntegerLit(611)), BinExpr(||, BinExpr(>, BinExpr(+, IntegerLit(4342344), IntegerLit(5432)), IntegerLit(7)), UnExpr(!, BinExpr(&&, BooleanLit(False), BinExpr(||, BooleanLit(False), BooleanLit(True)))))))
	VarDecl(a, FloatType, BinExpr(+, BinExpr(%, BinExpr(/, BinExpr(*, Id(x), Id(x)), IntegerLit(2)), IntegerLit(2)), BinExpr(*, BinExpr(%, Id(c), IntegerLit(10)), FloatLit(3.0))))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), IntegerLit(0)]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), ArrayCell(y, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(0), IntegerLit(0)])), BinExpr(*, ArrayCell(h, [BinExpr(*, ArrayCell(g, [BinExpr(%, IntegerLit(5), IntegerLit(2))]), ArrayCell(t, [IntegerLit(0), ArrayCell(t, [IntegerLit(1)])]))]), IntegerLit(8))), IntegerLit(1)), UnExpr(-, IntegerLit(1)))])]), IntegerLit(3))), VarDecl(b, BooleanType, BinExpr(&&, BinExpr(!=, IntegerLit(234235), IntegerLit(611)), BinExpr(||, BinExpr(>, BinExpr(+, IntegerLit(4342344), IntegerLit(5432)), IntegerLit(7)), UnExpr(!, BinExpr(&&, BooleanLit(False), BinExpr(||, BooleanLit(False), BooleanLit(True)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_full_5(self):
        input = """
            /*Test associative */
            /*Test associative */
            /*Test associative */
            /*Test associative */

            a : float = x * x /2 % 2 +(c% 10)*3.0;

            main : function void() {
                arr[i, 0] = a[b[x+y[1,2,2,0,0]-h[g[5%2]*t[0,t[1]]] * 8+1--1]] + 3;
                b : boolean = (5!=6) && ( (4+5 > 7) || !(false && (false || true)));

                /*Test associative */
            /*Test associative */
            /*Test associative */
            /*Test associative */

               
            }

             /*Test associative */
            /*Test associative */
            /*Test associative */
            /*Test associative */
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(%, BinExpr(/, BinExpr(*, Id(x), Id(x)), IntegerLit(2)), IntegerLit(2)), BinExpr(*, BinExpr(%, Id(c), IntegerLit(10)), FloatLit(3.0))))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), IntegerLit(0)]), BinExpr(+, ArrayCell(a, [ArrayCell(b, [BinExpr(-, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), ArrayCell(y, [IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(0), IntegerLit(0)])), BinExpr(*, ArrayCell(h, [BinExpr(*, ArrayCell(g, [BinExpr(%, IntegerLit(5), IntegerLit(2))]), ArrayCell(t, [IntegerLit(0), ArrayCell(t, [IntegerLit(1)])]))]), IntegerLit(8))), IntegerLit(1)), UnExpr(-, IntegerLit(1)))])]), IntegerLit(3))), VarDecl(b, BooleanType, BinExpr(&&, BinExpr(!=, IntegerLit(5), IntegerLit(6)), BinExpr(||, BinExpr(>, BinExpr(+, IntegerLit(4), IntegerLit(5)), IntegerLit(7)), UnExpr(!, BinExpr(&&, BooleanLit(False), BinExpr(||, BooleanLit(False), BooleanLit(True)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_full_6(self):
        input = """
            main : function void() {
                x = a() + b()*c(d);
                if (x < a(arr[0,i])) return;
                x = x / max(x,y+sub(x-y));
                for (i = 1, i < n , i/2) {
                    {
                        k : integer = 0;
                        k = i;
                        if (k < 10 ) break;

                        for (i = 1, i < n , i/2) {
                            {
                                k : integer = 0;
                                k = i;
                                if (k < 10 ) break;
                            }
                        }
                    }
                }
                print("The result is ",x);
                x = a() + b()*c(d);
                if (x < a(arr[0,i])) return;
                x = x / max(x,y+sub(x-y));
                for (i = 1, i < n , i/2) {
                    {
                        k : integer = 0;
                        k = i;
                        if (k < 10 ) break;

                        for (i = 1, i < n , i/2) {
                            {
                                k : integer = 0;
                                k = i;
                                if (k < 10 ) break;


                                print("The result is ",x);
                x = a() + b()*c(d);
                if (x < a(arr[0,i])) return;
                x = x / max(x,y+sub(x-y));
                for (i = 1, i < n , i/2) {
                    {
                        k : integer = 0;
                        k = i;
                        if (k < 10 ) break;

                        for (i = 1, i < n , i/2) {
                            {
                                k : integer = 0;
                                k = i;
                                if (k < 10 ) break;
                            }
                        }
                    }
                }
                print("The result is ",x);
                            }
                        }
                    }
                }
                print("The result is ",x);

                
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, FuncCall(a, []), BinExpr(*, FuncCall(b, []), FuncCall(c, [Id(d)])))), IfStmt(BinExpr(<, Id(x), FuncCall(a, [ArrayCell(arr, [IntegerLit(0), Id(i)])])), ReturnStmt()), AssignStmt(Id(x), BinExpr(/, Id(x), FuncCall(max, [Id(x), BinExpr(+, Id(y), FuncCall(sub, [BinExpr(-, Id(x), Id(y))]))]))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt()), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt())])]))])])), CallStmt(print, StringLit(The result is ), Id(x)), AssignStmt(Id(x), BinExpr(+, FuncCall(a, []), BinExpr(*, FuncCall(b, []), FuncCall(c, [Id(d)])))), IfStmt(BinExpr(<, Id(x), FuncCall(a, [ArrayCell(arr, [IntegerLit(0), Id(i)])])), ReturnStmt()), AssignStmt(Id(x), BinExpr(/, Id(x), FuncCall(max, [Id(x), BinExpr(+, Id(y), FuncCall(sub, [BinExpr(-, Id(x), Id(y))]))]))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt()), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt()), CallStmt(print, StringLit(The result is ), Id(x)), AssignStmt(Id(x), BinExpr(+, FuncCall(a, []), BinExpr(*, FuncCall(b, []), FuncCall(c, [Id(d)])))), IfStmt(BinExpr(<, Id(x), FuncCall(a, [ArrayCell(arr, [IntegerLit(0), Id(i)])])), ReturnStmt()), AssignStmt(Id(x), BinExpr(/, Id(x), FuncCall(max, [Id(x), BinExpr(+, Id(y), FuncCall(sub, [BinExpr(-, Id(x), Id(y))]))]))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt()), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([BlockStmt([VarDecl(k, IntegerType, IntegerLit(0)), AssignStmt(Id(k), Id(i)), IfStmt(BinExpr(<, Id(k), IntegerLit(10)), BreakStmt())])]))])])), CallStmt(print, StringLit(The result is ), Id(x))])]))])])), CallStmt(print, StringLit(The result is ), Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_full_7(self):
        input = """
            x, y, i : integer;
            main: function void(){
                for(i=0,i<10,i+1)
                    arr[i]=i;

                for(i=0,i<10,i+1)
                    if(arr[i]%2==0)
                        x = x + arr[i];
                    else
                        return y + arr[i];
                    if(arr[i]%2==0)
                      {  x = x + arr[i];
                      
                      for(i=0,i<10,i+1)
                          if(arr[i]%2==0)
                            {  x = x + arr[i];
                            
                            for(i=0,i<10,i+1)
                                arr[i]=i;
                            }
                    }
                    else
                        return y + arr[i];
                print(x,y);
                }  
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(arr, [Id(i)]), Id(i))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(x), BinExpr(+, Id(x), ArrayCell(arr, [Id(i)]))), ReturnStmt(BinExpr(+, Id(y), ArrayCell(arr, [Id(i)]))))), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), ArrayCell(arr, [Id(i)]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), ArrayCell(arr, [Id(i)]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(arr, [Id(i)]), Id(i)))])))]), ReturnStmt(BinExpr(+, Id(y), ArrayCell(arr, [Id(i)])))), CallStmt(print, Id(x), Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_full_8(self):
        input = """
            x, y, i : integer;
            main: function void()
            {
                for(i=0,i<10,i+1)
                    arr[i]=i;

                for(i=0,i<10,i+1)
                    if(arr[i]%2==0)
                        x = x + arr[i];
                    else
                        return y + arr[i];

                print(x,y);
                }  
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(i, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(arr, [Id(i)]), Id(i))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(x), BinExpr(+, Id(x), ArrayCell(arr, [Id(i)]))), ReturnStmt(BinExpr(+, Id(y), ArrayCell(arr, [Id(i)]))))), CallStmt(print, Id(x), Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_full_9(self):
        input = """
            func : function void()
            {
                ans = 0;
                for (i = 1, i <= n  , i + 1) 
                    for ( j = n, j <i , j -1){
                        ans = ans + (i*j*arrayA[i]);

                        ans = 0;
                    for (i = 1, i <= n  , i + 1) 
                        for ( j = n, j <i , j -1){
                            ans = ans + (i*j*arrayA[i]);
                        }

                        print(ans);
                    }

                    print(ans);
            }

            main: function void(){
                func();
                return;  
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(ans), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)])))), AssignStmt(Id(ans), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), Id(n)), BinExpr(<, Id(j), Id(i)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), BinExpr(*, BinExpr(*, Id(i), Id(j)), ArrayCell(arrayA, [Id(i)]))))]))), CallStmt(print, Id(ans))]))), CallStmt(print, Id(ans))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(func, ), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_full_10(self):
        input = """
            main: function void() {
                printString("");
                {
                    {
                        {
                            {
                                {
                                    {
                                        {
                                            n: function void() {
                                                printString("");
                                            }
                                        }
                                    }

                                    {
                                        {
                                            n: function void() {
                                                printString("");
                                            }
                                        }
                                    }
                                }

                                {
                                        {
                                            n: function void() {
                                                printString("");
                                            }
                                        }
                                    }
                            

                            {
                                        {
                                            n: function void() {
                                                printString("");
                                            }
                                        }
                                    }
                            }
                        }
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit()), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([FuncDecl(n, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit())]))])]), BlockStmt([BlockStmt([FuncDecl(n, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit())]))])])]), BlockStmt([BlockStmt([FuncDecl(n, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit())]))])]), BlockStmt([BlockStmt([FuncDecl(n, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit())]))])])])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_full_11(self):
        input = """
            main : function void() {
                arr : array[7] of integer = {5, 4, 9, 1, 4, 6, 3 };
                n : integer = sizeof(arr)/sizeof(arr[0]);
                pair1, pair2 : integer;
                if (findPairs(arr, n, pair1, pair2)) {
                    if (checkAnswer(arr, n, pair1, pair2)){
                        printString("Your answer is correct.");  

                        if (findPairs(arr, n, pair1, pair2)) {
                    if (checkAnswer(arr, n, pair1, pair2)){
                        printString("Your answer is correct.");

                        if (findPairs(arr, n, pair1, pair2)) {
                    if (checkAnswer(arr, n, pair1, pair2)){
                        printString("Your answer is correct.");

                        if (findPairs(arr, n, pair1, pair2)) {
                    if (checkAnswer(arr, n, pair1, pair2)){
                        printString("Your answer is correct.");                    
                    }
                    else printString("Your answer is incorrect.");
                }
                else printString("No pair found.");                    
                    }
                    else printString("Your answer is incorrect.");
                }
                else printString("No pair found.");                    
                    }
                    else printString("Your answer is incorrect.");
                }
                else printString("No pair found.");                  
                    }
                    else printString("Your answer is incorrect.");
                }
                else printString("No pair found.");

                
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([7], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(4), IntegerLit(6), IntegerLit(3)])), VarDecl(n, IntegerType, BinExpr(/, FuncCall(sizeof, [Id(arr)]), FuncCall(sizeof, [ArrayCell(arr, [IntegerLit(0)])]))), VarDecl(pair1, IntegerType), VarDecl(pair2, IntegerType), IfStmt(FuncCall(findPairs, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([IfStmt(FuncCall(checkAnswer, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([CallStmt(printString, StringLit(Your answer is correct.)), IfStmt(FuncCall(findPairs, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([IfStmt(FuncCall(checkAnswer, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([CallStmt(printString, StringLit(Your answer is correct.)), IfStmt(FuncCall(findPairs, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([IfStmt(FuncCall(checkAnswer, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([CallStmt(printString, StringLit(Your answer is correct.)), IfStmt(FuncCall(findPairs, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([IfStmt(FuncCall(checkAnswer, [Id(arr), Id(n), Id(pair1), Id(pair2)]), BlockStmt([CallStmt(printString, StringLit(Your answer is correct.))]), CallStmt(printString, StringLit(Your answer is incorrect.)))]), CallStmt(printString, StringLit(No pair found.)))]), CallStmt(printString, StringLit(Your answer is incorrect.)))]), CallStmt(printString, StringLit(No pair found.)))]), CallStmt(printString, StringLit(Your answer is incorrect.)))]), CallStmt(printString, StringLit(No pair found.)))]), CallStmt(printString, StringLit(Your answer is incorrect.)))]), CallStmt(printString, StringLit(No pair found.)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))




    def test_full_12(self):
        input = """
        floatTest: function void (){
                a = .e52;
                a = .e-52;

                a = .e00000000000000000000000;
                a = .e-0000000000000000000000;

                a = .e00000000000000000000000;
                a = .e+0000000000000000000000;

                a = .0e52;
                a = 0.e52;
                a = 0.0e52;

                a = .0e-52;
                a = 0.e-52;
                a = 0.0e-52;

                a = .0e0000000052;
                a = 0.e0000000052;
                a = 0.0e0000000052;

                a = .0e-0000000052;
                a = 0.e-0000000052;
                a = 0.0e-0000000052;

                a = .5e52;
                a = 5.e52;
                a = 5.5e52;

                a = .5e0000052;
                a = 5.e000052;
                a = 5.5e00000052;

                a = .5e-00052;
                a = 5.e-00052;
                a = 5.5e-000052;

                a = .5e-000;
                a = 5.e-000;
                a = 5.5e-0000;

                a = 5e52;
                a = 0e52;

                a = 5e+0000052;
                a = 0e-00000052;
            
                a = 0e-000000;
                a = 0e-000000;
                a = 0.0000e-000000;
                a = 0e-0000001;
                a = 434_5.342324;
                
                a = 5_236_7387.1323e52;
                a = 5_236_7387.e0052;
                a = 5_236_7387.1323e0052;
                a = 7387.e52;  
        }
        """
        expect = """Program([
	FuncDecl(floatTest, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(5e+51)), AssignStmt(Id(a), FloatLit(5e+52)), AssignStmt(Id(a), FloatLit(5.5e+52)), AssignStmt(Id(a), FloatLit(5e+51)), AssignStmt(Id(a), FloatLit(5e+52)), AssignStmt(Id(a), FloatLit(5.5e+52)), AssignStmt(Id(a), FloatLit(5e-53)), AssignStmt(Id(a), FloatLit(5e-52)), AssignStmt(Id(a), FloatLit(5.5e-52)), AssignStmt(Id(a), FloatLit(0.5)), AssignStmt(Id(a), FloatLit(5.0)), AssignStmt(Id(a), FloatLit(5.5)), AssignStmt(Id(a), FloatLit(5e+52)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(5e+52)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(a), FloatLit(4345.342324)), AssignStmt(Id(a), FloatLit(5.23673871323e+59)), AssignStmt(Id(a), FloatLit(5.2367387e+59)), AssignStmt(Id(a), FloatLit(5.23673871323e+59)), AssignStmt(Id(a), FloatLit(7.387e+55))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))






    def test_full_13(self):
        input = """
        x, y, z: integer;
        a: float = 1.2;
        b,c: boolean = true, false;
        d: array[1,2] of boolean;
        e,f: array[2,3] of string;
        g: array[1] of float = {a+1.2};
        h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};

        main: function void (){}
        abc: function integer(){}
        def: function integer() inherit abc{}
        ghi: function array[1,2] of boolean () {}
        klm: function array[1,2] of string () inherit ghi {}
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
	VarDecl(a, FloatType, FloatLit(1.2))
	VarDecl(b, BooleanType, BooleanLit(True))
	VarDecl(c, BooleanType, BooleanLit(False))
	VarDecl(d, ArrayType([1, 2], BooleanType))
	VarDecl(e, ArrayType([2, 3], StringType))
	VarDecl(f, ArrayType([2, 3], StringType))
	VarDecl(g, ArrayType([1], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))]))
	VarDecl(h, ArrayType([1, 2], StringType), ArrayLit([StringLit(D96), StringLit(MT22)]))
	VarDecl(i, ArrayType([1, 2], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(abc, IntegerType, [], None, BlockStmt([]))
	FuncDecl(def, IntegerType, [], abc, BlockStmt([]))
	FuncDecl(ghi, ArrayType([1, 2], BooleanType), [], None, BlockStmt([]))
	FuncDecl(klm, ArrayType([1, 2], StringType), [], ghi, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_full_14(self):
        input = """
        main: function void (){x, y, z: integer;
        a: float = 1.2;
        b,c: boolean = true, false;
        d: array[1,2] of boolean;
        e,f: array[2,3] of string;
        g: array[1] of float = {a+1.2};
        h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};}
        abc: function integer(){x, y, z: integer;
        a: float = 1.2;
        b,c: boolean = true, false;
        d: array[1,2] of boolean;
        e,f: array[2,3] of string;
        g: array[1] of float = {a+1.2};
        h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};}
        def: function integer() inherit abc{x, y, z: integer;
        a: float = 1.2;
        b,c: boolean = true, false;
        d: array[1,2] of boolean;
        e,f: array[2,3] of string;
        g: array[1] of float = {a+1.2};
        h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};}
        ghi: function array[1,2] of boolean () {x, y, z: integer;
        a: float = 1.2;
        b,c: boolean = true, false;
        d: array[1,2] of boolean;
        e,f: array[2,3] of string;
        g: array[1] of float = {a+1.2};
        h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};}
        klm: function array[1,2] of string () inherit ghi {x, y, z: integer;
        a: float = 1.2;
        b,c: boolean = true, false;
        d: array[1,2] of boolean;
        e,f: array[2,3] of string;
        g: array[1] of float = {a+1.2};
        h,i: array[1,2] of string = {"D96","MT22"}, {{}, "BKOOL"};}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(a, FloatType, FloatLit(1.2)), VarDecl(b, BooleanType, BooleanLit(True)), VarDecl(c, BooleanType, BooleanLit(False)), VarDecl(d, ArrayType([1, 2], BooleanType)), VarDecl(e, ArrayType([2, 3], StringType)), VarDecl(f, ArrayType([2, 3], StringType)), VarDecl(g, ArrayType([1], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))])), VarDecl(h, ArrayType([1, 2], StringType), ArrayLit([StringLit(D96), StringLit(MT22)])), VarDecl(i, ArrayType([1, 2], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))]))
	FuncDecl(abc, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(a, FloatType, FloatLit(1.2)), VarDecl(b, BooleanType, BooleanLit(True)), VarDecl(c, BooleanType, BooleanLit(False)), VarDecl(d, ArrayType([1, 2], BooleanType)), VarDecl(e, ArrayType([2, 3], StringType)), VarDecl(f, ArrayType([2, 3], StringType)), VarDecl(g, ArrayType([1], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))])), VarDecl(h, ArrayType([1, 2], StringType), ArrayLit([StringLit(D96), StringLit(MT22)])), VarDecl(i, ArrayType([1, 2], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))]))
	FuncDecl(def, IntegerType, [], abc, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(a, FloatType, FloatLit(1.2)), VarDecl(b, BooleanType, BooleanLit(True)), VarDecl(c, BooleanType, BooleanLit(False)), VarDecl(d, ArrayType([1, 2], BooleanType)), VarDecl(e, ArrayType([2, 3], StringType)), VarDecl(f, ArrayType([2, 3], StringType)), VarDecl(g, ArrayType([1], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))])), VarDecl(h, ArrayType([1, 2], StringType), ArrayLit([StringLit(D96), StringLit(MT22)])), VarDecl(i, ArrayType([1, 2], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))]))
	FuncDecl(ghi, ArrayType([1, 2], BooleanType), [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(a, FloatType, FloatLit(1.2)), VarDecl(b, BooleanType, BooleanLit(True)), VarDecl(c, BooleanType, BooleanLit(False)), VarDecl(d, ArrayType([1, 2], BooleanType)), VarDecl(e, ArrayType([2, 3], StringType)), VarDecl(f, ArrayType([2, 3], StringType)), VarDecl(g, ArrayType([1], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))])), VarDecl(h, ArrayType([1, 2], StringType), ArrayLit([StringLit(D96), StringLit(MT22)])), VarDecl(i, ArrayType([1, 2], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))]))
	FuncDecl(klm, ArrayType([1, 2], StringType), [], ghi, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), VarDecl(a, FloatType, FloatLit(1.2)), VarDecl(b, BooleanType, BooleanLit(True)), VarDecl(c, BooleanType, BooleanLit(False)), VarDecl(d, ArrayType([1, 2], BooleanType)), VarDecl(e, ArrayType([2, 3], StringType)), VarDecl(f, ArrayType([2, 3], StringType)), VarDecl(g, ArrayType([1], FloatType), ArrayLit([BinExpr(+, Id(a), FloatLit(1.2))])), VarDecl(h, ArrayType([1, 2], StringType), ArrayLit([StringLit(D96), StringLit(MT22)])), VarDecl(i, ArrayType([1, 2], StringType), ArrayLit([ArrayLit([]), StringLit(BKOOL)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))


    def test_full_15(self):
        input = """
        abc: function integer(a: integer){}
        def: function integer(a: array[3] of integer) inherit abc{}
        ghi: function array[1,2] of boolean (out n: integer) {}
        klm: function array[1,2] of string (inherit out a: array[3] of integer, n: integer) inherit ghi {}
        """
        expect = """Program([
	FuncDecl(abc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([]))
	FuncDecl(def, IntegerType, [Param(a, ArrayType([3], IntegerType))], abc, BlockStmt([]))
	FuncDecl(ghi, ArrayType([1, 2], BooleanType), [OutParam(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(klm, ArrayType([1, 2], StringType), [InheritOutParam(a, ArrayType([3], IntegerType)), Param(n, IntegerType)], ghi, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_full_16(self):
        input = """
        abs: function integer() {
            return 0;
            return 0;
            return 0;
            return 0;
        }
        main: function void() {
            return;
            return;
            return;
            return;
        }
        """
        expect = """Program([
	FuncDecl(abs, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(0)), ReturnStmt(IntegerLit(0)), ReturnStmt(IntegerLit(0)), ReturnStmt(IntegerLit(0))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(), ReturnStmt(), ReturnStmt(), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_full_17(self):
        input = """
        x, y, z: integer = 1, 2, 3;
        x, y, z: integer = 1, 2, 3;
        x, y, z: integer = 1, 2, 3;
        x, y, z: integer = 1, 2, 3;
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_full_18(self):
        input = """
        x , y : boolean = true , false ;
                    a1, a2 : auto = b1, b2 ;
        x , y : boolean = true , false ;
                    a1, a2 : auto = b1, b2 ;
        x , y : boolean = true , false ;
                    a1, a2 : auto = b1, b2 ;
        """
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(a1, AutoType, Id(b1))
	VarDecl(a2, AutoType, Id(b2))
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(a1, AutoType, Id(b1))
	VarDecl(a2, AutoType, Id(b2))
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(a1, AutoType, Id(b1))
	VarDecl(a2, AutoType, Id(b2))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))


    def test_full_19(self):
        input = """
        plus: function integer(b: integer) {
            a: integer = 2;
            return a + b;
            a: integer = 2;
            return a + b;
            a: integer = 2;
            return a + b;
            a: integer = 2;
            return a + b;
        }
        abs: function integer() inherit plus {
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
        }
        """
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(b, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b))), VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b))), VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b))), VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_full_20(self):
        input = """
        x: integer;

         abs: function integer() inherit plus {
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_full_21(self):
        input = """
        x,y,z: integer;

         abs: function integer() inherit plus {
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
        }

        plus: function integer(b: integer) {
            a: integer = 2;
            return a + b;
            a: integer = 2;
            return a + b;
            a: integer = 2;
            return a + b;
            a: integer = 2;
            return a + b;
        }
        abs: function integer() inherit plus {
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
            c: integer = a + plus(5);
            return c;
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c))]))
	FuncDecl(plus, IntegerType, [Param(b, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b))), VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b))), VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b))), VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_full_22(self):
        input = """________________________: integer = "____________________________________________";"""
        expect = """Program([
	VarDecl(________________________, IntegerType, StringLit(____________________________________________))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_full_23(self):
        input = """_____x, _____y, _____z: integer = _____1, _____2, _____3;
        _____a, _____b: float;"""
        expect = """Program([
	VarDecl(_____x, IntegerType, Id(_____1))
	VarDecl(_____y, IntegerType, Id(_____2))
	VarDecl(_____z, IntegerType, Id(_____3))
	VarDecl(_____a, FloatType)
	VarDecl(_____b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 323))


    def test_full_24(self):
        input = """
        plus: function integer(b: integer) {
        a: integer = 2;
        return a + b;
        }
        abs: function integer() inherit plus {
        c: integer = a + plus(5);
        return c;
        }
        plus: function integer(b: integer) {
        a: integer = 2;
        return a + b;
        }
        abs: function integer() inherit plus {
        c: integer = a + plus(5);
        return c;
        for(i = 1, i<length(a), i+1) print(a[i]);
            while(a[1]<n) {
                print(a[1]);
                a[1] = a[1] - 1;for(i = 1, i<length(a), i+1) print(a[i]);
            while(a[1]<n) {
                print(a[1]);
                a[1] = a[1] - 1;
            }
            do {
                a[2] = a[2] - n;
            } while(a[2] > 0);
            }
            do {
                a[2] = a[2] - n;for(i = 1, i<length(a), i+1) print(a[i]);
            while(a[1]<n) {
                print(a[1]);
                a[1] = a[1] - 1;
            }
            do {
                a[2] = a[2] - n;
            } while(a[2] > 0);
            } while(a[2] > 0);
        }
        """
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(b, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c))]))
	FuncDecl(plus, IntegerType, [Param(b, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(abs, IntegerType, [], plus, BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), FuncCall(plus, [IntegerLit(5)]))), ReturnStmt(Id(c)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)))])), DoWhileStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, ArrayCell(a, [IntegerLit(2)]), Id(n)))]))])), DoWhileStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, ArrayCell(a, [IntegerLit(2)]), Id(n))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)))])), DoWhileStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, ArrayCell(a, [IntegerLit(2)]), Id(n)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_full_25(self):
        input = """
        printArray: function void (inherit a: array[3] of integer,n: integer){
            for(i = 1, i<length(a), i+1) print(a[i]);
            while(a[1]<n) {
                print(a[1]);
                a[1] = a[1] - 1;
                for(i = 1, i<length(a), i+1) print(a[i]);
            while(a[1]<n) {
                print(a[1]);
                a[1] = a[1] - 1;
                for(i = 1, i<length(a), i+1) print(a[i]);
            while(a[1]<n) {
                print(a[1]);
                a[1] = a[1] - 1;
            }
            do {
                a[2] = a[2] - n;
            } while(a[2] > 0);
            }
            do {
                a[2] = a[2] - n;
            } while(a[2] > 0);
            }
            do {
                a[2] = a[2] - n;
            } while(a[2] > 0);
        }
        """
        expect = """Program([
	FuncDecl(printArray, VoidType, [InheritParam(a, ArrayType([3], IntegerType)), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)]))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)))])), DoWhileStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, ArrayCell(a, [IntegerLit(2)]), Id(n)))]))])), DoWhileStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, ArrayCell(a, [IntegerLit(2)]), Id(n)))]))])), DoWhileStmt(BinExpr(>, ArrayCell(a, [IntegerLit(2)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, ArrayCell(a, [IntegerLit(2)]), Id(n)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_full_26(self):
        input = """
        printArray: function void (a: array[3,1] of integer,n: integer){
            while(a[1,1]<n) {
                print(a[1,1]);
                if(n > 1) n = n-1;
                else break;
            }
            {
                m: integer = 5;
                for(i = 1, i<length(a), i+1) {
                    if(a[max(i,2),1]>m) {continue;}
                    else {m = m-1;}
                    m = m + 2;
                     while(a[1,1]<n) {
                print(a[1,1]);
                if(n > 1) n = n-1;
                else break;
            }
            {
                m: integer = 5;
                for(i = 1, i<length(a), i+1) {
                    if(a[max(i,2),1]>m) {continue;}
                    else {m = m-1;}
                    m = m + 2;
                }
            }

            {
                 while(a[1,1]<n) {
                print(a[1,1]);
                if(n > 1) n = n-1;
                else break;
            }
            {
                m: integer = 5;
                for(i = 1, i<length(a), i+1) {
                    if(a[max(i,2),1]>m) {continue;}
                    else {m = m-1;}
                    m = m + 2;
                }
            }
            }
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(printArray, VoidType, [Param(a, ArrayType([3, 1], IntegerType)), Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1), IntegerLit(1)])), IfStmt(BinExpr(>, Id(n), IntegerLit(1)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), BreakStmt())])), BlockStmt([VarDecl(m, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [FuncCall(max, [Id(i), IntegerLit(2)]), IntegerLit(1)]), Id(m)), BlockStmt([ContinueStmt()]), BlockStmt([AssignStmt(Id(m), BinExpr(-, Id(m), IntegerLit(1)))])), AssignStmt(Id(m), BinExpr(+, Id(m), IntegerLit(2))), WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1), IntegerLit(1)])), IfStmt(BinExpr(>, Id(n), IntegerLit(1)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), BreakStmt())])), BlockStmt([VarDecl(m, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [FuncCall(max, [Id(i), IntegerLit(2)]), IntegerLit(1)]), Id(m)), BlockStmt([ContinueStmt()]), BlockStmt([AssignStmt(Id(m), BinExpr(-, Id(m), IntegerLit(1)))])), AssignStmt(Id(m), BinExpr(+, Id(m), IntegerLit(2)))]))]), BlockStmt([WhileStmt(BinExpr(<, ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), Id(n)), BlockStmt([CallStmt(print, ArrayCell(a, [IntegerLit(1), IntegerLit(1)])), IfStmt(BinExpr(>, Id(n), IntegerLit(1)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), BreakStmt())])), BlockStmt([VarDecl(m, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [FuncCall(max, [Id(i), IntegerLit(2)]), IntegerLit(1)]), Id(m)), BlockStmt([ContinueStmt()]), BlockStmt([AssignStmt(Id(m), BinExpr(-, Id(m), IntegerLit(1)))])), AssignStmt(Id(m), BinExpr(+, Id(m), IntegerLit(2)))]))])])]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_full_27(self):
        input = """
        main: function void () {
            {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
        }
        main: function void () {
            {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])])]))
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_full_28(self):
        input = """
        Rectangle: function void (a: float, b: integer, out c:float) {
        }
        Square: function void(inherit b: integer) inherit Rectangle{
            
        }
        """
        expect = """Program([
	FuncDecl(Rectangle, VoidType, [Param(a, FloatType), Param(b, IntegerType), OutParam(c, FloatType)], None, BlockStmt([]))
	FuncDecl(Square, VoidType, [InheritParam(b, IntegerType)], Rectangle, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_full_29(self):
        input = """
        main: function void () {
                a1, b2 : integer = a + 1, 0 ;
                a  = 3;


                /*  
                {{{{{{{{{{{{{}}}}}}}}}}}}}
                */
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a1, IntegerType, BinExpr(+, Id(a), IntegerLit(1))), VarDecl(b2, IntegerType, IntegerLit(0)), AssignStmt(Id(a), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test_full_30(self):
        input = """
        /* Program([
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(toInteger, IntegerType, [], None, BlockStmt([]))
]) */
toString : function string () {
            /* Program([
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(toInteger, IntegerType, [], None, BlockStmt([]))
]) */
        }
        toInteger : function integer () {

            /* Program([
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(toInteger, IntegerType, [], None, BlockStmt([]))
]) */
        }"""
        expect = """Program([
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(toInteger, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_full_31(self):
        input = """
        main: function void () {
                b = a + a1;
                c = b*a/2.0;
            }
            
            toString : function string () {
        }
        main: function void () {
                b = a + a1;
                c = b*a/2.0;
            }
            
            toString : function string () {
        }
        main: function void () {
                b = a + a1;
                c = b*a/2.0;
            }
            
            toString : function string () {
        }
        toInteger : function integer () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(a), Id(a1))), AssignStmt(Id(c), BinExpr(/, BinExpr(*, Id(b), Id(a)), FloatLit(2.0)))]))
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(a), Id(a1))), AssignStmt(Id(c), BinExpr(/, BinExpr(*, Id(b), Id(a)), FloatLit(2.0)))]))
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(a), Id(a1))), AssignStmt(Id(c), BinExpr(/, BinExpr(*, Id(b), Id(a)), FloatLit(2.0)))]))
	FuncDecl(toString, StringType, [], None, BlockStmt([]))
	FuncDecl(toInteger, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_full_32(self):
        input = """
        a : float = 12 - 2*3/4 + 1 +1 / 5;
         a : float = 2 + 2%2/2*-2 ;
                b : float = 1*1--1+1/1 ;
                c : float = a + b / (2*1.0+1) ;
                a : float = 2 + 2%2/2*-2 ;
                b : float = 1*1--1+1/1 ;
                c : float = a + b / (2*1.0+1) ;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(+, BinExpr(-, IntegerLit(12), BinExpr(/, BinExpr(*, IntegerLit(2), IntegerLit(3)), IntegerLit(4))), IntegerLit(1)), BinExpr(/, IntegerLit(1), IntegerLit(5))))
	VarDecl(a, FloatType, BinExpr(+, IntegerLit(2), BinExpr(*, BinExpr(/, BinExpr(%, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), UnExpr(-, IntegerLit(2)))))
	VarDecl(b, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), IntegerLit(1)), UnExpr(-, IntegerLit(1))), BinExpr(/, IntegerLit(1), IntegerLit(1))))
	VarDecl(c, FloatType, BinExpr(+, Id(a), BinExpr(/, Id(b), BinExpr(+, BinExpr(*, IntegerLit(2), FloatLit(1.0)), IntegerLit(1)))))
	VarDecl(a, FloatType, BinExpr(+, IntegerLit(2), BinExpr(*, BinExpr(/, BinExpr(%, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), UnExpr(-, IntegerLit(2)))))
	VarDecl(b, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), IntegerLit(1)), UnExpr(-, IntegerLit(1))), BinExpr(/, IntegerLit(1), IntegerLit(1))))
	VarDecl(c, FloatType, BinExpr(+, Id(a), BinExpr(/, Id(b), BinExpr(+, BinExpr(*, IntegerLit(2), FloatLit(1.0)), IntegerLit(1)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    
    
    def test_full_33(self):
        input = """
                a : float = 2 + 2%2/2*-2 ;
                b : float = 1*1--1+1/1 ;
                c : float = a + b / (2*1.0+1) ;
                a : float = 2 + 2%2/2*-2 ;
                b : float = 1*1--1+1/1 ;
                c : float = a + b / (2*1.0+1) ;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, IntegerLit(2), BinExpr(*, BinExpr(/, BinExpr(%, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), UnExpr(-, IntegerLit(2)))))
	VarDecl(b, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), IntegerLit(1)), UnExpr(-, IntegerLit(1))), BinExpr(/, IntegerLit(1), IntegerLit(1))))
	VarDecl(c, FloatType, BinExpr(+, Id(a), BinExpr(/, Id(b), BinExpr(+, BinExpr(*, IntegerLit(2), FloatLit(1.0)), IntegerLit(1)))))
	VarDecl(a, FloatType, BinExpr(+, IntegerLit(2), BinExpr(*, BinExpr(/, BinExpr(%, IntegerLit(2), IntegerLit(2)), IntegerLit(2)), UnExpr(-, IntegerLit(2)))))
	VarDecl(b, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), IntegerLit(1)), UnExpr(-, IntegerLit(1))), BinExpr(/, IntegerLit(1), IntegerLit(1))))
	VarDecl(c, FloatType, BinExpr(+, Id(a), BinExpr(/, Id(b), BinExpr(+, BinExpr(*, IntegerLit(2), FloatLit(1.0)), IntegerLit(1)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_full_34(self):
        input = """
        a : boolean = true ;
        b : boolean = !a && false || (false && true || true) ;  
        c : boolean = !!b || false && false;
        """
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
	VarDecl(b, BooleanType, BinExpr(||, BinExpr(&&, UnExpr(!, Id(a)), BooleanLit(False)), BinExpr(||, BinExpr(&&, BooleanLit(False), BooleanLit(True)), BooleanLit(True))))
	VarDecl(c, BooleanType, BinExpr(&&, BinExpr(||, UnExpr(!, UnExpr(!, Id(b))), BooleanLit(False)), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_full_35(self):
        input = """
        a1, a2 : string = "Hello ", "World!" ;
        a: string = a1 :: a2 ;            
        a: string = (a :: ( a :: "a" ) ) :: a;        
        a1, a2 : string = "Hello ", "World!" ;
        a: string = a1 :: a2 ;            
        a: string = (a :: ( a :: "a" ) ) :: a;        
        """
        expect = """Program([
	VarDecl(a1, StringType, StringLit(Hello ))
	VarDecl(a2, StringType, StringLit(World!))
	VarDecl(a, StringType, BinExpr(::, Id(a1), Id(a2)))
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(a), BinExpr(::, Id(a), StringLit(a))), Id(a)))
	VarDecl(a1, StringType, StringLit(Hello ))
	VarDecl(a2, StringType, StringLit(World!))
	VarDecl(a, StringType, BinExpr(::, Id(a1), Id(a2)))
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(a), BinExpr(::, Id(a), StringLit(a))), Id(a)))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))


    def test_full_36(self):
        input = """               
        b: boolean = 1!= 2 || (0==0.1) ;     

        a1, a2 : string = "Hello ", "World!" ;
        a: string = a1 :: a2 ;            
        a: string = (a :: ( a :: "a" ) ) :: a;        
        a1, a2 : string = "Hello ", "World!" ;
        a: string = a1 :: a2 ;            
        a: string = (a :: ( a :: "a" ) ) :: a;    
        """
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(!=, IntegerLit(1), BinExpr(||, IntegerLit(2), BinExpr(==, IntegerLit(0), FloatLit(0.1)))))
	VarDecl(a1, StringType, StringLit(Hello ))
	VarDecl(a2, StringType, StringLit(World!))
	VarDecl(a, StringType, BinExpr(::, Id(a1), Id(a2)))
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(a), BinExpr(::, Id(a), StringLit(a))), Id(a)))
	VarDecl(a1, StringType, StringLit(Hello ))
	VarDecl(a2, StringType, StringLit(World!))
	VarDecl(a, StringType, BinExpr(::, Id(a1), Id(a2)))
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(a), BinExpr(::, Id(a), StringLit(a))), Id(a)))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_full_37(self):
        input = """               
        a : boolean = (3 > 2 ) || (7/2 <= 4+3) && !(1.0e1+1 >= 0) ;     
        a : boolean = (3 > 2 ) || (7/2 <= 4+3) && !(1.0e1+1 >= 0) ;     
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(>, IntegerLit(3), IntegerLit(2)), BinExpr(<=, BinExpr(/, IntegerLit(7), IntegerLit(2)), BinExpr(+, IntegerLit(4), IntegerLit(3)))), UnExpr(!, BinExpr(>=, BinExpr(+, FloatLit(10.0), IntegerLit(1)), IntegerLit(0)))))
	VarDecl(a, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(>, IntegerLit(3), IntegerLit(2)), BinExpr(<=, BinExpr(/, IntegerLit(7), IntegerLit(2)), BinExpr(+, IntegerLit(4), IntegerLit(3)))), UnExpr(!, BinExpr(>=, BinExpr(+, FloatLit(10.0), IntegerLit(1)), IntegerLit(0)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_full_38(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
            a1, a2 : string = "Hello ", "World!" ;
        a: string = a1 :: a2 ;            
        a: string = (a :: ( a :: "a" ) ) :: a;        
        a1, a2 : string = "Hello ", "World!" ;
        a: string = a1 :: a2 ;            
        a: string = (a :: ( a :: "a" ) ) :: a;  
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
	VarDecl(a1, StringType, StringLit(Hello ))
	VarDecl(a2, StringType, StringLit(World!))
	VarDecl(a, StringType, BinExpr(::, Id(a1), Id(a2)))
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(a), BinExpr(::, Id(a), StringLit(a))), Id(a)))
	VarDecl(a1, StringType, StringLit(Hello ))
	VarDecl(a2, StringType, StringLit(World!))
	VarDecl(a, StringType, BinExpr(::, Id(a1), Id(a2)))
	VarDecl(a, StringType, BinExpr(::, BinExpr(::, Id(a), BinExpr(::, Id(a), StringLit(a))), Id(a)))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_full_39(self):
        input = """               
            a : array [2] of integer;
            arr : array [1,2,3] of string;
            a : array [2] of integer;
            arr : array [1,2,3] of string;
            a : array [2] of integer;
            arr : array [1,2,3] of string;
        """
        expect = """Program([
	VarDecl(a, ArrayType([2], IntegerType))
	VarDecl(arr, ArrayType([1, 2, 3], StringType))
	VarDecl(a, ArrayType([2], IntegerType))
	VarDecl(arr, ArrayType([1, 2, 3], StringType))
	VarDecl(a, ArrayType([2], IntegerType))
	VarDecl(arr, ArrayType([1, 2, 3], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_full_40(self):
        input = """               
            arr : array [1_0] of float = {1,2,3,4,5,6,7,8,9,10};
            arr : array [1_0] of float = {1,2,3,4,5,6,7,8,9,10};
            arr : array [1_0] of float = {1,2,3,4,5,6,7,8,9,10};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([10], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)]))
	VarDecl(arr, ArrayType([10], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)]))
	VarDecl(arr, ArrayType([10], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_full_41(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_full_42(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_full_43(self):
        input = """
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_full_44(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        """
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_full_45(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }
        count : auto = 0;
        main: function void () {
                
        }
        """
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_full_46(self):
        input = """
        main: function void () {
                count = 1;
                str = "";
        }
        main: function void () {
                count = 1;
                str = "";
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_full_47(self):
        input = """
        main: function void () {
              if (a>b) a = b;
        }
        main: function void () {
              if (a>b) a = b;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_full_48(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_full_49(self):
        input = """
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_full_50(self):
        input = """
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                
        }
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                   
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_full_51(self):
        input = """
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;           
        }
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;               
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    def test_full_52(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_full_53(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_full_54(self):
        input = """
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_full_55(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        """
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_full_56(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }
        count : auto = 0;
        main: function void () {
                
        }
        """
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_full_57(self):
        input = """
        main: function void () {
                count = 1;
                str = "";
        }
        main: function void () {
                count = 1;
                str = "";
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_full_58(self):
        input = """
        main: function void () {
              if (a>b) a = b;
        }
        main: function void () {
              if (a>b) a = b;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test_full_59(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_full_60(self):
        input = """
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_full_61(self):
        input = """
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                
        }
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                   
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_full_62(self):
        input = """
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;           
        }
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;               
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    def test_full_63(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_full_64(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_full_65(self):
        input = """
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_full_66(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        """
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_full_67(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }
        count : auto = 0;
        main: function void () {
                
        }
        """
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_full_68(self):
        input = """
        main: function void () {
                count = 1;
                str = "";
        }
        main: function void () {
                count = 1;
                str = "";
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_full_69(self):
        input = """
        main: function void () {
              if (a>b) a = b;
        }
        main: function void () {
              if (a>b) a = b;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test_full_70(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_full_71(self):
        input = """
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_full_72(self):
        input = """
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                
        }
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                   
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_full_73(self):
        input = """
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;           
        }
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;               
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    def test_full_74(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_full_75(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_full_76(self):
        input = """
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_full_77(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        """
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_full_78(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }
        count : auto = 0;
        main: function void () {
                
        }
        """
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_full_79(self):
        input = """
        main: function void () {
                count = 1;
                str = "";
        }
        main: function void () {
                count = 1;
                str = "";
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_full_80(self):
        input = """
        main: function void () {
              if (a>b) a = b;
        }
        main: function void () {
              if (a>b) a = b;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test_full_81(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_full_82(self):
        input = """
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_full_83(self):
        input = """
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                
        }
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                   
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_full_84(self):
        input = """
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;           
        }
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;               
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
    def test_full_85(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_full_86(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_full_87(self):
        input = """
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_full_88(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        """
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_full_89(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }
        count : auto = 0;
        main: function void () {
                
        }
        """
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_full_90(self):
        input = """
        main: function void () {
                count = 1;
                str = "";
        }
        main: function void () {
                count = 1;
                str = "";
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1)), AssignStmt(Id(str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_full_91(self):
        input = """
        main: function void () {
              if (a>b) a = b;
        }
        main: function void () {
              if (a>b) a = b;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test_full_92(self):
        input = """
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        main: function void () {
              if (a>b) {a = b;}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_full_93(self):
        input = """
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        main: function void () {
              if (a>b) {}
              else {
                print("Value a = ", a);
              }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([]), BlockStmt([CallStmt(print, StringLit(Value a = ), Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_full_94(self):
        input = """
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                
        }
        main: function void () {
              if (a>b) {{{{{}}}}}
              else a = "This is 'else' ";                   
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])]), AssignStmt(Id(a), StringLit(This is 'else' )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_full_95(self):
        input = """
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;           
        }
        main: function void () {
              if (a>b) {{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
              else if (true) a = b;
                  else a = 0;               
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([BlockStmt([])])])])])])])])])])])])])])]), IfStmt(BooleanLit(True), AssignStmt(Id(a), Id(b)), AssignStmt(Id(a), IntegerLit(0))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    def test_full_96(self):
        input = """               
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
            value : array[2,3] of float = {{1.2,-4.0e10,1.02*12/1},{a, b, 7.0}};
            S : array[0] of string = {};
        """
        expect = """Program([
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
	VarDecl(value, ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.2), UnExpr(-, FloatLit(40000000000.0)), BinExpr(/, BinExpr(*, FloatLit(1.02), IntegerLit(12)), IntegerLit(1))]), ArrayLit([Id(a), Id(b), FloatLit(7.0)])]))
	VarDecl(S, ArrayType([0], StringType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_full_97(self):
        input = """               
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
            printArr: function void(out arr:array[5] of string) 
                { return (arr[0]);}
            myPets : array[5] of string = {"Cat", "Dog", "Parot", "Pig", "Ducky"} ;    
        """
        expect = """Program([
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
	FuncDecl(printArr, VoidType, [OutParam(arr, ArrayType([5], StringType))], None, BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]))
	VarDecl(myPets, ArrayType([5], StringType), ArrayLit([StringLit(Cat), StringLit(Dog), StringLit(Parot), StringLit(Pig), StringLit(Ducky)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_full_98(self):
        input = """
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        main: function void () {
                count = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(count), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_full_99(self):
        input = """
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        average : float = 0.0;
        beginString : string = "";
        main: function void () {
                beginString = "hello world";
                average = sum/number;
        }
        """
        expect = """Program([
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
	VarDecl(average, FloatType, FloatLit(0.0))
	VarDecl(beginString, StringType, StringLit())
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(beginString), StringLit(hello world)), AssignStmt(Id(average), BinExpr(/, Id(sum), Id(number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_full_100(self):
        input = """
        count : auto = 0;
        main: function void () {
                
        }
        count : auto = 0;
        main: function void () {
                
        }
        """
        expect = """Program([
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(count, AutoType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
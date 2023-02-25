# # 1913652
# # Trịnh Duy Hưng

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test01(self):
        input = """
        x,y,z : integer = 1,2,3,4;
        """
        expect = "Error on line 2 col 31: ,"
        self.assertTrue(TestParser.test(input, expect, 1001))

    def test02(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
                writeInt(1);
            }
            printInteger(x);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1002))

    def test03(self):
        input = """
        main : function void {
            for (i = 1, j < 10, i + 1) {
                writeInt(1);
            }
            printInteger(x);
        }
        """
        expect = "Error on line 2 col 29: {"
        self.assertTrue(TestParser.test(input, expect,1003))

    def test04(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1004))

    def test05(self):
        input = r"""A, B: integer = 5, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1005))

    def test06(self):
        input = r"""A, B: string = "abc", "def";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1006))

    def test07(self):
        input = '''
            x: integer = 65;
            mess: function integer(n: integer){
                return n/50 * 2;
            }
            main: function void () {
                delta: integer = mess(7);
                printInteger(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1007))

    def test08(self):
        input = '''
            add: function integer(n: integer){
                sum: integer = 0;
                for (i = 0, i<=n, i+1){
                    sum = sum + i;
                }
                return sum;
            }
            main: function void () {
                delta: integer = add(10);
                printInteger(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1008))

    def test09(self):
        input = '''
            x: integer = 65;
            fact: function integer(n: integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1009))

    def test10(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i!=0){
                    i = i - 1;
                }
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1010))

    def test11(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
            }
            printInteger(x);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1011))

    def test12(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
                printInteger(x)
            }
            printInteger(x);
        }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 1012))

    def test13(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
                writeInt(a);
            }
            printInteger();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1013))
        
    def test14(self):
        input = r"""A, B: float = 1.2, 3.4e-10;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1014))

    def test15(self):
        input = r"""A, B: boolean = true, false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1015))

    def test16(self):
        input = r"""A, B: array[1,2] of integer = {1, 2}, {3, foo(4)};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1016))

    def test17(self):
        input = r"""A, B: auto = 1, foo(4);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1017))

    def test18(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i>20){
                    i = i + 2;
                }
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,1018))

    def test19(self):
        input = '''
            voidA: function integer(n: integer){
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1019))

    def test20(self):
        input = '''
            main: function void () {
                delta: string = "dat";
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1020))
    
    def test21(self):
        input = '''
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1021))

    def test22(self):
        input = """
        main : function void() {
            for (i = 1, j < 10, i + 1) {
                writeInt(1);
            }
            printInteger;
        }
        """
        expect = "Error on line 6 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 1022))

    def test23(self):
        input = """
        main : void() {
            for (i = 1, j < 10, i + 1) {
                writeInt(1);
            }
            printInteger(x);
        }
        """
        expect = "Error on line 2 col 15: void"
        self.assertTrue(TestParser.test(input, expect, 1023))

    def test24(self):
        input = """
        main : function void() {
            for (i = 1, i + 1) {
                writeInt(1);
            }
            printInteger(x);
        }
        """
        expect = "Error on line 3 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 1024))

    def test25(self):
        input = """
        main : function() {
            for (i = 1, j < 10, i + 1) {
                writeInt(1);
            }
            printInteger(x);
        }
        """
        expect = "Error on line 2 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 1025))

    def test26(self):
        input = r"""A, B: float = 1, 2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1026))

    def test27(self):
        input = r"""A: function integer() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1027))

    def test28(self):
        input = r"""A: function integer() inherit foo {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1028))

    def test29(self):
        input = r""" 
            inc: function void(out n: integer) {
                n  = n+ 1;
                return n;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1029))

    def test30(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                printBoolean(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1030))

    def test31(self):
        input = '''
            main: function void () {
                b: array [5] of integer;
                b[4] = 3;
                printInteger(b[4]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1031))

    def test32(self):
        input = '''
            main: function void () {
                delta: integer = 3+34*30/5*16/4*2/2+19%4+2%2;
                printInteger(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1032))

    def test33(self):
        input = '''
            main: function void () {
                i: integer = 10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1033))

    def test34(self):
        input = '''
            main: function void () {
                i: integer = -10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1034))

    def test35(self):
        input = '''
            main: function void () {
                delta: float = 130.34e2;
                printFloat(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1035))

    def test36(self):
        input = """
        main : function void() {
            for (i = 1, j < 10) {
                writeInt(1);
            }
        }
        """
        expect = "Error on line 3 col 30: )"
        self.assertTrue(TestParser.test(input, expect, 1036))

    def test37(self):
        input = """
        main : function void() {
            if(true){
                for (i = 1, i < 10, i+1) {
                    writeInt(i);
            }
            }else{
                printInteger(0);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1037))

    def test38(self):
        input = """
        main : function void() {
            if(true){
                for (i = 1, i < 10, i+1) {
                    writeInt(i);
            }
            }else{
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1038))

    def test39(self):
        input = """
        main : function void() {
            if(true){
                for (i = 1, i < 10, i+1) {
                    writeInt(i);
            }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1039))
    
    def test40(self):
        input = """
        main : function void() {
            if(true){
            }else{
                printInteger(0);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1040))
    def test41(self):
        input = r"""
        learningtofly: function integer() {
            return -----foo(1_2 + 2 || 4 :: 5);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1041))

    def test42(self):
        input = r"""x:integer = a + b * c - d / e % f;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1042))

    def test43(self):
        input = r"""x:float=1E-4+10.0;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1043))

    def test44(self):
        input = r"""
        boo: boolean =  a && b || c && !d;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1044))

    def test45(self):
        input = r"""
        
            newStr: string = "Hello "::"World!";
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1045))

    def test46(self):
        input = r"""
        main: function void(){
            eq = a == b;
            neq = a != b;
            lt = a < b;
            le = a <= b;
            gt = a > b;
            ge = a >= b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1046))

    def test47(self):
        input = '''
            main: function void () {
                delta: string = "true";
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1047))

    def test48(self):
        input = '''
            voidA: function integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1048))

    def test49(self):
        input = '''
            voidA: function integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer){
                n = n + 24;
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1049))

    def test50(self):
        input = '''
            main: function void () {
                delta: boolean = !true&&!false||true||false||!false;
                printBoolean(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1050))

    def test51(self):
        input = """
        fact : function integer(n: integer) {
            if(n==0) return 1;
            else return n*fact(n-1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1051))

    def test52(self):
        input = """
        delta: integer = 3;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1052))

    def test53(self):
        input = """True : string = "It's true!" 
        false : string = "it's not true..." """
        expect = "Error on line 2 col 8: false"
        self.assertTrue(TestParser.test(input, expect, 1053))

    def test54(self):
        input = """
        a, b, c: integer = 3, 4, 6;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1054))

    def test55(self):
        input = """
        a, b, c, d: integer = 3, 4, 6;
        """
        expect = "Error on line 2 col 37: ;"
        self.assertTrue(TestParser.test(input, expect, 1055))

    def test56(self):
        input = """
        main : void() {
            for (i = 1, j < 10, i + 1) {
                writeInt(1);
            }
            printInteger(x);
        }
        """
        expect = "Error on line 2 col 15: void"
        self.assertTrue(TestParser.test(input, expect, 1056))

    def test57(self):
        input = r"""
        main: function void() {
            a : integer = 3;
            b : integer = a;
            a = b;
            b = foo(a&&b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1057))

    def test58(self):
        input = r"""
        a : integer = f00(22-foo(a + too(a)));
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1058))

    def test59(self):
        input = r"""
        a :integer = b = f00(22-foo(a + too(a)));
        """
        expect = "Error on line 2 col 23: ="
        self.assertTrue(TestParser.test(input, expect, 1059))

    def test60(self):
        input = """
        main : function void() {
            a, b : integer = round(123.0e2), randomInt();
            sum : integer = a + b + arr[0,0];
            print(a, sum);
            return ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1060))

    def test61(self):
        input = r"""
        a :integer = f00(b=22-foo(a + too(a)));
        """
        expect = "Error on line 2 col 26: ="
        self.assertTrue(TestParser.test(input, expect, 1061))

    def test62(self):
        input = r"""
        x :boolean = a = b = c;
        """
        expect = "Error on line 2 col 23: ="
        self.assertTrue(TestParser.test(input, expect, 1062))

    def test63(self):
        input = '''
            main: function void () {
                delta: string;
                delta = "abcd"::"298";
                printBoolean(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1063))

    def test64(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                temp: boolean = !delta||false||!false;
                printBoolean(temp);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1064))

    def test65(self):
        input = r"""
        learningtofly: function integer() {
            as, n : string = "q423 \\", "dwaf"::"dwad";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1065))

    def test66(self):
        input = '''
            main: function void () {
                a,c: boolean = true,!false;
                printBoolean(a);
                printBoolean(c);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1066))

    def test67(self):
        input = """
        x : array [2, 3] of integer
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 1067))

    def test68(self):
        input = """
        x : array [2, 3] of float;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1068))

    def test69(self):
        input = """
        x : array [2, 3, 4, 5] of integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1069))

    def test70(self):
        input = r"""
        learningtofly: function integer() {
            return !32_23_12-3_6-2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1070))

    def test71(self):
        input = r"""
        a = foo(4) = c = d;
        """
        expect = "Error on line 2 col 10: ="
        self.assertTrue(TestParser.test(input, expect, 1071))

    def test72(self):
        input = r"""
        b : integer = 5;
        a : integer = b = 6;
        """
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 1072))

    def test73(self):
        input = r"""
        main: function void() {
            if (a&&B) {
                a = b;
                c = d;
            } else  
                c = 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1073))

    def test74(self):
        input = r"""
        main: function void() {
            if (a&&B) {
                a = b;
                c = d;
            } else {} // empty
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1074))

    def test75(self):
        input = '''
            main: function void () {
                a,c: string = "true","!false";
                printString(a);
                printString(c);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1075))

    def test76(self):
        input = '''
            main: function void () {
                a,c: string = "true","!false";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1076))

    def test77(self):
        input = '''
            main: function void () {
                a,c: string = "true","det/tsef";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1077))
    
    def test78(self):
        input = '''
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                printInteger(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1078))

    def test79(self):
        input = """
        x : auto = 0.0;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1079))

    def test80(self):
        input = """
        x : auto = 0.0;
        y : auto = true;
        z : auto = "This is a string";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1080))

    def test81(self):
        input = """
        x,y,z,y,t,n : auto = 1,2,3,4,5,6;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1081))

    def test82(self):
        input = """
        x : array [] of integer;
        """
        expect = "Error on line 2 col 19: ]"
        self.assertTrue(TestParser.test(input, expect, 1082))

    def test83(self):
        input = r"""
        main: function void() {
            if (a&&B) {
                a = b;
                c = d;
                return False;
            } else 
                break;
            return ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1083))

    def test84(self):
        input = r"""
        main: function void() {
            for (i = 1, i <= 10, 1 + i)
            {
                a = a + 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1084))

    def test85(self):
        input = """
        main: function void() {
            while (i != 10 + 12)
                a : integer = 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1085))

    def test86(self):
        input = """
        main : function void() {
            {
                a : integer = 5;
                b = a* 2_0 -3 ;
                for (i = b, i > 1 , i-1)
                print(Array[0, i]);
            }
            return ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1086))

    def test87(self):
        input = '''
            voidA: function string (s: string){
                i: integer = 4;
                while (i>0){
                    s = s::"qua";
                }
                return s;
            }
            main: function void () {
                delta: string = "av";
                delta = voidA(delta);
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1087))

    def test88(self):
        input = '''
            voidAB: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(23);
                delta = delta/2 + delta/2/3;
                printInteger(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1088))

    def test89(self):
        input = '''
            voidA: function integer(n: array[5] of integer){
                return n[4];
            }
            main: function void () {
                delta: integer = 34+-4--5;
                delta = delta*2;
                printInteger(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1089))

    def test90(self):
        input = '''
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        continue;
                    }
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1090))

    def test91(self):
        input = '''
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        break;
                    }
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1091))

    def test92(self):
        input = '''
            main: function void () {
                for (i = 10, i >= 0, i - 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        break;
                    }
                }
                return;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1092))

    def test93(self):
        input = """
        fact : function integer(n: integer) {
            if(n==0) return 1;
            else return n*fact(n-1);
        }
        main: function void () {
            delta : integer;
            delta = fact(5)*fact(4)*fact(3);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1093))

    def test94(self):
        input = """
        fact : function integer(n: integer) {
            if(n==0) return 1;
            else return n*fact(n-1);
        }
        main: function void () {
            delta : integer;
            delta =  -fact(5);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1094))

    def test95(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
        }
        delta = inc(5,1);
        """
        expect = "Error on line 5 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 1095))

    def test96(self):
        input = """
        inc : function integer (out n : integer, delta : integer){
            n = n + delta;
            return n;
        }
        main: function void () {
        delta = inc(5;1);
        }
        """
        expect = "Error on line 7 col 21: ;"
        self.assertTrue(TestParser.test(input, expect, 1096))

    def test97(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
        }
        main: function void() {
            delta = inc(5,1);
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1097))

    def test98(self):
        input = """a: integer = 3;b,c:string = "abc","def";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1098))

    def test99(self):
        input = """e, r, t, f: integer = 6, 5, 4;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 1099))

    def test100(self):
        input = """
        inc : function void (out n : integer, delta : integer){
            n = n + delta;
            i : integer;
            for(i = 1, i < 10){
                writeInt(i);
            } 
        }
        """
        expect = "Error on line 5 col 29: )"
        self.assertTrue(TestParser.test(input, expect, 1100))
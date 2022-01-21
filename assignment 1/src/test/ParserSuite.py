import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):


    # def test29(self):
    #     input = """a[1] != b[1] && 2 * c >= 9 || abcd % 5"""
    #     expect = "Error on line 1 col 22: >="
    #     self.assertTrue(TestParser.test(input,expect,229))
    # def test30(self):
    #     input = """a != b >= c"""
    #     expect = "Error on line 1 col 7: >="
    #     self.assertTrue(TestParser.test(input,expect,230))



   

    # def test1(self):
    #     input = """
    #         Class Program {
    #             main() {
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 201))

    # def test2(self):
    #     input = """
    #         Class Program {
    #             getName() {
    #                 Var b: Float = 0.3;
    #             }

    #             main() {
    #                 Var a: Int;
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 202))

    # def test3(self):
    #     input = """
    #         Class Program {
                

    #             fksfywkfwi (a, b: Int ; d : Float) {
    #                 Self.age = age;
    #                 a = d;
    #            }
    #         }
                    
              
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 203))


    # def test4(self):
    #     input = """
    #         Class Program {
    #             main(){}
    #         }
    #         Class MeowMeow: Dog {
    #             Var b: Int;
    #             Var $a, c, d: Float = .e4, 2., 78.9;
    #             Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 204))

    # def test5(self):
    #     input = """
    #         Class Program {
    #             main(){
    #                 If (a >= b) {
    #                     Var a: Int = 0;
    #                     a = a + 3;
    #                 }
    #                 Elseif (b >= c) {
    #                     getName(a >= b);
    #                 }
    #                 Elseif (12 >= g) {
    #                     insert("String");
    #                 }
    #                 Else {
    #                     GiaBao = Hieu;
    #                     Hung = Vi;
    #                 }
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 205))

    
        
    # def test6(self):
    #     input = """
    #         Class Pro {
    #             Main(a: Int; b: Int) {
    #                 Return a || b < c.get(1,2) && 23 + 1.4;
    #             }
    #         }

    #         Class Program {
    #             main(){}
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 206))




    # def test7(self):
    #     input = """

    #         Self.arr[4] = a.a(1,2,3,4)  +  a.fwefnj();

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 207))
        
    # def test7(self):
    #     input = """
    #         Class Pro {
    #             MainMenu(a: Int; b: Int) {
    #                 Self.arr[4] = b.getName() + a.exp();
    #             }
    #         }

    #         Class Program {
    #             main(){
    #                 hung = hung.age(sadf,ver,rgre,qwe)[3].calc::$fsfsa::asffa()::wefeafwf.wewifw();
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 207))



    # def test8(self):
    #     input = """
    #             Class MyClass {
    #                 Var name: String;
    #                 Var age: Int = 0;

    #                 $printName() {
    #                     out.print(Self.name);
    #                 }

    #                 setAge(_age: Int) {
    #                     Self.age = _age;
    #                 }
    #             }
                
    #             Class Program {
    #                 main(){}
    #             }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 208))



    # def test9(self):
    #     input = """
    #         Class $Dog {
    #             Var $d: Int = 0x12345;
    #             foo() {
    #                 func(a,b,c);
    #                 Return result;
    #             }
    #         }
    #         Class Program {
    #             main(){}
    #         }
    #     """
    #     expect = "Error on line 2 col 18: $Dog"
    #     self.assertTrue(TestParser.test(input, expect, 209))


    # def test10(self):
    #     input = """
    #         Class super {
    #             get(){

    #             }
    #         }
    #         Class child: super {
    #             set() {
    #                 Return super::get();
    #             }
    #         }
    #     """
    #     expect = "Error on line 12 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 210))
        
    # def test11(self):
    #     input = """
    #         Class myClass {
    #             method() {
    #                 Foreach (i In 0 .. 100 By e <= i) {
    #                     a[1][2] = a[1][1] + b[1][3][i];
    #                 }
    #                 Return a <= b;
    #             }
    #         }
    #         Class Program {
    #             main() {

    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 211))
    

    # def test12(self):
    #     input = """
    #         Class Dog: Animal {
                
    #         }

    #         Class Snake: De {
                
    #         }

    #         Class Program {
               
    #         }

    #         Class Dog: Animal {
                
    #         }

            
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 212))


    # def test13(self):
    #     input = """
    #         Class Dog: Animal {
    #             $gaugau() {
    #                 Out.print(Self.gau);
    #             }
    #         }

    #         Class Program {
    #             main() {
    #                 Var a: Int;
    #             }
    #         }

    #         Class Dog: Animal {
    #             $gaugau() {
    #                 Out.print(Self.gau);
    #             }
    #         }

    #         Class Dog: Animal {
    #             $gaugau() {
    #                 Out.print(Self.gau);
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 213))

    # def test14(self):
    #     input = """
            
    #          Class Program {
                
    #             loop(a: Int; b: Float) {
    #                 Foreach (i In 0 .. 150 By i <= 8) {
    #                     sum = sum + a[i];

    #                     Foreach (i In 0 .. 150) {
    #                     sum = sum + a[i];
    #                     }
    #                 }
    #             }
    #             loop(a: Int; b: Float) {
    #                 Foreach (i In 0 .. 150 By i <= 8) {
    #                     sum = sum + a[i];

    #                     Foreach (i In 0 .. 150) {
    #                     sum = sum + a[i];
    #                     }
    #                 }
    #             }

                
    #         } 
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 214))


    # def test15(self):
    #     input = """
    #         Class ari {
    #             $_getMethod() {
    #                 Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
    #             }
    #         }
    #         Class Program {
    #             main() {
    #                 a = (myConst + b) && a + b + abcde;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 215))

        



















   















































    # def test1(self):
    #     input = """
    #         Class Dog: Animal {
    #             $gaugau() {
    #                 a = b[7][2];
    #             }
    #         }
    #         Class Snake: De {
    #             $OpOp() {
    #                 Return Self.Op;
    #             }
    #         }
    #         Class Program {
    #             main() {
    #                 Var a, b: Int;
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 201))
    # def test2(self):
    #     input = """
    #         Class Program {
    #             getName() {
    #                 Var b: Float = 0.3;
    #             }
    #             main() {
    #                 Var a: Int;
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 202))
    # def test3(self):
    #     input = """
    #         Class Program {
    #             getName() {
    #                 Var b: Float = 0.3;
    #             }
                
    #             main() {
    #                 If (a >= b) {
    #                     Var a: Int = 0;
    #                     a = a + 3;
    #                 }
    #                 Elseif (b >= c) {
    #                     Self.getName(a >= b);
    #                 }
    #                 Elseif (12 >= g) {
    #                     Self.insert("String");
    #                 }
    #                 Else {
    #                     GiaBao = Hieu;
    #                     Hung = Vi;
    #                 }
    #             }

    #             setAge(age: Int) {
    #                 Self.age = age;
    #             }
    #         }
            
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 203))
    # def test4(self):
    #     input = """ 
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class MeowMeow: Dog {
    #             Var b: Int;
    #             Var $a, c, d: Float = .e4, 2., 78.9;
    #             Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 204))
    # def test5(self):
    #     input = """
    #         Class Program {
    #             main(){

    #             }
    #         }
    #         Class mini {
    #             loop(a: Int; b: Float) {
    #                 Foreach (i In 0 .. 150 By i <= 8) {
    #                     sum = sum + a[i];
    #                 }
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 205))
    # def test6(self):
    #     input = """
    #         Class Pro {
    #             Main(a: Int; b: Int) {
    #                 Return a || b < c.get(1,2) && 23 + 1.4;
    #             }
    #         }
    #         Class Program {
    #             main() {
    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 206))
    # def test7(self):
    #     input = """
    #         Class Pro {
    #             MainMenu(a: Int; b: Int) {
    #                 Self.arr[4] = b.getName() + a.exp();
    #             }
    #         }
    #         Class Program {
    #             main(){

    #             }
    #         }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 207))
    # def test8(self):
    #     input = """
    #             Class MyClass {
    #                 Var name: String;
    #                 Var age: Int = 0;
    #                 $printName() {
    #                     Out.print(Self.name);
    #                 }
    #                 setAge(_age: Int) {
    #                     Self.age = _age;
    #                 }
    #             }
    #             Class Program {
    #                 main(){

    #                 }
    #             }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 208))
    # def test9(self):
    #     input = """
    #         Class $Dog {
    #             Var $d: Int = 0x12345;
    #             foo() {
    #                 func(a,b,c);
    #                 Return result;
    #             }
    #         }
    #         Class Program {
    #             main(){

    #             }
    #         }
    #     """
    #     expect = "Error on line 2 col 18: $Dog"
    #     self.assertTrue(TestParser.test(input, expect, 209))
    # def test10(self):
    #     input = """
    #         Class super {
    #             get(){

    #             }
    #         }
    #         Class child: super {
    #             set() {
    #                 Return super::get();
    #             }
    #         }
    #     """
    #     expect = "Error on line 12 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 210))
    # def test11(self):
    #     input = """
    #         Class myClass {
    #             method() {
    #                 Foreach (i In 0 .. 100 By e <= i) {
    #                     a[1][2] = a[1][1] + b[1][3][i];
    #                 }
    #                 Return a <= b;
    #             }
    #         }
    #         Class Program {
    #             main() {

    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 211))
    # def test12(self):
    #     input = """
    #         Class ari {
    #             $_getMethod() {
    #                 Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
    #             }
    #         }
    #         Class Program {
    #             main() {
    #                 a = (myConst + b) && a + b + abcde;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 212))

    # def test13(self):
    #     input = """
    #         Class myDog {
    #             method(a: Array[Int, 4]) {
    #                 Return a[0]
    #             }
    #         }
    #         Class Program {
    #             main(){}
    #         }
    #     """
    #     expect = "Error on line 5 col 16: }"
    #     self.assertTrue(TestParser.test(input, expect,213))

    # def test14(self):
    #     input = """
    #         Class myVar {
    #             Constructor(arr: Array[Float, 3]) {
    #                 Self.a = arr[1];
    #                 Self.b = arr[2];
    #                 Self.c = arr[2][1];
    #             }
    #         }
    #         Class Program {
    #             main(){}
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,214))

    # def test15(self):
    #     input = """
    #         Class Program {
    #             main(){}
    #         }
    #         Class Des {
    #             Destructor() {
    #                 Des.Delete();
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,215))

    # def test16(self):
    #     input = """
    #         Class Program {
    #             main(){}
    #         }

    #         Class Main {
    #             menu() {
    #                 Return Self.arr;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,216))

    # def test17(self):
    #     input = """
    #         Class Program {
    #             dethod() {
    #                 Return Self.method();
    #             }
    #             main(){}
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,217))

    # def test18(self):
    #     input = """
    #         Class Meow {
    #             returnMethod() {

    #             }
    #             Constructor() {
    #                 Self.init = value;
    #             }
    #             Destructor() {
    #                 Mew.EraseAll();
    #             }
    #         }
    #         Class Program {
    #             main(){

    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,218))

    # def test19(self):
    #     input = """
    #         Class foo {
    #             Var Foo: Int = 0xFF;
    #         }
    #     """
    #     expect = "Error on line 5 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect,219))

    # def test20(self):
    #     input = """
    #         Class ari {
    #             Constructor(a, b : Int)
    #             {
    #                 Out.print("Contructor");
    #             }
    #             Destructor()
    #             {
    #                 Out.print("Destructor");
    #             }
    #             $_getMethod() {
    #                 Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
    #             }
    #         }
    #         Class Program {
    #             Constructor(a, b : Int)
    #             {
    #                 Out.print("Contructor");
    #             }
    #             Destructor()
    #             {
    #                 Out.print("Destructor");
    #             }
    #             main() {
    #                 a = (myConst + b) && a + b + abcde;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,220))

    # def test21(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 Out.print("Hello From Main");
    #             }
    #         }
    #         Class iden {}
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,221))

    # def test22(self):
    #     input = """
    #         Class myFunc {
    #             func(s: Int; r: String) {
    #                 Return Stand.Str(s + r);
    #             }
    #         }
    #         Class Program {
    #             main() {}
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,222))

    # def test23(self):
    #     input = """
    #         Class Program {
    #             main(){}
    #         }

    #         Class class1 {
    #             Var name: String;
    #         }
    #         Class class2 {
    #             Val $height: Float = 1.75;
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,223))

    # def test24(self):
    #     input = """
    #         Class obj {
    #             Var _obj: Int = 0, 9;
    #         }
    #         Class Program {
    #             main() {
    #                 func(Array("a", "b", "c"));
    #                 Return Self.arr;
    #             }
    #         }
    #     """
    #     expect = "Error on line 3 col 33: ,"
    #     self.assertTrue(TestParser.test(input, expect,224))

    def test25(self):
        input = """
            
                b[1].name,
                
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,225))
    # def test25(self):
    #     input = """
    #         Class Program {
    #             main() {
                
    #             }
    #         }
    #         Class lop {
    #             attr(a, b: Int) {
    #                 Return a[4] != b[1].name;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,225))

    # def test26(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class parent {
    #             Var lname, fname: String = "";
    #             $getName() {
    #                 Return Self.name[2];
    #             }
    #         }
    #     """
    #     expect = "Error on line 8 col 45: ;"
    #     self.assertTrue(TestParser.test(input, expect,226))

    # def test27(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 Return New object();
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,227))

    # def test28(self):
    #     input = """
    #         Class Program {
    #             main(a: Int, b: Float) {

    #             }
    #         }
    #     """
    #     expect = "Error on line 3 col 21: a"
    #     self.assertTrue(TestParser.test(input, expect,228))

    # def test29(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class Func {
    #             Constructor(){Return name;}
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,229))

    # def test30(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class className {
    #             Destructor(param: Int, param_2: String) {

    #             }
    #         }
    #     """
    #     expect = "Error on line 8 col 27: param"
    #     self.assertTrue(TestParser.test(input, expect,230))

    # def test31(self):
    #     input = """
    #         Class Dog {
    #             Var name: Int;
    #             Var age: Int = 2, 6, 4;
    #         }
    #         Class Program {
    #             main() {

    #             }
    #         }
    #     """
    #     expect = "Error on line 4 col 32: ,"
    #     self.assertTrue(TestParser.test(input, expect,231))

    # def test32(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 Foreach (idx In 1 .. 100 + 5 By a[i] >= 9) {
    #                     If (a[i][1] != b[1]) {
    #                         Return;
    #                     }
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,232))

    # def test33(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class Another {
    #             function() {
    #                 program.Main();
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,233))

    # def test34(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class Name {
    #             hello(s1, s2, s3: String) {
    #                 Return Str.concat(s1, s2, s3);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,234))

    # def test35(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 Out.print(Dog.sound());
    #             }
    #         }
    #         Class Dog {
    #             sound() {
    #                 Return New Animal().dogSound();
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,235))

    # def test36(self):
    #     input = """
    #         Class Program {
    #             Var a: Int = 0;
    #             main() {
    #                 a = New obj("string 1");
    #                 Out.print(a.age);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,236))

    # def test37(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class Method {
    #             newMethod(a: String) {
    #                 Return a[0].length;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,237))

    # def test38(self):
    #     input = """
    #         Class Program {
    #             Var a, b, c: Int = 1, 2, 3 >= 9 + 5;
    #             main() {
    #                 If (a >= b) {
    #                     Foreach (i In 0 .. c[5][3].length By 1) {
    #                         If (c[i]) {
    #                             Continue;
    #                         }
    #                         Else {
    #                             Break;
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,238))

    # def test39(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class newClass {
    #             Val count: Int = 150;
    #             Val sum, rate: Float = 10.2, 34.4;
    #             PrintOut() {
    #                 Return Self.count * Self.rate;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,239))

    # def test40(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 Stand.getVector();
    #             }
    #         }
    #         Class myClass {
    #             $method() {
    #                 Return Self.sound()[2];
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,240))

    # def test41(self):
    #     input = """
    #         Class class {
    #             Var a, b, c: Int = 3, 4, 5;
    #             $print() {
    #                 Return Array(a,b,c);
    #             }
    #         }
    #         Class Program {
    #             main() {

    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,241))

    # def test42(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class Par {
    #             Var con: String;
    #             Var me: Float = 0.2;
    #             $get() {
    #                 Local.Store.sieuthi();
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,242))

    # def test43(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Out.print(a, b, 3);
    #     """
    #     expect = "Error on line 7 col 12: Out"
    #     self.assertTrue(TestParser.test(input, expect,243))

    # def test44(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 If (a == b) {
    #                     Foreach (i In 1 .. len By 2) {
    #                         Continue;
    #                     }
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,244))

    # def test45(self):
    #     input = """
    #         Class Program {
    #             main() {
    #                 Dog.name = Cat.name +. "1";
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,245))

    # def test46(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class Meo: Dog {
    #             $get() {
    #                 Self.name = Dog::name;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,246))

    # def test47(self):
    #     input = """
    #         If (a >= b) {
    #             Return Program;
    #         }
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class Buffalo: $Animals {
    #             Dog.scopeMethod();
    #         }
    #     """
    #     expect = "Error on line 2 col 12: If"
    #     self.assertTrue(TestParser.test(input, expect,247))

    # def test48(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Foreach (i In 0 .. 10 By 1 + 2 + 3 + a.get - b.name) {
    #             Continue;
    #             Break;
    #         }
    #     """
    #     expect = "Error on line 7 col 12: Foreach"
    #     self.assertTrue(TestParser.test(input, expect,248))

    # def test49(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class A {
    #             Return New B(A);
    #         }
    #     """
    #     expect = "Error on line 8 col 16: Return"
    #     self.assertTrue(TestParser.test(input, expect,249))

    # def test50(self):
    #     input = """
    #         Class Program {
    #             main() {

    #             }
    #         }
    #         Class B: A {
    #             Var a, b: Float = 3.5, 5;
    #             Return a;
    #         }
    #     """
    #     expect = "Error on line 9 col 16: Return"
    #     self.assertTrue(TestParser.test(input, expect,250))

   

#  25 37 38

    # def test51(self):
    #     input = """
    #         Class Program {
    #             main() {

    #                 Var a : Int = New Animal().Dog().Beagle();
    #             }

    #             func() {

    #                 test();

    #                 test().a().b().c().d();

    #                 test().a()::b::c.d();

    #                 test().a::test().b::c::d::e::$f();

    #                 test(1,a,b,23234,0x12).a______AFEFE::$_EAFWEFtest(AASDSAwqqeqw, 132___216387__78.34e-362536)._____bfwefew::c::d::e::$f(\"qwdqdq\");
                
    #             }
    #         }
            
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,251))

    # def test52(self):
    #     input = """
    #         Class Program {
    #             main() {

    #                 Var a : Int = New Animal();

    #                 Var a : Int = New Animal().Dog().Beagle();
    #             }

    #             Var a : Int = New Animal();

    #             Var $a : Int = New Animal().Dog().Beagle();

    #             Var a : Int = New Animal().Dog();

    #             func() {

    #                 Var a : Int = New Animal();

    #                 Var $a : Int = New Animal().Dog().Beagle();

    #                 Var a : Int = New Animal().Dog().Beagle();

    #             }
    #         }
            
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,252))







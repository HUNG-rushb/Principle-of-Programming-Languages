import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))









    # def test1(self):
    #     input = """Var a : Int;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test2(self):
    #     input = """Var $bcd : Array[Int, 6];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))

    # def test3(self):
    #     input = """Var $e : String;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,203))
    # def test4(self):
    #     input = """Val $e : Float;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,204))
    # def test5(self):
    #     input = """Var $e : Boolean;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,205))
        
    # def test6(self):
    #     input = """Var a : Int = 5;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,206))

    # def test7(self):
    #     input = """Var a : Int = 56_789;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,207))
    # def test8(self):
    #     input = """Var a : Boolean = True;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,208))
    # def test9(self):
    #     input = """Var a : String = "AbcDEF\n";"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,209))
    # def test10(self):
    #     input = """Var a : Float = 1.8e-12;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,210))
    # def test11(self):
    #     input = """Var a : Int = 0b100101;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,211))
    







    # def test12(self):
    #     input = """Var a : Int = 5 + 4;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,212))
    # def test13(self):
    #     input = """Var a : Int = 5 + b;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,213))
    # def test14(self):
    #     input = """Var a : Int = 5 + b - c / 6 * d + 6;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,214))
    # def test15(self):
    #     input = """Var a : Boolean = !b;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,215))
        
    # def test16(self):
    #     input = """Var a : Int = b[5];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,216))
    # def test17(self):
    #     input = """Var a : String = "abc" +. "bcd";"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,217))
    # def test18(self):
    #     input = """Var $bcd : Array[Array[String, 7], 6];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,218))
    # def test19(self):
    #     input = """Var $bcd : Boolean = a && b || c;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,219))
    # def test20(self):
    #     input = """Var $bcd : Boolean = a && (b || c);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,220))

    # def test21(self):
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.56) - (c / d);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,221))

    # def test22(self):
    #     input = """Var $bcd : Array[Int, 3] = Array(1, 4, 3);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,222))

    # def test23(self):
    #     input = """Var $bcd : Array[Array[Int, 3], 3] = Array(
    #         Array(1, 2, 3),
    #         Array(4, 5, 6),
    #         Array(7, 8, 9));"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,223))

    # def test24(self):
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.56) - (c / d) + arr[6];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,224))
    # def test25(self):
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.56) - (c / d) + arr[6] - ar[5][7];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,225))
    # def test26(self):
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.56) - (c / d) + (arr[6] - ar[5][7]) * a[3][5][1][2];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,226))

    # def test27(self):
    #     input = """Var $bcd : Int = player.a;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,227))

    # def test28(self):
    #     input = """Var $bcd : Int = New Player(a, b, c);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,227))
 


    # def test29(self):
    #     input = """a[1] != b[1] && 2 * c >= 9 || abcd % 5"""
    #     expect = "Error on line 1 col 22: >="
    #     self.assertTrue(TestParser.test(input,expect,229))
    # def test30(self):
    #     input = """a != b >= c"""
    #     expect = "Error on line 1 col 7: >="
    #     self.assertTrue(TestParser.test(input,expect,230))











    # def test_expression_1(self):
    #     input = """ 12 + 1.2 - c !b >= 8 || 4 || (a + b) """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 204))
    # def test_expression_2(self):
    #     input = """ (myConst + b) && a + b + abcde """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 205))
    # def test_expression_3(self):
    #     input = """ a.get(a != b) + b.set(1 == 2) """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 206))
    # def test_expression_4(self):
    #     # input = """ b || a """
    #     input = """ (myConst < b || myConst >= a) && -8 + 2e4 + 5e-9 """
    #     expect = "Error on line 1 col 25: >="
    #     self.assertTrue(TestParser.test(input, expect, 207))
    # def test_expression_5(self):
    #     input = """ (myConst + b) != (a || b && c) """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 208))
    # def test_expression_6(self):
    #     input = """ 12 / 2 % 3 + 5 - 6 * 5.6 """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 209))
    # def test_expression_7(self):
    #     input = """ 1_23.6 + 56_123_123.4e-12 - 12. * 071 """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 210))
    # def test_expression_8(self):
    #     input = """ 0b1001 * 0xAF + 0B00001 - 1_234_908 """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 211))
    # def test_expression_9(self):
    #     input = """ (myConst + b) && a + b + abcde """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 212))

    # def test_expression_10(self):
    #     input = """ (myConst + b) && a + b + abcde """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 213))


















   

    def test1(self):
        input = """
            Class Program {
                main() {
                
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

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
    #         Class Pro {
    #             MainMenu(a: Int; b: Int) {
    #                 Self.arr[4] = b.getName() + a.exp();
    #             }
    #         }
    #         Class Program {
    #             main(){}
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
    #                     print(Self.name);
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

        



















#   def test1(self):
#         input = """
#             Class Dog: Animal {
#                 $gaugau() {
#                     Out.print(Self.gau);
#                 }
#             }
#             Class Snake: De {
#                 $OpOp() {
#                     Return Self.Op;
#                 }
#             }
#             Class Program {
#                 main() {
#                     Var a: Int;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))
#     def test2(self):
#         input = """
#             Class Program {
#                 getName() {
#                     Var b: Float = 0.3;
#                 }
#                 main() {
#                     Var a: Int;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))
#     def test3(self):
#         input = """
#             Class Program {
#                 getName() {
#                     Var b: Float = 0.3;
#                 }
#                 main() {
#                     If (a >= b) {
#                         Var a: Int = 0;
#                         a = a + 3;
#                     }
#                     Elseif (b >= c) {
#                         Self.getName(a >= b);
#                     }
#                     Elseif (12 >= g) {
#                         Self.insert("String");
#                     }
#                     Else {
#                         GiaBao = Hieu;
#                         Hung = Vi;
#                     }
#                 }

#                 setAge(age: Int) {
#                     Self.age = age;
#                 }
#             }
            
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 203))
#     def test4(self):
#         input = """
#             Class Program {
#                 main(){}
#             }
#             Class MeowMeow: Dog {
#                 Var b: Int;
#                 Var $a, c, d: Float = .e4, 2., 78.9;
#                 Var a: Array[Float, 5] = Array(1.2, 3.6, 34e5, 23e4, 12.7e4);
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 204))
#     def test5(self):
#         input = """
#             Class Program {
#                 main(){}
#             }
#             Class mini {
#                 loop(a: Int; b: Float) {
#                     Foreach (i In 0 .. 150 By i <= 8) {
#                         sum = sum + a[i];
#                     }
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 205))
#     def test6(self):
#         input = """
#             Class Pro {
#                 Main(a: Int; b: Int) {
#                     Return a || b < c.get(1,2) && 23 + 1.4;
#                 }
#             }
#             Class Program {
#                 main(){}
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 206))
#     def test7(self):
#         input = """
#             Class Pro {
#                 MainMenu(a: Int; b: Int) {
#                     Self.arr[4] = b.getName() + a.exp();
#                 }
#             }
#             Class Program {
#                 main(){}
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 207))
#     def test8(self):
#         input = """
#                 Class MyClass {
#                     Var name: String;
#                     Var age: Int = 0;
#                     $printName() {
#                         Out.print(Self.name);
#                     }
#                     setAge(_age: Int) {
#                         Self.age = _age;
#                     }
#                 }
#                 Class Program {
#                     main(){}
#                 }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 208))
#     def test9(self):
#         input = """
#             Class $Dog {
#                 Var $d: Int = 0x12345;
#                 foo() {
#                     func(a,b,c);
#                     Return result;
#                 }
#             }
#             Class Program {
#                 main(){}
#             }
#         """
#         expect = "Error on line 2 col 18: $Dog"
#         self.assertTrue(TestParser.test(input, expect, 209))
#     def test10(self):
#         input = """
#             Class super {
#                 get(){

#                 }
#             }
#             Class child: super {
#                 set() {
#                     Return super::get();
#                 }
#             }
#         """
#         expect = "Error on line 12 col 8: <EOF>"
#         self.assertTrue(TestParser.test(input, expect, 210))
#     def test11(self):
#         input = """
#             Class myClass {
#                 method() {
#                     Foreach (i In 0 .. 100 By e <= i) {
#                         a[1][2] = a[1][1] + b[1][3][i];
#                     }
#                     Return a <= b;
#                 }
#             }
#             Class Program {
#                 main() {

#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 211))
#     def test12(self):
#         input = """
#             Class ari {
#                 $_getMethod() {
#                     Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
#                 }
#             }
#             Class Program {
#                 main() {
#                     a = (myConst + b) && a + b + abcde;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 212))

#     def test13(self):
#         input = """
#             Class myDog {
#                 method(a: Array[Int, 4]) {
#                     Return a[0]
#                 }
#             }
#             Class Program {
#                 main(){}
#             }
#         """
#         expect = "Error on line 5 col 16: }"
#         self.assertTrue(TestParser.test(input, expect,213))

#     def test14(self):
#         input = """
#             Class myVar {
#                 Constructor(arr: Array[Float, 3]) {
#                     Self.a = arr[1];
#                     Self.b = arr[2];
#                     Self.c = arr[2][1];
#                 }
#             }
#             Class Program {
#                 main(){}
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,214))

#     def test15(self):
#         input = """
#             Class Program {
#                 main(){}
#             }
#             Class Des {
#                 Destructor() {
#                     Des.Delete();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,215))

#     def test16(self):
#         input = """
#             Class Program {
#                 main(){}
#             }

#             Class Main {
#                 menu() {
#                     Return Self.arr;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,216))

#     def test17(self):
#         input = """
#             Class Program {
#                 dethod() {
#                     Return Self.method();
#                 }
#                 main(){}
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,217))

#     def test18(self):
#         input = """
#             Class Meow {
#                 returnMethod() {

#                 }
#                 Constructor() {
#                     Self.init = value;
#                 }
#                 Destructor() {
#                     Mew.EraseAll();
#                 }
#             }
#             Class Program {
#                 main(){

#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,218))

#     def test19(self):
#         input = """
#             Class foo {
#                 Var Foo: Int = 0xFF;
#             }
#         """
#         expect = "Error on line 5 col 8: <EOF>"
#         self.assertTrue(TestParser.test(input, expect,219))

#     def test20(self):
#         input = """
#             Class ari {
#                 Constructor(a, b : Int)
#                 {
#                     Out.print("Contructor");
#                 }
#                 Destructor()
#                 {
#                     Out.print("Destructor");
#                 }
#                 $_getMethod() {
#                     Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
#                 }
#             }
#             Class Program {
#                 Constructor(a, b : Int)
#                 {
#                     Out.print("Contructor");
#                 }
#                 Destructor()
#                 {
#                     Out.print("Destructor");
#                 }
#                 main() {
#                     a = (myConst + b) && a + b + abcde;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,220))

#     def test21(self):
#         input = """
#             Class Program {
#                 main() {
#                     Out.print("Hello From Main");
#                 }
#             }
#             Class iden {}
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,221))

#     def test22(self):
#         input = """
#             Class myFunc {
#                 func(s: Int; r: String) {
#                     Return Stand.Str(s + r);
#                 }
#             }
#             Class Program {
#                 main() {}
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,222))

#     def test23(self):
#         input = """
#             Class Program {
#                 main(){}
#             }

#             Class class1 {
#                 Var name: String;
#             }
#             Class class2 {
#                 Val $height: Float = 1.75;
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,223))

#     def test24(self):
#         input = """
#             Class obj {
#                 Var _obj: Int = 0, 9;
#             }
#             Class Program {
#                 main() {
#                     func(Array("a", "b", "c"));
#                     Return Self.arr;
#                 }
#             }
#         """
#         expect = "Error on line 3 col 33: ,"
#         self.assertTrue(TestParser.test(input, expect,224))

#     def test25(self):
#         input = """
#             Class lop {
#                 attr(a, b: Int) {
#                     Return a[1] * b[1].name;
#                 }
#             }
#             Class Program {
#                 main() {
#                     Return a;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,225))

#     def test26(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class parent {
#                 Var lname, fname: String = "";
#                 $getName() {
#                     Return Self.name[2];
#                 }
#             }
#         """
#         expect = "Error on line 8 col 45: ;"
#         self.assertTrue(TestParser.test(input, expect,226))

#     def test27(self):
#         input = """
#             Class Program {
#                 main() {
#                     Return New object();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,227))

#     def test28(self):
#         input = """
#             Class Program {
#                 main(a: Int, b: Float) {

#                 }
#             }
#         """
#         expect = "Error on line 3 col 21: a"
#         self.assertTrue(TestParser.test(input, expect,228))

#     def test29(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class Func {
#                 Constructor(){Return name;}
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,229))

#     def test30(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class className {
#                 Destructor(param: Int, param_2: String) {

#                 }
#             }
#         """
#         expect = "Error on line 8 col 27: param"
#         self.assertTrue(TestParser.test(input, expect,230))

#     def test31(self):
#         input = """
#             Class Dog {
#                 Var name: Int;
#                 Var age: Int = 2, 6, 4;
#             }
#             Class Program {
#                 main() {

#                 }
#             }
#         """
#         expect = "Error on line 4 col 32: ,"
#         self.assertTrue(TestParser.test(input, expect,231))

#     def test32(self):
#         input = """
#             Class Program {
#                 main() {
#                     Foreach (idx In 1 .. 100 + 5 By a[i] >= 9) {
#                         If (a[i][1] != b[1]) {
#                             Return;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,232))

#     def test33(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class Another {
#                 function() {
#                     program.Main();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,233))

#     def test34(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class Name {
#                 hello(s1, s2, s3: String) {
#                     Return Str.concat(s1, s2, s3);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,234))

#     def test35(self):
#         input = """
#             Class Program {
#                 main() {
#                     Out.print(Dog.sound());
#                 }
#             }
#             Class Dog {
#                 sound() {
#                     Return New Animal().dogSound();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,235))

#     def test36(self):
#         input = """
#             Class Program {
#                 Var a: Int = 0;
#                 main() {
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,236))

#     def test37(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class Method {
#                 newMethod(a: String) {
#                     Return a[0].length;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,237))

#     def test38(self):
#         input = """
#             Class Program {
#                 Var a, b, c: Int = 1, 2, 3 >= 9 + 5;
#                 main() {
#                     If (a >= b) {
#                         Foreach (i In 0 .. c[5][3].length By 1) {
#                             If (c[i]) {
#                                 Continue;
#                             }
#                             Else {
#                                 Break;
#                             }
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,238))

#     def test39(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class newClass {
#                 Val count: Int = 150;
#                 Val sum, rate: Float = 10.2, 34.4;
#                 PrintOut() {
#                     Return Self.count * Self.rate;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,239))

#     def test40(self):
#         input = """
#             Class Program {
#                 main() {
#                     Stand.getVector();
#                 }
#             }
#             Class myClass {
#                 $method() {
#                     Return Self.sound()[2];
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,240))
#     def test41(self):
#         input = """
#             Class Program {
#                 main()
#                 {
                    
#                 }
#                 loop(a: Int; b: Float) {
#                     Foreach (i In 0 .. 150 By i <= 8) {
#                         sum = sum + a[i];
#                     }
#                 }

#                 loop2 (a: Int; b: Float) {
#                     Foreach (i In 0 .. 150) {
#                         sum = sum + a[i];
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,241))
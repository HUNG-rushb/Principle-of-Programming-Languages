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
    
    def test12(self):
        input = """Var a : Int = 5 + 4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test13(self):
        input = """Var a : Int = 5 + b;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test14(self):
        input = """Var a : Int = 5 + b - c / 6 * d + 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test15(self):
        input = """Var a : Boolean = !b;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
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
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.5_6) - (c / d);"""
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
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.5_6) - (c / d) + arr[6];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,224))
    # def test25(self):
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.5_6) - (c / d) + arr[6] - ar[5][7];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,225))
    # def test26(self):
    #     input = """Var $bcd : Float = 1_25.6e5 + (5.4 - 9.5_6) - (c / d) + (arr[6] - ar[5][7]) * a[3][5][1][2];"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,226))
    # def test27(self):
    #     input = """Var $bcd : Int = player.a;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,227))
    # def test27(self):
    #     input = """Var $bcd : Int = New Player(a, b, c);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,227))
    # def test28(self):
    #     input = """Var $bcd : Int = Player::a;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,228))
    # def test28(self):
    #     input = """Var $bcd : Int = player.a(b,c,d);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,228))
    # def test29(self):
    #     input = """a[1] != b[1] && 2 * c >= 9 || abcd % 5"""
    #     expect = "Error on line 1 col 22: >="
    #     self.assertTrue(TestParser.test(input,expect,229))
    # def test30(self):
    #     input = """a != b >= c"""
    #     expect = "Error on line 1 col 7: >="
    #     self.assertTrue(TestParser.test(input,expect,230))











#     def test_expression_1(self):
#         input = """ 12 + 1.2 - c !b >= 8 || 4 || (a + b) """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 204))
#     def test_expression_2(self):
#         input = """ (myConst + b) && a + b + abcde """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 205))
#     def test_expression_3(self):
#         input = """ a.get(a != b) + b.set(1 == 2) """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 206))
#     def test_expression_4(self):
#         # input = """ b || a """
#         input = """ (myConst < b || myConst >= a) && -8 + 2e4 + 5e-9 """
#         expect = "Error on line 1 col 25: >="
#         self.assertTrue(TestParser.test(input, expect, 207))
#     def test_expression_5(self):
#         input = """ (myConst + b) != (a || b && c) """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 208))
#     def test_expression_6(self):
#         input = """ 12 / 2 % 3 + 5 - 6 * 5.6 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 209))
#     def test_expression_7(self):
#         input = """ 1_23.6 + 56_123_123.4e-12 - 12. * 071 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 210))
#     def test_expression_8(self):
#         input = """ 0b1001 * 0xAF + 0B00001 - 1_234_908 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 211))
#     def test_expression_9(self):
#         input = """ (myConst + b) && a + b + abcde """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 212))
#     def test_expression_10(self):
#         input = """ (myConst + b) && a + b + abcde """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 213)
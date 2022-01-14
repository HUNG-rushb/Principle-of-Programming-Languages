import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # def test_operators(self):
        # self.assertTrue(TestLexer.test("+ - * / <= >= = < > && || ==. = ==","+,-,*,/,<=,>=,,=,<,>,&&,||,==.,=,==,<EOF>", 101))
        # self.assertTrue(TestLexer.test("+ - * / < > && || ==. = ==","+,-,*,/,<,>,&&,||,==.,=,==,<EOF>", 101))

    # def test_identifier_1(self):
    #     self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    # def test_identifier_2(self):
    #     self.assertTrue(TestLexer.test("23427b5", "23427,b5,<EOF>", 103))

    # def test_identifier_3(self):
    #     self.assertTrue(TestLexer.test("_duyhung135", "_duyhung135,<EOF>", 104))

    # def test_identifier_dollar(self):
    #     self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 105))

    # def test_identifier_dollar_2(self):
    #     self.assertTrue(TestLexer.test("$_dollarstatic", "$_dollarstatic,<EOF>", 106))

    # def test_identifier_7(self):
    #     self.assertTrue(TestLexer.test("   $duy     hung", "$duy,hung,<EOF>", 107))

    # def test_identifier_8(self):
    #     self.assertTrue(TestLexer.test("_12343_my const", "_12343_my,const,<EOF>", 108))

    # def test_identifier_9(self):
    #     self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 109))

    # def test_identifier_10(self):
    #     self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 110))

    # def test_identifier_11(self):
    #     self.assertTrue(TestLexer.test("%duyHUNG", "%,duyHUNG,<EOF>", 111))

    # def test_identifier_12(self):
    #     self.assertTrue(TestLexer.test("* + hung      /   ", "*,+,hung,/,<EOF>", 112))

    # def test_identifier_13(self):
    #     self.assertTrue(TestLexer.test("$", "Error Token $", 113))

    # def test_var_declare(self):
    #     self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xaff", "Var,$dec,,,num,:,Int,=,0b0101110,,,0xaff,<EOF>", 114))
    
    # def test_float_number(self):
    #     self.assertTrue(TestLexer.test("12.45e67", "12.45e67,<EOF>", 115))

    # def test_hex_number(self):
    #     self.assertTrue(TestLexer.test("0x1A2b", "0x1A2b,<EOF>", 116))

    # def test_binary_number(self):
    #     self.assertTrue(TestLexer.test("0b0101110010010010100101", "0b0101110010010010100101,<EOF>", 117))

    # def test_binary_number_2(self):
    #     self.assertTrue(TestLexer.test("0B01010101_ABfwfkmdfks23343_dweidmwef", "0B01010101,_ABfwfkmdfks23343_dweidmwef,<EOF>", 118))

    # def test_octal_number(self):
    #     self.assertTrue(TestLexer.test("071235663636215", "071235663636215,<EOF>", 119))

    # def test_octal_number_2(self):
    #     self.assertTrue(TestLexer.test("023352345231_ddfiweufAdeifBT_zzzzzz", "023352345231,_ddfiweufAdeifBT_zzzzzz,<EOF>", 120))

    # def test_octal_number_3(self):
    #     self.assertTrue(TestLexer.test("000000001234567765531243_duyhungZzDW____wfwoeifj", "000000001234567765531243,_duyhungZzDW____wfwoeifj,<EOF>", 121))

    # def test_numbers(self):
    #     self.assertTrue(TestLexer.test("12314234 0B1010010 0.234 1E-21321  0x19283263246Abdef 0120234573 0.1227000010", 
    #     "12314234,0B1010010,0.234,1E-21321,0x19283263246Abdef,0120234573,0.1227000010,<EOF>", 122))

    # def test_block_comment_1(self):
    #     self.assertTrue(TestLexer.test("""
    #         ## Testing comment fowifjowfnwio!@#@#$$#%@^@%^&?<>":{{}}({}()}:(){(})}) ##
    #     """, "<EOF>", 123))

    # def test_block_comment_2(self):
    #     self.assertTrue(TestLexer.test("## ASCWEasdasd !@@#%$#  %lgvkhjk$%^&*(&*~{}[]\;]\p/.,.,<>>) ##", "<EOF>",124))
    
    # def test_block_comment_3(self):
    #     self.assertTrue(TestLexer.test("## # ASCWEasdasd !@@#%$#%$%^&*(&*~{}[]\;]\p/.,.,<>>) # ##", "<EOF>",125))

    # def test_hex_number_2(self):
    #     self.assertTrue(TestLexer.test("0x1A2bFf09", "0x1A2bFf09,<EOF>", 126))

    # def test_hex_number_3(self):
    #     self.assertTrue(TestLexer.test("0x09aFZXY_asd123", "0x09aF,ZXY_asd123,<EOF>", 127))

    # def test_keywords(self):
    #     self.assertTrue(TestLexer.test("""
    #     Break Continue If Elseif Else Foreach True False Array In Int 
    #     Float Boolean String Return Null Class Val Var Constructor Destructor New By""", 
    #     "Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,By,<EOF>", 128))

    def test_hex_number_3(self):
        self.assertTrue(TestLexer.test("0x09aFZXY_asd123", "0x09aF,ZXY_asd123,<EOF>", 129))

    def test_hex_number_3(self):
        self.assertTrue(TestLexer.test("0x09aFZXY_asd123", "0x09aF,ZXY_asd123,<EOF>", 130))







    # def test_string_1(self):
    #     self.assertTrue(TestLexer.test("\"aj\elhadef\"", "Illegal Escape In String: aj\e", 117)) 

    # def test_string_2(self):
    #     self.assertTrue(TestLexer.test("\"ab3j\tlhadef\"", "ab3j    lhadef,<EOF>", 118))  

    # def test_string_3(self):
    #     self.assertTrue(TestLexer.test("""
    #         "Hello from '"Python'""
    #     """, """Hello from "Python",<EOF>""", 119))  

    # def test_string_4(self):
    #     self.assertTrue(TestLexer.test("\"abc \r babc", """Unclosed String: abc babc""", 120))

    # def test_expression_1(self):
    #     self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9", "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 121))
    
    # def test_expression_2(self):
    #     self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34", "34,<,9,+,12e3,-,1.34,<EOF>", 122))














        

#     def test_array(self):
#         self.assertTrue(TestLexer.test("Array(1,2,3,4)", "Array,(,1,,,2,,,3,,,4,),<EOF>", 124))

#     def test_if_else_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             If (a > b) {Return a;}
#             Elseif (a == b) {a = a + b;}
#             Else {Return b;}
#             """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 125))

#     def test_for_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($x In 1 .. 100 By 1) {
#                 sum = sum + a[$x];
#             }
#             """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 126))
    
#     def test_for_block_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             {
#                 Var r, s: Int; 
#                 r = 2.0; 
#                 Var a, b: Array[Int, 5]; 
#                 s = r * r * Self.myPI; 
#                 a[0] = s;
#             }
#             """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 127))
   
  
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))

    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
        
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))



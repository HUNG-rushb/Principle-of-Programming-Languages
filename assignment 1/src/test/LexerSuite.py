import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # def test_operators(self):
    #     self.assertTrue(TestLexer.test("+ - * / <= >= = < > && || ==. = ==",
    #     "+,-,*,/,<=,>=,=,<,>,&&,||,==.,=,==,<EOF>", 101))

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

    # def test_float_(self):
    #     self.assertTrue(TestLexer.test(
    #         "12.34e167777 34E-2314690 1E3 12.2 875.3E+6", "12.34e167777,34E-2314690,1E3,12.2,875.3E+6,<EOF>", 115))

    # def test_integer(self):
    #     self.assertTrue(TestLexer.test(
    #         "1_234 34 12_56_234 0189", "1234,34,1256234,01,89,<EOF>", 116))

    # def test_hex_number(self):
    #     self.assertTrue(TestLexer.test("0x1T 0XA100 0x123 0x0000",
    #                     "0x1,T,0XA100,0x123,0x0000,<EOF>", 117))

    # def test_string_2(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #         "a\\nbc"
    #         """, "a\\nbc,<EOF>", 118))

    # def test_hex_number_2(self):
    #     self.assertTrue(TestLexer.test("0xFG 0FAA X123",
    #                     "0xF,G,0,FAA,X123,<EOF>", 119))
    # def test_string_1(self):
    #     self.assertTrue(TestLexer.test("\"abc\\nabcde\"",
    #                     "abc\\nabcde,<EOF>", 120))

    def test_string_3(self):
        self.assertTrue(TestLexer.test("""
            "dfafuwifweij123123ninfwuef wefbmfbo_3249182 '"weufnwGJTTYR32479akfnkjsdf'""
        """, """dfafuwifweij123123ninfwuef wefbmfbo_3249182 "weufnwGJTTYR32479akfnkjsdf",<EOF>""", 121))

    def test_string_4(self):
        self.assertTrue(TestLexer.test("\"\r\r\"", """,<EOF>""", 122))

    def test_block_comment_1(self):
        self.assertTrue(TestLexer.test("""
            ## Testing comment fowifjowfnwio!@#@#$$#%@^@%^&?<>":{{}}({}()}:(){(})}) ##
        """, "<EOF>", 123))

    def test_block_comment_2(self):
        self.assertTrue(TestLexer.test("## ASCWEasdasd !@@#%$#  %lgvkhjk$%^&*(&*~{}[]\;]\p/.,.,<>>) ##", "<EOF>",124))
    
    def test_block_comment_3(self):
        self.assertTrue(TestLexer.test("## # ASCWEasdasd !@@#%$#%$%^&*(&*~{}[]\;]\p/.,.,<>>) # ##", "<EOF>",125))

    def test_hex_number_2(self):
        self.assertTrue(TestLexer.test("0x1A2bFf09", "0x1A2bFf09,<EOF>", 126))

    def test_hex_number_3(self):
        self.assertTrue(TestLexer.test("0x09aFZXY_asd123", "0x09aF,ZXY_asd123,<EOF>", 127))

    def test_keywords(self):
        self.assertTrue(TestLexer.test("""
        Break Continue If Elseif Else Foreach True False Array In Int 
        Float Boolean String Return Null Class Val Var Constructor Destructor New By""", 
        "Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,Null,Class,Val,Var,Constructor,Destructor,New,By,<EOF>", 128))

    def test_float_number_29(self):
        self.assertTrue(TestLexer.test(
        "90000.32482e67234981 3411E-872199 10101E6667213 345.67890000 17756488.30102E+0009 2099. .46578995 .e37777 .47876e12345 49823.e410 45666.e134_23542344 19453.49992_45rwkejrtnjk", 
        "90000.32482e67234981,3411E-872199,10101E6667213,345.67890000,17756488.30102E+0009,2099.,.46578995,.e37777,.47876e12345,49823.e410,45666.e134,_23542344,19453.49992,_45rwkejrtnjk,<EOF>", 129))

    def test_hex_oct_number_30(self):
        self.assertTrue(TestLexer.test("0x23987TABCDEF 0XA100 0x123 0x0000 00123 0346 0895 0345","0x23987,TABCDEF,0XA100,0x123,0x0000,00123,0346,0,895,0345,<EOF>", 130))


    # def test1(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("Var $x, num : Int = 5, 6;","Var,$x,,,num,:,Int,=,5,,,6,;,<EOF>",101))
    # def test2(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("Var $x, num, $y, 9gh : Int = 5, 6, 7;","Var,$x,,,num,,,$y,,,9,gh,:,Int,=,5,,,6,,,7,;,<EOF>",102))
    # def test3(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xaff;","Var,$dec,,,num,:,Int,=,0b0101110,,,0xaff,;,<EOF>",103))
    # def test4(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("Var $dec: Int = -58910;","Var,$dec,:,Int,=,-,58910,;,<EOF>",104))
    # def test5(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("Var $dec: Float = -1.562e-90;","Var,$dec,:,Float,=,-,1.562e-90,;,<EOF>",105))
    # def test6(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"GameDevClub HCMUT\";","GameDevClub HCMUT,;,<EOF>",106))
    # def test7(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"GameDev\\Club HCMUT\";","Illegal Escape In String: GameDev\\C",107))
    # def test8(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("""\"GameDev'"lub '"HCMUT\";""","""GameDev"lub "HCMUT,;,<EOF>""",108))
    # def test9(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"GameDev\\tlub \\tHCMUT\";","GameDev\\tlub \\tHCMUT,;,<EOF>",109))
    # def test10(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"GameDev\\blub \\bHCMUT\";","GameDev\\blub \\bHCMUT,;,<EOF>",110))
    # def test11(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"GameDev\\dlub \\dHCMUT\";","Illegal Escape In String: GameDev\\d",111))
    # def test12(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"GameDev\\nlub \\nHCMUT\";","""GameDev\\nlub \\nHCMUT,;,<EOF>""",112))
    # def test13(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"GameDevClub HCMUT\\t;","Unclosed String: GameDevClub HCMUT\\t;",113))
    # def test14(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("a[6] = 6;","a,[,6,],=,6,;,<EOF>",114))
    # def test15(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("Var $arr : Array[Int, 5] = Array(1, 5, 6);","Var,$arr,:,Array,[,Int,,,5,],=,Array,(,1,,,5,,,6,),;,<EOF>",115))
    # def test16(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("Var $arr : Array[Array[Int, 6], 5];","Var,$arr,:,Array,[,Array,[,Int,,,6,],,,5,],;,<EOF>",116))
    # def test17(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("""Var $arr : Array[Array[Int, 3], 3] = 
    #                                    Array(
    #                                        Array(1,2,5),
    #                                        Array(2,5,6),
    #                                        Array(5,8,7)
    #                                        );""","Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,<EOF>",117))
    # def test18(self):
    #     self.assertTrue(TestLexer.test("_", "_,<EOF>", 118))
    # def test19(self):
    #     self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 119))
    # def test20(self):
    #     self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 120))
    # def test21(self):
    #     self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 121))
    # def test22(self):
    #     self.assertTrue(TestLexer.test("123a##123##", "123,a,<EOF>", 122))
    # def test23(self):
    #     self.assertTrue(TestLexer.test("_av45", "_av45,<EOF>", 123))
    # def test24(self):
    #     self.assertTrue(TestLexer.test("$_free", "$_free,<EOF>", 124))
    # def test25(self):
    #     self.assertTrue(TestLexer.test("$saf afte", "$saf,afte,<EOF>", 125)) 
    # def test26(self):
    #     self.assertTrue(TestLexer.test("_12343_my const", "_12343_my,const,<EOF>", 126))
    # def test27(self):
    #     self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 127))
    # def test28(self):
    #     self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 128))
    # def test29(self):
    #     self.assertTrue(TestLexer.test("%eHello", "%,eHello,<EOF>", 129))
    # def test30(self):
    #     self.assertTrue(TestLexer.test("*abcd", "*,abcd,<EOF>", 130))
    # def test31(self):
    #     self.assertTrue(TestLexer.test("$", "Error Token $", 131))
    # def test32(self):
    #     self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xaff", "Var,$dec,,,num,:,Int,=,0b0101110,,,0xaff,<EOF>", 132))
    # def test33(self):
    #     self.assertTrue(TestLexer.test("12.45e67", "12.45e67,<EOF>", 133))
    # def test34(self):
    #     self.assertTrue(TestLexer.test("0x1T", "0x1,T,<EOF>", 134))
    # def test35(self):
    #     self.assertTrue(TestLexer.test("\"aj\\elhadef\"", "Illegal Escape In String: aj\\e", 135)) 
    # def test36(self):
    #     self.assertTrue(TestLexer.test("\"ab3j\\tlhadef\"", "ab3j\\tlhadef,<EOF>", 136))  
    # def test37(self):
    #     self.assertTrue(TestLexer.test("""
    #         "Hello from '"Python'""
    #     """, """Hello from "Python",<EOF>""", 137))  
    # def test38(self):
    #     self.assertTrue(TestLexer.test("\"abc \\r babc", """Unclosed String: abc \\r babc""", 138))
    # def test39(self):
    #     self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9", "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 139))
    # def test40(self):
    #     self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34", "34,<,9,+,12e3,-,1.34,<EOF>", 140))
    # def test41(self):
    #     self.assertTrue(TestLexer.test("""
    #         ## This is comment ##
    #     """, "<EOF>", 141))
    # def test42(self):
    #     self.assertTrue(TestLexer.test("Array(1,2,3,4)", "Array,(,1,,,2,,,3,,,4,),<EOF>", 142))
    # def test43(self):
    #     self.assertTrue(TestLexer.test("""
    #         If (a > b) {Return a;}
    #         Elseif (a == b) {a = a + b;}
    #         Else {Return b;}
    #         """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 143))
    # def test44(self):
    #     self.assertTrue(TestLexer.test("""
    #         Foreach ($x In 1 .. 100 By 1) {
    #             sum = sum + a[$x];
    #         }
    #         """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 144))
    # def test45(self):
    #     self.assertTrue(TestLexer.test("""
    #         {
    #             Var r, s: Int; 
    #             r = 2.0; 
    #             Var a, b: Array[Int, 5]; 
    #             s = r * r * Self.myPI; 
    #             a[0] = s;
    #         }
    #         """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 145))
    # def test46(self):
    #     self.assertTrue(TestLexer.test("\"##This is a string, not a comment##\"", "##This is a string, not a comment##,<EOF>", 146))
    # def test47(self):
    #     self.assertTrue(TestLexer.test("\"Son Tung MTP", "Unclosed String: Son Tung MTP", 147))
    # def test48(self):
    #     self.assertTrue(TestLexer.test("e12hcbdge", "e12hcbdge,<EOF>", 148))
    # def test49(self):
    #     self.assertTrue(TestLexer.test("Val $arrayList : Array[String, 6] = Array(\"ABC\",\"DEF\",\"GHI\",\"JKL\",\"MNO\",\"PQR\");", "Val,$arrayList,:,Array,[,String,,,6,],=,Array,(,ABC,,,DEF,,,GHI,,,JKL,,,MNO,,,PQR,),;,<EOF>", 149))
    # def test50(self):
    #     self.assertTrue(TestLexer.test("""
    #         Foreach ($i In 1 .. 100 By 1) {
    #             e = e + $i;
    #             k[$i] = k[$i + 1];
    #             Foreach ($j In 1 .. 100 By 1) {
    #                 e = e - $j;
    #                 l[$i] = l[$j] + e; 
    #             }
    #         }
    #         """, "Foreach,(,$i,In,1,..,100,By,1,),{,e,=,e,+,$i,;,k,[,$i,],=,k,[,$i,+,1,],;,Foreach,(,$j,In,1,..,100,By,1,),{,e,=,e,-,$j,;,l,[,$i,],=,l,[,$j,],+,e,;,},},<EOF>", 150))
    # def test51(self):
    #     self.assertTrue(TestLexer.test("Var $randNum : Int = 1_564_781_1235;", "Var,$randNum,:,Int,=,15647811235,;,<EOF>", 151))
    # def test52(self):
    #     self.assertTrue(TestLexer.test("Val myString : String = \"abce\\t456\";", "Val,myString,:,String,=,abce\\t456,;,<EOF>", 152))
    # def test53(self):
    #     self.assertTrue(TestLexer.test("Var henry, sofia, lucy, lina : Int = 0b01101, 0Xabcd5, 0562, 1254_3;", "Var,henry,,,sofia,,,lucy,,,lina,:,Int,=,0b01101,,,0Xabcd5,,,0562,,,12543,;,<EOF>", 153))
    # def test54(self):
    #     self.assertTrue(TestLexer.test("Var s : String = \"ABC", "Var,s,:,String,=,Unclosed String: ABC", 154))
    # def test55(self):
    #     self.assertTrue(TestLexer.test("""Var s : String = \"adsfsdf\\das\"""", "Var,s,:,String,=,Illegal Escape In String: adsfsdf\\d", 155))
    # def test56(self):
    #     self.assertTrue(TestLexer.test("\"It\\'s me\"", "It\\'s me,<EOF>", 156))
    # def test57(self):
    #     self.assertTrue(TestLexer.test("\"Faker!!! What was that !!!\"", "Faker!!! What was that !!!,<EOF>", 157))
    # def test58(self):
    #     self.assertTrue(TestLexer.test("Var s : String = \"adsfsdfas\"", "Var,s,:,String,=,adsfsdfas,<EOF>", 158))
    # def test59(self):
    #     self.assertTrue(TestLexer.test("Var a : Int;", "Var,a,:,Int,;,<EOF>", 159))
    # def test60(self):
    #     self.assertTrue(TestLexer.test("""
    #                                    4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
    #                                    ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>", 160))
    # def test61(self):
    #     self.assertTrue(TestLexer.test("\"xin\\r\\b\\f\\tchao\"","""xin\\r\\b\\f\\tchao,<EOF>""", 161))
    # def test62(self):
    #     self.assertTrue(TestLexer.test("""\"0.1anc\\'cv" 0.mne "12\\\\3\"""", """0.1anc\\'cv,0.,mne,12\\\\3,<EOF>""", 162))
    # def test63(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1_25_6.5;", "Var,$a,:,Float,=,1256.5,;,<EOF>", 163))
    # def test64(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1_25_6.005;", "Var,$a,:,Float,=,1256.005,;,<EOF>", 164))
    # def test65(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1_25_6.005e12_3;", "Var,$a,:,Float,=,1256.005e123,;,<EOF>", 165))
    # def test66(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 0.2_3_4_5;", "Var,$a,:,Float,=,0.2345,;,<EOF>", 166))
    # def test67(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1e-12_5;", "Var,$a,:,Float,=,1e-125,;,<EOF>", 167))
    # def test68(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1e+12_5;", "Var,$a,:,Float,=,1e+125,;,<EOF>", 168))
    # def test69(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1.560000000000000e-12_5;", "Var,$a,:,Float,=,1.560000000000000e-125,;,<EOF>", 169))
    # def test70(self):
    #     self.assertTrue(TestLexer.test("Var $b : Int = 0b1_0101_110_1_1_0;", "Var,$b,:,Int,=,0b10101110110,;,<EOF>", 170))
    # def test71(self):
    #     self.assertTrue(TestLexer.test("Var $a : Int = 0x45_Abc_df_89_a;", "Var,$a,:,Int,=,0x45Abcdf89a,;,<EOF>", 171))
    # def test72(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1.000000;", "Var,$a,:,Float,=,1.000000,;,<EOF>", 172))
    # def test73(self):
    #     self.assertTrue(TestLexer.test("Var $a : Float = 1.0000001;", "Var,$a,:,Float,=,1.0000001,;,<EOF>", 173))
    # def test74(self):
    #     self.assertTrue(TestLexer.test("(*nac*)+1.1 \"ba\\qm\\f\"", "(,*,nac,*,),+,1.1,Illegal Escape In String: ba\\q", 174))
    # def test75(self):
    #     self.assertTrue(TestLexer.test("NmkobYn{!}+I1+\"`YS2h.J(", "NmkobYn,{,!,},+,I1,+,Unclosed String: `YS2h.J(", 175))
    # def test76(self):
    #     self.assertTrue(TestLexer.test("\"acms!,lds \" {\"abc\"} 123\"abc", """acms!,lds ,{,abc,},123,Unclosed String: abc""", 176))
    # def test77(self):
    #     self.assertTrue(TestLexer.test("""38n"[#Ffs?0ED"0."T`#""", "38,n,[#Ffs?0ED,0.,Unclosed String: T`#", 177))
    # def test78(self):
    #     self.assertTrue(TestLexer.test("\"abc\\tabc\"", "abc\\tabc,<EOF>", 178))
    # def test79(self):
    #     self.assertTrue(TestLexer.test("""\"ab\\rc\\nd\\be\\fadb\\r\"""","""ab\\rc\\nd\\be\\fadb\\r,<EOF>""", 179))
    # def test80(self):
    #     self.assertTrue(TestLexer.test("""\"ahi\"hi\"""", "ahi,hi,Unclosed String: ", 180))
    # def test81(self):
    #     self.assertTrue(TestLexer.test("\"Look at the cleanse, look at the moves! Faker! What was that?!!\"", "Look at the cleanse, look at the moves! Faker! What was that?!!,<EOF>", 181))
    # def test82(self):
    #     self.assertTrue(TestLexer.test("\"Thang 1 cua anh\"", "Thang 1 cua anh,<EOF>", 182))
    # def test83(self):
    #     self.assertTrue(TestLexer.test("\"Thang 2 cua anh\"", "Thang 2 cua anh,<EOF>", 183))
    # def test84(self):
    #     self.assertTrue(TestLexer.test("\"Thang 3 cua anh\"", "Thang 3 cua anh,<EOF>", 184))
    # def test85(self):
    #     self.assertTrue(TestLexer.test("\"Thang 4 cua anh\"", "Thang 4 cua anh,<EOF>", 185))
    # def test86(self):
    #     self.assertTrue(TestLexer.test("\"Thang 5 cua anh\"", "Thang 5 cua anh,<EOF>", 186))
    # def test87(self):
    #     self.assertTrue(TestLexer.test("\"Thang 6 cua anh\"", "Thang 6 cua anh,<EOF>", 187))
    # def test88(self):
    #     self.assertTrue(TestLexer.test("\"Thang 7 cua anh, em va co don\"", "Thang 7 cua anh, em va co don,<EOF>", 188))
    # def test89(self):
    #     self.assertTrue(TestLexer.test("\"Thang 8 cua anh\"", "Thang 8 cua anh,<EOF>", 189))
    # def test90(self):
    #     self.assertTrue(TestLexer.test("\"Thang 9 cua anh\"", "Thang 9 cua anh,<EOF>", 190))
    # def test91(self):
    #     self.assertTrue(TestLexer.test("\"Thang 10 cua anh\"", "Thang 10 cua anh,<EOF>", 191))
    # def test92(self):
    #     self.assertTrue(TestLexer.test("\"Thang 11 cua anh\"", "Thang 11 cua anh,<EOF>", 192))
    # def test93(self):
    #     self.assertTrue(TestLexer.test("\"Thang 12 cua anh\"", "Thang 12 cua anh,<EOF>", 193))
    # def test94(self):
    #     self.assertTrue(TestLexer.test("\"7 cuoc goi nho\"", "7 cuoc goi nho,<EOF>", 194))
    # def test95(self):
    #     self.assertTrue(TestLexer.test("""
    #                                    "W-n '"3107'" full album"
    #                                    """, "W-n \"3107\" full album,<EOF>", 195))
    # def test96(self):
    #     self.assertTrue(TestLexer.test("\"Den bao gio moi co the quen di nhung cau chuyen ma ta da trao, den bao gio moi co the yeu mot nguoi den sau\"", "Den bao gio moi co the quen di nhung cau chuyen ma ta da trao, den bao gio moi co the yeu mot nguoi den sau,<EOF>", 196))
    # def test97(self):
    #     self.assertTrue(TestLexer.test("\"Den bao gio moi co the quen di nhung ky niem ma ta da qua, va neu hom nay la ngay, ma chung ta da roi xa, chi can ai do canh ben dung lai va niu lay em chi mot phut giay\"", "Den bao gio moi co the quen di nhung ky niem ma ta da qua, va neu hom nay la ngay, ma chung ta da roi xa, chi can ai do canh ben dung lai va niu lay em chi mot phut giay,<EOF>", 197))
    # def test98(self):
    #     self.assertTrue(TestLexer.test("\"La vi yeu em nen anh mac sai lam\"", "La vi yeu em nen anh mac sai lam,<EOF>", 198))
    # def test99(self):
    #     self.assertTrue(TestLexer.test("\"Samsung Galaxy A50 voi 5 camera macro chup can canh, dem lai trai nghiem thuc te cho nguoi dung\"", "Samsung Galaxy A50 voi 5 camera macro chup can canh, dem lai trai nghiem thuc te cho nguoi dung,<EOF>", 199))
    # def test100(self):
    #     self.assertTrue(TestLexer.test("\"Khong lam ma doi co an, thi chi co an dau b***, an c** - Huan Rose\"", "Khong lam ma doi co an, thi chi co an dau b***, an c** - Huan Rose,<EOF>", 200))
        

    

    def test_hex_oct_number(self):
        self.assertTrue(TestLexer.test("0x1T 0XA100 0x123 0x0000 00123 0346 0895 0345","0x1,T,0XA100,0x123,0x0000,00123,0346,0,895,0345,<EOF>", 110))
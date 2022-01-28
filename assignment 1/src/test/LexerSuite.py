# Trịnh Duy Hưng
# 1913652

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # def test_1(self):
    #     self.assertTrue(TestLexer.test("+ - * / <= >= = < > && || ==. = ==",
    #     "+,-,*,/,<=,>=,=,<,>,&&,||,==.,=,==,<EOF>", 101))

    # def test_2(self):
    #     self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    # def test_3(self):
    #     self.assertTrue(TestLexer.test("23427b5", "23427,b5,<EOF>", 103))

    # def test_4(self):
    #     self.assertTrue(TestLexer.test("_duyhung135", "_duyhung135,<EOF>", 104))

    # def test_5(self):
    #     self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 105))

    # def test_6(self):
    #     self.assertTrue(TestLexer.test("$_dollarstatic", "$_dollarstatic,<EOF>", 106))

    # def test_7(self):
    #     self.assertTrue(TestLexer.test("   $duy     hung", "$duy,hung,<EOF>", 107))

    # def test_8(self):
    #     self.assertTrue(TestLexer.test("_12343_my const", "_12343_my,const,<EOF>", 108))

    # def test_9(self):
    #     self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 109))

    # def test_10(self):
    #     self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 110))

    # def test_11(self):
    #     self.assertTrue(TestLexer.test("%duyHUNG", "%,duyHUNG,<EOF>", 111))

    # def test_12(self):
    #     self.assertTrue(TestLexer.test("* + hung      /   ", "*,+,hung,/,<EOF>", 112))

    # def test_13(self):
    #     self.assertTrue(TestLexer.test("$", "Error Token $", 113))

    # def test_14(self):
    #     self.assertTrue(TestLexer.test("Val $_fajfaksd_ASDFADS213134Asdvas, num____fasdfh__2136512_____dafds: Int = 0b0101110010101010100011111, 0xAFFabcdefABCDEF",
    #                     "Val,$_fajfaksd_ASDFADS213134Asdvas,,,num____fasdfh__2136512_____dafds,:,Int,=,0b0,101110010101010100011111,,,0xAFFabcdefABCDEF,<EOF>", 114))

    # def test_15(self):
    #     self.assertTrue(TestLexer.test(
    #         "18_8_128_2.364872364245e67 10002322E-97381237 232431E01023473 134422.787902 178434554357.4947563E+343256669 24346436. .452345 .e123133 .7674e99995 41239778.e23124410 4587467.e213400001_232342354 17635235_89996_111154_9.49324_888845484926e3 43351_2000098898934.3_777456342356", 
    #         "18_8_128_2.364872364245e67,10002322E-97381237,232431E01023473,134422.787902,178434554357.4947563E+343256669,24346436.,.,452345,.e123133,.7674e99995,41239778.e23124410,45.87467e121340000,_232342354,17635235_89996_111154_9.49324,_888845484926e3,433512000098898934.3,_777456342356,<EOF>", 115))

    # def test_16(self):
    #     self.assertTrue(TestLexer.test(
    #         "1_2_3_4321479326523469234 39237247362177374 12039434778957392_5_6_2_3_4 01812374738946466", "1234321479326523469234,39237247362177374,1203943477895739256234,01,812374738946466,<EOF>", 116))

    # def test_17(self):
    #     self.assertTrue(TestLexer.test("""
    #     ## LoreamsdASDFOWFWJEFJ3129834329adasfdksfsdksdljfs
    #     """, "Error Token #", 117))

    # def test_18(self):   
    #     self.assertTrue(TestLexer.test("""
    #     ##
    #     asdajfsk767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFdjfwqwqlqdk
    #     ##
    #     DSAFWEFWEFOIWEWsdafbawuefygweu_______________________3214932842346935436971346912736
    #     ##df767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFkss
    #     ###sf767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFdjsls
    #     ##
    #     """, "DSAFWEFWEFOIWEWsdafbawuefygweu_______________________3214932842346935436971346912736,Error Token #", 118))

    # def test_19(self):
    #     self.assertTrue(TestLexer.test("\"34gegefaafwdfwogg\\mafwfweghterwd5768o\"","Illegal Escape In String: 34gegefaafwdfwogg\\m",119))

    # def test_20(self):
    #     self.assertTrue(TestLexer.test("$FSDGM834738____sadfidufuhabc 123476761abnvdsjjsdnMMMMASDZZZ_sdjdv _16855555423 dfwedwfwePPIHDWU3536dtehiiiiiiiiiiiif",
    #                     "$FSDGM834738____sadfidufuhabc,123476761,abnvdsjjsdnMMMMASDZZZ_sdjdv,_16855555423,dfwedwfwePPIHDWU3536dtehiiiiiiiiiiiif,<EOF>", 120))

    # def test_21(self):
    #     self.assertTrue(TestLexer.test("""
    #         "fwoieijwofjndanfDAFKWEOWJEGWG '"fjdsdsaklfjsaldkPPWHDNJNjnewwjnccedefg'""
    #     """, """fwoieijwofjndanfDAFKWEOWJEGWG '"fjdsdsaklfjsaldkPPWHDNJNjnewwjnccedefg'",<EOF>""", 121))

    # def test_22(self):
    #     self.assertTrue(TestLexer.test("19789rthtrh \"wefwegxwgergyffwfewewz\k 456","19789,rthtrh,Illegal Escape In String: wefwegxwgergyffwfewewz\k",122))

    # def test_23(self):
    #     self.assertTrue(TestLexer.test("""
    #         ## Testing comment fowifjowfnwio!@#@#$$#%@^@%^&?<>":{{}}({}()}:(){(})}) ##
    #     """, "<EOF>", 123))

    # def test_24(self):
    #     self.assertTrue(TestLexer.test("## ASCWEasdasd !@@#%$#  %lgvkhjk$%^&*(&*~{}[]\;]\p/.,.,<>>) ##", "<EOF>",124))
    
    # def test_25(self):
    #     self.assertTrue(TestLexer.test("## # ASCWEasdasd !@@#%$#%$%^&*(&*~{}[]\;]\p/.,.,<>>) # ##", "<EOF>",125))

    # def test_26(self):
    #     self.assertTrue(TestLexer.test("Array(18983423,4000003023003032,352546546,9191993941294983248)",
    #                 "Array,(,18983423,,,4000003023003032,,,352546546,,,9191993941294983248,),<EOF>", 126))

    # def test_27(self):
    #     self.assertTrue(TestLexer.test("""
    #         If (a123555 > B______123213) {Return a_63475_IIIIIIIIII;}
    #         Elseif (c99999 == d0000007) {hunghunga = duydydtdda + opopopopopopb;}
    #         Else {Return ppppppppppppppppppppppppppppppppp;}
    #         """, "If,(,a123555,>,B______123213,),{,Return,a_63475_IIIIIIIIII,;,},Elseif,(,c99999,==,d0000007,),{,hunghunga,=,duydydtdda,+,opopopopopopb,;,},Else,{,Return,ppppppppppppppppppppppppppppppppp,;,},<EOF>", 127))

    # def test_28(self):
    #     self.assertTrue(TestLexer.test("""
    #         Foreach ($l_LLLLLLLLLLLLLL In 19 .. 100234 By 191) {
    #             saloaloaloalaolaooo = saloaloaloalaolaooo + iiiuiuiuiuiuiu[$mn_______________7436fhhf];
    #         }
    #         """, "Foreach,(,$l_LLLLLLLLLLLLLL,In,19,..,100234,By,191,),{,saloaloaloalaolaooo,=,saloaloaloalaolaooo,+,iiiuiuiuiuiuiu,[,$mn_______________7436fhhf,],;,},<EOF>", 128))

    # def test_29(self):
    #     self.assertTrue(TestLexer.test("""
    #         {
    #             Var jijijijijdaf, ijijijji: Int;
    #             pkpsdfkpfasdf = 2_4546_898432.0123146;
    #             Val a7654334, b7654334: Array[String, 987798798];
    #             tutyuytus = pkpsdfkpfasdf * pkpsdfkpfasdf * Self.nidsidf;
    #             uasdfhhhhhhhha[192837] = ppppppp;
    #         }
    #         """, "{,Var,jijijijijdaf,,,ijijijji,:,Int,;,pkpsdfkpfasdf,=,24546898432.0123146,;,Val,a7654334,,,b7654334,:,Array,[,String,,,987798798,],;,tutyuytus,=,pkpsdfkpfasdf,*,pkpsdfkpfasdf,*,Self,.,nidsidf,;,uasdfhhhhhhhha,[,192837,],=,ppppppp,;,},<EOF>", 129))

    # def test_30(self):
    #     self.assertTrue(TestLexer.test("""
    #         Var $arjijijijijdaf : Array[Array[Boolean, 3], 3] = Array(
    #                                                     Array(199,987798798,7565),
    #                                                     Array(346723439,87765,1236),
    #                                                     Array(9000000005,1348,9632847)
    #                                                     );
    #         )""", "Var,$arjijijijijdaf,:,Array,[,Array,[,Boolean,,,3,],,,3,],=,Array,(,Array,(,199,,,987798798,,,7565,),,,Array,(,346723439,,,87765,,,1236,),,,Array,(,9000000005,,,1348,,,9632847,),),;,),<EOF>", 130))

    # def test_37(self):
    #     self.assertTrue(TestLexer.test("""anitrinhduyhungmal.canguyenthachngocquynht.talfuckk(cpluspus + "fio___adfshuf___sefoooobc");""",
    #                                     """anitrinhduyhungmal,.,canguyenthachngocquynht,.,talfuckk,(,cpluspus,+,fio___adfshuf___sefoooobc,),;,<EOF>""",137))
    
    # def test_32(self):
    #         self.assertTrue(TestLexer.test("""
    #                 0b111111111987 0B09998888 67.9898454600003443 34577777 0X2D3abcFfFfDdddDDD
    #                 """, "0b111111111,987,0B0,9998888,67.9898454600003443,34577777,0X2D3abcFfFfDdddDDD,<EOF>", 132))

    # def test_33(self):
    #     self.assertTrue(TestLexer.test("""
    #             New Return True False Foreach If Elseif Else Float Int String Var Val Constructor Destructor Null Class By In
    #             """, "New,Return,True,False,Foreach,If,Elseif,Else,Float,Int,String,Var,Val,Constructor,Destructor,Null,Class,By,In,<EOF>", 133))

    # def test_34(self):
    #     self.assertTrue(TestLexer.test("""
    #             + - * / % == != ! > < >= <= || && . :: ( ) { } [ ] ==. +.
    #             """, "+,-,*,/,%,==,!=,!,>,<,>=,<=,||,&&,.,::,(,),{,},[,],==.,+.,<EOF>", 134))

    # def test_35(self):
    #     self.assertTrue(TestLexer.test("\"duyhungduyhung\"ngocquynhngocquynh\"",
    #     "duyhungduyhung,ngocquynhngocquynh,Unclosed String: ",135))
    
    # def test_36(self):
    #     self.assertTrue(TestLexer.test("\"jkqajkajqka\\njkqajkajqka\"","jkqajkajqka\\njkqajkajqka,<EOF>",136))

    # def test_37(self):
    #     self.assertTrue(TestLexer.test("\"abhunghung\\thunghung\\nbhunghung\"","abhunghung\\thunghung\\nbhunghung,<EOF>",137))

    # def test_38(self):
    #     self.assertTrue(TestLexer.test("Return triangle.getCurriculum(1010304 false true + * - 8988) - (new object()).arrayer[8444];",
    #     "Return,triangle,.,getCurriculum,(,1010304,false,true,+,*,-,8988,),-,(,new,object,(,),),.,arrayer,[,8444,],;,<EOF>",138))

    # def test_39(self):
    #     self.assertTrue(TestLexer.test("""
    #     "7777.645656454235dfdsgjsidfgji888888...98f834jfjfnnvnvnnv\'trinhduyhung" 8956854.nguyenthachngocquynh "878736636\\\\0b10010101111111111"
    #     ""","7777.645656454235dfdsgjsidfgji888888...98f834jfjfnnvnvnnv'trinhduyhung,8956854.,nguyenthachngocquynh,878736636\\\\0b10010101111111111,<EOF>",139))

    # def test_40(self):
    #     self.assertTrue(TestLexer.test("Trinh_Duy_Hung_fdfijf \"trinhduyhung1!!@#$@%%%%*&*&*&*&*&@#$@$#@$%^i\\n\" 555555555555jijijijiyz",
    #                                     "Trinh_Duy_Hung_fdfijf,trinhduyhung1!!@#$@%%%%*&*&*&*&*&@#$@$#@$%^i\\n,555555555555,jijijijiyz,<EOF>",140))

    # def test_41(self):
    #     self.assertTrue(TestLexer.test("\"!h$5FBi6qwddasd\"_nguyenthachngocquynhq\"!SZRhungquynh,H}\"sI666677fpw",
    #                                         "!h$5FBi6qwddasd,_nguyenthachngocquynhq,!SZRhungquynh,H},sI666677fpw,<EOF>",141))
        
    # def test_42(self):
    #     self.assertTrue(TestLexer.test("""
    #     uwufhweuf4"&uwufhweufJ^1uwufhweufa_." QuwufhweufGn"?6uwufhweuf7Sp"{,}6Asz"Yx]("
    #     ""","uwufhweuf4,&uwufhweufJ^1uwufhweufa_.,QuwufhweufGn,?6uwufhweuf7Sp,{,,,},6,Asz,Yx](,<EOF>",142))

    # def test_43(self):
    #     self.assertTrue(TestLexer.test("0ff234f23f2f1_\"^VzxvLRfffffuuu@\\\\OushungquynhM;\"uGquynhhungM+jfffasdE",
    #                                     "0,ff234f23f2f1_,^VzxvLRfffffuuu@\\\\OushungquynhM;,uGquynhhungM,+,jfffasdE,<EOF>",143))


    # def test_44(self):
    #     self.assertTrue(TestLexer.test("\"(trinhduyhungItrinhduyhungFtrinhduyhungq+trinhduyhunglq(\"trinhduyhungIhKtrinhduyhung6we(*.*)GdvS{(}",
    #                                     "(trinhduyhungItrinhduyhungFtrinhduyhungq+trinhduyhunglq(,trinhduyhungIhKtrinhduyhung6we,(,*,.,*,),GdvS,{,(,},<EOF>",144))

    # def test_45(self):
    #     self.assertTrue(TestLexer.test("\"btrinhduyhungac\\mtrinhduyhunga\"","Illegal Escape In String: btrinhduyhungac\\m",145))

    # def test_46(self):
    #     self.assertTrue(TestLexer.test("\"btrinhduyhungatrinhduyhungMD\\HtrinhduyhungLtrinhduyhungSc\\ntrinhduyhungatrinhduyhung\"","Illegal Escape In String: btrinhduyhungatrinhduyhungMD\\H",146))

    # def test_47(self):
    #     self.assertTrue(TestLexer.test("\",dtrinhduyhungls\\Ftrinhduyhung1trinhduyhung2trinhduyhung!trinhduyhungLtrinhduyhungS\\ktrinhduyhungctrinhduyhung\\trinhduyhungnatrinhduyhung\"","Illegal Escape In String: ,dtrinhduyhungls\\F",147))

    # def test_48(self):
    #     self.assertTrue(TestLexer.test("\"atrinhduyhungdo\\madotrinhduyhung\"","Illegal Escape In String: atrinhduyhungdo\\m",148))

    # def test_49(self):
    #     self.assertTrue(TestLexer.test("78799923trinhduyhungnguyenthachngocquynhabc \"xtrinhduyhungytrinhduyhungz\k 456",
    #                                 "78799923,trinhduyhungnguyenthachngocquynhabc,Illegal Escape In String: xtrinhduyhungytrinhduyhungz\k",149))

    # def test_50(self):
    #     self.assertTrue(TestLexer.test("\"nguyenthachngocquynhanguyenthachngocquynha\wb\"","Illegal Escape In String: nguyenthachngocquynhanguyenthachngocquynha\w",150))

    # def test_51(self):
    #     self.assertTrue(TestLexer.test("bnguyenthachngocquynha+1786544332+\"nnguyenthachngocquynha\"\"mnguyenthachngocquynhd+119238219.2-401203040468\lb",
    #                                     "bnguyenthachngocquynha,+,1786544332,+,nnguyenthachngocquynha,Illegal Escape In String: mnguyenthachngocquynhd+119238219.2-401203040468\l",151))

    # def test_52(self):
    #     self.assertTrue(TestLexer.test("\"1.744462+1.744463+1.744464\\o'\"123","Illegal Escape In String: 1.744462+1.744463+1.744464\\o",152))

    # def test_53(self):
    #     self.assertTrue(TestLexer.test("(*nangocquynhdethuongc*)/2232881.73181231 \"bcuoingocquynha\\qm\f\"",
    #                                     "(,*,nangocquynhdethuongc,*,),/,2232881.73181231,Illegal Escape In String: bcuoingocquynha\q",153))

    # def test_54(self):
    #     self.assertTrue(TestLexer.test("\"congocquynhdangyeuncahngocquynhdangyeueo\\uabc","Illegal Escape In String: congocquynhdangyeuncahngocquynhdangyeueo\\u",154))

    # def test_55(self):
    #     self.assertTrue(TestLexer.test("\"trinhduyhungbatrinhduyhungcxytrinhduyhungc",
    #                                         "Unclosed String: trinhduyhungbatrinhduyhungcxytrinhduyhungc",155))

    # def test_56(self):
    #     self.assertTrue(TestLexer.test("NngocquynhsexymkngocquynhsexyobYngocquynhsexyn{!}+I1+\"`YSnewyodjdjdj2h.ueywuJ(",
    #                                         "NngocquynhsexymkngocquynhsexyobYngocquynhsexyn,{,!,},+,I1,+,Unclosed String: `YSnewyodjdjdj2h.ueywuJ(",156))

    # def test_57(self):
    #     self.assertTrue(TestLexer.test("\"abeQuynhbeRotcbeQuynhbeRotnv \" \"ahunghudhdhdbc","abeQuynhbeRotcbeQuynhbeRotnv ,Unclosed String: ahunghudhdhdbc",157))

    # def test_58(self):
    #     self.assertTrue(TestLexer.test("\"bsaunaycuoiQuynhcms!,lds \" {\"gh6473f94f8hhhhfhASDGGGGGGGGGGGGGGGGGc\"} 123\"abeQuynhdethuong7273817361bc",
    #                                     "bsaunaycuoiQuynhcms!,lds ,{,gh6473f94f8hhhhfhASDGGGGGGGGGGGGGGGGGc,},123,Unclosed String: abeQuynhdethuong7273817361bc",158))

    # def test_59(self):
    #     self.assertTrue(TestLexer.test("a+11.23749283470202002+\"masdanfjsdDAviidd_______m.123\" 12 \"%^_)3141927777&",
    #                                     "a,+,11.23749283470202002,+,masdanfjsdDAviidd_______m.123,12,Unclosed String: %^_)3141927777&",159))

    # def test_60(self):
    #     self.assertTrue(TestLexer.test("323344448n\"[#FfQuynhsQuynh?0ED\"1.1\"dddd`#","323344448,n,[#FfQuynhsQuynh?0ED,1.1,Unclosed String: dddd`#",160))

    def test_string_16(self):
        self.assertTrue(TestLexer.test("\"str1  \\r ahihi \"","str1  \\r ahihi ,<EOF>",161))

    def test_unclose_string_7(self):
        self.assertTrue(TestLexer.test("\"He asked me: '\"Where \\t is John?'\"\"","He asked me: \'\"Where \\t is John?\'\",<EOF>",162))
    def test_unclose_string_8(self):
        self.assertTrue(TestLexer.test("\"  str \\\' \\\" str \"","Illegal Escape In String:   str \\' \\\"",163))
        #   str \' \"
    def test_string_17(self):
        self.assertTrue(TestLexer.test("\" \\\\ \\n \\t \\n fddd \\\\\" "," \\\\ \\n \\t \\n fddd \\\\,<EOF>",164))

    def test_21(self):
        self.assertTrue(TestLexer.test("{ 1,2  ,  32,  2}; {1.2,2., 3e8  , 4.0e-1}","{,1,,,2,,,32,,,2,},;,{,1.2,,,2.,,,3e8,,,4.0e-1,},<EOF>",165))
    def test_22(self):
        self.assertTrue(TestLexer.test("{true,false   ,  true, false}; {\" nam\", \" vat ly \"  ,  \" aaa \" }",
        """{,true,,,false,,,true,,,false,},;,{, nam,,, vat ly ,,, aaa ,},<EOF>""",166))

    def test_stmt_1(self):
        self.assertTrue(TestLexer.test("if(a != b)\nthen continuea=a+1;\nelse b=0;","if,(,a,!=,b,),then,continuea,=,a,+,1,;,else,b,=,0,;,<EOF>",167))
    def test_stmt_2(self):
        self.assertTrue(TestLexer.test("return newn then animal(a,b + c);","return,newn,then,animal,(,a,,,b,+,c,),;,<EOF>",168))
    def test_stmt_3(self):
        self.assertTrue(TestLexer.test("callFn then unction(a + b*c % (d+2));","callFn,then,unction,(,a,+,b,*,c,%,(,d,+,2,),),;,<EOF>",169))
    def test_stmt_4(self):
        self.assertTrue(TestLexer.test("""
        a[7+9] = 12;
        Foreach(i = 1 In 1 .. str.length) {
            b[i] = b[i] + 1;
        }
        """,
        "a,[,7,+,9,],=,12,;,Foreach,(,i,=,1,In,1,..,str,.,length,),{,b,[,i,],=,b,[,i,],+,1,;,},<EOF>", 170))










#     def test_compile_error(self):
#         self.assertTrue(TestLexer.test("""
#         "a\nbcvbddds"
#         """, "Unclosed String: a", 97))
#     def test_compile_error_2(self):
#         self.assertTrue(TestLexer.test("""
#         "a
#         cdef"
#         """, "Unclosed String: a", 98))
#     def test111(self):
#         self.assertTrue(TestLexer.test("0b0000001 0x00AFF 0004511","0b0,00,00,01,0x0,0,AFF,00,04511,<EOF>",99))
 
#     def test_identifier_1(self):
#         self.assertTrue(TestLexer.test("_ _123 __abc__", "_,_123,__abc__,<EOF>", 100))

#     def test_identifier_2(self):
#         self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 101))

#     def test_identifier_3(self):
#         self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 102))

#     def test_identifier_4(self):
#         self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 103))

#     def test_identifier_5(self):
#         self.assertTrue(TestLexer.test("_av45", "_av45,<EOF>", 104))

#     def test_identifier_6(self):
#         self.assertTrue(TestLexer.test(""" $_free """, "$_free,<EOF>", 105))

#     def test_identifier_7(self):
#         self.assertTrue(TestLexer.test("$saf afte", "$saf,afte,<EOF>", 106))

#     def test_identifier_8(self):
#         self.assertTrue(TestLexer.test(
#             "_12343_my const", "_12343_my,const,<EOF>", 107))

#     def test_identifier_9(self):
#         self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 108))

#     def test_identifier_10(self):
#         self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 109))

#     def test_identifier_11(self):
#         self.assertTrue(TestLexer.test("%eHello", "%,eHello,<EOF>", 110))

#     def test_identifier_12(self):
#         self.assertTrue(TestLexer.test("*abcd", "*,abcd,<EOF>", 111))

#     def test_identifier_13(self):
#         self.assertTrue(TestLexer.test("$", "Error Token $", 112))

#     def test_identifier_14(self):
#         self.assertTrue(TestLexer.test("$abc 1adv _123 df3df",
#                         "$abc,1,adv,_123,df3df,<EOF>", 113))

#     def test_var_declare(self):
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF",
#                         "Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,<EOF>", 114))

#    
#     def test_string_3(self):
#         self.assertTrue(TestLexer.test("""
#             "Hello from '"Python'""
#         """, """Hello from '"Python'",<EOF>""", 121))

#     def test_string_4(self):
#         self.assertTrue(TestLexer.test("\"\r\"", """
# ,<EOF>""", 122))

#     def test_expression_1(self):
#         self.assertTrue(TestLexer.test("(23 >= 5 && a != 9) || 7 + 9",
#                         "(,23,>=,5,&&,a,!=,9,),||,7,+,9,<EOF>", 123))

#     def test_expression_2(self):
#         self.assertTrue(TestLexer.test("34 < 9 + 12e3 - 1.34",
#                         "34,<,9,+,12e3,-,1.34,<EOF>", 124))

#     def test_comment_3(self):
#         self.assertTrue(TestLexer.test("""
#             ## This is comment ##
#         """, "<EOF>", 125))

#     def test_array(self):
#         self.assertTrue(TestLexer.test("Array(1,2,3,4)",
#                         "Array,(,1,,,2,,,3,,,4,),<EOF>", 126))

#     def test_if_else_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             If (a > b) {Return a;}
#             Elseif (a == b) {a = a + b;}
#             Else {Return b;}
#             """, "If,(,a,>,b,),{,Return,a,;,},Elseif,(,a,==,b,),{,a,=,a,+,b,;,},Else,{,Return,b,;,},<EOF>", 127))

#     def test_for_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($x In 1 .. 100 By 1) {
#                 sum = sum + a[$x];
#             }
#             """, "Foreach,(,$x,In,1,..,100,By,1,),{,sum,=,sum,+,a,[,$x,],;,},<EOF>", 128))

#     def test_for_block_stmt(self):
#         self.assertTrue(TestLexer.test("""
#             {
#                 Var r, s: Int;
#                 r = 2.0;
#                 Var a, b: Array[Int, 5];
#                 s = r * r * Self.myPI;
#                 a[0] = s;
#             }
#             """, "{,Var,r,,,s,:,Int,;,r,=,2.0,;,Var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>", 129))

#     def test_array_2(self):
#         self.assertTrue(TestLexer.test("""
#             Var $arr : Array[Array[Int, 3], 3] = Array(
#                                                         Array(1,2,5),
#                                                         Array(2,5,6),
#                                                         Array(5,8,7)
#                                                         );
#             )""", "Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,),<EOF>", 130))

#     def test_string_5(self):
#         self.assertTrue(TestLexer.test("""
#                 Var s : String = \"adsfsdf\\vas\"
#                 """, "Var,s,:,String,=,Illegal Escape In String: adsfsdf\\v", 131))

#     def test_literal(self):
#             self.assertTrue(TestLexer.test("""
#                     0b12 0b01 12.34 1560 0X1B
#                     """, "0b1,2,0b0,1,12.34,1560,0X1B,<EOF>", 132))

#     def test_keyword(self):
#         self.assertTrue(TestLexer.test("""
#                 New Return True False Foreach If Elseif Else Float Int String Var Val Constructor Destructor Null Class By In
#                 """, "New,Return,True,False,Foreach,If,Elseif,Else,Float,Int,String,Var,Val,Constructor,Destructor,Null,Class,By,In,<EOF>", 133))

#     def test_operator(self):
#         self.assertTrue(TestLexer.test("""
#                 + - * / % == != ! > < >= <= || && . :: ( ) { } [ ] ==. +.
#                 """, "+,-,*,/,%,==,!=,!,>,<,>=,<=,||,&&,.,::,(,),{,},[,],==.,+.,<EOF>", 134))

#     # "ahi"hi"
#     def test_string_6(self):
#         self.assertTrue(TestLexer.test("\"ahi\"hi\"",
#         "ahi,hi,Unclosed String: ",135))
#     # "abc\nabc"
#     def test_string_7(self):
#         self.assertTrue(TestLexer.test("\"abc\\nabc\"","abc\\nabc,<EOF>",136))

#     # "abc\ta\nbc"
#     def test_string_8(self):
#         self.assertTrue(TestLexer.test("\"abc\\ta\\nbc\"","abc\\ta\\nbc,<EOF>",137))

#     def test_string_9(self):
#         self.assertTrue(TestLexer.test("\"abc\" 0 \"12ab\\fc0.1\"","abc,0,12ab\\fc0.1,<EOF>",138))

#     def test_string_10(self):
#         self.assertTrue(TestLexer.test("""
#         "0.1anc\'cv" 0.mne "12\\\\3"
#         ""","0.1anc'cv,0.,mne,12\\\\3,<EOF>",139))

#     def test_string_11(self):
#         self.assertTrue(TestLexer.test("abc \"abc1!!@#$$%^i\\n\" 12yz","abc,abc1!!@#$$%^i\\n,12,yz,<EOF>",140))

#     def test_string_12(self):
#         self.assertTrue(TestLexer.test("\"!h$5FBi6\"_q\"!SZR,H}\"sIfpw","!h$5FBi6,_q,!SZR,H},sIfpw,<EOF>",141))

#     def test_string_13(self):
#         self.assertTrue(TestLexer.test("""
#         4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
#         ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>",142))

#     def test_string_14(self):
#         self.assertTrue(TestLexer.test("0f1_\"^VLR@\\\\OusM;\"uGM+jE","0,f1_,^VLR@\\\\OusM;,uGM,+,jE,<EOF>",143))

#     def test_string_15(self):
#         self.assertTrue(TestLexer.test("\"(IFq+lq(\"IhK6we(*.*)GdvS{(}","(IFq+lq(,IhK6we,(,*,.,*,),GdvS,{,(,},<EOF>",144))

#     def test_illegal_escape_1(self):
#         self.assertTrue(TestLexer.test("\"bac\\ma\"","Illegal Escape In String: bac\\m",145))

#     def test_illegal_escape_2(self):
#         self.assertTrue(TestLexer.test("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",146))

#     def test_illegal_escape_3(self):
#         self.assertTrue(TestLexer.test("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",147))

#     def test_illegal_escape_4(self):
#         self.assertTrue(TestLexer.test("\"ado\\mado\"","Illegal Escape In String: ado\\m",148))

#     def test_illegal_escape_5(self):
#         self.assertTrue(TestLexer.test("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\k",149))

#     def test_illegal_escape_6(self):
#         self.assertTrue(TestLexer.test("\"aa\wb\"","Illegal Escape In String: aa\w",150))

#     def test_illegal_escape_7(self):
#         self.assertTrue(TestLexer.test("ba+12+\"na\"\"md+1.2-468\lb","ba,+,12,+,na,Illegal Escape In String: md+1.2-468\l",151))

#     def test_illegal_escape_8(self):
#         self.assertTrue(TestLexer.test("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",152))

#     def test_illegal_escape_9(self):
#         self.assertTrue(TestLexer.test("(*nac*)+1.1 \"ba\\qm\f\"","(,*,nac,*,),+,1.1,Illegal Escape In String: ba\q",153))

#     def test_illegal_escape_10(self):
#         self.assertTrue(TestLexer.test("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",154))

#     def test_unclose_String_1(self):
#         self.assertTrue(TestLexer.test("\"bacxyc","Unclosed String: bacxyc",155))

#     def test_unclose_String_2(self):
#         self.assertTrue(TestLexer.test("NmkobYn{!}+I1+\"`YS2h.J(","NmkobYn,{,!,},+,I1,+,Unclosed String: `YS2h.J(",156))

#     def test_unclose_String_3(self):
#         self.assertTrue(TestLexer.test("\"acnv \" \"abc","acnv ,Unclosed String: abc",157))

#     def test_unclose_String_4(self):
#         self.assertTrue(TestLexer.test("\"acms!,lds \" {\"abc\"} 123\"abc","acms!,lds ,{,abc,},123,Unclosed String: abc",158))

#     def test_unclose_String_5(self):
#         self.assertTrue(TestLexer.test("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,mam.123,12,Unclosed String: %^&",159))

#     def test_unclose_String_6(self):
#         self.assertTrue(TestLexer.test("38n\"[#Ffs?0ED\"0.\"T`#","38,n,[#Ffs?0ED,0.,Unclosed String: T`#",160))

#     def test_string_16(self):
#         self.assertTrue(TestLexer.test("\"str1  \\r ahihi \"","str1  \\r ahihi ,<EOF>",161))

#     def test_unclose_string_7(self):
#         self.assertTrue(TestLexer.test("\"He asked me: '\"Where \\t is John?'\"\"","He asked me: \'\"Where \\t is John?\'\",<EOF>",162))
#     def test_unclose_string_8(self):
#         self.assertTrue(TestLexer.test("\"  str \\\' \\\" str \"","Illegal Escape In String:   str \\' \\\"",163))
#         #   str \' \"
#     def test_string_17(self):
#         self.assertTrue(TestLexer.test("\" \\\\ \\n \\t \\n fddd \\\\\" "," \\\\ \\n \\t \\n fddd \\\\,<EOF>",164))

#     def test_21(self):
#         self.assertTrue(TestLexer.test("{ 1,2  ,  32,  2}; {1.2,2., 3e8  , 4.0e-1}","{,1,,,2,,,32,,,2,},;,{,1.2,,,2.,,,3e8,,,4.0e-1,},<EOF>",165))
#     def test_22(self):
#         self.assertTrue(TestLexer.test("{true,false   ,  true, false}; {\" nam\", \" vat ly \"  ,  \" aaa \" }",
#         """{,true,,,false,,,true,,,false,},;,{, nam,,, vat ly ,,, aaa ,},<EOF>""",166))

#     def test_stmt_1(self):
#         self.assertTrue(TestLexer.test("if(a != b)\nthen continuea=a+1;\nelse b=0;","if,(,a,!=,b,),then,continuea,=,a,+,1,;,else,b,=,0,;,<EOF>",167))
#     def test_stmt_2(self):
#         self.assertTrue(TestLexer.test("return newn then animal(a,b + c);","return,newn,then,animal,(,a,,,b,+,c,),;,<EOF>",168))
#     def test_stmt_3(self):
#         self.assertTrue(TestLexer.test("callFn then unction(a + b*c % (d+2));","callFn,then,unction,(,a,+,b,*,c,%,(,d,+,2,),),;,<EOF>",169))
#     def test_stmt_4(self):
#         self.assertTrue(TestLexer.test("""
#         a[7+9] = 12;
#         Foreach(i = 1 In 1 .. str.length) {
#             b[i] = b[i] + 1;
#         }
#         """,
#         "a,[,7,+,9,],=,12,;,Foreach,(,i,=,1,In,1,..,str,.,length,),{,b,[,i,],=,b,[,i,],+,1,;,},<EOF>", 170))

#     def test_stmt_5(self):
#         self.assertTrue(TestLexer.test("""
#         a = 1;
#         b[1+c] = (true && !f || _z) != false;
#         """
#         ,"a,=,1,;,b,[,1,+,c,],=,(,true,&&,!,f,||,_z,),!=,false,;,<EOF>",171))
#     def test_stmt_6(self):
#         self.assertTrue(TestLexer.test("""animal.cat.talk(s + "abc");""","""animal,.,cat,.,talk,(,s,+,abc,),;,<EOF>""",172))
#     def test_stmt_7(self):
#         self.assertTrue(TestLexer.test("return abc.getArea(1 true + 2) - (new obj()).arr[1];","return,abc,.,getArea,(,1,true,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",173))

#     def test_stmt_8(self):
#         self.assertTrue(TestLexer.test("""
#         function_test(a: Int) {
#             ## comment at here ##
#             getString("input");
#         }
#         ""","function_test,(,a,:,Int,),{,getString,(,input,),;,},<EOF>", 174))

#     def test_met_de_8(self):
#         self.assertTrue(TestLexer.test("""
#         String Return(input: String; l: Int) {
#             classSTR.getData(input);
#             if (l > 0) {
#                 return getS() + input;
#             }
#             else {
#                 return input;
#             }
#         }
#         """
#         ,"String,Return,(,input,:,String,;,l,:,Int,),{,classSTR,.,getData,(,input,),;,if,(,l,>,0,),{,return,getS,(,),+,input,;,},else,{,return,input,;,},},<EOF>", 175))
#     def test_met_de_9(self):
#         self.assertTrue(TestLexer.test("int return(){int data=?getINPUT();return data;}\nint[5] getArray(int l){int[5] arr;\nfor i:=0 to l do arr[i] := getData();\nreturn arr;}",
#                                        "int,return,(,),{,int,data,=,Error Token ?",176))
#     def test_met_de_10(self):
#         self.assertTrue(TestLexer.test(""" string get_Special_String(){return "abc\\g!!";}""","""string,get_Special_String,(,),{,return,Illegal Escape In String: abc\g""",177))

#     def test_integer_real1(self):
#         self.assertTrue(TestLexer.test("1.2 1.0 0.1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42",
#         "1.2,1.0,0.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>",178))

        
#     def test_integer_real2(self):
#         self.assertTrue(TestLexer.test("9.0 12e8 0.33E-3 128e-42","9.0,12e8,0.33E-3,128e-42,<EOF>",179))
#     def test_integer_real3(self):

#         self.assertTrue(TestLexer.test("11.0 12.0e8 0.11+E-3 145e-42","11.0,12.0e8,0.11,+,E,-,3,145e-42,<EOF>",180))
#     def test_integer_real4(self):
#         self.assertTrue(TestLexer.test("0.11E2 1.11 0.33 1.0e12 1E-15","0.11E2,1.11,0.33,1.0e12,1E-15,<EOF>",181))
#     def test_integer_real5(self):
#         self.assertTrue(TestLexer.test("e--12 e12 E-15 99e 1 1. 1","e,-,-,12,e12,E,-,15,99,e,1,1.,1,<EOF>",182))

#     def test_integer_real7(self):
#         self.assertTrue(TestLexer.test("12.2e0 -101 11E-2 11.1e2","12.2e0,-,101,11E-2,11.1e2,<EOF>",183))

#     def test_comment_4(self):
#         self.assertTrue(TestLexer.test("""
#         ## Function(){} abcd
#             abcde ##
#             abcd_abcde
#         ## ##
#         ""","abcd_abcde,<EOF>",184))

#     def test_random_1(self):
#         input ="""
#         add(s: Int, t: Int) {
#             Var obj = New Bus();
#             if (s > 0) {
#                 obj.insert(s,t);
#             }
#             else {
#                 return obj;
#             }
#         }
#     """
#         output = "add,(,s,:,Int,,,t,:,Int,),{,Var,obj,=,New,Bus,(,),;,if,(,s,>,0,),{,obj,.,insert,(,s,,,t,),;,},else,{,return,obj,;,},},<EOF>"
#         self.assertTrue(TestLexer.test(input,output,185))
#     def test_random_2(self):
#         input = """
#         remove(s: Int, t: Int, obj: Class) {
#             obj.removeBus(t);
#         }

#         minPark() {
#             return max;
#         }
#         """
#         output = "remove,(,s,:,Int,,,t,:,Int,,,obj,:,Class,),{,obj,.,removeBus,(,t,),;,},minPark,(,),{,return,max,;,},<EOF>"
#         self.assertTrue(TestLexer.test(input, output, 186))

#     def test_unclose_string_9(self):
#         # "str1 \" \n dd "
#         self.assertTrue(TestLexer.test("\"str1 \\\" \n dd \" ","Illegal Escape In String: str1 \\\"",187))
#     def test_unclose_string_10(self):
#         self.assertTrue(TestLexer.test("\"line 1 df dfff","""Unclosed String: line 1 df dfff""",188))
#     def test_illegal_escape_11(self):
#         self.assertTrue(TestLexer.test("\"str11\\ \"","Illegal Escape In String: str11\\ ",189))
#     def test_unclose_string_11(self):
#         self.assertTrue(TestLexer.test("\"str1  Hello World\'\" ahihi ","Unclosed String: str1  Hello World\'\" ahihi ",190))

#     def test_illegal_escape_12(self):
#             """test identifiers"""
#             self.assertTrue(TestLexer.test("\"GameDev\\dlub \\dHCMUT\";",
#                             "Illegal Escape In String: GameDev\\d", 191))
#     def test_string_18(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"GameDev\\nlub \\nHCMUT\";","""GameDev\\nlub \\nHCMUT,;,<EOF>""",192))
    
#     def test_var_declare_2(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("""Var $arr : Array[Array[Int, 3], 3] = 
#                                        Array(
#                                            Array(1,2,5),
#                                            Array(2,5,6),
#                                            Array(5,8,7)
#                                            );""","Var,$arr,:,Array,[,Array,[,Int,,,3,],,,3,],=,Array,(,Array,(,1,,,2,,,5,),,,Array,(,2,,,5,,,6,),,,Array,(,5,,,8,,,7,),),;,<EOF>",193))
    
#     def test_random_3(self):
#         self.assertTrue(TestLexer.test("""
#                                        4"&J^1a_." QGn"?67Sp"{,}6Asz"Yx]("
#                                        ""","4,&J^1a_.,QGn,?67Sp,{,,,},6,Asz,Yx](,<EOF>", 194)) 

#     def test_foreach(self):
#         self.assertTrue(TestLexer.test("""
#             Foreach ($i In 1 .. 100 By 1) {
#                 e = e + $i;
#                 k[$i] = k[$i + 1];
#                 Foreach ($j In 1 .. 100 By 1) {
#                     e = e - $j;
#                     l[$i] = l[$j] + e; 
#                 }
#             }
#             """, "Foreach,(,$i,In,1,..,100,By,1,),{,e,=,e,+,$i,;,k,[,$i,],=,k,[,$i,+,1,],;,Foreach,(,$j,In,1,..,100,By,1,),{,e,=,e,-,$j,;,l,[,$i,],=,l,[,$j,],+,e,;,},},<EOF>", 195))
#     def test_string_19(self):
#         self.assertTrue(TestLexer.test("\"##This is a string, not a comment##\"", "##This is a string, not a comment##,<EOF>", 196))
    
#     def test_var_declare_3(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $x, num, $y, 9gh : Int = 5, 6, 7;","Var,$x,,,num,,,$y,,,9,gh,:,Int,=,5,,,6,,,7,;,<EOF>",197))
#     def test_var_declare_4(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Var $dec, num: Int = 0b0101110, 0xAFF;","Var,$dec,,,num,:,Int,=,0b0,101110,,,0xAFF,;,<EOF>",198))
#     def test_if_stmt(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("""
#             If (a >= b) {
#                 a = a + b;
#             }
#             Elseif (b >= c) {
#                 b = a + b || r;
#             }
#             Else {
#                 Return result;
#             }
#         ""","If,(,a,>=,b,),{,a,=,a,+,b,;,},Elseif,(,b,>=,c,),{,b,=,a,+,b,||,r,;,},Else,{,Return,result,;,},<EOF>",199))
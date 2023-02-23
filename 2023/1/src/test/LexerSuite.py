# # 1913652
# # Trịnh Duy Hưng

# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase):

#     # def test_0(self):
#     #     self.assertTrue(TestLexer.test(" + - * / % ! <= >= < > && ||  == !=  ::     ",
#     #     "+,-,*,/,%,!,<=,>=,<,>,&&,||,==,!=,::,<EOF>", 100))
    

#     # def test_1(self):
#     #     self.assertTrue(TestLexer.test("           + - * / % ! <= >= < > && ||  == !=  ::                ",
#     #     "+,-,*,/,%,!,<=,>=,<,>,&&,||,==,!=,::,<EOF>",101))

#     # def test_2(self):
#     #     self.assertTrue(TestLexer.test("/* wefwfwe */", "<EOF>", 102))

#     # def test_3(self):
#     #     self.assertTrue(TestLexer.test("23427b5", "23427,b5,<EOF>", 103))

#     # def test_4(self):
#     #     self.assertTrue(TestLexer.test("_duyhung135", "_duyhung135,<EOF>", 104))

#     # def test_5(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     // quhiuhef
#     #     // quhiuhef
#     #     // quhiuhef
#     #     // quhiuhef
        
#     #     """, "<EOF>", 105))

#     def test_6(self):
#         self.assertTrue(TestLexer.test("""
#         "He asked me:\"Where is John?\""
#         """, "$_dollarstatic,<EOF>", 106))

#     # def test_7(self):
#     #     self.assertTrue(TestLexer.test("   $duy     hung", "$duy,hung,<EOF>", 107))

#     # def test_8(self):
#     #     self.assertTrue(TestLexer.test("_12343_my const", "_12343_my,const,<EOF>", 108))

#     # def test_9(self):
#     #     self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 109))

#     # def test_10(self):
#     #     self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 110))

#     # def test_11(self):
#     #     self.assertTrue(TestLexer.test("%duyHUNG", "%,duyHUNG,<EOF>", 111))

#     # def test_12(self):
#     #     self.assertTrue(TestLexer.test("* + hung      /   ", "*,+,hung,/,<EOF>", 112))

#     # def test_13(self):
#     #     self.assertTrue(TestLexer.test("$", "Error Token $", 113))

#     # def test_14(self):
#     #     self.assertTrue(TestLexer.test("Val $_fajfaksd_ASDFADS213134Asdvas, num____fasdfh__2136512_____dafds: Int = 0b0101110010101010100011111, 0xAFABCDEF",
#     #                     "Val,$_fajfaksd_ASDFADS213134Asdvas,,,num____fasdfh__2136512_____dafds,:,Int,=,0b0,101110010101010100011111,,,0xAFABCDEF,<EOF>", 114))

#     # def test_15(self):
#     #     self.assertTrue(TestLexer.test(
#     #         "18_8_128_2.364872364245e67 10002322E-97381237 232431E01023473 134422.787902 178434554357.4947563E+343256669 24346436. .452345 .e123133 .7674e99995 41239778.e23124410 4587467.e213400001_232342354 17635235_89996_111154_9.49324_888845484926e3 43351_2000098898934.3_777456342356", 
#     #         "1881282.364872364245e67,10002322E-97381237,232431E01023473,134422.787902,178434554357.4947563E+343256669,24346436.,.,452345,.e123133,.7674e99995,41239778.e23124410,4587467.e213400001,_232342354,17635235899961111549.49324,_888845484926e3,433512000098898934.3,_777456342356,<EOF>", 115))

#     # def test_16(self):
#     #     self.assertTrue(TestLexer.test(
#     #         "1_2_3_4321479326523469234 39237247362177374 12039434778957392_5_6_2_3_4 1812374738946466", "1_2_3_4321479326523469234,39237247362177374,12039434778957392_5_6_2_3_4,1812374738946466,<EOF>", 116))

#     # def test_17(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     ## LoreamsdASDFOWFWJEFJ3129834329adasfdksfsdksdljfs
#     #     """, "Error Token #", 117))

#     # def test_18(self):   
#     #     self.assertTrue(TestLexer.test("""
#     #     ##
#     #     asdajfsk767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFdjfwqwqlqdk
#     #     ##
#     #     DSAFWEFWEFOIWEWsdafbawuefygweu_______________________3214932842346935436971346912736
#     #     ##df767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFkss
#     #     ###sf767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFdjsls
#     #     ##
#     #     """, "DSAFWEFWEFOIWEWsdafbawuefygweu_______________________3214932842346935436971346912736,Error Token #", 118))

#     # def test_19(self):
#     #     self.assertTrue(TestLexer.test("\"34gegefaafwdfwogg\\mafwfweghterwd5768o\"","Illegal Escape In String: 34gegefaafwdfwogg\\m",119))

#     # def test_20(self):
#     #     self.assertTrue(TestLexer.test("$FSDGM834738____sadfidufuhabc 123476761abnvdsjjsdnMMMMASDZZZ_sdjdv _16855555423 dfwedwfwePPIHDWU3536dtehiiiiiiiiiiiif",
#     #                     "$FSDGM834738____sadfidufuhabc,123476761,abnvdsjjsdnMMMMASDZZZ_sdjdv,_16855555423,dfwedwfwePPIHDWU3536dtehiiiiiiiiiiiif,<EOF>", 120))

#     # def test_21(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         "fwoieijwofjndanfDAFKWEOWJEGWG '"fjdsdsaklfjsaldkPPWHDNJNjnewwjnccedefg'""
#     #     """, """fwoieijwofjndanfDAFKWEOWJEGWG '"fjdsdsaklfjsaldkPPWHDNJNjnewwjnccedefg'",<EOF>""", 121))

#     # def test_22(self):
#     #     self.assertTrue(TestLexer.test("19789rthtrh \"wefwegxwgergyffwfewewz\k 456","19789,rthtrh,Illegal Escape In String: wefwegxwgergyffwfewewz\k",122))

#     # def test_23(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         ## Testing comment fowifjowfnwio!@#@#$$#%@^@%^&?<>":{{}}({}()}:(){(})}) ##
#     #     """, "<EOF>", 123))

#     # def test_24(self):
#     #     self.assertTrue(TestLexer.test("## ASCWEasdasd !@@#%$#  %lgvkhjk$%^&*(&*~{}[]\;]\p/.,.,<>>) ##", "<EOF>",124))
    
#     # def test_25(self):
#     #     self.assertTrue(TestLexer.test("## # ASCWEasdasd !@@#%$#%$%^&*(&*~{}[]\;]\p/.,.,<>>) # ##", "<EOF>",125))

#     # def test_26(self):
#     #     self.assertTrue(TestLexer.test("Array(18983423,4000003023003032,352546546,9191993941294983248)",
#     #                 "Array,(,18983423,,,4000003023003032,,,352546546,,,9191993941294983248,),<EOF>", 126))

#     # def test_27(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         If (a123555 > B______123213) {Return a_63475_IIIIIIIIII;}
#     #         Elseif (c99999 == d0000007) {hunghunga = duydydtdda + opopopopopopb;}
#     #         Else {Return ppppppppppppppppppppppppppppppppp;}
#     #         """, "If,(,a123555,>,B______123213,),{,Return,a_63475_IIIIIIIIII,;,},Elseif,(,c99999,==,d0000007,),{,hunghunga,=,duydydtdda,+,opopopopopopb,;,},Else,{,Return,ppppppppppppppppppppppppppppppppp,;,},<EOF>", 127))

#     # def test_28(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         Foreach ($l_LLLLLLLLLLLLLL In 19 .. 100234 By 191) {
#     #             saloaloaloalaolaooo = saloaloaloalaolaooo + iiiuiuiuiuiuiu[$mn_______________7436fhhf];
#     #         }
#     #         """, "Foreach,(,$l_LLLLLLLLLLLLLL,In,19,..,100234,By,191,),{,saloaloaloalaolaooo,=,saloaloaloalaolaooo,+,iiiuiuiuiuiuiu,[,$mn_______________7436fhhf,],;,},<EOF>", 128))

#     # def test_29(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         {
#     #             Var jijijijijdaf, ijijijji: Int;
#     #             pkpsdfkpfasdf = 2_4546_898432.0123146;
#     #             Val a7654334, b7654334: Array[String, 987798798];
#     #             tutyuytus = pkpsdfkpfasdf * pkpsdfkpfasdf * Self.nidsidf;
#     #             uasdfhhhhhhhha[192837] = ppppppp;
#     #         }
#     #         """, "{,Var,jijijijijdaf,,,ijijijji,:,Int,;,pkpsdfkpfasdf,=,24546898432.0123146,;,Val,a7654334,,,b7654334,:,Array,[,String,,,987798798,],;,tutyuytus,=,pkpsdfkpfasdf,*,pkpsdfkpfasdf,*,Self,.,nidsidf,;,uasdfhhhhhhhha,[,192837,],=,ppppppp,;,},<EOF>", 129))

#     # def test_30(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         Var $arjijijijijdaf : Array[Array[Boolean, 3], 3] = Array(
#     #                                                     Array(199,987798798,7565),
#     #                                                     Array(346723439,87765,1236),
#     #                                                     Array(9000000005,1348,9632847)
#     #                                                     );
#     #         )""", "Var,$arjijijijijdaf,:,Array,[,Array,[,Boolean,,,3,],,,3,],=,Array,(,Array,(,199,,,987798798,,,7565,),,,Array,(,346723439,,,87765,,,1236,),,,Array,(,9000000005,,,1348,,,9632847,),),;,),<EOF>", 130))

#     # def test_31(self):
#     #     self.assertTrue(TestLexer.test("""anitrinhduyhungmal.canguyenthachngocquynht.talfuckk(cpluspus + "fio___adfshuf___sefoooobc");""",
#     #                                     """anitrinhduyhungmal,.,canguyenthachngocquynht,.,talfuckk,(,cpluspus,+,fio___adfshuf___sefoooobc,),;,<EOF>""",131))
    
#     # def test_32(self):
#     #         self.assertTrue(TestLexer.test("""
#     #                 0b111111111987 0B09998888 67.9898454600003443 34577777 0X2D3FFDDDD
#     #                 """, "0b111111111,987,0B0,9998888,67.9898454600003443,34577777,0X2D3FFDDDD,<EOF>", 132))

#     # def test_33(self):
#     #     self.assertTrue(TestLexer.test("""
#     #             New Return True False Foreach If Elseif Else Float Int String Var Val Constructor Destructor Null Class By In
#     #             """, "New,Return,True,False,Foreach,If,Elseif,Else,Float,Int,String,Var,Val,Constructor,Destructor,Null,Class,By,In,<EOF>", 133))

#     # def test_34(self):
#     #     self.assertTrue(TestLexer.test("""
#     #             + - * / % == != ! > < >= <= || && . :: ( ) { } [ ] ==. +.
#     #             """, "+,-,*,/,%,==,!=,!,>,<,>=,<=,||,&&,.,::,(,),{,},[,],==.,+.,<EOF>", 134))

#     # def test_35(self):
#     #     self.assertTrue(TestLexer.test("\"duyhungduyhung\"ngocquynhngocquynh\"",
#     #     "duyhungduyhung,ngocquynhngocquynh,Unclosed String: ",135))
    
#     # def test_36(self):
#     #     self.assertTrue(TestLexer.test("\"jkqajkajqka\\njkqajkajqka\"","jkqajkajqka\\njkqajkajqka,<EOF>",136))

#     # def test_37(self):
#     #     self.assertTrue(TestLexer.test("\"abhunghung\\thunghung\\nbhunghung\"","abhunghung\\thunghung\\nbhunghung,<EOF>",137))

#     # def test_38(self):
#     #     self.assertTrue(TestLexer.test("Return triangle.getCurriculum(1010304 false true + * - 8988) - (new object()).arrayer[8444];",
#     #     "Return,triangle,.,getCurriculum,(,1010304,false,true,+,*,-,8988,),-,(,new,object,(,),),.,arrayer,[,8444,],;,<EOF>",138))

#     # def test_39(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     "7777.645656454235dfdsgjsidfgji888888...98f834jfjfnnvnvnnv\'trinhduyhung" 8956854.nguyenthachngocquynh "878736636\\\\0b10010101111111111"
#     #     ""","7777.645656454235dfdsgjsidfgji888888...98f834jfjfnnvnvnnv'trinhduyhung,8956854.,nguyenthachngocquynh,878736636\\\\0b10010101111111111,<EOF>",139))

#     # def test_40(self):
#     #     self.assertTrue(TestLexer.test("Trinh_Duy_Hung_fdfijf \"trinhduyhung1!!@#$@%%%%*&*&*&*&*&@#$@$#@$%^i\\n\" 555555555555jijijijiyz",
#     #                                     "Trinh_Duy_Hung_fdfijf,trinhduyhung1!!@#$@%%%%*&*&*&*&*&@#$@$#@$%^i\\n,555555555555,jijijijiyz,<EOF>",140))

#     # def test_41(self):
#     #     self.assertTrue(TestLexer.test("\"!h$5FBi6qwddasd\"_nguyenthachngocquynhq\"!SZRhungquynh,H}\"sI666677fpw",
#     #                                         "!h$5FBi6qwddasd,_nguyenthachngocquynhq,!SZRhungquynh,H},sI666677fpw,<EOF>",141))
        
#     # def test_42(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     uwufhweuf4"&uwufhweufJ^1uwufhweufa_." QuwufhweufGn"?6uwufhweuf7Sp"{,}6Asz"Yx]("
#     #     ""","uwufhweuf4,&uwufhweufJ^1uwufhweufa_.,QuwufhweufGn,?6uwufhweuf7Sp,{,,,},6,Asz,Yx](,<EOF>",142))

#     # def test_43(self):
#     #     self.assertTrue(TestLexer.test("0ff234f23f2f1_\"^VzxvLRfffffuuu@\\\\OushungquynhM;\"uGquynhhungM+jfffasdE",
#     #                                     "0,ff234f23f2f1_,^VzxvLRfffffuuu@\\\\OushungquynhM;,uGquynhhungM,+,jfffasdE,<EOF>",143))

#     # def test_44(self):
#     #     self.assertTrue(TestLexer.test("\"(trinhduyhungItrinhduyhungFtrinhduyhungq+trinhduyhunglq(\"trinhduyhungIhKtrinhduyhung6we(*.*)GdvS{(}",
#     #                                     "(trinhduyhungItrinhduyhungFtrinhduyhungq+trinhduyhunglq(,trinhduyhungIhKtrinhduyhung6we,(,*,.,*,),GdvS,{,(,},<EOF>",144))

#     # def test_45(self):
#     #     self.assertTrue(TestLexer.test("\"btrinhduyhungac\\mtrinhduyhunga\"","Illegal Escape In String: btrinhduyhungac\\m",145))

#     # def test_46(self):
#     #     self.assertTrue(TestLexer.test("\"btrinhduyhungatrinhduyhungMD\\HtrinhduyhungLtrinhduyhungSc\\ntrinhduyhungatrinhduyhung\"","Illegal Escape In String: btrinhduyhungatrinhduyhungMD\\H",146))

#     # def test_47(self):
#     #     self.assertTrue(TestLexer.test("\",dtrinhduyhungls\\Ftrinhduyhung1trinhduyhung2trinhduyhung!trinhduyhungLtrinhduyhungS\\ktrinhduyhungctrinhduyhung\\trinhduyhungnatrinhduyhung\"","Illegal Escape In String: ,dtrinhduyhungls\\F",147))

#     # def test_48(self):
#     #     self.assertTrue(TestLexer.test("\"atrinhduyhungdo\\madotrinhduyhung\"","Illegal Escape In String: atrinhduyhungdo\\m",148))

#     # def test_49(self):
#     #     self.assertTrue(TestLexer.test("78799923trinhduyhungnguyenthachngocquynhabc \"xtrinhduyhungytrinhduyhungz\k 456",
#     #                                 "78799923,trinhduyhungnguyenthachngocquynhabc,Illegal Escape In String: xtrinhduyhungytrinhduyhungz\k",149))

#     # def test_50(self):
#     #     self.assertTrue(TestLexer.test("\"nguyenthachngocquynhanguyenthachngocquynha\wb\"","Illegal Escape In String: nguyenthachngocquynhanguyenthachngocquynha\w",150))

#     # def test_51(self):
#     #     self.assertTrue(TestLexer.test("bnguyenthachngocquynha+1786544332+\"nnguyenthachngocquynha\"\"mnguyenthachngocquynhd+119238219.2-401203040468\lb",
#     #                                     "bnguyenthachngocquynha,+,1786544332,+,nnguyenthachngocquynha,Illegal Escape In String: mnguyenthachngocquynhd+119238219.2-401203040468\l",151))

#     # def test_52(self):
#     #     self.assertTrue(TestLexer.test("\"1.744462+1.744463+1.744464\\o'\"123","Illegal Escape In String: 1.744462+1.744463+1.744464\\o",152))

#     # def test_53(self):
#     #     self.assertTrue(TestLexer.test("(*nangocquynhdethuongc*)/2232881.73181231 \"bcuoingocquynha\\qm\f\"",
#     #                                     "(,*,nangocquynhdethuongc,*,),/,2232881.73181231,Illegal Escape In String: bcuoingocquynha\q",153))

#     # def test_54(self):
#     #     self.assertTrue(TestLexer.test("\"congocquynhdangyeuncahngocquynhdangyeueo\\uabc","Illegal Escape In String: congocquynhdangyeuncahngocquynhdangyeueo\\u",154))

#     # def test_55(self):
#     #     self.assertTrue(TestLexer.test("\"trinhduyhungbatrinhduyhungcxytrinhduyhungc",
#     #                                         "Unclosed String: trinhduyhungbatrinhduyhungcxytrinhduyhungc",155))

#     # def test_56(self):
#     #     self.assertTrue(TestLexer.test("NngocquynhsexymkngocquynhsexyobYngocquynhsexyn{!}+I1+\"`YSnewyodjdjdj2h.ueywuJ(",
#     #                                         "NngocquynhsexymkngocquynhsexyobYngocquynhsexyn,{,!,},+,I1,+,Unclosed String: `YSnewyodjdjdj2h.ueywuJ(",156))

#     # def test_57(self):
#     #     self.assertTrue(TestLexer.test("\"abeQuynhbeRotcbeQuynhbeRotnv \" \"ahunghudhdhdbc","abeQuynhbeRotcbeQuynhbeRotnv ,Unclosed String: ahunghudhdhdbc",157))

#     # def test_58(self):
#     #     self.assertTrue(TestLexer.test("\"bsaunaycuoiQuynhcms!,lds \" {\"gh6473f94f8hhhhfhASDGGGGGGGGGGGGGGGGGc\"} 123\"abeQuynhdethuong7273817361bc",
#     #                                     "bsaunaycuoiQuynhcms!,lds ,{,gh6473f94f8hhhhfhASDGGGGGGGGGGGGGGGGGc,},123,Unclosed String: abeQuynhdethuong7273817361bc",158))

#     # def test_59(self):
#     #     self.assertTrue(TestLexer.test("a+11.23749283470202002+\"masdanfjsdDAviidd_______m.123\" 12 \"%^_)3141927777&",
#     #                                     "a,+,11.23749283470202002,+,masdanfjsdDAviidd_______m.123,12,Unclosed String: %^_)3141927777&",159))

#     # def test_60(self):
#     #     self.assertTrue(TestLexer.test("323344448n\"[#FfQuynhsQuynh?0ED\"1.1\"dddd`#","323344448,n,[#FfQuynhsQuynh?0ED,1.1,Unclosed String: dddd`#",160))

#     # def test_61(self):
#     #     self.assertTrue(TestLexer.test("\"stnguyenthachngocquynhr1  \\r ahnguyenthachngocquynhihi \"","stnguyenthachngocquynhr1  \\r ahnguyenthachngocquynhihi ,<EOF>",161))

#     # def test_62(self):
#     #     self.assertTrue(TestLexer.test("\"He aajjTrinhDuyked me: '\"ajjTrinhDuyhere \\t ajjTrinhDuys ajjTrinhDuyohn?'\"\"",
#     #                                         "He aajjTrinhDuyked me: \'\"ajjTrinhDuyhere \\t ajjTrinhDuys ajjTrinhDuyohn?\'\",<EOF>",162))

#     # def test_63(self):
#     #     self.assertTrue(TestLexer.test("\"  sQuynhdiahuongtr \\\' \\\" sQuynhdiahuongtr \"","Illegal Escape In String:   sQuynhdiahuongtr \\' \\\"",163))
     
#     # def test_64(self):
#     #     self.assertTrue(TestLexer.test("\" \\\\ \\n \\t \\n fbeQuynhditbudffffdvvd \\\\\" "," \\\\ \\n \\t \\n fbeQuynhditbudffffdvvd \\\\,<EOF>",164))

#     # def test_65(self):
#     #     self.assertTrue(TestLexer.test("{ 1,2  ,  37766662,  2}; {1.923489282,2., 111113e8  , 4645.0e-1}","{,1,,,2,,,37766662,,,2,},;,{,1.923489282,,,2.,,,111113e8,,,4645.0e-1,},<EOF>",165))

#     # def test_66(self):
#     #     self.assertTrue(TestLexer.test("{true,false   ,  true, false}; {\" nareiuiqpm\", \" vreiuiqpat lreiuiqpy \"  ,  \" ancxbaa \" }",
#     #                                     """{,true,,,false,,,true,,,false,},;,{, nareiuiqpm,,, vreiuiqpat lreiuiqpy ,,, ancxbaa ,},<EOF>""",166))

#     # def test_67(self):
#     #     self.assertTrue(TestLexer.test("if(a != b)\nthen continuea=a+1;\nelse b=0;","if,(,a,!=,b,),then,continuea,=,a,+,1,;,else,b,=,0,;,<EOF>",167))

#     # def test_68(self):
#     #     self.assertTrue(TestLexer.test("return nebeQuynhlozmupwn then anbeQuynhlozmupimal(abeQuynhlozmup,bbeQuynhlozmup + cbeQuynhlozmup);",
#     #                                     "return,nebeQuynhlozmupwn,then,anbeQuynhlozmupimal,(,abeQuynhlozmup,,,bbeQuynhlozmup,+,cbeQuynhlozmup,),;,<EOF>",168))

#     # def test_69(self):
#     #     self.assertTrue(TestLexer.test("cffffallFn then ffffunction(ayuie + byuie*cyuie % (dyuie+2));",
#     #                                     "cffffallFn,then,ffffunction,(,ayuie,+,byuie,*,cyuie,%,(,dyuie,+,2,),),;,<EOF>",169))

#     # def test_70(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     yervva[7766+9766] = 12;
#     #     Foreach(i = 1 In 1 .. styervvr.lenyervvgth) {
#     #         yervvb[i] = yervvb[i] + 1766;
#     #     }
#     #     """,
#     #     "yervva,[,7766,+,9766,],=,12,;,Foreach,(,i,=,1,In,1,..,styervvr,.,lenyervvgth,),{,yervvb,[,i,],=,yervvb,[,i,],+,1766,;,},<EOF>", 170))

#     # def test_71(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     aQuynhQuynh = 1345;
#     #     bQuynhQuynh[1345+cQuynhQuynh] = (trffwfefweue && !fvdsfd || _zQuynhQuynh) != false;
#     #     """
#     #     ,"aQuynhQuynh,=,1345,;,bQuynhQuynh,[,1345,+,cQuynhQuynh,],=,(,trffwfefweue,&&,!,fvdsfd,||,_zQuynhQuynh,),!=,false,;,<EOF>",171))

#     # def test_72(self):
#     #     self.assertTrue(TestLexer.test("""aniQuynhdethuongmal.cQuynhdethuongat.taQuynhdethuonglk(sQuynhdethuong + "QuynhdethuongabcQuynhdethuong");""",
#     #                                     """aniQuynhdethuongmal,.,cQuynhdethuongat,.,taQuynhdethuonglk,(,sQuynhdethuong,+,QuynhdethuongabcQuynhdethuong,),;,<EOF>""",172))

#     # def test_73(self):
#     #     self.assertTrue(TestLexer.test("return aghjjbc.gedadsadastArea(1 trfalseue + 2) - (new obj()).arr[1];",
#     #                                     "return,aghjjbc,.,gedadsadastArea,(,1,trfalseue,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",173))

#     # def test_74(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     funHungnection_test(aloaloo: String) {
#     #         ## alo alo alo alo phai Quynh hong da##
#     #         getTrinhDuyHungString("inHungneput");
#     #     }
#     #     ""","funHungnection_test,(,aloaloo,:,String,),{,getTrinhDuyHungString,(,inHungneput,),;,},<EOF>", 174))

#     # def test_75(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     Float Break(output: Float; l: Bool) {
#     #         classfwefSTR.gefweftData(output);
#     #         if (l6733 > 0) {
#     #             Break getS() + output;
#     #         }
#     #         else {
#     #             Break output;
#     #         }
#     #         else {
#     #             Break output;
#     #         }
#     #     }
#     #     """
#     #     ,"Float,Break,(,output,:,Float,;,l,:,Bool,),{,classfwefSTR,.,gefweftData,(,output,),;,if,(,l6733,>,0,),{,Break,getS,(,),+,output,;,},else,{,Break,output,;,},else,{,Break,output,;,},},<EOF>", 175))

#     # def test_76(self):
#     #     self.assertTrue(TestLexer.test("float return(){float dataAnalist=?getWife()",
#     #                                    "float,return,(,),{,float,dataAnalist,=,Error Token ?",176))
#     # def test_77(self):
#     #     self.assertTrue(TestLexer.test(""" float getQuynhForever(){return "afwefuiawfjdsojfiasojbc\\g!!";}""",
#     #                                     """float,getQuynhForever,(,),{,return,Illegal Escape In String: afwefuiawfjdsojfiasojbc\g""",177))

#     # def test_78(self):
#     #     self.assertTrue(TestLexer.test("345.2345 9855.0 0.11111111111 34534e+7781112 85522.12342E-45552 10101010101.4238e-9999999 .534699E11111111 0.234524874340000000000000000033134663E-13453927432743",
#     #                                     "345.2345,9855.0,0.11111111111,34534e+7781112,85522.12342E-45552,10101010101.4238e-9999999,.534699E11111111,0.234524874340000000000000000033134663E-13453927432743,<EOF>",178))

#     # def test_79(self):
#     #     self.assertTrue(TestLexer.test("                12_47_23_98_5_72_3_2e8             /                      983216363628E-12347492321",
#     #                                     "1247239857232e8,/,983216363628E-12347492321,<EOF>",179))

#     # def test_80(self):
#     #     self.assertTrue(TestLexer.test("0x0",
#     #                                     "0x0,<EOF>",180))

#     # def test_81(self):
#     #     self.assertTrue(TestLexer.test("12_38_21_47_9_9_99.183999990000000000000000000000000001112342",
#     #                                     "123821479999.183999990000000000000000000000000001112342,<EOF>",181))

#     # def test_82(self):
#     #     self.assertTrue(TestLexer.test("e--12            E--4345    102E--56757",
#     #                                     "e,-,-,12,E,-,-,4345,102,E,-,-,56757,<EOF>",182))

#     # def test_83(self):
#     #     self.assertTrue(TestLexer.test("4325134442.667724e0 -999999999999999 45345351e-57345 32451.12333e8678",
#     #                                     "4325134442.667724e0,-,999999999999999,45345351e-57345,32451.12333e8678,<EOF>",183))

#     # def test_84(self):
#     #     self.assertTrue(TestLexer.test("""
#     #     ## Function(){} abcd
#     #         abcde ##
#     #         anhsecogangcuoiemnhaQuynh
#     #     ## ##
#     #     ""","anhsecogangcuoiemnhaQuynh,<EOF>",184))

#     # def test_85(self):
#     #     input ="""
#     #     wedding(sdddddddd: Float, tdddddddd: Float) {
#     #         Var object = New Bus();
#     #         if (sdddddddd > 00) {
#     #             object.insert(sdddddddd,tdddddddd);
#     #         }
#     #         else {
#     #             return object;
#     #         }
#     #     }
#     # """
#     #     output = "wedding,(,sdddddddd,:,Float,,,tdddddddd,:,Float,),{,Var,object,=,New,Bus,(,),;,if,(,sdddddddd,>,00,),{,object,.,insert,(,sdddddddd,,,tdddddddd,),;,},else,{,return,object,;,},},<EOF>"
#     #     self.assertTrue(TestLexer.test(input,output,185))

#     # def test_86(self):
#     #     input = """
#     #     nevergiveup(sdddddddd: Float, tdddddddd: Float, object: Boolean) {
#     #         object.removeBus(t);
#     #     }

#     #     hunglovequynh() {
#     #         return truelove;
#     #     }
#     #     """
#     #     output = "nevergiveup,(,sdddddddd,:,Float,,,tdddddddd,:,Float,,,object,:,Boolean,),{,object,.,removeBus,(,t,),;,},hunglovequynh,(,),{,return,truelove,;,},<EOF>"
#     #     self.assertTrue(TestLexer.test(input, output, 186))

#     def test_87(self):
#         self.assertTrue(TestLexer.test("\"met youin the back during twelve o fivedd \\\" \n dd \" ",
#                                         "Illegal Escape In String: met youin the back during twelve o fivedd \\\"",187))

#     def test_88(self):
#         self.assertTrue(TestLexer.test("\"happy 10 years anniversary","""Unclosed String: happy 10 years anniversary""",188))

#     def test_89(self):
#         self.assertTrue(TestLexer.test("\"wfiwuefwifjlsadfsdhfhfhfhfhhfhfhf1\\ \"",
#                                         "Illegal Escape In String: wfiwuefwifjlsadfsdhfhfhfhfhhfhfhf1\\ ",189))

#     def test_90(self):
#         self.assertTrue(TestLexer.test("\"Hung thich Quynh lam do ahihi\'\" ahihi ",
#                                                 "Unclosed String: Hung thich Quynh lam do ahihi\'\" ahihi ",190))

#     def test_91(self):
#             """test identifiers"""
#             self.assertTrue(TestLexer.test("\"WebDev\\dclub \\dBKU\";",
#                                             "Illegal Escape In String: WebDev\\d", 191))
                            
#     def test_92(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"Quynhdethuongahihi\\nfkkkkkkoekofkw \\niwillmarryou\";",
#                                         """Quynhdethuongahihi\\nfkkkkkkoekofkw \\niwillmarryou,;,<EOF>""",192))
    
#     # def test_93(self):
#     #     """test identifiers"""
#     #     self.assertTrue(TestLexer.test("""Var $Hung_love_Quynh : Array[Array[Boolean, 3], 3] = 
#     #                                    Array(
#     #                                        Array(true,false,false),
#     #                                        Array(false,true,true),
#     #                                        Array(false,false,true)
#     #                                        );""",
#     #                                 "Var,$Hung_love_Quynh,:,Array,[,Array,[,Boolean,,,3,],,,3,],=,Array,(,Array,(,true,,,false,,,false,),,,Array,(,false,,,true,,,true,),,,Array,(,false,,,false,,,true,),),;,<EOF>",193))
    
#     # def test_94(self):
#     #     self.assertTrue(TestLexer.test("""
#     #                                    234"&23J^1a_.23" QGn"?6dddddddddddddddddddddddddddddddddddddddd7Sp"{,}6678209Adddwsz"Ydqdwx]("
#     #                                    ""","234,&23J^1a_.23,QGn,?6dddddddddddddddddddddddddddddddddddddddd7Sp,{,,,},6678209,Adddwsz,Ydqdwx](,<EOF>", 194)) 

#     # def test_95(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         Foreach ($i In 1 .. 100 By 1) {
#     #             e = e + $i;
#     #             k[$i] = k[$i + 1];
#     #             Foreach ($j In 1 .. 100 By 1) {
#     #                 e = e - $j;
#     #                 l[$i] = l[$j] + e; 
#     #             }
#     #         }
#     #         """, "Foreach,(,$i,In,1,..,100,By,1,),{,e,=,e,+,$i,;,k,[,$i,],=,k,[,$i,+,1,],;,Foreach,(,$j,In,1,..,100,By,1,),{,e,=,e,-,$j,;,l,[,$i,],=,l,[,$j,],+,e,;,},},<EOF>", 195))

#     def test_96(self):
#         self.assertTrue(TestLexer.test("\"##Nguyen Thach Ngoc Quynh##\"", 
#                                             "##Nguyen Thach Ngoc Quynh##,<EOF>", 196))
    
#     # def test_97(self):
#     #     self.assertTrue(TestLexer.test("Val $xdxxdxdXDXDXDXD, afhhhhhhhhh, $fwweieeeeeee, 9$gh : Array = 5732828791111, 6732828791111, 7732828791111;",
#     #                                     "Val,$xdxxdxdXDXDXDXD,,,afhhhhhhhhh,,,$fwweieeeeeee,,,9,$gh,:,Array,=,5732828791111,,,6732828791111,,,7732828791111,;,<EOF>",197))

#     # def test_98(self):
#     #     self.assertTrue(TestLexer.test("Var $husadhfosddiidid, hope1day: Boolean = 0b0123456789, 0x473738FEBED;",
#     #                                     "Var,$husadhfosddiidid,,,hope1day,:,Boolean,=,0b0,123456789,,,0x473738FEBED,;,<EOF>",198))

#     # def test_99(self):
#     #     self.assertTrue(TestLexer.test("""
#     #         If (aQuynhdethuongquadi >= bQuynhdethuongquadi) {
#     #             aQuynhdethuongquadi = aQuynhdethuongquadi + bQuynhdethuongquadi;
#     #         }
#     #         Elseif (b >= cQuynhdethuongquadi) {
#     #             bQuynhdethuongquadi = aQuynhdethuongquadi + bQuynhdethuongquadi || rQuynhdethuongquadi;
#     #         }
#     #         Else {
#     #             Return Quynhdethuongquadi;
#     #         }
#     #         Else {
#     #             Return Quynhdethuongquadi;
#     #         }
#     #         Else {
#     #             Return Quynhdethuongquadi;
#     #         }
#     #     ""","If,(,aQuynhdethuongquadi,>=,bQuynhdethuongquadi,),{,aQuynhdethuongquadi,=,aQuynhdethuongquadi,+,bQuynhdethuongquadi,;,},Elseif,(,b,>=,cQuynhdethuongquadi,),{,bQuynhdethuongquadi,=,aQuynhdethuongquadi,+,bQuynhdethuongquadi,||,rQuynhdethuongquadi,;,},Else,{,Return,Quynhdethuongquadi,;,},Else,{,Return,Quynhdethuongquadi,;,},Else,{,Return,Quynhdethuongquadi,;,},<EOF>",199))

# # End 100 testcases

# import unittest
# from TestUtils import TestLexer


# class LexerSuite(unittest.TestCase):

#     # def test_1(self):
#     #     """test identifiers"""
#     #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    
#     # def test_2(self):
#     #     """test comment"""
#     #     self.assertTrue(TestLexer.test(
#     #         """
#     #         //abc
#     #         /* comment */ */            
#     #         """
#     #         , "*,/,<EOF>", 102))

#     # def test_3(self):
#     #     """intlit floatlit"""
#     #     self.assertTrue(TestLexer.test(
#     #         """
#     #         1234 123
#     #         1_72
#     #         1_234_567
#     #         1.234 1.2e3 7E-10
#     #         1_234.567
#     #         """
#     #         , "1234,123,172,1234567,1.234,1.2e3,7E-10,1234.567,<EOF>", 103))
         

  

#     def test_5(self):
#         """stringlit"""
#         self.assertTrue(TestLexer.test(
#             """
#             "This is a string containing tab \\t"
#             "He asked me: \\"Where is John?\\""
#             """
#             , """This is a string containing tab \\t,He asked me: "Where is John?",<EOF>""", 105))

    # def test_6(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         auto break boolean do else
    #         false float for function if
    #         integer return string true while
    #         void out continue of inherit
    #         array
    #         """
    #         , """auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>""", 106))

    # def test_7(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         + - * / %
    #         ! && || ==
    #         != < <= > >=
    #         ::
    #         """
    #         , """+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>""", 107))

    # def test_8(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         ( ) [ ] . , ; : { } =
    #         """
    #         , """(,),[,],.,,,;,:,{,},=,<EOF>""", 108))

    # def test_9(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         x : integer = 65;
    #         fact : function integer (n : integer ) {
    #             if (n == 0) return 1 ;
    #             else return n * fact (n - 1 ) ;
    #         }
    #         inc : function void (out n : integer , delta : integer ) {
    #             n = n + delta ;
    #         }
    #         main : function void () {
    #             delta : integer = fact (3) ;
    #             inc(x,delta) ;
    #             printInteger(x) ;
    #         }
    #         """
    #         , """x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>""", 109))

    # def test_10(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         //abc
    #         /* commemts */
    #         // eof
    #         """
    #         , "<EOF>", 110))
    
    # def test_11(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         {1, 5, 7, 12} {"Kangxi", "Yongzheng", "Qianlong"}
    #         """
    #         , "{,1,,,5,,,7,,,12,},{,Kangxi,,,Yongzheng,,,Qianlong,},<EOF>", 111))

    # def test_12(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         x : array [2, 3] of integer;
    #         fact : function integer (n : integer ) {
    #             for (i = 1, i < 10, i + 1) {
    #                 writeInt(i);
    #             }
    #         }
    #         main : function void () {
    #             r, s: integer;
    #             r = 2.0;
    #             a, b: array [5] of integer;
    #             s = r * r * myPI;
    #             a[0] = s;
    #         }
    #         """
    #         , "x,:,array,[,2,,,3,],of,integer,;,fact,:,function,integer,(,n,:,integer,),{,for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},},main,:,function,void,(,),{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>", 112))


import unittest
from TestUtils import TestLexer


# class LexerSuite(unittest.TestCase):
    # def test_inline_comment(self):
    #     self.assertTrue(TestLexer.test("// This is a comment", "<EOF>", 101))
    # def test_inline_comment2(self):
    #     self.assertTrue(TestLexer.test("// This is a comment \n", "<EOF>", 102))
    # def test_inline_comment3(self):
    #     self.assertTrue(TestLexer.test("// This is a comment with \"\\\" inside.", "<EOF>", 103))
    # def test_inline_comment4(self):
    #     self.assertTrue(TestLexer.test("//*This is still a inline comment", "<EOF>", 104))
    # def test_inline_comment5(self):
    #     self.assertTrue(TestLexer.test("//*This is still a inline comment*/", "<EOF>", 105))
    # def test_block_comment1(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment */", "<EOF>", 106))
    # def test_block_comment2(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment \nwith multiple lines */", "<EOF>", 107))
    # def test_block_comment3(self):
    #     self.assertTrue(TestLexer.test("/* This is a block //comment */", "<EOF>", 108))
    # def test_block_comment4(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment end with \"* /\" */", "<EOF>", 109))
    # def test_block_comment5(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment \n//Inline Comment */", "<EOF>", 110))
    # def test_block_comment6(self):
    #     self.assertTrue(TestLexer.test("/* This is a unclose block comment ", "/,*,This,is,a,unclose,block,comment,<EOF>", 111))

    # def test_block_comment7(self):
    #     self.assertTrue(TestLexer.test("/* This is another block comment */ */", "*,/,<EOF>", 112))
    #     # *,/,<EOF>

    # def test_nested_comment1(self):
    #     self.assertTrue(TestLexer.test("// A line comment // contains another line comment . ", "<EOF>", 113))
    # def test_nested_comment2(self):
    #     self.assertTrue(TestLexer.test("/*a block cmt /*cover a block cmt*/ */ ", "*,/,<EOF>", 114))
    # def test_nested_comment3(self):
    #     self.assertTrue(TestLexer.test("/*block comment 1*/\n/*block comment2*///inline comment", "<EOF>", 115))
    
    # def test_identifier(self):
    #     self.assertTrue(TestLexer.test("my name is Hoa", "my,name,is,Hoa,<EOF>", 116))
    # def test_identifier2(self):
    #     self.assertTrue(TestLexer.test("__", "__,<EOF>", 117))
    # def test_identifier3(self):
    #     self.assertTrue(TestLexer.test("Ident 1 id1", "Ident,1,id1,<EOF>", 118))
    # def test_identifier4(self):
    #     self.assertTrue(TestLexer.test("1Cat+2_Dogs", "1,Cat,+,2,_Dogs,<EOF>", 101))
    # def test_identifier4(self):
    #     self.assertTrue(TestLexer.test("X/123", "X,/,123,<EOF>", 119))
    # def test_identifier5(self):
    #     self.assertTrue(TestLexer.test("_count 123number||sum", "_count,123,number,||,sum,<EOF>", 120))
    # def test_identifier6(self):
    #     self.assertTrue(TestLexer.test("1day, I go to _school123_.;", "1,day,,,I,go,to,_school123_,.,;,<EOF>", 121))
     
    # def test_keyword1(self):
    #     self.assertTrue(TestLexer.test("autobreakboolean", "autobreakboolean,<EOF>", 122))
    # def test_keyword2(self):
    #     self.assertTrue(TestLexer.test("integer function void", "integer,function,void,<EOF>", 123))
        
    # def test_integer1(self):
    #     self.assertTrue(TestLexer.test("0090", "0,0,90,<EOF>", 124))
    # def test_integer2(self):
    #     self.assertTrue(TestLexer.test("-090x90", "-,0,90,x90,<EOF>", 125))

    # def test_integer3(self):
    #     self.assertTrue(TestLexer.test("123 _123 1_23 123_ __123", "123,_123,123,123,_,__123,<EOF>", 126))

    # def test_integer4(self):
    #     self.assertTrue(TestLexer.test("123*901/10", "123,*,901,/,10,<EOF>", 127))

    # def test_integer5(self):
    #     self.assertTrue(TestLexer.test("1_23__456_", "123456,_,<EOF>", 128))

    # def test_integer6(self):
    #     self.assertTrue(TestLexer.test("5 + 100/20", "5,+,100,/,20,<EOF>", 129))
    # def test_integer7(self):
    #     self.assertTrue(TestLexer.test("-1000-10+-100/1", "-,1000,-,10,+,-,100,/,1,<EOF>", 130))
    # def test_integer8(self):
    #     self.assertTrue(TestLexer.test("80 < 120 && (3-7) >= 7", "80,<,120,&&,(,3,-,7,),>=,7,<EOF>", 131))
    # def test_integer9(self):
    #     self.assertTrue(TestLexer.test("5!=8 || 12%4 == 0", "5,!=,8,||,12,%,4,==,0,<EOF>", 132))
    # def test_integer10(self):
    #     self.assertTrue(TestLexer.test("x00_0 010 1000x", "x00_0,0,10,1000,x,<EOF>", 133))
    
    # def test_float1(self):
    #     self.assertTrue(TestLexer.test("1.2e10", "1.2e10,<EOF>", 101))
    # def test_float2(self):
    #     self.assertTrue(TestLexer.test(" 7.5 0.6 ", "7.5,0.6,<EOF>", 157))
    # def test_float3(self):
    #     self.assertTrue(TestLexer.test(" 5.1+1e5 ","5.1,+,1e5,<EOF>",158))
    # def test_float4(self):
    #     self.assertTrue(TestLexer.test(" 6.8+9.2 ","6.8,+,9.2,<EOF>",159))
    # def test_float5(self):
    #     self.assertTrue(TestLexer.test(" -1.3+1e3 ","-,1.3,+,1e3,<EOF>",160))

    # def test_float6(self):
    #     self.assertTrue(TestLexer.test(" .6 ",".,6,<EOF>",101))
    # def test_float7(self):
    #     self.assertTrue(TestLexer.test(" 7E15 ","7E15,<EOF>",101))

    # def test_float8(self):
    #     self.assertTrue(TestLexer.test(" 1.0e ","1.0,e,<EOF>",101))

    # def test_float9(self):
    #     self.assertTrue(TestLexer.test("4.1e3 ","4.1e3,<EOF>",101))
    # def test_float10(self):
    #     self.assertTrue(TestLexer.test(" 5e-8+6 ","5e-8,+,6,<EOF>",101))
    # def test_float11(self):
    #     self.assertTrue(TestLexer.test(" 10.0e-2.2e-3 ","10.0e-2,.2e-3,<EOF>",101))
   
    # def test_string(self):
    #     self.assertTrue(TestLexer.test(""""Hello World !" ""","""Hello World !,<EOF>""",101))
    # def test_string2(self):
    #     self.assertTrue(TestLexer.test(""""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture." ""","""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture.,<EOF>""",101))
    # def test_string3(self):
    #     self.assertTrue(TestLexer.test(""""Hello World !\"\n\"The result is: \"2 ""","""Hello World !,The result is: ,2,<EOF>""",101))
    # def test_string4(self):
    #     self.assertTrue(TestLexer.test(""""abc" ""","""abc,<EOF>""",101))
    # def test_string9(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\t"|"|b6783\\")&* ""","""%^&*(	,Error Token |""",101))
    
    # def test_string_comment(self):
    #     self.assertTrue(TestLexer.test(""" "Hello /*My*/ World" ""","""Hello /*My*/ World,<EOF>""",101))
    # ## chỗ này có lỗi ko? nếu có là unclosed string hay error token # 
    # def test_string_comment2(self):
    #     self.assertTrue(TestLexer.test(""" "Hello World/* " */  ""","""Hello World/* ,*,/,<EOF>""",101))
    # def test_string_comment3(self):
    #     self.assertTrue(TestLexer.test(""" "Hello //My World" ""","""Hello //My World,<EOF>""",101))
    
    # def test_string_escape(self):
    #     self.assertTrue(TestLexer.test(""""This is a string containing tab \t." """, """This is a string containing tab \t.,<EOF>""", 101))







    # def test_string_escape2(self):
    #     self.assertTrue(TestLexer.test("""\"He asked me: \"Where is John?\"\" """, 
    #     """He asked me: \"Where is John?\",<EOF>""", 151))
    # ## He asked me: "Where is John?" lồng string trong string


    # def test_string_escape3(self):
    #     self.assertTrue(TestLexer.test("""
    #     "This sentence contains new line
    #     "
    #     """, """Unclosed String: This sentence contains new line""", 152))

    # def test_unclosed_string17(self):
    #     self.assertTrue(TestLexer.test(""" "\\"" "'ab'c ""","""\\",Unclosed String: 'ab'c """,178))

    

    # def test_float10(self):
    #     self.assertTrue(TestLexer.test("e-10 0E e+0e 00.e .e-10 .0e1 .0e-1",
    #     "e,-,10,0,E,e,+,0,e,0,0,.,e,.,e,-,10,.0e1,.0e-1,<EOF>",133))
  

   
    # def test_string_escape4(self):
    #     self.assertTrue(TestLexer.test(""""Print it ( a line char \\n )" """, """Print it ( a line char \\n ),<EOF>""", 101))
    # def test_string_escape5(self):
    #     self.assertTrue(TestLexer.test(""""There is a backspace \b. before here." """, """There is a backspace \b. before here.,<EOF>""", 101))

    # def test_string_escape6(self):
    #     self.assertTrue(TestLexer.test(""""Multiple chars \\\\" """, """Multiple chars \\\\,<EOF>""", 101))
    # def test_string_escape7(self):
    #     self.assertTrue(TestLexer.test(""""He asked me: \\"Where is John?\\"" """, """He asked me: \\"Where is John?\\",<EOF>""", 101))
    # def test_string_escape8(self):
    #     self.assertTrue(TestLexer.test("""" Print integer number by \"printInt(anArg: int)\"" """, """ Print integer number by \"printInt(anArg: int)\",<EOF>""", 101))
    # def test_string_escape9(self):
    #     self.assertTrue(TestLexer.test(""""We combine \' \f. \t. \'" """, """We combine \' \f. \t. \',<EOF>""", 101))
    # def test_string_escape10(self):
    #     self.assertTrue(TestLexer.test(""""This is a string containing /*comment*/" """, """This is a string containing /*comment*/,<EOF>""", 101))
    # def test_string_escape11(self):
    #     self.assertTrue(TestLexer.test(""""He said: \'He said:\'I saw him.\'\'" """, """He said: \'He said:\'I saw him.\'\',<EOF>""", 101))
    # def test_string_escape12(self):
    #     self.assertTrue(TestLexer.test(""""He said: \"He said:\"I saw him.\"\"" """, """He said: \"He said:\"I saw him.\"\",<EOF>""", 101))
    # def test_unclosed_string13(self):
    #     self.assertTrue(TestLexer.test(""" " " "" " """,""" ,,Unclosed String:  """,101))
    # def test_unclosed_string14(self):
    #     self.assertTrue(TestLexer.test("""  "Test \n Unclosed String"  ""","""Unclosed String: Test \n""",101))
    # def test_unclosed_string15(self):
    #     self.assertTrue(TestLexer.test(""" "Test Unclosed String\\" \n" ""","""Unclosed String: Test Unclosed String\\" \n""",101))
    # def test_unclosed_string16(self):
    #     self.assertTrue(TestLexer.test(""" "line 1\\n line 2\n" ""","""Unclosed String: line 1\\n line 2\n""",101))
    # def test_unclosed_string17(self):
    #     self.assertTrue(TestLexer.test(""" "\\"" "'**'* ""","""\\",Unclosed String: '**'* """,101))
    # def test_unclosed_string18(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\n"|"|b6783\\")&* ""","""Unclosed String: %^&*(\n""",101))
    # def test_unclosed_string19(self):
    #     self.assertTrue(TestLexer.test("""\"Open string""", """Unclosed String: \"Open string""", 101))
    # def test_unclosed_string20(self):
    #     self.assertTrue(TestLexer.test(""" "Open string \n.\"""", """Unclosed String: \"Open string""", 101))
    
    # def test_illegal_string4(self):
    #     self.assertTrue(TestLexer.test("""  "abc123a\\mabc"  ""","""Illegal Escape In String: abc123a\\m""",101))
    # def test_illegal_string5(self):
    #     self.assertTrue(TestLexer.test("""   123-4"abc123a\\b\\iasVm"  ""","""123,-,4,Illegal Escape In String: abc123a\\b\\i""",101))
    # def test_illegal_string6(self):
    #     self.assertTrue(TestLexer.test("""  "Hi, this is abc \\h\\n\\t "  ""","""Illegal Escape In String: Hi, this is abc \h""",101))
    # def test_illegal_string7(self):
    #     self.assertTrue(TestLexer.test(""" "     " " " "" "\\t\\b\\g" ""","""     , ,,Illegal Escape In String: \\t\\b\\g""",101))
    # def test_illegal_string8(self):
    #     self.assertTrue(TestLexer.test(""" "X=004*0875.E-2\\087.02" ""","""Illegal Escape In String: X=004*0875.E-2\0""",101))
    # def test_illegal_string9(self):
    #     self.assertTrue(TestLexer.test(""" "illegal_escape\" ""","""Illegal Escape In String: illegal_escape\"""",101))
    # def test_illegal_string10(self):
    #     self.assertTrue(TestLexer.test(""" 
    #     "t \ {abcd}\\efg"
    #     ""","Illegal Escape In String: t \ ",101))


    # def test_operator(self):
    #     self.assertTrue(TestLexer.test("+ - * / ! % || && != == <= >= > < =", "+,-,*,/,!,%,||,&&,!=,==,<=,>=,>,<,=,<EOF>", 101))
    # def test_operator2(self):
    #     self.assertTrue(TestLexer.test("2*2 + 2^ 1", "2,*,2,+,2,Error Token ^", 101))
    # def test_operator3(self):
    #     self.assertTrue(TestLexer.test("do {print(a);} while (a & b);", "do,{,print,(,a,),;,},while,(,a,Error Token &", 101))
    # def test_operator4(self):
    #     self.assertTrue(TestLexer.test("income=income + salary*1.2*rate[1]+month#3;", "income,=,income,+,salary,*,1.2,*,rate,[,1,],+,month,Error Token #", 101))
    # def test_operator5(self):
    #     self.assertTrue(TestLexer.test("cost = sum((y-h(i))**2)", "cost,=,sum,(,(,y,-,h,(,i,),),*,*,2,),<EOF>", 101))
    # def test_operator6(self):
    #     self.assertTrue(TestLexer.test("x = (4 + 3i)(2 + 5i).i^2", "x,=,(,4,+,3,i,),(,2,+,5,i,),.,i,Error Token ^", 101))
    # def test_operator7(self):
    #     self.assertTrue(TestLexer.test("+-*/%*()/*//$#", "+,-,*,/,%,*,(,),/,*,<EOF>", 101))

    # def test_separators(self):
    #     self.assertTrue(TestLexer.test("(  ) [ ] { } ; ,  =", "(,),[,],{,},;,,,=,<EOF>", 101))
    
    # def test_full1(self):
    #     self.assertTrue(TestLexer.test("array[1+2,0]=0;","array,[,1,+,2,,,0,],=,0,;,<EOF>",101))
    # def test_full2(self):
    #     self.assertTrue(TestLexer.test("x,y,z: float = 1.20e10, 7E-2, 3*a","x,,,y,,,z,:,float,=,1.20e10,,,7E-2,,,3,*,a,<EOF>",101))
    # def test_full3(self):
    #     self.assertTrue(TestLexer.test("20>>3<<4<===>=b","20,>,>,3,<,<,4,<=,==,>=,b,<EOF>",101))
    # def test_full4(self):
    #     self.assertTrue(TestLexer.test("(2.2+03)||a!==3&a","(,2.2,+,0,3,),||,a,!=,=,3,Error Token &",101))
    # def test_full5(self):
    #     self.assertTrue(TestLexer.test("super(a[0,0],b*c-d,+3.4e-1+.0e-2);","super,(,a,[,0,,,0,],,,b,*,c,-,d,,,+,3.4e-1,+,.0e-2,),;,<EOF>",170)) 
                                                                            # super,(,a,[,0,,,0,],,,b,*,c,-,d,,,+,3.4e-1,+,.,e,-,2,),;,<EOF>
    # def test_float10(self):
    #     self.assertTrue(TestLexer.test("e-10 0E e+0e 00.e .e-10 .0e1 .0e-1","e,-,10,0,E,e,+,0,e,0,0,.,e,.,e,-,10,.0e1,.0e-1,<EOF>",101))   
    #     #xem lại                                                             e,-,10,0,E,e,+,0,e,0,0,.,e,.,e,-,10,.0e1,.0e-1,<EOF>
    # # def test_statement1(self):
    # #     self.assertTrue(TestLexer.test("a:string =\"Hello, World!\n\"","a,:,string,=,Unclosed String: Hello, World!\n",101))  # xem lại
    # def test_statement2(self):
    #     self.assertTrue(TestLexer.test("printInteger(123);","printInteger,(,123,),;,<EOF>", 101)) 
    # def test_statement3(self):
    #     self.assertTrue(TestLexer.test("arr: array[1,2] of integer = {{-1,2}};","arr,:,array,[,1,,,2,],of,integer,=,{,{,-,1,,,2,},},;,<EOF>", 101)) 
    # def test_statement3(self):
    #     self.assertTrue(TestLexer.test("printInteger(123);","printInteger,(,123,),;,<EOF>", 101)) 



#     def test_program_1(self):
#         self.assertTrue(TestLexer.test("""
# main : function void() {                                      
#     printString("Hello World");
#     return ;
# }
# """, "main,:,function,void,(,),{,printString,(,Hello World,),;,return,;,},<EOF>",101))
#     def test_program_2(self):
#         self.assertTrue(TestLexer.test("""
# main : function void() {                                       
# // first block
# {
#     // second block
#     {
#         // third block
#         {
#             // fourth block
#         }
#     }
# }}""", "main,:,function,void,(,),{,{,{,{,},},},},<EOF>",101))
#     def test_program_3(self):
#         self.assertTrue(TestLexer.test("""
# a : integer = 0;
# main : function void() {                                      
#     return a;
# }
# """, "a,:,integer,=,0,;,main,:,function,void,(,),{,return,a,;,},<EOF>",101))
#     def test_program_4(self):
#         self.assertTrue(TestLexer.test("""
# a : integer = 0;
# main : function void() {                                      
#     return a;
# }
# """, "a,:,integer,=,0,;,main,:,function,void,(,),{,return,a,;,},<EOF>",101))
#     def test_program_5(self):
#         self.assertTrue(TestLexer.test("""
# {
# r, s: integer;
# r = 2.0;
# a, b: array [5] of integer;
# s = r * r * myPI;
# a[0] = s;
# }
# """, "{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>",101))
#     def test_program_6(self):
#         self.assertTrue(TestLexer.test("""
# main: function void () {
#     if (a>b) if (true) printString("TRUE"); else printString("FALSE");
#     else printInteger(b);
#     return;
# }
# """, "main,:,function,void,(,),{,if,(,a,>,b,),if,(,true,),printString,(,TRUE,),;,else,printString,(,FALSE,),;,else,printInteger,(,b,),;,return,;,},<EOF>",101))
#     def test_program_7(self):
#         self.assertTrue(TestLexer.test("""
# main: function void () {
#     for (i = n, , i%2) printString("Computer is working...\n");
# }
# """, "main,:,function,void,(,),{,for,(,i,=,n,,,,,i,%,2,),printString,(,Unclosed String: Computer is working...\n",101))
#     def test_program_8(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 do {
#                     if (a == 10) break;
#                     a = a - 1; 
#                     printInteger(a);
#                 }
#                 while(a > 0);
#             }
# """, "main,:,function,void,(,),{,do,{,if,(,a,==,10,),break,;,a,=,a,-,1,;,printInteger,(,a,),;,},while,(,a,>,0,),;,},<EOF>",101))
#     def test_program_9(self):
#         self.assertTrue(TestLexer.test("""
#             main : function void() {
#                 a, b : integer = round(123.0e2), randomInt();
#                 /*
#                 Calculate sum of 2 numbers a & b
#                 */
#                 sum : integer = a + b + arr[0,0];
#                 print(a, sum);
#                 return ;
#             }
# """, "main,:,function,void,(,),{,a,,,b,:,integer,=,round,(,123.0e2,),,,randomInt,(,),;,sum,:,integer,=,a,+,b,+,arr,[,0,,,0,],;,print,(,a,,,sum,),;,return,;,},<EOF>",101))
#     def test_program_10(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void() {
#                 a : string = "Hello world"; // string 
#                 return a::"!";
#             }  
# """, "main,:,function,void,(,),{,a,:,string,=,Hello world,;,return,a,::,!,;,},<EOF>",101))
#     def test_program_11(self):
#         self.assertTrue(TestLexer.test("""
#             main : function void() {
#             foo(2__0 + -x_1, 4.0e-2 / y2);
#             goo();
#             return ;
#         } 
# """, "main,:,function,void,(,),{,foo,(,20,+,-,x_1,,,4.0e-2,/,y2,),;,goo,(,),;,return,;,},<EOF>",101))
#     def test_program_12(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 a = 2 + 2%2/2*-2 ;
#                 b = 1*1--1+1/1 ;
#                 c = a + b / (2*1.0+1) ;                
#             }
# """, "main,:,function,void,(,),{,a,=,2,+,2,%,2,/,2,*,-,2,;,b,=,1,*,1,-,-,1,+,1,/,1,;,c,=,a,+,b,/,(,2,*,1.0,+,1,),;,},<EOF>",101))
#     def test_program_13(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 a = true ;
#                 b = !a && false || (false && true || true) ;  
#                 c = !!b || false ;             
#             }
# """, "main,:,function,void,(,),{,a,=,true,;,b,=,!,a,&&,false,||,(,false,&&,true,||,true,),;,c,=,!,!,b,||,false,;,},<EOF>",101))
#     def test_program_14(self):
#         self.assertTrue(TestLexer.test("""
#             True : string = "It's true!" 
#             false : string = "it's not true..." 
# """, "True,:,string,=,It's true!,false,:,string,=,it's not true...,<EOF>",101))
    


class LexerSuite(unittest.TestCase):
    # def test_integer3(self):
    #     self.assertTrue(TestLexer.test("123 _123 1_23 123 __123", "123,_123,123,123,__123,<EOF>", 101))
    # def test_block_comment7(self):
    #     self.assertTrue(TestLexer.test("/* This is another block comment / */", "<EOF>", 101))

    # def test_1(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    
    # def test_2(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         //abc
    #         /* comment */ */            
    #         """
    #         , "*,/,<EOF>", 102))

    # def test_3(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         1234 123
    #         1_72
    #         1_234_567
    #         1.234 1.2e3 7E-10
    #         1_234.567
    #         e-10
    #         """
    #         , "1234,123,172,1234567,1.234,1.2e3,7E-10,1234.567,e,-,10,<EOF>", 103))

# !
    # def test_5(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         "This is a string containing tab \t"
    #         "He asked me: \\"Where is John?\\""
    #         """
    #         , """This is a string containing tab \t,He asked me: \\"Where is John?\\",<EOF>""", 1005))

            # This is a string containing tab 	,He asked me: "Where is John?",<EOF>

    # def test_6(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         auto break boolean do else
    #         false float for function if
    #         integer return string true while
    #         void out continue of inherit
    #         array
    #         """
    #         , """auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>""", 106))

    # def test_7(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         + - * / %
    #         ! && || ==
    #         != < <= > >=
    #         ::
    #         """
    #         , """+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>""", 107))

    # def test_8(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         ( ) [ ] . , ; : { } =
    #         """
    #         , """(,),[,],.,,,;,:,{,},=,<EOF>""", 108))

    # def test_9(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         x : integer = 65;
    #         fact : function integer (n : integer ) {
    #             if (n == 0) return 1 ;
    #             else return n * fact (n - 1 ) ;
    #         }
    #         inc : function void (out n : integer , delta : integer ) {
    #             n = n + delta ;
    #         }
    #         main : function void () {
    #             delta : integer = fact (3) ;
    #             inc(x,delta) ;
    #             printInteger(x) ;
    #         }
    #         """
    #         , """x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>""", 109))

    # def test_10(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         //abc
    #         /* commemts */
    #         // eof
    #         """
    #         , "<EOF>", 110))
    
    # def test_11(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         {1, 5, 7, 12} {"Kangxi", "Yongzheng", "Qianlong"}
    #         """
    #         , "{,1,,,5,,,7,,,12,},{,Kangxi,,,Yongzheng,,,Qianlong,},<EOF>", 111))

    # def test_12(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         x : array [2, 3] of integer;
    #         fact : function integer (n : integer ) {
    #             for (i = 1, i < 10, i + 1) {
    #                 writeInt(i);
    #             }
    #         }
    #         main : function void () {
    #             r, s: integer;
    #             r = 2.0;
    #             a, b: array [5] of integer;
    #             s = r * r * myPI;
    #             a[0] = s;
    #         }
    #         """
    #         , "x,:,array,[,2,,,3,],of,integer,;,fact,:,function,integer,(,n,:,integer,),{,for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},},main,:,function,void,(,),{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>", 112))

    # def test_inline_comment(self):
    #     self.assertTrue(TestLexer.test("// This is a comment", "<EOF>", 101))
    # def test_inline_comment2(self):
    #     self.assertTrue(TestLexer.test("// This is a comment \n", "<EOF>", 101))
    # def test_inline_comment3(self):
    #     self.assertTrue(TestLexer.test("// This is a comment with \"\\\" inside.", "<EOF>", 101))
    # def test_inline_comment4(self):
    #     self.assertTrue(TestLexer.test("//*This is still a inline comment", "<EOF>", 101))
    # def test_inline_comment5(self):
    #     self.assertTrue(TestLexer.test("//*This is still a inline comment*/", "<EOF>", 101))
    # def test_block_comment1(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment */", "<EOF>", 102))
    # def test_block_comment2(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment \nwith multiple lines */", "<EOF>", 102))
    # def test_block_comment3(self):
    #     self.assertTrue(TestLexer.test("/* This is a block //comment */", "<EOF>", 102))
    # def test_block_comment4(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment end with \"* /\" */", "<EOF>", 102))
    # def test_block_comment5(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment \n//Inline Comment */", "<EOF>", 102))
    # def test_block_comment6(self):
    #     self.assertTrue(TestLexer.test("/* This is a unclose block comment ", "/,*,This,is,a,unclose,block,comment,<EOF>", 102))
    # def test_block_comment7(self):
    #     self.assertTrue(TestLexer.test("/* This is another block comment */ */", "*,/,<EOF>", 101))
    # def test_nested_comment1(self):
    #     self.assertTrue(TestLexer.test("// A line comment // contains another line comment . ", "<EOF>", 101))
    # def test_nested_comment2(self):
    #     self.assertTrue(TestLexer.test("/*a block cmt /*cover a block cmt*/ */ ", "*,/,<EOF>", 101))
    # def test_nested_comment3(self):
    #     self.assertTrue(TestLexer.test("/*block comment 1*/\n/*block comment2*///inline comment", "<EOF>", 101))
    
























    # def test_identifier(self):
    #     self.assertTrue(TestLexer.test("my name is Hoa", "my,name,is,Hoa,<EOF>", 101))
    # def test_identifier2(self):
    #     self.assertTrue(TestLexer.test("__", "__,<EOF>", 101))
    # def test_identifier3(self):
    #     self.assertTrue(TestLexer.test("Ident 1 id1", "Ident,1,id1,<EOF>", 101))
    # # def test_identifier4(self):
    # #     self.assertTrue(TestLexer.test("1Cat+2_Dogs", "1,Cat,+,2,_Dogs,<EOF>", 101))
    # def test_identifier4(self):
    #     self.assertTrue(TestLexer.test("X/123", "X,/,123,<EOF>", 101))
    # def test_identifier5(self):
    #     self.assertTrue(TestLexer.test("_count 123number||sum", "_count,123,number,||,sum,<EOF>", 101))
    # def test_identifier6(self):
    #     self.assertTrue(TestLexer.test("1day, I go to _school123_.;", "1,day,,,I,go,to,_school123_,.,;,<EOF>", 101))
     
    # def test_keyword1(self):
    #     self.assertTrue(TestLexer.test("autobreakboolean", "autobreakboolean,<EOF>", 101))
    # def test_keyword2(self):
    #     self.assertTrue(TestLexer.test("integer function void", "integer,function,void,<EOF>", 101))
        
    # def test_integer1(self):
    #     self.assertTrue(TestLexer.test("0090", "0,0,90,<EOF>", 101))
    # def test_integer2(self):
    #     self.assertTrue(TestLexer.test("-090x90", "-,0,90,x90,<EOF>", 101))

    # # def test_integer3(self):
    # #     self.assertTrue(TestLexer.test("123 _123 1_23 123_ __123", "123,_123,123,123,__123,<EOF>", 101))

    # # def test_integer5(self):
    # #     self.assertTrue(TestLexer.test("1_23__456_", "123456,<EOF>", 101))

    # def test_integer4(self):
    #     self.assertTrue(TestLexer.test("123*901/10", "123,*,901,/,10,<EOF>", 101))
  
    # def test_integer6(self):
    #     self.assertTrue(TestLexer.test("5 + 100/20", "5,+,100,/,20,<EOF>", 101))
    # def test_integer7(self):
    #     self.assertTrue(TestLexer.test("-1000-10+-100/1", "-,1000,-,10,+,-,100,/,1,<EOF>", 101))
    # def test_integer8(self):
    #     self.assertTrue(TestLexer.test("80 < 120 && (3-7) >= 7", "80,<,120,&&,(,3,-,7,),>=,7,<EOF>", 101))
    # def test_integer9(self):
    #     self.assertTrue(TestLexer.test("5!=8 || 12%4 == 0", "5,!=,8,||,12,%,4,==,0,<EOF>", 101))
    # def test_integer10(self):
    #     self.assertTrue(TestLexer.test("x00_0 010 1000x", "x00_0,0,10,1000,x,<EOF>", 101))
    
    # def test_float1(self):
    #     self.assertTrue(TestLexer.test("1.2e10", "1.2e10,<EOF>", 101))
    # def test_float2(self):
    #     self.assertTrue(TestLexer.test(" 7.5 0.6 ", "7.5,0.6,<EOF>", 101))
    # def test_float3(self):
    #     self.assertTrue(TestLexer.test(" 5.1+1e5 ","5.1,+,1e5,<EOF>",101))
    # def test_float4(self):
    #     self.assertTrue(TestLexer.test(" 6.8+9.2 ","6.8,+,9.2,<EOF>",101))
    # def test_float5(self):
    #     self.assertTrue(TestLexer.test(" -1.3+1e3 ","-,1.3,+,1e3,<EOF>",101))
    # def test_float6(self):
    #     self.assertTrue(TestLexer.test(" .6 ",".,6,<EOF>",101))
    # def test_float7(self):
    #     self.assertTrue(TestLexer.test(" 7E15 ","7E15,<EOF>",101))
    # def test_float8(self):
    #     self.assertTrue(TestLexer.test(" 1.0e ","1.0,e,<EOF>",101))
    # def test_float9(self):
    #     self.assertTrue(TestLexer.test("4.1e3 ","4.1e3,<EOF>",101))
    # def test_float10(self):
    #     self.assertTrue(TestLexer.test(" 5e-8+6 ","5e-8,+,6,<EOF>",101))
    # def test_float11(self):
    #     self.assertTrue(TestLexer.test(" 10.0e-2.2e-3 ","10.0e-2,.2e-3,<EOF>",101))
   
    # def test_string(self):
    #     self.assertTrue(TestLexer.test(""""Hello World !" ""","""Hello World !,<EOF>""",101))
    # def test_string2(self):
    #     self.assertTrue(TestLexer.test(""""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture." ""","""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture.,<EOF>""",101))
    # def test_string3(self):
    #     self.assertTrue(TestLexer.test(""""Hello World !\"\n\"The result is: \"2 ""","""Hello World !,The result is: ,2,<EOF>""",101))
    # # def test_string4(self):
    # #     self.assertTrue(TestLexer.test(""""abc" ""","""abc,<EOF>""",101))
    # def test_string9(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\t"|"|b6783\\")&* ""","""%^&*(	,Error Token |""",101))
    
    # def test_string_comment(self):
    #     self.assertTrue(TestLexer.test(""" "Hello /*My*/ World" ""","""Hello /*My*/ World,<EOF>""",101))
    # ## chỗ này có lỗi ko? nếu có là unclosed string hay error token # 
    # # def test_string_comment2(self):
    # #     self.assertTrue(TestLexer.test(""" "Hello World/* " */  ""","""Hello World/* ,*,/,<EOF>""",101))
    # def test_string_comment3(self):
    #     self.assertTrue(TestLexer.test(""" "Hello //My World" ""","""Hello //My World,<EOF>""",101))
    
    # def test_string_escape(self):
    #     self.assertTrue(TestLexer.test(""""This is a string containing tab \t." """, """This is a string containing tab \t.,<EOF>""", 101))

    
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!

#     def test_unclosed_string15(self):
#         self.assertTrue(TestLexer.test(""" "Test Unclosed String\\" \n" ""","""Unclosed String: Test Unclosed String\\" \n""",1014))
#                                                                                 #  Unclosed String: "Test Unclosed String\" 
                          
#     def test_string_escape7(self):
#         self.assertTrue(TestLexer.test(""""He asked me: \\"Where is John?\\"" """, """He asked me: \\"Where is John?\\",<EOF>""", 1010))



#     def test_string_escape3(self):
#         self.assertTrue(TestLexer.test(""""This sentence contains new line\n." """, """Unclosed String: This sentence contains new line\n""", 1007))

#     def test_string_escape4(self):
#         self.assertTrue(TestLexer.test(""""Print it ( a line char \\n )" """, """Print it ( a line char \\n ),<EOF>""", 101))
#     def test_string_escape5(self):
#         self.assertTrue(TestLexer.test(""""There is a backspace \b. before here." """, """There is a backspace \b. before here.,<EOF>""", 101))




   




#     def test_string_escape6(self):
#         self.assertTrue(TestLexer.test(""""Multiple chars \\\\" """, """Multiple chars \\\\,<EOF>""", 1009))
    
#                                                                                     #   He asked me: "Where is John?",<EOF>
#     def test_string_escape8(self):
#         self.assertTrue(TestLexer.test("""" Print integer number by \"printInt(anArg: int)\"" """, """ Print integer number by ,printInt,(,anArg,:,int,),,<EOF>""", 1011))
#     def test_string_escape9(self):
#         self.assertTrue(TestLexer.test(""""We combine \' \f. \t. \'" """, """We combine \' \f. \t. \',<EOF>""", 101))
#     def test_string_escape10(self):
#         self.assertTrue(TestLexer.test(""""This is a string containing /*comment*/" """, """This is a string containing /*comment*/,<EOF>""", 101))
#     def test_string_escape11(self):
#         self.assertTrue(TestLexer.test(""""He said: \'He said:\'I saw him.\'\'" """, """He said: \'He said:\'I saw him.\'\',<EOF>""", 101))
#     def test_string_escape12(self):
#         self.assertTrue(TestLexer.test(""""He said: \\"He said:\\"I saw him.\\"\\"" """, """He said: \\"He said:\\"I saw him.\\"\\",<EOF>""", 1000))



#     def test_unclosed_string13(self):
#         self.assertTrue(TestLexer.test(""" " " "" " """,""" ,,Unclosed String:  """,101))
#     def test_unclosed_string14(self):
#         self.assertTrue(TestLexer.test("""  "Test \n Unclosed String"  ""","""Unclosed String: Test \n""",101))
#     def test_unclosed_string15(self):
#         self.assertTrue(TestLexer.test(""" "Test Unclosed String\\" \n" ""","""Unclosed String: Test Unclosed String\\" \n""",101))
#     def test_unclosed_string16(self):
#         self.assertTrue(TestLexer.test(""" "line 1\\n line 2\n" ""","""Unclosed String: line 1\\n line 2\n""",101))
#     def test_unclosed_string17(self):
#         self.assertTrue(TestLexer.test(""" "\\"" "'ab'c ""","""\\",Unclosed String: 'ab'c """,101))
#     def test_unclosed_string18(self):
#         self.assertTrue(TestLexer.test(""" "%^&*(\n"|"|b6783\\")&* ""","""Unclosed String: %^&*(\n""",101))
#     def test_unclosed_string19(self):
#         self.assertTrue(TestLexer.test(""""\\"Open string""", """Unclosed String: \\"Open string""", 101))
#     def test_unclosed_string20(self):
#         self.assertTrue(TestLexer.test(""" "Open string \n.\\" """, """Unclosed String: Open string \n""", 303))
    
#     def test_illegal_string4(self):
#         self.assertTrue(TestLexer.test("""  "abc123a\\mabc"  ""","""Illegal Escape In String: abc123a\\m""",301))
#     def test_illegal_string5(self):
#         self.assertTrue(TestLexer.test("""   123-4"abc123a\\b\\iasVm"  ""","""123,-,4,Illegal Escape In String: abc123a\\b\\i""",302))
#     def test_illegal_string6(self):
#         self.assertTrue(TestLexer.test("""  "Hi, this is abc \\h\\n\\t "  ""","""Illegal Escape In String: Hi, this is abc \h""",303))
#     def test_illegal_string7(self):
#         self.assertTrue(TestLexer.test(""" "     " " " "" "\\t\\b\\g" ""","""     , ,,Illegal Escape In String: \\t\\b\\g""",304))
#     def test_illegal_string8(self):
#         self.assertTrue(TestLexer.test(""" "X=004*0875.E-2\\087.02" ""","""Illegal Escape In String: X=004*0875.E-2\\0""",305))
#     def test_illegal_string9(self):
#         self.assertTrue(TestLexer.test(""" "illegal_escape\" ""","""illegal_escape,<EOF>""",306))
#     def test_illegal_string10(self):
#         self.assertTrue(TestLexer.test(""" 
#         "t \ {abcd}\\efg"
#         ""","Illegal Escape In String: t \ ",101))






#     def test_operator(self):
#         self.assertTrue(TestLexer.test("+ - * / ! % || && != == <= >= > < =", "+,-,*,/,!,%,||,&&,!=,==,<=,>=,>,<,=,<EOF>", 101))
#     def test_operator2(self):
#         self.assertTrue(TestLexer.test("2*2 + 2^ 1", "2,*,2,+,2,Error Token ^", 101))
#     def test_operator3(self):
#         self.assertTrue(TestLexer.test("do {print(a);} while (a & b);", "do,{,print,(,a,),;,},while,(,a,Error Token &", 101))
#     def test_operator4(self):
#         self.assertTrue(TestLexer.test("income=income + salary*1.2*rate[1]+month#3;", "income,=,income,+,salary,*,1.2,*,rate,[,1,],+,month,Error Token #", 101))
#     def test_operator5(self):
#         self.assertTrue(TestLexer.test("cost = sum((y-h(i))**2)", "cost,=,sum,(,(,y,-,h,(,i,),),*,*,2,),<EOF>", 101))
#     def test_operator6(self):
#         self.assertTrue(TestLexer.test("x = (4 + 3i)(2 + 5i).i^2", "x,=,(,4,+,3,i,),(,2,+,5,i,),.,i,Error Token ^", 101))
#     def test_operator7(self):
#         self.assertTrue(TestLexer.test("+-*/%*()/*//$#", "+,-,*,/,%,*,(,),/,*,<EOF>", 101))











#     def test_separators(self):
#         self.assertTrue(TestLexer.test("(  ) [ ] { } ; ,  =", "(,),[,],{,},;,,,=,<EOF>", 101))
    
#     def test_full1(self):
#         self.assertTrue(TestLexer.test("array[1+2,0]=0;","array,[,1,+,2,,,0,],=,0,;,<EOF>",101))
#     def test_full2(self):
#         self.assertTrue(TestLexer.test("x,y,z: float = 1.20e10, 7E-2, 3*a","x,,,y,,,z,:,float,=,1.20e10,,,7E-2,,,3,*,a,<EOF>",101))
#     def test_full3(self):
#         self.assertTrue(TestLexer.test("20>>3<<4<===>=b","20,>,>,3,<,<,4,<=,==,>=,b,<EOF>",101))
#     def test_full4(self):
#         self.assertTrue(TestLexer.test("(2.2+03)||a!==3&a","(,2.2,+,0,3,),||,a,!=,=,3,Error Token &",101))
#     def test_full5(self):
#         self.assertTrue(TestLexer.test("super(a[0,0],b*c-d,+3.4e-1+.e-2);","super,(,a,[,0,,,0,],,,b,*,c,-,d,,,+,3.4e-1,+,.e-2,),;,<EOF>",101)) 
    
#     def test_float10(self): 
#         self.assertTrue(TestLexer.test("0.e-11 1.2E-22 0E 00.e .0e1 .0e-1","0.e-11,1.2E-22,0,E,0,0.,e,.0e1,.0e-1,<EOF>",101))   
#     def test_string_escape2(self):
#         self.assertTrue(TestLexer.test(""""He asked me: \\"Where is John?\\"" """, """He asked me: \\"Where is John?\\",<EOF>""", 151))
#     ## He asked me: "Where is John?" lồng string trong string
#     def test_string_escape3(self):
#         self.assertTrue(TestLexer.test("""
#         "This sentence contains new line
#         "
#         """, """Unclosed String: This sentence contains new line\n""", 152))
#     def test_statement1(self):
#         self.assertTrue(TestLexer.test("a:string =\"Hello, World!\n\"","a,:,string,=,Unclosed String: Hello, World!\n",101))  # xem lại
#     def test_statement2(self):
#         self.assertTrue(TestLexer.test("printInteger(123);","printInteger,(,123,),;,<EOF>", 101)) 
#     def test_statement3(self):
#         self.assertTrue(TestLexer.test("arr: array[1,2] of integer = {{-1,2}};","arr,:,array,[,1,,,2,],of,integer,=,{,{,-,1,,,2,},},;,<EOF>", 101)) 
#     def test_statement3(self):
#         self.assertTrue(TestLexer.test("printInteger(123);","printInteger,(,123,),;,<EOF>", 101)) 
#     def test_program_1(self):
#         self.assertTrue(TestLexer.test("""
# main : function void() {                                      
#     printString("Hello World");
#     return ;
# }
# """, "main,:,function,void,(,),{,printString,(,Hello World,),;,return,;,},<EOF>",101))
#     def test_program_2(self):
#         self.assertTrue(TestLexer.test("""
# main : function void() {                                       
# // first block
# {
#     // second block
#     {
#         // third block
#         {
#             // fourth block
#         }
#     }
# }}""", "main,:,function,void,(,),{,{,{,{,},},},},<EOF>",101))
#     def test_program_3(self):
#         self.assertTrue(TestLexer.test("""
# a : integer = 0;
# main : function void() {                                      
#     return a;
# }
# """, "a,:,integer,=,0,;,main,:,function,void,(,),{,return,a,;,},<EOF>",101))
#     def test_program_4(self):
#         self.assertTrue(TestLexer.test("""
# a : integer = 0;
# main : function void() {                                      
#     return a;
# }
# """, "a,:,integer,=,0,;,main,:,function,void,(,),{,return,a,;,},<EOF>",101))
#     def test_program_5(self):
#         self.assertTrue(TestLexer.test("""
# {
# r, s: integer;
# r = 2.0;
# a, b: array [5] of integer;
# s = r * r * myPI;
# a[0] = s;
# }
# """, "{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>",101))
#     def test_program_6(self):
#         self.assertTrue(TestLexer.test("""
# main: function void () {
#     if (a>b) if (true) printString("TRUE"); else printString("FALSE");
#     else printInteger(b);
#     return;
# }
# """, "main,:,function,void,(,),{,if,(,a,>,b,),if,(,true,),printString,(,TRUE,),;,else,printString,(,FALSE,),;,else,printInteger,(,b,),;,return,;,},<EOF>",101))
#     def test_program_7(self):
#         self.assertTrue(TestLexer.test("""
# main: function void () {
#     for (i = n, , i%2) printString("Computer is working...\n");
# }
# """, "main,:,function,void,(,),{,for,(,i,=,n,,,,,i,%,2,),printString,(,Unclosed String: Computer is working...\n",101))
#     def test_program_8(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 do {
#                     if (a == 10) break;
#                     a = a - 1; 
#                     printInteger(a);
#                 }
#                 while(a > 0);
#             }
# """, "main,:,function,void,(,),{,do,{,if,(,a,==,10,),break,;,a,=,a,-,1,;,printInteger,(,a,),;,},while,(,a,>,0,),;,},<EOF>",101))
#     def test_program_9(self):
#         self.assertTrue(TestLexer.test("""
#             main : function void() {
#                 a, b : integer = round(123.0e2), randomInt();
#                 /*
#                 Calculate sum of 2 numbers a & b
#                 */
#                 sum : integer = a + b + arr[0,0];
#                 print(a, sum);
#                 return ;
#             }
# """, "main,:,function,void,(,),{,a,,,b,:,integer,=,round,(,123.0e2,),,,randomInt,(,),;,sum,:,integer,=,a,+,b,+,arr,[,0,,,0,],;,print,(,a,,,sum,),;,return,;,},<EOF>",101))
#     def test_program_10(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void() {
#                 a : string = "Hello world"; // string 
#                 return a::"!";
#             }  
# """, "main,:,function,void,(,),{,a,:,string,=,Hello world,;,return,a,::,!,;,},<EOF>",101))
#     def test_program_11(self):
#         self.assertTrue(TestLexer.test("""
#             main : function void() {
#             foo(2__0 + -x_1, 4.0e-2 / y2);
#             goo();
#             return ;
#         } 
# """, "main,:,function,void,(,),{,foo,(,20,+,-,x_1,,,4.0e-2,/,y2,),;,goo,(,),;,return,;,},<EOF>",101))
#     def test_program_12(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 a = 2 + 2%2/2*-2 ;
#                 b = 1*1--1+1/1 ;
#                 c = a + b / (2*1.0+1) ;                
#             }
# """, "main,:,function,void,(,),{,a,=,2,+,2,%,2,/,2,*,-,2,;,b,=,1,*,1,-,-,1,+,1,/,1,;,c,=,a,+,b,/,(,2,*,1.0,+,1,),;,},<EOF>",101))
#     def test_program_13(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 a = true ;
#                 b = !a && false || (false && true || true) ;  
#                 c = !!b || false ;             
#             }
# """, "main,:,function,void,(,),{,a,=,true,;,b,=,!,a,&&,false,||,(,false,&&,true,||,true,),;,c,=,!,!,b,||,false,;,},<EOF>",101))
#     def test_program_14(self):
#         self.assertTrue(TestLexer.test("""
#             True : string = "It's true!" 
#             false : string = "it's not true..." 
# """, "True,:,string,=,It's true!,false,:,string,=,it's not true...,<EOF>",101))
#     def test_integer3(self):
#         self.assertTrue(TestLexer.test("123 _123 1_23 0123__45_6 __123", "123,_123,123,0,123456,__123,<EOF>", 1002))
#     def test_integer5(self):
#         self.assertTrue(TestLexer.test("1_23__456_", "123456,<EOF>", 1003))



















    # def test_string_escape3(self):
    #     self.assertTrue(TestLexer.test(""" "This sentence contains new line\n." """, """Unclosed String: This sentence contains new line\n""", 1007))
    # def test_unclosed_string13(self):
    #     self.assertTrue(TestLexer.test(""" " " "" " """,""" ,,Unclosed String:  """,101))
    # def test_unclosed_string14(self):
    #     self.assertTrue(TestLexer.test("""  "Test \n Unclosed String"  ""","""Unclosed String: Test \n""",101))
    # def test_unclosed_string15(self):
    #     self.assertTrue(TestLexer.test(""" "Test Unclosed String\\" \n" ""","""Unclosed String: Test Unclosed String\\" \n""",101))
    # def test_unclosed_string16(self):
    #     self.assertTrue(TestLexer.test(""" "line 1\\n line 2\n" ""","""Unclosed String: line 1\\n line 2\n""",101))
    # def test_unclosed_string17(self):
    #     self.assertTrue(TestLexer.test(""" "\\"" "'ab'c ""","""\\",Unclosed String: 'ab'c """,101))
    # def test_unclosed_string18(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\n"|"|b6783\\")&* ""","""Unclosed String: %^&*(\n""",101))
    # def test_unclosed_string19(self):
    #     self.assertTrue(TestLexer.test(""""\\"Open string""", """Unclosed String: \\"Open string""", 101))
    # def test_unclosed_string20(self):
    #     self.assertTrue(TestLexer.test(""" "Open string \n.\\" """, """Unclosed String: Open string \n""", 303))
    # def test_unclosed_string18(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\n"|"|b6783\\")&* ""","""Unclosed String: %^&*(\n""",101))
    # def test_float11(self):
    #     self.assertTrue(TestLexer.test(" .2e-3 .E2 .e-22 10.0e-2.2e-3 1. 1.e2 1.2E+10 2.45e-333 0.22 0.e2 23e8 4E 9e-10.34 ",".2e-3,.E2,.e-22,10.0e-2,.2e-3,1.,1.e2,1.2E+10,2.45e-333,0.22,0.e2,23e8,4,E,9e-10,.,34,<EOF>",101))
    # def test_integer3(self):
    #     self.assertTrue(TestLexer.test("123 _123 1_23 123 __123", "123,_123,123,123,__123,<EOF>", 101))
    # def test_block_comment7(self):
    #     self.assertTrue(TestLexer.test("/* This is another block comment / */", "<EOF>", 101))

    # def test_1(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    
    # def test_2(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         //abc
    #         /* comment */ */            
    #         """
    #         , "*,/,<EOF>", 102))

    # def test_3(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         1234 123
    #         1_72
    #         1_234_567
    #         1.234 1.2e3 7E-10
    #         1_234.567
    #         e-10
    #         """
    #         , "1234,123,172,1234567,1.234,1.2e3,7E-10,1234.567,e,-,10,<EOF>", 103))

    # def test_5(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         "This is a string containing tab \t"
    #         "He asked me: \\"Where is John?\\""
    #         """
    #         , """This is a string containing tab \t,He asked me: \\"Where is John?\\",<EOF>""", 105))

    # def test_6(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         auto break boolean do else
    #         false float for function if
    #         integer return string true while
    #         void out continue of inherit
    #         array
    #         """
    #         , """auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>""", 106))

    # def test_7(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         + - * / %
    #         ! && || ==
    #         != < <= > >=
    #         ::
    #         """
    #         , """+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>""", 107))

    # def test_8(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         ( ) [ ] . , ; : { } =
    #         """
    #         , """(,),[,],.,,,;,:,{,},=,<EOF>""", 108))

    # def test_9(self):
    #     """intlit floatlit"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         x : integer = 65;
    #         fact : function integer (n : integer ) {
    #             if (n == 0) return 1 ;
    #             else return n * fact (n - 1 ) ;
    #         }
    #         inc : function void (out n : integer , delta : integer ) {
    #             n = n + delta ;
    #         }
    #         main : function void () {
    #             delta : integer = fact (3) ;
    #             inc(x,delta) ;
    #             printInteger(x) ;
    #         }
    #         """
    #         , """x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>""", 109))

    # def test_10(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         //abc
    #         /* commemts */
    #         // eof
    #         """
    #         , "<EOF>", 110))
    
    # def test_11(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         {1, 5, 7, 12} {"Kangxi", "Yongzheng", "Qianlong"}
    #         """
    #         , "{,1,,,5,,,7,,,12,},{,Kangxi,,,Yongzheng,,,Qianlong,},<EOF>", 111))

    # def test_12(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test(
    #         """
    #         x : array [2, 3] of integer;
    #         fact : function integer (n : integer ) {
    #             for (i = 1, i < 10, i + 1) {
    #                 writeInt(i);
    #             }
    #         }
    #         main : function void () {
    #             r, s: integer;
    #             r = 2.0;
    #             a, b: array [5] of integer;
    #             s = r * r * myPI;
    #             a[0] = s;
    #         }
    #         """
    #         , "x,:,array,[,2,,,3,],of,integer,;,fact,:,function,integer,(,n,:,integer,),{,for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},},main,:,function,void,(,),{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>", 112))

    # def test_inline_comment(self):
    #     self.assertTrue(TestLexer.test("// This is a comment", "<EOF>", 101))
    # def test_inline_comment2(self):
    #     self.assertTrue(TestLexer.test("// This is a comment \n", "<EOF>", 101))
    # def test_inline_comment3(self):
    #     self.assertTrue(TestLexer.test("// This is a comment with \"\\\" inside.", "<EOF>", 101))
    # def test_inline_comment4(self):
    #     self.assertTrue(TestLexer.test("//*This is still a inline comment", "<EOF>", 101))
    # def test_inline_comment5(self):
    #     self.assertTrue(TestLexer.test("//*This is still a inline comment*/", "<EOF>", 101))
    # def test_block_comment1(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment */", "<EOF>", 102))
    # def test_block_comment2(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment \nwith multiple lines */", "<EOF>", 102))
    # def test_block_comment3(self):
    #     self.assertTrue(TestLexer.test("/* This is a block //comment */", "<EOF>", 102))
    # def test_block_comment4(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment end with \"* /\" */", "<EOF>", 102))
    # def test_block_comment5(self):
    #     self.assertTrue(TestLexer.test("/* This is a block comment \n//Inline Comment */", "<EOF>", 102))
    # def test_block_comment6(self):
    #     self.assertTrue(TestLexer.test("/* This is a unclose block comment ", "/,*,This,is,a,unclose,block,comment,<EOF>", 102))
    # def test_block_comment7(self):
    #     self.assertTrue(TestLexer.test("/* This is another block comment */ */", "*,/,<EOF>", 101))
    # def test_nested_comment1(self):
    #     self.assertTrue(TestLexer.test("// A line comment // contains another line comment . ", "<EOF>", 101))
    # def test_nested_comment2(self):
    #     self.assertTrue(TestLexer.test("/*a block cmt /*cover a block cmt*/ */ ", "*,/,<EOF>", 101))
    # def test_nested_comment3(self):
    #     self.assertTrue(TestLexer.test("/*block comment 1*/\n/*block comment2*///inline comment", "<EOF>", 101))
    
    # def test_identifier(self):
    #     self.assertTrue(TestLexer.test("my name is Hoa", "my,name,is,Hoa,<EOF>", 101))
    # def test_identifier2(self):
    #     self.assertTrue(TestLexer.test("__", "__,<EOF>", 101))
    # def test_identifier3(self):
    #     self.assertTrue(TestLexer.test("Ident 1 id1", "Ident,1,id1,<EOF>", 101))
    # # def test_identifier4(self):
    # #     self.assertTrue(TestLexer.test("1Cat+2_Dogs", "1,Cat,+,2,_Dogs,<EOF>", 101))
    # def test_identifier4(self):
    #     self.assertTrue(TestLexer.test("X/123", "X,/,123,<EOF>", 101))
    # def test_identifier5(self):
    #     self.assertTrue(TestLexer.test("_count 123number||sum", "_count,123,number,||,sum,<EOF>", 101))
    # def test_identifier6(self):
    #     self.assertTrue(TestLexer.test("1day, I go to _school123_.;", "1,day,,,I,go,to,_school123_,.,;,<EOF>", 101))
     
    # def test_keyword1(self):
    #     self.assertTrue(TestLexer.test("autobreakboolean", "autobreakboolean,<EOF>", 101))
    # def test_keyword2(self):
    #     self.assertTrue(TestLexer.test("integer function void", "integer,function,void,<EOF>", 101))
        
    # def test_integer1(self):
    #     self.assertTrue(TestLexer.test("0090", "0,0,90,<EOF>", 101))
    # def test_integer2(self):
    #     self.assertTrue(TestLexer.test("-090x90", "-,0,90,x90,<EOF>", 101))
    # def test_integer3(self):
    #     self.assertTrue(TestLexer.test("123 _123 1_23 123_ __123", "123,_123,123,123,__123,<EOF>", 101))
    # def test_integer4(self):
    #     self.assertTrue(TestLexer.test("123*901/10", "123,*,901,/,10,<EOF>", 101))

   
    


    # def test_integer6(self):
    #     self.assertTrue(TestLexer.test("5 + 100/20", "5,+,100,/,20,<EOF>", 101))
    # def test_integer7(self):
    #     self.assertTrue(TestLexer.test("-1000-10+-100/1", "-,1000,-,10,+,-,100,/,1,<EOF>", 101))
    # def test_integer8(self):
    #     self.assertTrue(TestLexer.test("80 < 120 && (3-7) >= 7", "80,<,120,&&,(,3,-,7,),>=,7,<EOF>", 101))
    # def test_integer9(self):
    #     self.assertTrue(TestLexer.test("5!=8 || 12%4 == 0", "5,!=,8,||,12,%,4,==,0,<EOF>", 101))
    # def test_integer10(self):
    #     self.assertTrue(TestLexer.test("x00_0 010 1000x", "x00_0,0,10,1000,x,<EOF>", 101))
    
    # def test_float1(self):
    #     self.assertTrue(TestLexer.test("1.2e10", "1.2e10,<EOF>", 101))
    # def test_float2(self):
    #     self.assertTrue(TestLexer.test(" 7.5 0.6 ", "7.5,0.6,<EOF>", 101))
    # def test_float3(self):
    #     self.assertTrue(TestLexer.test(" 5.1+1e5 ","5.1,+,1e5,<EOF>",101))
    # def test_float4(self):
    #     self.assertTrue(TestLexer.test(" 6.8+9.2 ","6.8,+,9.2,<EOF>",101))
    # def test_float5(self):
    #     self.assertTrue(TestLexer.test(" -1.3+1e3 ","-,1.3,+,1e3,<EOF>",101))
    # def test_float6(self):
    #     self.assertTrue(TestLexer.test(" .6 ",".,6,<EOF>",101))
    # def test_float7(self):
    #     self.assertTrue(TestLexer.test(" 7E15 ","7E15,<EOF>",101))
    # def test_float8(self):
    #     self.assertTrue(TestLexer.test(" 1.0e ","1.0,e,<EOF>",101))
    # def test_float9(self):
    #     self.assertTrue(TestLexer.test("4.1e3 ","4.1e3,<EOF>",101))

   
    


    # def test_float11(self):
    #     self.assertTrue(TestLexer.test(" 10.0e-2.2e-3 ","10.0e-2,.2e-3,<EOF>",101))
   
    # def test_string(self):
    #     self.assertTrue(TestLexer.test(""""Hello World !" ""","""Hello World !,<EOF>""",101))
    # def test_string2(self):
    #     self.assertTrue(TestLexer.test(""""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture." ""","""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture.,<EOF>""",101))
    # def test_string3(self):
    #     self.assertTrue(TestLexer.test(""""Hello World !\"\n\"The result is: \"2 ""","""Hello World !,The result is: ,2,<EOF>""",101))
    # # def test_string4(self):
    # #     self.assertTrue(TestLexer.test(""""abc" ""","""abc,<EOF>""",101))
    # def test_string9(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\t"|"|b6783\\")&* ""","""%^&*(	,Error Token |""",101))
    
    # def test_string_comment(self):
    #     self.assertTrue(TestLexer.test(""" "Hello /*My*/ World" ""","""Hello /*My*/ World,<EOF>""",101))
    # ## chỗ này có lỗi ko? nếu có là unclosed string hay error token # 
    # # def test_string_comment2(self):
    # #     self.assertTrue(TestLexer.test(""" "Hello World/* " */  ""","""Hello World/* ,*,/,<EOF>""",101))
    # def test_string_comment3(self):
    #     self.assertTrue(TestLexer.test(""" "Hello //My World" ""","""Hello //My World,<EOF>""",101))
    
    # def test_string_escape(self):
    #     self.assertTrue(TestLexer.test(""""This is a string containing tab \t." """, """This is a string containing tab \t.,<EOF>""", 101))
    # def test_string_escape2(self):
    #     self.assertTrue(TestLexer.test(""""He asked me: \"Where is John?\"" """, """He asked me: \"Where is John?\",<EOF>""", 101))
    # ## He asked me: "Where is John?" lồng string trong string
    # def test_string_escape3(self):
    #     self.assertTrue(TestLexer.test(""""This sentence contains new line\n." """, """Unclosed String: \"This sentence contains new line\n""", 101))
    # def test_string_escape4(self):
    #     self.assertTrue(TestLexer.test(""""Print it ( a line char \\n )" """, """Print it ( a line char \\n ),<EOF>""", 101))
    # def test_string_escape5(self):
    #     self.assertTrue(TestLexer.test(""""There is a backspace \b. before here." """, """There is a backspace \b. before here.,<EOF>""", 101))
    # def test_string_escape6(self):
    #     self.assertTrue(TestLexer.test(""""Multiple chars \\\\" """, """Multiple chars \\\\,<EOF>""", 101))
    # def test_string_escape7(self):
    #     self.assertTrue(TestLexer.test(""""He asked me: \\"Where is John?\\"" """, """He asked me: \\"Where is John?\\",<EOF>""", 101))
    # def test_string_escape8(self):
    #     self.assertTrue(TestLexer.test("""" Print integer number by \"printInt(anArg: int)\"" """, """ Print integer number by ,printInt,(,anArg,:,int,),,<EOF>""", 1001))
    # def test_string_escape9(self):
    #     self.assertTrue(TestLexer.test(""""We combine \' \f. \t. \'" """, """We combine \' \f. \t. \',<EOF>""", 101))
    # def test_string_escape10(self):
    #     self.assertTrue(TestLexer.test(""""This is a string containing /*comment*/" """, """This is a string containing /*comment*/,<EOF>""", 101))
    # def test_string_escape11(self):
    #     self.assertTrue(TestLexer.test(""""He said: \'He said:\'I saw him.\'\'" """, """He said: \'He said:\'I saw him.\'\',<EOF>""", 101))
    # def test_string_escape12(self):
    #     self.assertTrue(TestLexer.test(""""He said: \\"He said:\\"I saw him.\\"\\"" """, """He said: \\"He said:\\"I saw him.\\"\\",<EOF>""", 1000))
    # def test_unclosed_string13(self):
    #     self.assertTrue(TestLexer.test(""" " " "" " """,""" ,,Unclosed String:  """,101))
    # def test_unclosed_string14(self):
    #     self.assertTrue(TestLexer.test("""  "Test \n Unclosed String"  ""","""Unclosed String: Test \n""",101))
    # def test_unclosed_string15(self):
    #     self.assertTrue(TestLexer.test(""" "Test Unclosed String\\" \n" ""","""Unclosed String: Test Unclosed String\\" \n""",101))
    # def test_unclosed_string16(self):
    #     self.assertTrue(TestLexer.test(""" "line 1\\n line 2\n" ""","""Unclosed String: line 1\\n line 2\n""",101))
    # def test_unclosed_string17(self):
    #     self.assertTrue(TestLexer.test(""" "\\"" "'ab'c ""","""\\",Unclosed String: 'ab'c """,101))
    # def test_unclosed_string18(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\n"|"|b6783\\")&* ""","""Unclosed String: %^&*(\n""",101))
    # def test_unclosed_string19(self):
    #     self.assertTrue(TestLexer.test(""""\\"Open string""", """Unclosed String: \\"Open string""", 101))
    # def test_unclosed_string20(self):
    #     self.assertTrue(TestLexer.test(""" "Open string \n.\\" """, """Unclosed String: Open string \n""", 303))
    
    # def test_illegal_string4(self):
    #     self.assertTrue(TestLexer.test("""  "abc123a\\mabc"  ""","""Illegal Escape In String: abc123a\\m""",301))
    # def test_illegal_string5(self):
    #     self.assertTrue(TestLexer.test("""   123-4"abc123a\\b\\iasVm"  ""","""123,-,4,Illegal Escape In String: abc123a\\b\\i""",302))
    # def test_illegal_string6(self):
    #     self.assertTrue(TestLexer.test("""  "Hi, this is abc \\h\\n\\t "  ""","""Illegal Escape In String: Hi, this is abc \h""",303))
    # def test_illegal_string7(self):
    #     self.assertTrue(TestLexer.test(""" "     " " " "" "\\t\\b\\g" ""","""     , ,,Illegal Escape In String: \\t\\b\\g""",304))
    # def test_illegal_string8(self):
    #     self.assertTrue(TestLexer.test(""" "X=004*0875.E-2\\087.02" ""","""Illegal Escape In String: X=004*0875.E-2\\0""",305))
    # def test_illegal_string9(self):
    #     self.assertTrue(TestLexer.test(""" "illegal_escape\" ""","""illegal_escape,<EOF>""",306))
    # def test_illegal_string10(self):
    #     self.assertTrue(TestLexer.test(""" 
    #     "t \ {abcd}\\efg"
    #     ""","Illegal Escape In String: t \ ",101))
    # def test_operator(self):
    #     self.assertTrue(TestLexer.test("+ - * / ! % || && != == <= >= > < =", "+,-,*,/,!,%,||,&&,!=,==,<=,>=,>,<,=,<EOF>", 101))
    # def test_operator2(self):
    #     self.assertTrue(TestLexer.test("2*2 + 2^ 1", "2,*,2,+,2,Error Token ^", 101))
    # def test_operator3(self):
    #     self.assertTrue(TestLexer.test("do {print(a);} while (a & b);", "do,{,print,(,a,),;,},while,(,a,Error Token &", 101))
    # def test_operator4(self):
    #     self.assertTrue(TestLexer.test("income=income + salary*1.2*rate[1]+month#3;", "income,=,income,+,salary,*,1.2,*,rate,[,1,],+,month,Error Token #", 101))
    # def test_operator5(self):
    #     self.assertTrue(TestLexer.test("cost = sum((y-h(i))**2)", "cost,=,sum,(,(,y,-,h,(,i,),),*,*,2,),<EOF>", 101))
    # def test_operator6(self):
    #     self.assertTrue(TestLexer.test("x = (4 + 3i)(2 + 5i).i^2", "x,=,(,4,+,3,i,),(,2,+,5,i,),.,i,Error Token ^", 101))
    # def test_operator7(self):
    #     self.assertTrue(TestLexer.test("+-*/%*()/*//$#", "+,-,*,/,%,*,(,),/,*,<EOF>", 101))

    # def test_separators(self):
    #     self.assertTrue(TestLexer.test("(  ) [ ] { } ; ,  =", "(,),[,],{,},;,,,=,<EOF>", 101))
    
    # def test_full1(self):
    #     self.assertTrue(TestLexer.test("array[1+2,0]=0;","array,[,1,+,2,,,0,],=,0,;,<EOF>",101))
    # def test_full2(self):
    #     self.assertTrue(TestLexer.test("x,y,z: float = 1.20e10, 7E-2, 3*a","x,,,y,,,z,:,float,=,1.20e10,,,7E-2,,,3,*,a,<EOF>",101))
    # def test_full3(self):
    #     self.assertTrue(TestLexer.test("20>>3<<4<===>=b","20,>,>,3,<,<,4,<=,==,>=,b,<EOF>",101))
    # def test_full4(self):
    #     self.assertTrue(TestLexer.test("(2.2+03)||a!==3&a","(,2.2,+,0,3,),||,a,!=,=,3,Error Token &",101))

    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # def test_full5(self):
    #     self.assertTrue(TestLexer.test("super(a[0,0],b*c-d,+3.4e-1+.e-2);","super,(,a,[,0,,,0,],,,b,*,c,-,d,,,+,3.4e-1,+,.e-2,),;,<EOF>",1017)) 
    #                                                                         super,(,a,[,0,,,0,],,,b,*,c,-,d,,,+,3.4e-1,+,.,e,-,2,),;,<EOF>                   
    # def test_float10(self):
    #     self.assertTrue(TestLexer.test(" 5e-8+6 ","5e-8,+,6,<EOF>",1015))

    # def test_unclosed_string18(self):
    #     self.assertTrue(TestLexer.test(""" "%^&*(\n\n"|"|b6783\\")&* ""","""Unclosed String: %^&*(""",1018))
    
    # def test_string_escape12(self):
    #     self.assertTrue(TestLexer.test(""""He said: \\"He said:\\"I saw him.\\"\\"" """, """He said: \\"He said:\\"I saw him.\\"\\",<EOF>""", 1000))

    # def test_unclosed_string19(self):
    #     self.assertTrue(TestLexer.test(""""\\"Open string""", """Unclosed String: \\"Open string""", 1019))

#     def test_program_7(self):
#         self.assertTrue(TestLexer.test("""
# main: function void () {
#     for (i = n, , i%2) printString("Computer is working...\n");
# }
# """, "main,:,function,void,(,),{,for,(,i,=,n,,,,,i,%,2,),printString,(,Unclosed String: Computer is working...\n",1021))

#     def test_integer5(self):
#         self.assertTrue(TestLexer.test("1_23__456_", "123456,_,<EOF>", 101))

#     def test_float10(self): 
#         self.assertTrue(TestLexer.test("0.e-11 1.2E-22 0E 00.e .0e1 .0e-1","0.e-11,1.2E-22,0,E,0,0.,e,.0e1,.0e-1,<EOF>",101))   
#     def test_string_escape2(self):
#         self.assertTrue(TestLexer.test(""""He asked me: \\"Where is John?\\"" """, """He asked me: \\"Where is John?\\",<EOF>""", 151))
#     ## He asked me: "Where is John?" lồng string trong string
#     def test_string_escape3(self):
#         self.assertTrue(TestLexer.test("""
#         "This sentence contains new line
#         "
#         """, """Unclosed String: This sentence contains new line\n""", 152))
#     def test_statement1(self):
#         self.assertTrue(TestLexer.test("a:string =\"Hello, World!\n\"","a,:,string,=,Unclosed String: Hello, World!\n",101))  # xem lại
#     def test_statement2(self):
#         self.assertTrue(TestLexer.test("printInteger(123);","printInteger,(,123,),;,<EOF>", 101)) 
#     def test_statement3(self):
#         self.assertTrue(TestLexer.test("arr: array[1,2] of integer = {{-1,2}};","arr,:,array,[,1,,,2,],of,integer,=,{,{,-,1,,,2,},},;,<EOF>", 101)) 
#     def test_statement3(self):
#         self.assertTrue(TestLexer.test("printInteger(123);","printInteger,(,123,),;,<EOF>", 101)) 
#     def test_program_1(self):
#         self.assertTrue(TestLexer.test("""
# main : function void() {                                      
#     printString("Hello World");
#     return ;
# }
# """, "main,:,function,void,(,),{,printString,(,Hello World,),;,return,;,},<EOF>",101))
#     def test_program_2(self):
#         self.assertTrue(TestLexer.test("""
# main : function void() {                                       
# // first block
# {
#     // second block
#     {
#         // third block
#         {
#             // fourth block
#         }
#     }
# }}""", "main,:,function,void,(,),{,{,{,{,},},},},<EOF>",101))
#     def test_program_3(self):
#         self.assertTrue(TestLexer.test("""
# a : integer = 0;
# main : function void() {                                      
#     return a;
# }
# """, "a,:,integer,=,0,;,main,:,function,void,(,),{,return,a,;,},<EOF>",101))
#     def test_program_4(self):
#         self.assertTrue(TestLexer.test("""
# a : integer = 0;
# main : function void() {                                      
#     return a;
# }
# """, "a,:,integer,=,0,;,main,:,function,void,(,),{,return,a,;,},<EOF>",101))
#     def test_program_5(self):
#         self.assertTrue(TestLexer.test("""
# {
# r, s: integer;
# r = 2.0;
# a, b: array [5] of integer;
# s = r * r * myPI;
# a[0] = s;
# }
# """, "{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>",101))
#     def test_program_6(self):
#         self.assertTrue(TestLexer.test("""
# main: function void () {
#     if (a>b) if (true) printString("TRUE"); else printString("FALSE");
#     else printInteger(b);
#     return;
# }
# """, "main,:,function,void,(,),{,if,(,a,>,b,),if,(,true,),printString,(,TRUE,),;,else,printString,(,FALSE,),;,else,printInteger,(,b,),;,return,;,},<EOF>",101))
#     def test_program_7(self):
#         self.assertTrue(TestLexer.test("""
# main: function void () {
#     for (i = n, , i%2) printString("Computer is working...\n");
# }
# """, "main,:,function,void,(,),{,for,(,i,=,n,,,,,i,%,2,),printString,(,Unclosed String: Computer is working...\n",101))
#     def test_program_8(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 do {
#                     if (a == 10) break;
#                     a = a - 1; 
#                     printInteger(a);
#                 }
#                 while(a > 0);
#             }
# """, "main,:,function,void,(,),{,do,{,if,(,a,==,10,),break,;,a,=,a,-,1,;,printInteger,(,a,),;,},while,(,a,>,0,),;,},<EOF>",101))
#     def test_program_9(self):
#         self.assertTrue(TestLexer.test("""
#             main : function void() {
#                 a, b : integer = round(123.0e2), randomInt();
#                 /*
#                 Calculate sum of 2 numbers a & b
#                 */
#                 sum : integer = a + b + arr[0,0];
#                 print(a, sum);
#                 return ;
#             }
# """, "main,:,function,void,(,),{,a,,,b,:,integer,=,round,(,123.0e2,),,,randomInt,(,),;,sum,:,integer,=,a,+,b,+,arr,[,0,,,0,],;,print,(,a,,,sum,),;,return,;,},<EOF>",101))
#     def test_program_10(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void() {
#                 a : string = "Hello world"; // string 
#                 return a::"!";
#             }  
# """, "main,:,function,void,(,),{,a,:,string,=,Hello world,;,return,a,::,!,;,},<EOF>",101))
#     def test_program_11(self):
#         self.assertTrue(TestLexer.test("""
#             main : function void() {
#             foo(2__0 + -x_1, 4.0e-2 / y2);
#             goo();
#             return ;
#         } 
# """, "main,:,function,void,(,),{,foo,(,20,+,-,x_1,,,4.0e-2,/,y2,),;,goo,(,),;,return,;,},<EOF>",101))
#     def test_program_12(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 a = 2 + 2%2/2*-2 ;
#                 b = 1*1--1+1/1 ;
#                 c = a + b / (2*1.0+1) ;                
#             }
# """, "main,:,function,void,(,),{,a,=,2,+,2,%,2,/,2,*,-,2,;,b,=,1,*,1,-,-,1,+,1,/,1,;,c,=,a,+,b,/,(,2,*,1.0,+,1,),;,},<EOF>",101))
#     def test_program_13(self):
#         self.assertTrue(TestLexer.test("""
#             main: function void () {
#                 a = true ;
#                 b = !a && false || (false && true || true) ;  
#                 c = !!b || false ;             
#             }
# """, "main,:,function,void,(,),{,a,=,true,;,b,=,!,a,&&,false,||,(,false,&&,true,||,true,),;,c,=,!,!,b,||,false,;,},<EOF>",101))
#     def test_program_14(self):
#         self.assertTrue(TestLexer.test("""
#             True : string = "It's true!" 
#             false : string = "it's not true..." 
# """, "True,:,string,=,It's true!,false,:,string,=,it's not true...,<EOF>",101))
#     def test_integer3(self):
#         self.assertTrue(TestLexer.test("123 _123 1_23 0123__45_6 __123", "123,_123,123,0,123456,__123,<EOF>", 1002))
#     def test_integer5(self):
#         self.assertTrue(TestLexer.test("1_23__456_", "123456,<EOF>", 1003))
























    # """test identifiers"""
    # def test_identifier_1(self):
    #     self.assertTrue(TestLexer.test(	" abcd","abcd,<EOF>",101))
    # def test_identifier_2(self):
    #     self.assertTrue(TestLexer.test(	"AbCd","AbCd,<EOF>",102))
    # def test_identifier_3(self):
    #     self.assertTrue(TestLexer.test(	"abc1","abc1,<EOF>",103))
    # def test_identifier_4(self):
    #     self.assertTrue(TestLexer.test(	"_etg","_etg,<EOF>",104))
    # def test_identifier_5(self):
    #     self.assertTrue(TestLexer.test(	"_bcd1234","_bcd1234,<EOF>",105))
    # def test_identifier_6(self):
    #     self.assertTrue(TestLexer.test(	"a_","a_,<EOF>",106))
    # def test_identifier_7(self):
    #     self.assertTrue(TestLexer.test(	"mg_311_acjav","mg_311_acjav,<EOF>",107))
        
    # """test integer"""
    # def test_integer_8(self):
    #     self.assertTrue(TestLexer.test(	"0 1_3 24_5 333_1","0,13,245,3331,<EOF>",108))
    # def test_integer_9(self):
    #     self.assertTrue(TestLexer.test(	"0 6_3 83_5 3_2_3_1","0,63,835,3231,<EOF>",109))
    # def test_integer_10(self):
    #     self.assertTrue(TestLexer.test(	"123asd","123,asd,<EOF>",110))
    # def test_integer_11(self):
    #     self.assertTrue(TestLexer.test(	"10_2_3_4","10234,<EOF>",111))
    # def test_integer_12(self):
    #     self.assertTrue(TestLexer.test(	"0abc","0,abc,<EOF>",112))
        
    # """test float"""
    # def test_float_13(self):
    #     self.assertTrue(TestLexer.test(	"e1 1e11 5E-3 2E-10","e1,1e11,5E-3,2E-10,<EOF>",113))
    # def test_float_14(self):
    #     self.assertTrue(TestLexer.test(	"1.2e3","1.2e3,<EOF>",114))
    # def test_float_15(self):
    #     self.assertTrue(TestLexer.test(	"7E-10","7E-10,<EOF>",115))
    # def test_float_16(self):
    #     self.assertTrue(TestLexer.test(	"1_234.567","1234.567,<EOF>",116))
    # def test_float_17(self):
    #     self.assertTrue(TestLexer.test(	"1_234.567abc","1234.567,abc,<EOF>",117))
    # def test_float_18(self):
    #     self.assertTrue(TestLexer.test(	"1e-5","1e-5,<EOF>",118))
        
    # """test boolean"""
    # def test_boolean_19(self):
    #     self.assertTrue(TestLexer.test(	"true","true,<EOF>",119))
    # def test_boolean_20(self):
    #     self.assertTrue(TestLexer.test(	"false true","false,true,<EOF>",120))
    # def test_boolean_21(self):
    #     self.assertTrue(TestLexer.test(	"false","false,<EOF>",121))
    # def test_boolean_22(self):
    #     self.assertTrue(TestLexer.test(	"true true","true,true,<EOF>",122))
    # def test_boolean_23(self):
    #     self.assertTrue(TestLexer.test(	"false false","false,false,<EOF>",123))
    
    # """test string"""
    # def test_string_24(self):
    #     self.assertTrue(TestLexer.test(	
    #         r""""String contain tab \t"
    #         """,
    #         """String contain tab \\t,<EOF>""",124))
    # def test_string_25(self):
    #     self.assertTrue(TestLexer.test(r""" "You said: abc?""",
    #         "Unclosed String: You said: abc?",125))
    # def test_string_26(self):
    #     self.assertTrue(TestLexer.test("""  "abc"  ""","abc,<EOF>",126))
    # def test_string_27(self):
    #     self.assertTrue(TestLexer.test(""" "abcasc" ""","abcasc,<EOF>",127))
    # def test_string_28(self):
    #     self.assertTrue(TestLexer.test(r""" "abc\\a" """,r"""abc\\a,<EOF>""",128))
    # def test_string_29(self):
    #     self.assertTrue(TestLexer.test(r""" "abc\t" """,r"""abc\t,<EOF>""",129))
    # def test_string_30(self):
    #     self.assertTrue(TestLexer.test(r""" "abc\a" """,r"""Illegal Escape In String: abc\a""",130))
    # def test_string_31(self):
    #     self.assertTrue(TestLexer.test(r""" "abc\\" """,r"""abc\\,<EOF>""",131))
    # def test_string_32(self):
    #     self.assertTrue(TestLexer.test(r""" "ab\"hvc" """,r"""ab\"hvc,<EOF>""",132))
    # def test_string_33(self):
    #     self.assertTrue(TestLexer.test(r""" "ab\?" """,r"""Illegal Escape In String: ab\?""",133))
    # def test_string_34(self):
    #     self.assertTrue(TestLexer.test(r""" "abc\" """,r"""Unclosed String: abc\" """,134))
    # def test_string_35(self):
    #     self.assertTrue(TestLexer.test(r""" "asd\a" """, r"""Illegal Escape In String: asd\a""" ,135))
    # def test_string_36(self):
    #     self.assertTrue(TestLexer.test(r""" "asd123asd\t123" """, r"""asd123asd\t123,<EOF>""" ,136))
    # def test_string_37(self):
    #     self.assertTrue(TestLexer.test(r""" "asdkas\\\\" """, r"""asdkas\\\\,<EOF>""" ,137))
    # def test_string_38(self):
    #     self.assertTrue(TestLexer.test(r""" "test """, r"""Unclosed String: test """ ,138))
    # def test_string_39(self):
    #     self.assertTrue(TestLexer.test(""" "test""test" ""","""test,test,<EOF>""" ,139))
    # def test_string_40(self):
    #     self.assertTrue(TestLexer.test(""" "a b c d e" """, """a b c d e,<EOF>""" ,140))
    # def test_string_41(self):
    #     self.assertTrue(TestLexer.test(r""" "a b c \t" """, r"""a b c \t,<EOF>""" ,141))
    # def test_string_42(self):
    #     self.assertTrue(TestLexer.test(r""" "a b c \a" """, r"""Illegal Escape In String: a b c \a""" ,142))
    # def test_string_43(self):
    #     self.assertTrue(TestLexer.test(r""" "abc \" \" " """, r"""abc \" \" ,<EOF>""" ,143))
    # def test_string_44(self):
    #     self.assertTrue(TestLexer.test(r""" "\"\\\\" """, r"""\"\\\\,<EOF>""" ,144))
    # def test_string_45(self):
    #     self.assertTrue(TestLexer.test(r""" "\\\\\"\a\t" """, r"""Illegal Escape In String: \\\\\"\a""" ,145))
    
    # """ Test Specific Characters """
    # def test_characters_46(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""+ - * / %
    #             ! && || == =
    #             != < <= > >=
    #             . ::
    #             ( ) [ ] .. , ; : { }
    #         """,
    #         "+,-,*,/,%,!,&&,||,==,=,!=,<,<=,>,>=,.,::,(,),[,],.,.,,,;,:,{,},<EOF>",
    #         146
    #     ))
        
    # """ Test Comment """
    # def test_comment_47(self):
    #     self.assertTrue(TestLexer.test(r""" /* comment */ ""","<EOF>",147))
    # def test_comment_48(self):
    #     self.assertTrue(TestLexer.test(r""" /* comment \n */ ""","<EOF>", 148))
    # def test_comment_49(self):
    #     self.assertTrue(TestLexer.test(r""" /* comment without close ""","/,*,comment,without,close,<EOF>", 149))
    # def test_comment_50(self):
    #     self.assertTrue(TestLexer.test(r""" // This is a comment ""","<EOF>", 150))
    # def test_comment_51(self):
    #     self.assertTrue(TestLexer.test(r""" /* This is a comment \n
    #                                    This is line 2 of comment \n
    #                                    This is line 3 of comment */""","<EOF>", 151))
    
    # """ Test Invalid Identifiers """
    # def test_invalid_52(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""123abc 123_abc 0123_123abc""","123,abc,123,_abc,0,123123,abc,<EOF>",152 ))
    # def test_invalid_53(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""_12371 __12___""","_12371,__12___,<EOF>",153 ))
    # def test_invalid_54(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""1e111021301 0eE10111""","1e111021301,0,eE10111,<EOF>",154))
        
    # def test_55(self):
    #     self.assertTrue(TestLexer.test(r""" "\"abc\\\\abc" """, r"""\"abc\\\\abc,<EOF>""" ,155))
    # def test_56(self):
    #     self.assertTrue(TestLexer.test(r""" "xya ` afv" """, r"""xya ` afv,<EOF>""" ,156))
    # def test_57(self):
    #     self.assertTrue(TestLexer.test(r""" "abc\t\r\f\n" """, r"""abc\t\r\f\n,<EOF>""" ,157))
    # def test_58(self):
    #     self.assertTrue(TestLexer.test(r""" "asd\\\\\"" """, r"""asd\\\\\",<EOF>""" ,158))
    # def test_59(self):
    #     self.assertTrue(TestLexer.test(r""" 1238970b123 """, r"""1238970,b123,<EOF>""" ,159))
    # def test_60(self):
    #     self.assertTrue(TestLexer.test(""" "abc""abc" ""","""abc,abc,<EOF>""" ,160))
        
    # """ Test Error Token """
    # def test_err_tok_61(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""
    #         & ^ % $ # ... \
    #             ""","Error Token &",161  ))
    # def test_err_tok_62(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""
    #         If a | b Else
    #         ""","If,a,Error Token |",162))
    # def test_err_tok_63(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""
    #         abc = abc & 2
    #         ""","abc,=,abc,Error Token &",163))
    # def test_identifier_64(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""
    #         xyz
    #         a = 5
    #         ""","xyz,a,=,5,<EOF>",164))
    # def test_identifier_65(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""
    #         integer ab2, ab3, ac
    #         ""","integer,ab2,,,ab3,,,ac,<EOF>",165))
        
    # """ Test Valid Keywords """
    # def test_keywords_66(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""auto break boolean do else false float for function if integer return string true while void out continue of inherit array
    #         """,
    #         r"""auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>""",
    #         166))
        
    # """test float literal"""
    # def test_float_67(self):
    #     self.assertTrue(TestLexer.test(	"1.123","1.123,<EOF>",167))
    # def test_float_68(self):
    #     self.assertTrue(TestLexer.test(	"0.123","0.123,<EOF>",168))
    # def test_float_69(self):
    #     self.assertTrue(TestLexer.test(	"00.123","0,0.123,<EOF>",169))
    # def test_float_70(self):
    #     self.assertTrue(TestLexer.test(	"123.2e3","123.2e3,<EOF>",170))
    # def test_float_71(self):
    #     self.assertTrue(TestLexer.test(	"1_3_2.2e-33","132.2e-33,<EOF>",171))
    # def test_float_72(self):
    #     self.assertTrue(TestLexer.test(	"0.123E-10","0.123E-10,<EOF>",172))
    # def test_float_73(self):
    #     self.assertTrue(TestLexer.test(	"12_3_4.123_3_4","1234.123,_3_4,<EOF>",173))
    # def test_float_74(self):
    #     self.assertTrue(TestLexer.test(	"00.001","0,0.001,<EOF>",174))
    
    # """test mixed"""
    # def test_comment_75(self):
    #     self.assertTrue(TestLexer.test(r""" // This is a comment \n
    #                                    This is a comment""","This,is,a,comment,<EOF>", 175))
    # def test_mixed_76(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""
    #         "bac abc and \t \r \\a\\b\b\n\\t\\\\\r ppl !!!"
    #         """,
    #         r"""bac abc and \t \r \\a\\b\b\n\\t\\\\\r ppl !!!,<EOF>""",176))
    # def test_mixed_77(self):
    #     self.assertTrue(TestLexer.test(
    #         r"""
    #         "bac abc and \t \r \\a\\b\b\n\\t\\\\\r kdf"
    #         """,
    #         r"""bac abc and \t \r \\a\\b\b\n\\t\\\\\r kdf,<EOF>""",177))
    # def test_mixed_78(self):
    #     self.assertTrue(TestLexer.test(r""" "abc" "deg "=-132=42=12-"hasagi """,
    #                                    "abc,deg ,=,-,132,=,42,=,12,-,Unclosed String: hasagi ", 178))
    # def test_mixed_79(self):
    #     self.assertTrue(TestLexer.test(r""" "YASUO \c\d\e" """, r"Illegal Escape In String: YASUO \c", 179))
    # def test_mixed_80(self):
    #     self.assertTrue(TestLexer.test(r""" "ZED d\hef" """, r"Illegal Escape In String: ZED d\h", 180))
    # def test_mixed_81(self):
    #     self.assertTrue(TestLexer.test(r""" "test""asd """, r"""test,Unclosed String: asd """  ,181))
    # def test_mixed_82(self):
    #     self.assertTrue(TestLexer.test(r"""a = Array[Int,0]""", r"""a,=,Array,[,Int,,,0,],<EOF>""" ,182))
    # def test_mixed_83(self):
    #     self.assertTrue(TestLexer.test(r"""Var a : Int; " """, r"""Var,a,:,Int,;,Unclosed String:  """ ,183))
    # def test_mixed_84(self):
    #     self.assertTrue(TestLexer.test(r"""a = "mystring" """, r"""a,=,mystring,<EOF>""" ,184))
    # def test_mixed_85(self):
    #     self.assertTrue(TestLexer.test(r"""a = "my string" """, r"""a,=,my string,<EOF>""" ,185))
    # def test_mixed_86(self):
    #     self.assertTrue(TestLexer.test(r""" "123_1230b01""", r"""Unclosed String: 123_1230b01""" ,186))
    # def test_mixed_87(self):
    #     self.assertTrue(TestLexer.test(r"""// A C++ style comment""", r"""<EOF>""" ,187))
    # def test_mixed_88(self):
    #     self.assertTrue(TestLexer.test(r"""/* A C-style comment */""", r"""<EOF>""" ,188))
    # def test_mixed_89(self):
    #     self.assertTrue(TestLexer.test(r"""a = "mystring \t" """, r"""a,=,mystring \t,<EOF>""" ,189))
    # def test_mixed_90(self):
    #     self.assertTrue(TestLexer.test(r"""a = "mystring\\\\" """, r"""a,=,mystring\\\\,<EOF>""" ,190))
    # def test_mixed_91(self):
    #     self.assertTrue(TestLexer.test(r""" "asdf ` asdf" """, r"""asdf ` asdf,<EOF>""" ,191))
    # def test_mixed_92(self):
    #     self.assertTrue(TestLexer.test(r""" "asdf\t\r\f" """, r"""asdf\t\r\f,<EOF>""" ,192))
    # def test_mixed_93(self):
    #     self.assertTrue(TestLexer.test(r""" "asd\\\\\"" """, r"""asd\\\\\",<EOF>""" ,193))
    # def test_mixed_94(self):
    #     self.assertTrue(TestLexer.test(r""" 1238970b123 """, r"""1238970,b123,<EOF>""" ,194))
    # def test_mixed_95(self):
    #     self.assertTrue(TestLexer.test(r""" 123"asasd \t \f \a" """, r"""123,Illegal Escape In String: asasd \t \f \a""" ,195))
    # def test_mixed_96(self):
    #     self.assertTrue(TestLexer.test(r"""101023456"123"" """, r"""101023456,123,Unclosed String:  """ ,196))
    # def test_mixed_97(self):
    #     self.assertTrue(TestLexer.test(r"""aAaAbBbB09809""", r"""aAaAbBbB09809,<EOF>""" ,197))
    # def test_mixed_98(self):
    #     self.assertTrue(TestLexer.test(r"""098098_123123aBaBb""", r"""0,98098123123,aBaBb,<EOF>""" ,198))
    # def test_mixed_99(self):
    #     self.assertTrue(TestLexer.test(r""" 1010101010 """, r"""1010101010,<EOF>""" ,199))
    # def test_mixed_200(self):
    #     self.assertTrue(TestLexer.test(r""" 0.123E-10AFC """, r"""0.123E-10,AFC,<EOF>""" ,200))











    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_underline_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a_bc", "a_bc,<EOF>", 102))
    
    def test_number_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a123", "a123,<EOF>", 103))

    def test_uppercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("ABC", "ABC,<EOF>", 104))
    
    def test_uppercase_underline_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("A_BC", "A_BC,<EOF>", 105))
    
    def test_uppercase_number_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("A123", "A123,<EOF>", 106))

    def test_mixedcase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("aBc", "aBc,<EOF>", 107))
    
    def test_mixedcase_underline_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a_Bc", "a_Bc,<EOF>", 108))

    def test_mixedcase_number_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a1Bc", "a1Bc,<EOF>", 109))
    
    def test_mixedcase_number_underline_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a1_Bc", "a1_Bc,<EOF>", 110))
    
    def test_multiple_underline_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a__bc", "a__bc,<EOF>", 111))

    def test_identifier_errorToken1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("ab?cd", "ab,Error Token ?", 112))

    def test_identifier_errorToken2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("ab~cd", "ab,Error Token ~", 113))
    
    def test_identifier_invalid1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1abc", "1,abc,<EOF>", 114))

    def test_identifier_invalid2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1a_bc", "1,a_bc,<EOF>", 115))
    
    def test_identifier_invalid3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1a123", "1,a123,<EOF>", 116))

    def test_identifier_invalid4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 117))

    def test_identifier_invalid5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1A_BC", "1,A_BC,<EOF>", 118))
    
    def test_string_literal0(self):
        """test string literal"""
        inp = r'''"ab
        c"'''
        expect = r'Unclosed String: ab'
        self.assertTrue(TestLexer.test(inp, expect, 119))

    def test_string_literal(self):
        """test string literal"""
        inp = r'''"abc\t"'''
        expect = r'abc,<EOF>'
        self.assertTrue(TestLexer.test("abc\t", expect, 120))

    def test_string_literal_with_escape(self):
        """test string literal"""
        inp = r'''"Said:\"Where\""'''
        expect = r'''Said:\"Where\",<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 121))
    
    def test_string_literal_with_escape2(self):
        """test string literal"""
        inp = r'''"a\\b"'''
        expect = r'''a\\b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 122))
    
    def test_string_literal_backspace(self):
        """test string literal"""
        inp = r'''"a\b"'''
        expect = r'''a\b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 123))

    def test_string_literal_formfeed(self):
        """test string literal"""
        inp = r'''"a\fbb"'''
        expect = r'''a\fbb,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 124))

    def test_string_literal_newline(self):
        """test string literal"""
        inp = r'''"afef\n"'''
        expect = r'''afef\n,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 125))

    def test_string_literal_illegalEscape(self):
        """test string literal"""
        inp = r'''"a\f\ubcde"'''
        expect = r'''Illegal Escape In String: a\f\u'''
        self.assertTrue(TestLexer.test(inp, expect, 126))
    
    def test_string_literal_unclosedString(self):
        """test string literal"""
        inp = r'''"abc'''
        expect = r'''Unclosed String: abc'''
        self.assertTrue(TestLexer.test(inp, expect, 127))
    
    def test_string_literal_unclosedString2(self):
        """test string literal"""
        inp = r'''"abc\"'''
        expect = r'''Unclosed String: abc\"'''
        self.assertTrue(TestLexer.test(inp, expect, 128))
    
    def test_string_literal_unclosedString3(self):
        """test string literal"""
        inp = r'''"abc\''''
        expect = r'''Unclosed String: abc\''''
        self.assertTrue(TestLexer.test(inp, expect, 129))

    def test_int_literal(self):
        """test number literal"""
        inp = '123'
        expect = r'123,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 130))

    def test_int_literal_with_0(self):
        """test number literal"""
        inp = '0123'
        expect = r'0,123,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 131))

    def test_int_literal_with_underline(self):
        """test number literal"""
        inp = '123_123_567'
        expect = r'123123567,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 132))

    def test_int_literal_with_0_and_underline(self):
        """test number literal"""
        inp = '0_123'
        expect = r'0,_123,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 133))
    
    def test_int_literal_with_0_and_underline2(self):
        """test number literal"""
        inp = '0_123_'
        expect = r'0,_123_,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 134))

    def test_int_literal_with_0_and_underline3(self):
        """test number literal"""
        inp = '0_123_456'
        expect = r'0,_123_456,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 135))

    def test_int_literal_with_0_and_underline4(self):
        """test number literal"""
        inp = '0_123_456_'
        expect = r'0,_123_456_,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 136))
    
    def test_float_literal(self):
        """test number literal"""
        inp = '123.123'
        expect = r'123.123,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 137))

    def test_float_literal_with_0(self):
        """test number literal"""
        inp = '0123.123'
        expect = r'0,123.123,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 138))

    def test_float_literal_with_underline(self):
        """test number literal"""
        inp = '123_123.15'
        expect = r'123123.15,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 139))

    def test_float_literal_exponent(self):
        """test number literal"""
        inp = '12.3e3'
        expect = r'12.3e3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 140))
    
    def test_float_literal_exponent2(self):
        """test number literal"""
        inp = '12.3e+3'
        expect = r'12.3e+3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 141))

    def test_float_literal_exponent3(self):
        """test number literal"""
        inp = '12.3e-3'
        expect = r'12.3e-3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 142))

    def test_float_literal_exponent4(self):
        """test number literal"""
        inp = '3E3'
        expect = r'3E3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 143))
    
    def test_float_literal_exponent5(self):
        """test number literal"""
        inp = '3E+3'
        expect = r'3E+3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 144))

    def test_float_literal_exponent6(self):
        """test number literal"""
        inp = '3E-3'
        expect = r'3E-3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 145))
    
    def test_float_literal_invalid1(self):
        """test number literal"""
        inp = '3E-'
        expect = r'3,E,-,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 146))
    
    def test_float_literal_invalid2(self):
        """test number literal"""
        inp = '12.25_2'
        expect = r'12.25,_2,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 147))

    def test_float_literal_invalid3(self):
        """test number literal"""
        inp = '12.25_2e3'
        expect = r'12.25,_2e3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 148))

    def test_float_literal_invalid4(self):
        """test number literal"""
        inp = '12.25_2e+3'
        expect = r'12.25,_2e,+,3,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 149))

    def test_boolean_literal(self):
        """test boolean literal"""
        inp = 'true'
        expect = r'true,<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 150))
    
    def test_array_literal(self):
        """test array literal"""
        inp = '{1,2,3,4}'
        expect = r'{,1,,,2,,,3,,,4,},<EOF>'
        self.assertTrue(TestLexer.test(inp, expect, 151))
    
    def test_array_literal2(self):
        """test array literal"""
        inp = r'''{"asd","dawfwa\"","3","4\'"}'''
        expect = r'''{,asd,,,dawfwa\",,,3,,,4\',},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 152))
        
    def test_comment1(self):
        """test comments"""
        inp = r'''/* Test */ab'''
        expect = r'''ab,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 153))
    
    def test_comment2(self):
        """test comments"""
        inp = r'''a // Test */ab'''
        expect = r'''a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 154))

    def test_comment3(self):
        """test comments"""
        inp = r'''a /* Test */ab'''
        expect = r'''a,ab,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 155))

    def test_comment4(self):
        """test comments"""
        inp = r'''a /* Test // dawf */ab /* Test */'''
        expect = r'''a,ab,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 156))
    
    def test_comment5(self):
        """test comments"""
        inp = r'''a  // \r\n dawf */ab /* Test */'''
        expect = r'''a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 157))
    
    def test_array_type(self):
        """test array type"""
        inp = r'''array [2] of integer'''
        expect = r'''array,[,2,],of,integer,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 158))
    
    def test_array_type2(self):
        """test array type"""
        inp = r'''array [2, 3] of integer'''
        expect = r'''array,[,2,,,3,],of,integer,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 159))
    
    def test_void_type1(self):
        """test void type"""
        inp = r'''void'''
        expect = r'''void,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 160))

    def test_auto_type1(self):
        """test auto type"""
        inp = r'''a, b: auto'''
        expect = r'''a,,,b,:,auto,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 161))

    def test_operator_signNegation1(self):
        """test operator signNegation"""
        inp = r'''-a'''
        expect = r'''-,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 162))
    
    def test_operator_signNegation2(self):
        """test operator signNegation"""
        inp = r'''-12.34'''
        expect = r'''-,12.34,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 163))

    def test_operator_addition(self):
        """test operator addition"""
        inp = r'''a+a'''
        expect = r'''a,+,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 164))
    
    def test_operator_subtraction(self):
        """test operator subtraction"""
        inp = r'''a-a'''
        expect = r'''a,-,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 165))
    
    def test_operator_multiplication(self):
        """test operator multiplication"""
        inp = r'''a*a'''
        expect = r'''a,*,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 166))
    
    def test_operator_division(self):
        """test operator division"""
        inp = r'''a/a'''
        expect = r'''a,/,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 167))
    
    def test_operator_modulo(self):
        """test operator modulo"""
        inp = r'''a%a'''
        expect = r'''a,%,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 168))
    
    def test_operator_mixed_airthmetic(self):
        """test operator mixed"""
        inp = r'''a+b-c*d/e%8'''
        expect = r'''a,+,b,-,c,*,d,/,e,%,8,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 169))
    
    def test_operator_boolNegation(self):
        """test operator negation"""
        inp = r'''!a'''
        expect = r'''!,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 170))

    def test_operator_boolAnd(self):
        """test operator boolAnd"""
        inp = r'''a&&a'''
        expect = r'''a,&&,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 171))
    
    def test_operator_boolOr(self):
        """test operator boolOr"""
        inp = r'''a||a'''
        expect = r'''a,||,a,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 172))
    
    def test_operator_mixed_bool(self):
        """test operator mixed"""
        inp = r'''a&&b||c'''
        expect = r'''a,&&,b,||,c,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 173))
    
    def test_operator_stringConcat(self):
        """test operator concatenation"""
        inp = r'''"daw"::"dawr"'''
        expect = r'''daw,::,dawr,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 174))
    
    def test_operator_equal(self):
        """test operator equal"""
        inp = r'''a==b'''
        expect = r'''a,==,b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 175))

    def test_operator_notEqual(self):
        """test operator notEqual"""
        inp = r'''a!=b'''
        expect = r'''a,!=,b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 176))
    
    def test_operator_lessThan(self):
        """test operator lessThan"""
        inp = r'''a<b'''
        expect = r'''a,<,b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 177))
    
    def test_operator_lessEqual(self):
        """test operator lessEqual"""
        inp = r'''a<=b'''
        expect = r'''a,<=,b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 178))
    
    def test_operator_greaterThan(self):
        """test operator greaterThan"""
        inp = r'''a>b'''
        expect = r'''a,>,b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 179))
    
    def test_operator_greaterEqual(self):
        """test operator greaterEqual"""
        inp = r'''a>=b'''
        expect = r'''a,>=,b,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 180))
    
    def test_operator_index(self):
        """test operator index"""
        inp = r'''a[b]'''
        expect = r'''a,[,b,],<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 181))
    
    def test_operator_index_list(self):
        """test operator index"""
        inp = r'''a[b,c]'''
        expect = r'''a,[,b,,,c,],<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 182))
    
    def test_function_call_empty(self):
        """test function call"""
        inp = r'''foo()'''
        expect = r'''foo,(,),<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 183))
    
    def test_function_call(self):
        """test function call"""
        inp = r'''foo(a,b,c)'''
        expect = r'''foo,(,a,,,b,,,c,),<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 184))
    
    def test_random_mixed1(self):
        """test random"""
        inp = r'''a[1+2]'''
        expect = r'''a,[,1,+,2,],<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 185))
    
    def test_random_mixed2(self):
        """test random"""
        inp = r'''a[1+2,3+4]'''
        expect = r'''a,[,1,+,2,,,3,+,4,],<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 186))

    def test_random_mixed3(self):
        """test random"""
        inp = r'''a=4;foo(a);return void;'''
        expect = r'''a,=,4,;,foo,(,a,),;,return,void,;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 187))
    
    def test_random_mixed4(self):
        inp = r'''main : function void ( ) { 
            delta : integer = fact (3); inc(x, delta); printint(x);
            }'''
        expect = r'''main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printint,(,x,),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 188))

    def test_random_mixed5(self):
        inp = r'''fact: function integer (n: integer) {
                    if (n == 0) return 1;
                    else return n * fact (n - 1);
            }'''
        expect = r'''fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 189))
    
    def test_random_mixed6(self):
        inp = r''' inc: function void(out n: integer) {
            n  = n+ 1;
        }'''
        expect = r'''inc,:,function,void,(,out,n,:,integer,),{,n,=,n,+,1,;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 190))

    def test_random_mixed7(self):
        inp = r'''fo_00: function integer (n_9: integer) {
                    if (n_9 == 0) return n + 12_12;
            }'''
        expect = r'''fo_00,:,function,integer,(,n_9,:,integer,),{,if,(,n_9,==,0,),return,n,+,1212,;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 191))

    def test_random_mixed8(self):
        inp = r'''main : function void ( ) { 
            delta : integer = fact (3); inc(x, delta); printint(x);
            }'''
        expect = r'''main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printint,(,x,),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 192))
    
    def test_random_mixed9(self):
        inp = r'''main : function void ( ) { 
            i : integer;
            for (i = 0; i < 10; i = i + 1) {
                do {
                    printint(i);
                    if (i == 5) break;
                } while (i < 10);
            }
        }'''
        expect = r'''main,:,function,void,(,),{,i,:,integer,;,for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,do,{,printint,(,i,),;,if,(,i,==,5,),break,;,},while,(,i,<,10,),;,},},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 193))
    
    def test_random_mixed10(self):
        inp = r'''create_matrix : function array (row: integer, col: integer) {
            mat : array[row,col] of integer;
            for (i = 0; i < row; i = i + 1) {
                for (j = 0; j < col; j = j + 1) {
                    mat[i,j] = 0;
                }
            }
            return mat;
        }'''
        expect = r'''create_matrix,:,function,array,(,row,:,integer,,,col,:,integer,),{,mat,:,array,[,row,,,col,],of,integer,;,for,(,i,=,0,;,i,<,row,;,i,=,i,+,1,),{,for,(,j,=,0,;,j,<,col,;,j,=,j,+,1,),{,mat,[,i,,,j,],=,0,;,},},return,mat,;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 194))
    
    def test_random_mixed11(self):
        inp = r'''main : function void ( ) { 
            mat : array[2,3] of integer;
            mat = create_matrix(2,3);
            print_matrix(mat);
        }'''
        expect = r'''main,:,function,void,(,),{,mat,:,array,[,2,,,3,],of,integer,;,mat,=,create_matrix,(,2,,,3,),;,print_matrix,(,mat,),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 195))
    
    def test_random_mixed12(self):
        inp = r'''hash : function integer (s: string) {
            h : integer = 0;
            for (i = 0; i < length(s); i = i + 1) {
                h = h + ord(s[i]);
            }
            return h;
        }'''
        expect = r'''hash,:,function,integer,(,s,:,string,),{,h,:,integer,=,0,;,for,(,i,=,0,;,i,<,length,(,s,),;,i,=,i,+,1,),{,h,=,h,+,ord,(,s,[,i,],),;,},return,h,;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 196))
    
    def test_random_mixed13(self):
        inp = r'''main : function void ( ) { 
            s : string;
            s = "Hello";
            printint(hash(s));
        }'''
        expect = r'''main,:,function,void,(,),{,s,:,string,;,s,=,Hello,;,printint,(,hash,(,s,),),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 197))
    
    def test_random_mixed14(self):
        inp = r'''{
                r, s: integer;
                r = 2.0;
                a, b: array [5] of integer;
                s = r * r * myPI;
                a[0] = s;
        }'''
        expect = r'''{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 198))
    
    def test_random_mixed15(self):
        inp = r'''fibo : function integer (n: integer) {
            if (n == 0) return 0;
            else if (n == 1) return 1;
            else return fibo(n - 1) + fibo(n - 2);
        }'''
        expect = r'''fibo,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,0,;,else,if,(,n,==,1,),return,1,;,else,return,fibo,(,n,-,1,),+,fibo,(,n,-,2,),;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 199))

    def test_random_mixed16(self):
        inp = r'''circumference : function float (r: float) {
            return 2.0 * myPI * r;
        }'''
        expect = r'''circumference,:,function,float,(,r,:,float,),{,return,2.0,*,myPI,*,r,;,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, expect, 200))
    




















    def test_lexer0(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 0))
        
    def test_lexer1(self):
        input = """{"}"""
        expect = """{,Unclosed String: }"""
        self.assertTrue(TestLexer.test(input, expect, 1))

    def test_lexer2(self):
        input = "{False,}"
        expect = "{,False,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 2))

    def test_lexer3(self):
        input = "// abcd"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 3))

    def test_lexer4(self):
        input = "/* abcxyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 4))

    def test_lexer5(self):
        input = "// this is a line comment /*"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 5))
    
    def test_lexer6(self):
        input = "{/* this is a line comment */ 180, 20}"
        expect = "{,180,,,20,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 6))

    def test_lexer7(self):
        input = """ "\\"aadadddldld\\"" """
        expect = """\\"aadadddldld\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 7))

    def test_lexer8(self):
        input = """ "dshf"""
        expect = """Unclosed String: dshf"""
        self.assertTrue(TestLexer.test(input, expect, 8))

    def test_lexer9(self):
        input = """ {/*"*****/*"}*/*"""
        expect = """{,*,Unclosed String: }*/*"""
        self.assertTrue(TestLexer.test(input, expect, 9))

    def test_lexer10(self):
        input = """sb0345"-a)
                    " """
        expect = """sb0345,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(input, expect, 10))

    def test_lexer11(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 11))

    def test_lexer12(self):
        input = """ "\\t\\ " """
        expect = """Illegal Escape In String: \\t\\ """
        self.assertTrue(TestLexer.test(input, expect, 12))

    def test_lexer13(self):
        input = """ "        " """
        expect = """        ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 13))

    def test_lexer14(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 14))

    def test_lexer15(self):
        input = "Var"
        expect = "Var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 15))

    def test_lexer16(self):
        input = "ab?svn"
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 16))

    def test_lexer17(self):
        input = "Var x;"
        expect = "Var,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 17))

    def test_lexer18(self):
        input = """{         "1" ,      "2"     ,      "3"       }"""
        expect = """{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 18))
    
    def test_lexer19(self):
        input = "12.000e3"
        expect = "12.000e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 19))
    
    def test_lexer20(self):
        input = "12.e-3"
        expect = "12.e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 20))
    
    def test_lexer21(self):
        self.assertTrue(TestLexer.test(""" abvccd """, """abvccd,<EOF>""", 21))
        
        
    def test_lexer22(self):
        input = """~!^^^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 22))

    def test_lexer23(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 23))
        
    def test_lexer24(self):
        input = '""'
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 24))
        
    def test_lexer25(self):
        input = '''
            for (i = 1, i < 10, i + 1) {
                writeInt(i);
                }
            '''
        expect = "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 25))
        
    def test_lexer26(self):
        input = '''
            foo(2 + x, 4.0 / y);
            goo();
            '''
        expect = "foo,(,2,+,x,,,4.0,/,y,),;,goo,(,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 26))
        
    def test_lexer27(self):
        input = '''
            {
                r, s: integer;
                r = 2.0;
                a, b: array [5] of integer;
                s = r * r * myPI;
                a[0] = s;
            }
            '''
        expect = "{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 27))
        
    def test_lexer28(self):
        input = '''
            "
            "
            '''
        expect = "Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 28))
        
    def test_lexer29(self):
        input = '''
            "103_5940"
            '''
        expect = "103_5940,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 29))
        
    def test_lexer30(self):
        input = '''
            1039_390_9024_
            '''
        expect = "10393909024,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 30))
        
    def test_lexer31(self):
        self.assertTrue(TestLexer.test("!a%5&&b||c+*", "!,a,%,5,&&,b,||,c,+,*,<EOF>", 31))

    def test_lexer32(self):
        self.assertTrue(TestLexer.test("a==b==01234!=43210<3>4", "a,==,b,==,0,1234,!=,43210,<,3,>,4,<EOF>", 32))

    def test_lexer33(self):
        self.assertTrue(TestLexer.test("*and<=>mod<\\<=", "*,and,<=,>,mod,<,Error Token \\", 33))

    def test_lexer34(self):
        self.assertTrue(TestLexer.test("/*this is a cmt*/", "<EOF>", 34))

    def test_lexer35(self):
        self.assertTrue(TestLexer.test("//hjhjhuhu/*youare live */", "<EOF>", 35))

    def test_lexer36(self):
        self.assertTrue(TestLexer.test("//hello my friend \n asda", "asda,<EOF>", 36))

    def test_lexer37(self):
        self.assertTrue(TestLexer.test("/*hello my friend \n nothinghjhj \n love */ ntp", "ntp,<EOF>", 37))

    def test_lexer38(self):
        self.assertTrue(TestLexer.test("asf aso Dowoad ", "asf,aso,Dowoad,<EOF>", 38))

    def test_lexer39(self):
        self.assertTrue(TestLexer.test("hello tat ca moi nguoi", "hello,tat,ca,moi,nguoi,<EOF>", 39))

    def test_lexer40(self):
        self.assertTrue(TestLexer.test("thu thu abc () ", "thu,thu,abc,(,),<EOF>", 40))

    def test_lexer41(self):
        self.assertTrue(TestLexer.test("01 10 001 100", "0,1,10,0,0,1,100,<EOF>", 41))

    def test_lexer42(self):
        self.assertTrue(TestLexer.test("0.1 0399 20_39 true false 0.3e55","0.1,0,399,2039,true,false,0.3e55,<EOF>", 42))

    def test_lexer43(self):
        self.assertTrue(TestLexer.test("5.e5 6. 5.e-8","5.e5,6.,5.e-8,<EOF>", 43))

    def test_lexer44(self):
        self.assertTrue(TestLexer.test("anD then false", "anD,then,false,<EOF>", 44))

    def test_lexer45(self):
        self.assertTrue(TestLexer.test("sTRIng False", "sTRIng,False,<EOF>", 45))

    def test_lexer46(self):
        self.assertTrue(TestLexer.test(""" ",dls\\F12" """, """Illegal Escape In String: ,dls\\F""", 46))

    def test_lexer47(self):
        input = "a88jdjij + a2x - 40 > 12"
        expect = "a88jdjij,+,a2x,-,40,>,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 47))

    def test_lexer48(self):
        input = "as<.>iooi"
        expect = "as,<,.,>,iooi,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 48))

    def test_lexer49(self):
        input = "[;]12kkkasijiasdijANXNMXMM\t"
        expect = "[,;,],12,kkkasijiasdijANXNMXMM,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 49))

    def test_lexer50(self):
        input = ":a:sxassa:,irejgioj0990hiju."
        expect = ":,a,:,sxassa,:,,,irejgioj0990hiju,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 50))
        
    def test_lexer51(self):
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
        expect = "x,:,integer,=,65,;,mess,:,function,integer,(,n,:,integer,),{,return,n,/,50,*,2,;,},main,:,function,void,(,),{,delta,:,integer,=,mess,(,7,),;,printInteger,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 51))

    def test_lexer52(self):
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
        expect = "add,:,function,integer,(,n,:,integer,),{,sum,:,integer,=,0,;,for,(,i,=,0,,,i,<=,n,,,i,+,1,),{,sum,=,sum,+,i,;,},return,sum,;,},main,:,function,void,(,),{,delta,:,integer,=,add,(,10,),;,printInteger,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 52))

    def test_lexer53(self):
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
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 53))

    def test_lexer54(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i!=0){
                    i--;
                }
                return  i;
            }
        '''
        expect = "main,:,function,void,(,),{,i,:,integer,=,10,;,while,(,i,!=,0,),{,i,-,-,;,},return,i,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 54))

    def test_lexer55(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i>20){
                    i+=2;
                }
                return  i;
            }
        '''
        expect = "main,:,function,void,(,),{,i,:,integer,=,10,;,while,(,i,>,20,),{,i,+,=,2,;,},return,i,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 55))

    def test_lexer56(self):
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
        expect = "voidA,:,function,integer,(,n,:,integer,),{,return,n,%,10,;,},voidB,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,voidA,(,delta,),;,},main,:,function,void,(,),{,delta,:,integer,=,5,;,voidB,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 56))

    def test_lexer57(self):
        input = '''
            main: function void () {
                delta: string = "dat";
                printString(delta);
            }
        '''
        expect = "main,:,function,void,(,),{,delta,:,string,=,dat,;,printString,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 57))

    def test_lexer58(self):
        input = '''
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        '''
        expect = "main,:,function,void,(,),{,delta,:,float,=,3.45,;,printFloat,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 58))

    def test_lexer59(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                printBoolean(delta);
            }
        '''
        expect = "main,:,function,void,(,),{,delta,:,boolean,=,true,;,printBoolean,(,delta,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 59))

    def test_lexer60(self):
        input = '''
            main: function void () {
                b: array [5] of integer = [1,2,3,4,6];
                printInteger(b[4]);
            }
        '''
        expect = "main,:,function,void,(,),{,b,:,array,[,5,],of,integer,=,[,1,,,2,,,3,,,4,,,6,],;,printInteger,(,b,[,4,],),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 60))

    def test_lexer61(self):
        input = "a = true, b = false"
        expect = "a,=,true,,,b,=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 61))

    def test_lexer62(self):
        input = """ "abc\\e def" """
        expect = """Illegal Escape In String: abc\\e"""
        self.assertTrue(TestLexer.test(input, expect, 62))
    
    def test_lexer63(self):
        input = """ "ab'c\\n def" """
        expect = """ab'c\\n def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 63))

    def test_lexer64(self):
        input = """~!^^^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 64))

    def test_lexer65(self):
        input = "!@^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 65))

    def test_lexer66(self):
        input = """a= "He said: " Im Super'Man "s" testtt; __world = 5; imple = 8;"""
        expect = """a,=,He said: ,Im,Super,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 66))

    def test_lexer67(self):
        input = """a= "He said: " Hello " \n ";"""
        expect = """a,=,He said: ,Hello,Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 67))

    def test_lexer68(self):
        input = """a = "Hello \n world !";"""
        expect = """a,=,Unclosed String: Hello """
        self.assertTrue(TestLexer.test(input, expect, 68))

    def test_lexer69(self):
        input = '{1,"an\\t",3}'
        expect = "{,1,,,an\\t,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 69))

    def test_lexer70(self):
        input = "{2.3, 4.2, 102e3}"
        expect = "{,2.3,,,4.2,,,102e3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 70))

    def test_lexer71(self):
        input = "a[4] = {1, 2,  3, 4}"
        expect = "a,[,4,],=,{,1,,,2,,,3,,,4,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 71))

    def test_lexer72(self):
        input = "==!=!&&||+-/"
        expect = "==,!=,!,&&,||,+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 72))

    def test_lexer73(self):
        input = "v[5] a;"
        expect = "v,[,5,],a,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 73))

    def test_lexer74(self):
        input = "a[3 + x.foo(2)] = a[b[2]] + 3;"
        expect = "a,[,3,+,x,.,foo,(,2,),],=,a,[,b,[,2,],],+,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 74))

    def test_lexer75(self):
        input = "s=r*r*myPI;"
        expect = "s,=,r,*,r,*,myPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 75))

    def test_lexer76(self):
        input = "1/2"
        expect = "1,/,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 76))

    def test_lexer77(self):
        input = """ " \\h " """
        expect = """Illegal Escape In String:  \h"""
        self.assertTrue(TestLexer.test(input, expect, 77))

    def test_lexer78(self):
        input = """ " \\naaa\\t" """
        expect = """ \\naaa\\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 78))

    def test_lexer79(self):
        input = "{}"
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 79))

    def test_lexer80(self):
        input = """{"}"""
        expect = """{,Unclosed String: }"""
        self.assertTrue(TestLexer.test(input, expect, 80))

    def test_lexer81(self):
        input = "{False,}"
        expect = "{,False,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 81))

    def test_lexer82(self):
        input = "//{\"}"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 82))

    def test_lexer83(self):
        input = "/* abcxyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 83))

    def test_lexer84(self):
        input = '''
                // this is a line comment"
                kakf
        '''
        expect = "kakf,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 84))
    
    def test_lexer85(self):
        input = "{/* this is a line comment */ 180, 20}"
        expect = "{,180,,,20,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 85))

    def test_lexer86(self):
        input = """ "\\"aadadddldld\\"" """
        expect = """\\"aadadddldld\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 86))

    def test_lexer87(self):
        input = """ "dshf"""
        expect = """Unclosed String: dshf"""
        self.assertTrue(TestLexer.test(input, expect, 87))

    def test_lexer88(self):
        input = """ {/*"*****/*"}*/*"""
        expect = """{,*,Unclosed String: }*/*"""
        self.assertTrue(TestLexer.test(input, expect, 88))

    def test_lexer89(self):
        input = """sb0345"-a)
                    " """
        expect = """sb0345,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(input, expect, 89))

    def test_lexer90(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 90))

    def test_lexer91(self):
        input = """ "\\t\\ " """
        expect = """Illegal Escape In String: \\t\\ """
        self.assertTrue(TestLexer.test(input, expect, 91))

    def test_lexer92(self):
        input = """ "        " """
        expect = """        ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 92))

    def test_lexer93(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 93))

    def test_lexer94(self):
        input = "Var"
        expect = "Var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 94))

    def test_lexer95(self):
        input = "ab?svn"
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 95))

    def test_lexer96(self):
        input = "Var x;"
        expect = "Var,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 96))

    def test_lexer97(self):
        input = """{         "1" ,      "2"     ,      "3"       }"""
        expect = """{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 97))
    
    def test_lexer98(self):
        input = "12.000e3"
        expect = "12.000e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 98))
    
    def test_lexer99(self):
        input = "12.e-3"
        expect = "12.e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 99))
    
    def test_lexer100(self):
        self.assertTrue(TestLexer.test(""" abvccd """, """abvccd,<EOF>""", 100))
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


class LexerSuite(unittest.TestCase):
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
    
    
    def test_string_escape8(self):
        self.assertTrue(TestLexer.test("""" Print integer number by \"printInt(anArg: int)\"" """, """Print integer number by \\"printInt(anArg: int)\\",<EOF>""", 1000))
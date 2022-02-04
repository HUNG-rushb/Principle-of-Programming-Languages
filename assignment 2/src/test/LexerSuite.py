# 1913652
# Trịnh Duy Hưng

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_0(self):
        self.assertTrue(TestLexer.test("+ + - * / <= >= = < > && || ==. = ==",
        "+,+,-,*,/,<=,>=,=,<,>,&&,||,==.,=,==,<EOF>", 100))

    def test_1(self):
        self.assertTrue(TestLexer.test("+ - * / <= >= = < > && || ==. = ==",
        "+,-,*,/,<=,>=,=,<,>,&&,||,==.,=,==,<EOF>", 101))

    def test_2(self):
        self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 102))

    def test_3(self):
        self.assertTrue(TestLexer.test("23427b5", "23427,b5,<EOF>", 103))

    def test_4(self):
        self.assertTrue(TestLexer.test("_duyhung135", "_duyhung135,<EOF>", 104))

    def test_5(self):
        self.assertTrue(TestLexer.test("$12abc", "$12abc,<EOF>", 105))

    def test_6(self):
        self.assertTrue(TestLexer.test("$_dollarstatic", "$_dollarstatic,<EOF>", 106))

    def test_7(self):
        self.assertTrue(TestLexer.test("   $duy     hung", "$duy,hung,<EOF>", 107))

    def test_8(self):
        self.assertTrue(TestLexer.test("_12343_my const", "_12343_my,const,<EOF>", 108))

    def test_9(self):
        self.assertTrue(TestLexer.test("1ABC", "1,ABC,<EOF>", 109))

    def test_10(self):
        self.assertTrue(TestLexer.test("@abcd!ed", "Error Token @", 110))

    def test_11(self):
        self.assertTrue(TestLexer.test("%duyHUNG", "%,duyHUNG,<EOF>", 111))

    def test_12(self):
        self.assertTrue(TestLexer.test("* + hung      /   ", "*,+,hung,/,<EOF>", 112))

    def test_13(self):
        self.assertTrue(TestLexer.test("$", "Error Token $", 113))

    def test_14(self):
        self.assertTrue(TestLexer.test("Val $_fajfaksd_ASDFADS213134Asdvas, num____fasdfh__2136512_____dafds: Int = 0b0101110010101010100011111, 0xAFABCDEF",
                        "Val,$_fajfaksd_ASDFADS213134Asdvas,,,num____fasdfh__2136512_____dafds,:,Int,=,0b0,101110010101010100011111,,,0xAFABCDEF,<EOF>", 114))

    def test_15(self):
        self.assertTrue(TestLexer.test(
            "18_8_128_2.364872364245e67 10002322E-97381237 232431E01023473 134422.787902 178434554357.4947563E+343256669 24346436. .452345 .e123133 .7674e99995 41239778.e23124410 4587467.e213400001_232342354 17635235_89996_111154_9.49324_888845484926e3 43351_2000098898934.3_777456342356", 
            "1881282.364872364245e67,10002322E-97381237,232431E01023473,134422.787902,178434554357.4947563E+343256669,24346436.,.,452345,.e123133,.7674e99995,41239778.e23124410,4587467.e213400001,_232342354,17635235899961111549.49324,_888845484926e3,433512000098898934.3,_777456342356,<EOF>", 115))

    def test_16(self):
        self.assertTrue(TestLexer.test(
            "1_2_3_4321479326523469234 39237247362177374 12039434778957392_5_6_2_3_4 01812374738946466", "1234321479326523469234,39237247362177374,1203943477895739256234,01,812374738946466,<EOF>", 116))

    def test_17(self):
        self.assertTrue(TestLexer.test("""
        ## LoreamsdASDFOWFWJEFJ3129834329adasfdksfsdksdljfs
        """, "Error Token #", 117))

    def test_18(self):   
        self.assertTrue(TestLexer.test("""
        ##
        asdajfsk767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFdjfwqwqlqdk
        ##
        DSAFWEFWEFOIWEWsdafbawuefygweu_______________________3214932842346935436971346912736
        ##df767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFkss
        ###sf767323283443274799712831236182497fjfiufhAFOAWEFWEFWJEFKFVFIVRFIFdjsls
        ##
        """, "DSAFWEFWEFOIWEWsdafbawuefygweu_______________________3214932842346935436971346912736,Error Token #", 118))

    def test_19(self):
        self.assertTrue(TestLexer.test("\"34gegefaafwdfwogg\\mafwfweghterwd5768o\"","Illegal Escape In String: 34gegefaafwdfwogg\\m",119))

    def test_20(self):
        self.assertTrue(TestLexer.test("$FSDGM834738____sadfidufuhabc 123476761abnvdsjjsdnMMMMASDZZZ_sdjdv _16855555423 dfwedwfwePPIHDWU3536dtehiiiiiiiiiiiif",
                        "$FSDGM834738____sadfidufuhabc,123476761,abnvdsjjsdnMMMMASDZZZ_sdjdv,_16855555423,dfwedwfwePPIHDWU3536dtehiiiiiiiiiiiif,<EOF>", 120))

    def test_21(self):
        self.assertTrue(TestLexer.test("""
            "fwoieijwofjndanfDAFKWEOWJEGWG '"fjdsdsaklfjsaldkPPWHDNJNjnewwjnccedefg'""
        """, """fwoieijwofjndanfDAFKWEOWJEGWG '"fjdsdsaklfjsaldkPPWHDNJNjnewwjnccedefg'",<EOF>""", 121))

    def test_22(self):
        self.assertTrue(TestLexer.test("19789rthtrh \"wefwegxwgergyffwfewewz\k 456","19789,rthtrh,Illegal Escape In String: wefwegxwgergyffwfewewz\k",122))

    def test_23(self):
        self.assertTrue(TestLexer.test("""
            ## Testing comment fowifjowfnwio!@#@#$$#%@^@%^&?<>":{{}}({}()}:(){(})}) ##
        """, "<EOF>", 123))

    def test_24(self):
        self.assertTrue(TestLexer.test("## ASCWEasdasd !@@#%$#  %lgvkhjk$%^&*(&*~{}[]\;]\p/.,.,<>>) ##", "<EOF>",124))
    
    def test_25(self):
        self.assertTrue(TestLexer.test("## # ASCWEasdasd !@@#%$#%$%^&*(&*~{}[]\;]\p/.,.,<>>) # ##", "<EOF>",125))

    def test_26(self):
        self.assertTrue(TestLexer.test("Array(18983423,4000003023003032,352546546,9191993941294983248)",
                    "Array,(,18983423,,,4000003023003032,,,352546546,,,9191993941294983248,),<EOF>", 126))

    def test_27(self):
        self.assertTrue(TestLexer.test("""
            If (a123555 > B______123213) {Return a_63475_IIIIIIIIII;}
            Elseif (c99999 == d0000007) {hunghunga = duydydtdda + opopopopopopb;}
            Else {Return ppppppppppppppppppppppppppppppppp;}
            """, "If,(,a123555,>,B______123213,),{,Return,a_63475_IIIIIIIIII,;,},Elseif,(,c99999,==,d0000007,),{,hunghunga,=,duydydtdda,+,opopopopopopb,;,},Else,{,Return,ppppppppppppppppppppppppppppppppp,;,},<EOF>", 127))

    def test_28(self):
        self.assertTrue(TestLexer.test("""
            Foreach ($l_LLLLLLLLLLLLLL In 19 .. 100234 By 191) {
                saloaloaloalaolaooo = saloaloaloalaolaooo + iiiuiuiuiuiuiu[$mn_______________7436fhhf];
            }
            """, "Foreach,(,$l_LLLLLLLLLLLLLL,In,19,..,100234,By,191,),{,saloaloaloalaolaooo,=,saloaloaloalaolaooo,+,iiiuiuiuiuiuiu,[,$mn_______________7436fhhf,],;,},<EOF>", 128))

    def test_29(self):
        self.assertTrue(TestLexer.test("""
            {
                Var jijijijijdaf, ijijijji: Int;
                pkpsdfkpfasdf = 2_4546_898432.0123146;
                Val a7654334, b7654334: Array[String, 987798798];
                tutyuytus = pkpsdfkpfasdf * pkpsdfkpfasdf * Self.nidsidf;
                uasdfhhhhhhhha[192837] = ppppppp;
            }
            """, "{,Var,jijijijijdaf,,,ijijijji,:,Int,;,pkpsdfkpfasdf,=,24546898432.0123146,;,Val,a7654334,,,b7654334,:,Array,[,String,,,987798798,],;,tutyuytus,=,pkpsdfkpfasdf,*,pkpsdfkpfasdf,*,Self,.,nidsidf,;,uasdfhhhhhhhha,[,192837,],=,ppppppp,;,},<EOF>", 129))

    def test_30(self):
        self.assertTrue(TestLexer.test("""
            Var $arjijijijijdaf : Array[Array[Boolean, 3], 3] = Array(
                                                        Array(199,987798798,7565),
                                                        Array(346723439,87765,1236),
                                                        Array(9000000005,1348,9632847)
                                                        );
            )""", "Var,$arjijijijijdaf,:,Array,[,Array,[,Boolean,,,3,],,,3,],=,Array,(,Array,(,199,,,987798798,,,7565,),,,Array,(,346723439,,,87765,,,1236,),,,Array,(,9000000005,,,1348,,,9632847,),),;,),<EOF>", 130))

    def test_31(self):
        self.assertTrue(TestLexer.test("""anitrinhduyhungmal.canguyenthachngocquynht.talfuckk(cpluspus + "fio___adfshuf___sefoooobc");""",
                                        """anitrinhduyhungmal,.,canguyenthachngocquynht,.,talfuckk,(,cpluspus,+,fio___adfshuf___sefoooobc,),;,<EOF>""",131))
    
    def test_32(self):
            self.assertTrue(TestLexer.test("""
                    0b111111111987 0B09998888 67.9898454600003443 34577777 0X2D3FFDDDD
                    """, "0b111111111,987,0B0,9998888,67.9898454600003443,34577777,0X2D3FFDDDD,<EOF>", 132))

    def test_33(self):
        self.assertTrue(TestLexer.test("""
                New Return True False Foreach If Elseif Else Float Int String Var Val Constructor Destructor Null Class By In
                """, "New,Return,True,False,Foreach,If,Elseif,Else,Float,Int,String,Var,Val,Constructor,Destructor,Null,Class,By,In,<EOF>", 133))

    def test_34(self):
        self.assertTrue(TestLexer.test("""
                + - * / % == != ! > < >= <= || && . :: ( ) { } [ ] ==. +.
                """, "+,-,*,/,%,==,!=,!,>,<,>=,<=,||,&&,.,::,(,),{,},[,],==.,+.,<EOF>", 134))

    def test_35(self):
        self.assertTrue(TestLexer.test("\"duyhungduyhung\"ngocquynhngocquynh\"",
        "duyhungduyhung,ngocquynhngocquynh,Unclosed String: ",135))
    
    def test_36(self):
        self.assertTrue(TestLexer.test("\"jkqajkajqka\\njkqajkajqka\"","jkqajkajqka\\njkqajkajqka,<EOF>",136))

    def test_37(self):
        self.assertTrue(TestLexer.test("\"abhunghung\\thunghung\\nbhunghung\"","abhunghung\\thunghung\\nbhunghung,<EOF>",137))

    def test_38(self):
        self.assertTrue(TestLexer.test("Return triangle.getCurriculum(1010304 false true + * - 8988) - (new object()).arrayer[8444];",
        "Return,triangle,.,getCurriculum,(,1010304,false,true,+,*,-,8988,),-,(,new,object,(,),),.,arrayer,[,8444,],;,<EOF>",138))

    def test_39(self):
        self.assertTrue(TestLexer.test("""
        "7777.645656454235dfdsgjsidfgji888888...98f834jfjfnnvnvnnv\'trinhduyhung" 8956854.nguyenthachngocquynh "878736636\\\\0b10010101111111111"
        ""","7777.645656454235dfdsgjsidfgji888888...98f834jfjfnnvnvnnv'trinhduyhung,8956854.,nguyenthachngocquynh,878736636\\\\0b10010101111111111,<EOF>",139))

    def test_40(self):
        self.assertTrue(TestLexer.test("Trinh_Duy_Hung_fdfijf \"trinhduyhung1!!@#$@%%%%*&*&*&*&*&@#$@$#@$%^i\\n\" 555555555555jijijijiyz",
                                        "Trinh_Duy_Hung_fdfijf,trinhduyhung1!!@#$@%%%%*&*&*&*&*&@#$@$#@$%^i\\n,555555555555,jijijijiyz,<EOF>",140))

    def test_41(self):
        self.assertTrue(TestLexer.test("\"!h$5FBi6qwddasd\"_nguyenthachngocquynhq\"!SZRhungquynh,H}\"sI666677fpw",
                                            "!h$5FBi6qwddasd,_nguyenthachngocquynhq,!SZRhungquynh,H},sI666677fpw,<EOF>",141))
        
    def test_42(self):
        self.assertTrue(TestLexer.test("""
        uwufhweuf4"&uwufhweufJ^1uwufhweufa_." QuwufhweufGn"?6uwufhweuf7Sp"{,}6Asz"Yx]("
        ""","uwufhweuf4,&uwufhweufJ^1uwufhweufa_.,QuwufhweufGn,?6uwufhweuf7Sp,{,,,},6,Asz,Yx](,<EOF>",142))

    def test_43(self):
        self.assertTrue(TestLexer.test("0ff234f23f2f1_\"^VzxvLRfffffuuu@\\\\OushungquynhM;\"uGquynhhungM+jfffasdE",
                                        "0,ff234f23f2f1_,^VzxvLRfffffuuu@\\\\OushungquynhM;,uGquynhhungM,+,jfffasdE,<EOF>",143))

    def test_44(self):
        self.assertTrue(TestLexer.test("\"(trinhduyhungItrinhduyhungFtrinhduyhungq+trinhduyhunglq(\"trinhduyhungIhKtrinhduyhung6we(*.*)GdvS{(}",
                                        "(trinhduyhungItrinhduyhungFtrinhduyhungq+trinhduyhunglq(,trinhduyhungIhKtrinhduyhung6we,(,*,.,*,),GdvS,{,(,},<EOF>",144))

    def test_45(self):
        self.assertTrue(TestLexer.test("\"btrinhduyhungac\\mtrinhduyhunga\"","Illegal Escape In String: btrinhduyhungac\\m",145))

    def test_46(self):
        self.assertTrue(TestLexer.test("\"btrinhduyhungatrinhduyhungMD\\HtrinhduyhungLtrinhduyhungSc\\ntrinhduyhungatrinhduyhung\"","Illegal Escape In String: btrinhduyhungatrinhduyhungMD\\H",146))

    def test_47(self):
        self.assertTrue(TestLexer.test("\",dtrinhduyhungls\\Ftrinhduyhung1trinhduyhung2trinhduyhung!trinhduyhungLtrinhduyhungS\\ktrinhduyhungctrinhduyhung\\trinhduyhungnatrinhduyhung\"","Illegal Escape In String: ,dtrinhduyhungls\\F",147))

    def test_48(self):
        self.assertTrue(TestLexer.test("\"atrinhduyhungdo\\madotrinhduyhung\"","Illegal Escape In String: atrinhduyhungdo\\m",148))

    def test_49(self):
        self.assertTrue(TestLexer.test("78799923trinhduyhungnguyenthachngocquynhabc \"xtrinhduyhungytrinhduyhungz\k 456",
                                    "78799923,trinhduyhungnguyenthachngocquynhabc,Illegal Escape In String: xtrinhduyhungytrinhduyhungz\k",149))

    def test_50(self):
        self.assertTrue(TestLexer.test("\"nguyenthachngocquynhanguyenthachngocquynha\wb\"","Illegal Escape In String: nguyenthachngocquynhanguyenthachngocquynha\w",150))

    def test_51(self):
        self.assertTrue(TestLexer.test("bnguyenthachngocquynha+1786544332+\"nnguyenthachngocquynha\"\"mnguyenthachngocquynhd+119238219.2-401203040468\lb",
                                        "bnguyenthachngocquynha,+,1786544332,+,nnguyenthachngocquynha,Illegal Escape In String: mnguyenthachngocquynhd+119238219.2-401203040468\l",151))

    def test_52(self):
        self.assertTrue(TestLexer.test("\"1.744462+1.744463+1.744464\\o'\"123","Illegal Escape In String: 1.744462+1.744463+1.744464\\o",152))

    def test_53(self):
        self.assertTrue(TestLexer.test("(*nangocquynhdethuongc*)/2232881.73181231 \"bcuoingocquynha\\qm\f\"",
                                        "(,*,nangocquynhdethuongc,*,),/,2232881.73181231,Illegal Escape In String: bcuoingocquynha\q",153))

    def test_54(self):
        self.assertTrue(TestLexer.test("\"congocquynhdangyeuncahngocquynhdangyeueo\\uabc","Illegal Escape In String: congocquynhdangyeuncahngocquynhdangyeueo\\u",154))

    def test_55(self):
        self.assertTrue(TestLexer.test("\"trinhduyhungbatrinhduyhungcxytrinhduyhungc",
                                            "Unclosed String: trinhduyhungbatrinhduyhungcxytrinhduyhungc",155))

    def test_56(self):
        self.assertTrue(TestLexer.test("NngocquynhsexymkngocquynhsexyobYngocquynhsexyn{!}+I1+\"`YSnewyodjdjdj2h.ueywuJ(",
                                            "NngocquynhsexymkngocquynhsexyobYngocquynhsexyn,{,!,},+,I1,+,Unclosed String: `YSnewyodjdjdj2h.ueywuJ(",156))

    def test_57(self):
        self.assertTrue(TestLexer.test("\"abeQuynhbeRotcbeQuynhbeRotnv \" \"ahunghudhdhdbc","abeQuynhbeRotcbeQuynhbeRotnv ,Unclosed String: ahunghudhdhdbc",157))

    def test_58(self):
        self.assertTrue(TestLexer.test("\"bsaunaycuoiQuynhcms!,lds \" {\"gh6473f94f8hhhhfhASDGGGGGGGGGGGGGGGGGc\"} 123\"abeQuynhdethuong7273817361bc",
                                        "bsaunaycuoiQuynhcms!,lds ,{,gh6473f94f8hhhhfhASDGGGGGGGGGGGGGGGGGc,},123,Unclosed String: abeQuynhdethuong7273817361bc",158))

    def test_59(self):
        self.assertTrue(TestLexer.test("a+11.23749283470202002+\"masdanfjsdDAviidd_______m.123\" 12 \"%^_)3141927777&",
                                        "a,+,11.23749283470202002,+,masdanfjsdDAviidd_______m.123,12,Unclosed String: %^_)3141927777&",159))

    def test_60(self):
        self.assertTrue(TestLexer.test("323344448n\"[#FfQuynhsQuynh?0ED\"1.1\"dddd`#","323344448,n,[#FfQuynhsQuynh?0ED,1.1,Unclosed String: dddd`#",160))

    def test_61(self):
        self.assertTrue(TestLexer.test("\"stnguyenthachngocquynhr1  \\r ahnguyenthachngocquynhihi \"","stnguyenthachngocquynhr1  \\r ahnguyenthachngocquynhihi ,<EOF>",161))

    def test_62(self):
        self.assertTrue(TestLexer.test("\"He aajjTrinhDuyked me: '\"ajjTrinhDuyhere \\t ajjTrinhDuys ajjTrinhDuyohn?'\"\"",
                                            "He aajjTrinhDuyked me: \'\"ajjTrinhDuyhere \\t ajjTrinhDuys ajjTrinhDuyohn?\'\",<EOF>",162))

    def test_63(self):
        self.assertTrue(TestLexer.test("\"  sQuynhdiahuongtr \\\' \\\" sQuynhdiahuongtr \"","Illegal Escape In String:   sQuynhdiahuongtr \\' \\\"",163))
     
    def test_64(self):
        self.assertTrue(TestLexer.test("\" \\\\ \\n \\t \\n fbeQuynhditbudffffdvvd \\\\\" "," \\\\ \\n \\t \\n fbeQuynhditbudffffdvvd \\\\,<EOF>",164))

    def test_65(self):
        self.assertTrue(TestLexer.test("{ 1,2  ,  37766662,  2}; {1.923489282,2., 111113e8  , 4645.0e-1}","{,1,,,2,,,37766662,,,2,},;,{,1.923489282,,,2.,,,111113e8,,,4645.0e-1,},<EOF>",165))

    def test_66(self):
        self.assertTrue(TestLexer.test("{true,false   ,  true, false}; {\" nareiuiqpm\", \" vreiuiqpat lreiuiqpy \"  ,  \" ancxbaa \" }",
                                        """{,true,,,false,,,true,,,false,},;,{, nareiuiqpm,,, vreiuiqpat lreiuiqpy ,,, ancxbaa ,},<EOF>""",166))

    def test_67(self):
        self.assertTrue(TestLexer.test("if(a != b)\nthen continuea=a+1;\nelse b=0;","if,(,a,!=,b,),then,continuea,=,a,+,1,;,else,b,=,0,;,<EOF>",167))

    def test_68(self):
        self.assertTrue(TestLexer.test("return nebeQuynhlozmupwn then anbeQuynhlozmupimal(abeQuynhlozmup,bbeQuynhlozmup + cbeQuynhlozmup);",
                                        "return,nebeQuynhlozmupwn,then,anbeQuynhlozmupimal,(,abeQuynhlozmup,,,bbeQuynhlozmup,+,cbeQuynhlozmup,),;,<EOF>",168))

    def test_69(self):
        self.assertTrue(TestLexer.test("cffffallFn then ffffunction(ayuie + byuie*cyuie % (dyuie+2));",
                                        "cffffallFn,then,ffffunction,(,ayuie,+,byuie,*,cyuie,%,(,dyuie,+,2,),),;,<EOF>",169))

    def test_70(self):
        self.assertTrue(TestLexer.test("""
        yervva[7766+9766] = 12;
        Foreach(i = 1 In 1 .. styervvr.lenyervvgth) {
            yervvb[i] = yervvb[i] + 1766;
        }
        """,
        "yervva,[,7766,+,9766,],=,12,;,Foreach,(,i,=,1,In,1,..,styervvr,.,lenyervvgth,),{,yervvb,[,i,],=,yervvb,[,i,],+,1766,;,},<EOF>", 170))

    def test_71(self):
        self.assertTrue(TestLexer.test("""
        aQuynhQuynh = 1345;
        bQuynhQuynh[1345+cQuynhQuynh] = (trffwfefweue && !fvdsfd || _zQuynhQuynh) != false;
        """
        ,"aQuynhQuynh,=,1345,;,bQuynhQuynh,[,1345,+,cQuynhQuynh,],=,(,trffwfefweue,&&,!,fvdsfd,||,_zQuynhQuynh,),!=,false,;,<EOF>",171))

    def test_72(self):
        self.assertTrue(TestLexer.test("""aniQuynhdethuongmal.cQuynhdethuongat.taQuynhdethuonglk(sQuynhdethuong + "QuynhdethuongabcQuynhdethuong");""",
                                        """aniQuynhdethuongmal,.,cQuynhdethuongat,.,taQuynhdethuonglk,(,sQuynhdethuong,+,QuynhdethuongabcQuynhdethuong,),;,<EOF>""",172))

    def test_73(self):
        self.assertTrue(TestLexer.test("return aghjjbc.gedadsadastArea(1 trfalseue + 2) - (new obj()).arr[1];",
                                        "return,aghjjbc,.,gedadsadastArea,(,1,trfalseue,+,2,),-,(,new,obj,(,),),.,arr,[,1,],;,<EOF>",173))

    def test_74(self):
        self.assertTrue(TestLexer.test("""
        funHungnection_test(aloaloo: String) {
            ## alo alo alo alo phai Quynh hong da##
            getTrinhDuyHungString("inHungneput");
        }
        ""","funHungnection_test,(,aloaloo,:,String,),{,getTrinhDuyHungString,(,inHungneput,),;,},<EOF>", 174))

    def test_75(self):
        self.assertTrue(TestLexer.test("""
        Float Break(output: Float; l: Bool) {
            classfwefSTR.gefweftData(output);
            if (l6733 > 0) {
                Break getS() + output;
            }
            else {
                Break output;
            }
            else {
                Break output;
            }
        }
        """
        ,"Float,Break,(,output,:,Float,;,l,:,Bool,),{,classfwefSTR,.,gefweftData,(,output,),;,if,(,l6733,>,0,),{,Break,getS,(,),+,output,;,},else,{,Break,output,;,},else,{,Break,output,;,},},<EOF>", 175))

    def test_76(self):
        self.assertTrue(TestLexer.test("float return(){float dataAnalist=?getWife()",
                                       "float,return,(,),{,float,dataAnalist,=,Error Token ?",176))
    def test_77(self):
        self.assertTrue(TestLexer.test(""" float getQuynhForever(){return "afwefuiawfjdsojfiasojbc\\g!!";}""",
                                        """float,getQuynhForever,(,),{,return,Illegal Escape In String: afwefuiawfjdsojfiasojbc\g""",177))

    def test_78(self):
        self.assertTrue(TestLexer.test("345.2345 9855.0 0.11111111111 34534e+7781112 85522.12342E-45552 10101010101.4238e-9999999 .534699E11111111 0.234524874340000000000000000033134663E-13453927432743",
                                        "345.2345,9855.0,0.11111111111,34534e+7781112,85522.12342E-45552,10101010101.4238e-9999999,.534699E11111111,0.234524874340000000000000000033134663E-13453927432743,<EOF>",178))

    def test_79(self):
        self.assertTrue(TestLexer.test("                12_47_23_98_5_72_3_2e8             /                      983216363628E-12347492321",
                                        "1247239857232e8,/,983216363628E-12347492321,<EOF>",179))

    def test_80(self):
        self.assertTrue(TestLexer.test("0x0",
                                        "0x0,<EOF>",180))

    def test_81(self):
        self.assertTrue(TestLexer.test("12_38_21_47_9_9_99.183999990000000000000000000000000001112342",
                                        "123821479999.183999990000000000000000000000000001112342,<EOF>",181))

    def test_82(self):
        self.assertTrue(TestLexer.test("e--12            E--4345    102E--56757",
                                        "e,-,-,12,E,-,-,4345,102,E,-,-,56757,<EOF>",182))

    def test_83(self):
        self.assertTrue(TestLexer.test("4325134442.667724e0 -999999999999999 45345351e-57345 32451.12333e8678",
                                        "4325134442.667724e0,-,999999999999999,45345351e-57345,32451.12333e8678,<EOF>",183))

    def test_84(self):
        self.assertTrue(TestLexer.test("""
        ## Function(){} abcd
            abcde ##
            anhsecogangcuoiemnhaQuynh
        ## ##
        ""","anhsecogangcuoiemnhaQuynh,<EOF>",184))

    def test_85(self):
        input ="""
        wedding(sdddddddd: Float, tdddddddd: Float) {
            Var object = New Bus();
            if (sdddddddd > 00) {
                object.insert(sdddddddd,tdddddddd);
            }
            else {
                return object;
            }
        }
    """
        output = "wedding,(,sdddddddd,:,Float,,,tdddddddd,:,Float,),{,Var,object,=,New,Bus,(,),;,if,(,sdddddddd,>,00,),{,object,.,insert,(,sdddddddd,,,tdddddddd,),;,},else,{,return,object,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input,output,185))

    def test_86(self):
        input = """
        nevergiveup(sdddddddd: Float, tdddddddd: Float, object: Boolean) {
            object.removeBus(t);
        }

        hunglovequynh() {
            return truelove;
        }
        """
        output = "nevergiveup,(,sdddddddd,:,Float,,,tdddddddd,:,Float,,,object,:,Boolean,),{,object,.,removeBus,(,t,),;,},hunglovequynh,(,),{,return,truelove,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, output, 186))

    def test_87(self):
        self.assertTrue(TestLexer.test("\"met youin the back during twelve o fivedd \\\" \n dd \" ",
                                        "Illegal Escape In String: met youin the back during twelve o fivedd \\\"",187))

    def test_88(self):
        self.assertTrue(TestLexer.test("\"happy 10 years anniversary","""Unclosed String: happy 10 years anniversary""",188))

    def test_89(self):
        self.assertTrue(TestLexer.test("\"wfiwuefwifjlsadfsdhfhfhfhfhhfhfhf1\\ \"",
                                        "Illegal Escape In String: wfiwuefwifjlsadfsdhfhfhfhfhhfhfhf1\\ ",189))

    def test_90(self):
        self.assertTrue(TestLexer.test("\"Hung thich Quynh lam do ahihi\'\" ahihi ",
                                                "Unclosed String: Hung thich Quynh lam do ahihi\'\" ahihi ",190))

    def test_91(self):
            """test identifiers"""
            self.assertTrue(TestLexer.test("\"WebDev\\dclub \\dBKU\";",
                                            "Illegal Escape In String: WebDev\\d", 191))
                            
    def test_92(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"Quynhdethuongahihi\\nfkkkkkkoekofkw \\niwillmarryou\";",
                                        """Quynhdethuongahihi\\nfkkkkkkoekofkw \\niwillmarryou,;,<EOF>""",192))
    
    def test_93(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("""Var $Hung_love_Quynh : Array[Array[Boolean, 3], 3] = 
                                       Array(
                                           Array(true,false,false),
                                           Array(false,true,true),
                                           Array(false,false,true)
                                           );""",
                                    "Var,$Hung_love_Quynh,:,Array,[,Array,[,Boolean,,,3,],,,3,],=,Array,(,Array,(,true,,,false,,,false,),,,Array,(,false,,,true,,,true,),,,Array,(,false,,,false,,,true,),),;,<EOF>",193))
    
    def test_94(self):
        self.assertTrue(TestLexer.test("""
                                       234"&23J^1a_.23" QGn"?6dddddddddddddddddddddddddddddddddddddddd7Sp"{,}6678209Adddwsz"Ydqdwx]("
                                       ""","234,&23J^1a_.23,QGn,?6dddddddddddddddddddddddddddddddddddddddd7Sp,{,,,},6678209,Adddwsz,Ydqdwx](,<EOF>", 194)) 

    def test_95(self):
        self.assertTrue(TestLexer.test("""
            Foreach ($i In 1 .. 100 By 1) {
                e = e + $i;
                k[$i] = k[$i + 1];
                Foreach ($j In 1 .. 100 By 1) {
                    e = e - $j;
                    l[$i] = l[$j] + e; 
                }
            }
            """, "Foreach,(,$i,In,1,..,100,By,1,),{,e,=,e,+,$i,;,k,[,$i,],=,k,[,$i,+,1,],;,Foreach,(,$j,In,1,..,100,By,1,),{,e,=,e,-,$j,;,l,[,$i,],=,l,[,$j,],+,e,;,},},<EOF>", 195))

    def test_96(self):
        self.assertTrue(TestLexer.test("\"##Nguyen Thach Ngoc Quynh##\"", 
                                            "##Nguyen Thach Ngoc Quynh##,<EOF>", 196))
    
    def test_97(self):
        self.assertTrue(TestLexer.test("Val $xdxxdxdXDXDXDXD, afhhhhhhhhh, $fwweieeeeeee, 9$gh : Array = 5732828791111, 6732828791111, 7732828791111;",
                                        "Val,$xdxxdxdXDXDXDXD,,,afhhhhhhhhh,,,$fwweieeeeeee,,,9,$gh,:,Array,=,5732828791111,,,6732828791111,,,7732828791111,;,<EOF>",197))

    def test_98(self):
        self.assertTrue(TestLexer.test("Var $husadhfosddiidid, hope1day: Boolean = 0b0123456789, 0x473738FEBED;",
                                        "Var,$husadhfosddiidid,,,hope1day,:,Boolean,=,0b0,123456789,,,0x473738FEBED,;,<EOF>",198))

    def test_99(self):
        self.assertTrue(TestLexer.test("""
            If (aQuynhdethuongquadi >= bQuynhdethuongquadi) {
                aQuynhdethuongquadi = aQuynhdethuongquadi + bQuynhdethuongquadi;
            }
            Elseif (b >= cQuynhdethuongquadi) {
                bQuynhdethuongquadi = aQuynhdethuongquadi + bQuynhdethuongquadi || rQuynhdethuongquadi;
            }
            Else {
                Return Quynhdethuongquadi;
            }
            Else {
                Return Quynhdethuongquadi;
            }
            Else {
                Return Quynhdethuongquadi;
            }
        ""","If,(,aQuynhdethuongquadi,>=,bQuynhdethuongquadi,),{,aQuynhdethuongquadi,=,aQuynhdethuongquadi,+,bQuynhdethuongquadi,;,},Elseif,(,b,>=,cQuynhdethuongquadi,),{,bQuynhdethuongquadi,=,aQuynhdethuongquadi,+,bQuynhdethuongquadi,||,rQuynhdethuongquadi,;,},Else,{,Return,Quynhdethuongquadi,;,},Else,{,Return,Quynhdethuongquadi,;,},Else,{,Return,Quynhdethuongquadi,;,},<EOF>",199))

# End 100 testcases
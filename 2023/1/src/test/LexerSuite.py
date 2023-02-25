# # 1913652
# # Trịnh Duy Hưng

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lexer0(self):
        self.assertTrue(TestLexer.test("njviuehrfiuwaojdoa_____sjfdoFAWEFAWECASDCdsVRERE______ifjiodjcvr436763172637126372________________", "njviuehrfiuwaojdoasjfdoifjiodjcvr436763172637126372________________,<EOF>", 0))
        
    def test_lexer1(self):
        input = """{"}"""
        expect = """{,Unclosed String: }"""
        self.assertTrue(TestLexer.test(input, expect, 1))

    def test_lexer2(self):
        input = "{False,}"
        expect = "{,False,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 2))

    def test_lexer3(self):
        input = "// owifjowowejoiwjefowejfijcsojios_____{}}{}}{}{}232235_+_+=-=-=-=-//*/*\\\||||||???.,.,><<<>>>{}{}{}{}{}>?><?<23424234>?<>?!@#"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 3))

    def test_lexer4(self):
        input = "/* jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKFwjfoiwjjvoeirvernvnernrjlj6465644849_________-______--__--+=_+-=_=_=-=-+-=32030323xyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 4))

    def test_lexer5(self):
        input = "// v;ier;fio fpoun unpirvoervoerr73289701802198301293 /*"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 5))
    
    def test_lexer6(self):
        input = "{/* 1832748302748092749056347658734 */ 182342445346540, 9898398928384923849238493284932}"
        expect = "{,182342445346540,,,9898398928384923849238493284932,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 6))

    def test_lexer7(self):
        input = """ "\\"iudhfiuawhfiwuehfiuew327498179812hhdekackadscbywucbaweufgyweuygfwiegfyuewtrry7328y272837827827382738273827382\\"" """
        expect = """\\"iudhfiuawhfiwuehfiuew327498179812hhdekackadscbywucbaweufgyweuygfwiegfyuewtrry7328y272837827827382738273827382\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 7))

    def test_lexer8(self):
        input = """ "fiwjfowiefoweur28738929837983ud8fudfauhuygsjkgfuiafywiuyfiweuyfuwefyiweufyiweff"""
        expect = """Unclosed String: fiwjfowiefoweur28738929837983ud8fudfauhuygsjkgfuiafywiuyfiweuyfuwefyiweufyiweff"""
        self.assertTrue(TestLexer.test(input, expect, 8))

    def test_lexer9(self):
        input = """ {/*"*****/*"}*/*"""
        expect = """{,*,Unclosed String: }*/*"""
        self.assertTrue(TestLexer.test(input, expect, 9))

    def test_lexer10(self):
        input = """_fewf_ovoi_____________________________45"-__________________________________________erjoierjoierjgoeirjgoiegjoeriga)
                    " """
        expect = """_fewf_ovoi_____________________________45,Unclosed String: -__________________________________________erjoierjoierjgoeirjgoiegjoeriga)"""
        self.assertTrue(TestLexer.test(input, expect, 10))

    def test_lexer11(self):
        input = """ "woefjowiajfowiefjowjfoi___________________984329849328432984732864327jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF\\x" """
        expect = """Illegal Escape In String: woefjowiajfowiefjowjfoi___________________984329849328432984732864327jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF\\x"""
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
        input = "fwkefjwkjfkwjefkwjefkwfjkweff4238749832743287429384787563467______________________nshfhf6276732672364327_________________________________c"
        expect = "fwkefjwkjfkwjefkwjefkwfjkweff4238749832743287429384787563467______________________nshfhf6276732672364327_________________________________c,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 14))

    def test_lexer15(self):
        input = "rgrgrgrgrgwr21333123131231231265324628e892e9_________________________________________________________________________fkwkflwkffkfkkfkfkfkfkfkfkowroiwr98r92rir2or230942049203942034920349320"
        expect = "rgrgrgrgrgwr21333123131231231265324628e892e9_________________________________________________________________________fkwkflwkffkfkkfkfkfkfkfkfkowroiwr98r92rir2or230942049203942034920349320,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 15))

    def test_lexer16(self):
        input = "_________________________________________________________________________?svn"
        expect = "_________________________________________________________________________,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 16))

    def test_lexer17(self):
        input = "HUngngngngnngngngngngngnngngngngngnngnng ruiewurewoiruoweiurqperuwqhasfkasdgfafawyeuewryiuwry7247324287823748237482347___________________________________________________________________;"
        expect = "HUngngngngnngngngngngngnngngngngngnngnng,ruiewurewoiruoweiurqperuwqhasfkasdgfafawyeuewryiuwry7247324287823748237482347___________________________________________________________________,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 17))

    def test_lexer18(self):
        input = """{         "37298742983472983471" ,      "2655464545444444444444444444"     ,      "33273874823748327482347328"       }"""
        expect = """{,37298742983472983471,,,2655464545444444444444444444,,,33273874823748327482347328,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 18))
    
    def test_lexer19(self):
        input = "3264264872364832746287346827364328746736437643746736.000000000000000000000000000000000000000000000000000000000000000000000000e1111111111111111111111111111111111111111111111111113"
        expect = "3264264872364832746287346827364328746736437643746736.000000000000000000000000000000000000000000000000000000000000000000000000e1111111111111111111111111111111111111111111111111113,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 19))
    
    def test_lexer20(self):
        input = "1743287482374283743827428347823742384738424732874283472837428347328472.e-743287482374283743827428347823742384738424732874283472837428347328473"
        expect = "1743287482374283743827428347823742384738424732874283472837428347328472.e-743287482374283743827428347823742384738424732874283472837428347328473,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 20))
    
    def test_lexer21(self):
        self.assertTrue(TestLexer.test(""" sfhkhfwkfhwefjewkljflwejfkwejflkawjfwkaejflwkfjlwkfjewkfjal """, """sfhkhfwkfhwefjewkljflwejfkwejflkawjfwkaejflwkfjlwkfjewkfjal,<EOF>""", 21))
        
        
    def test_lexer22(self):
        input = """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!^^^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 22))

    def test_lexer23(self):
        input = "!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 23))
        
    def test_lexer24(self):
        input = '""'
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 24))
        
    def test_lexer25(self):
        input = '''
            for (i = 1344242342423423432432423432, i < 1fwefhweuhfiwjeiwejf0, i + 1) {
                writeInt(i);
                }
            '''
        expect = "for,(,i,=,1344242342423423432432423432,,,i,<,1fwefhweuhfiwjeiwejf0,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 25))
        
    def test_lexer26(self):
        input = '''
            fwewerwrwrwerwerwerewrewoo(92384932849284932849284928342 + x__________________________________________________, 44564646546546546546464.0 / y);
            gowewerwerwerwrwerewrwerwero();
            '''
        expect = "fwewerwrwrwerwerwerewrewoo,(,92384932849284932849284928342,+,x__________________________________________________,,,44564646546546546546464.0,/,y,),;,gowewerwerwerwrwerewrwerwero,(,),;,<EOF>"
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
            "1324342343243243203_593423423423324240"
            '''
        expect = "1324342343243243203_593423423423324240,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 29))
        
    def test_lexer30(self):
        input = '''
            13231214324324054353453439_390_21231239123243430434342434344232323232323233232_
            '''
        expect = "1323121432432405435345343939021231239123243430434342434344232323232323233232,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 30))
        
    def test_lexer31(self):
        self.assertTrue(TestLexer.test("!a%5&&b||c+*", "!,a,%,5,&&,b,||,c,+,*,<EOF>", 31))

    def test_lexer32(self):
        self.assertTrue(TestLexer.test("a==b==01234!=432101312312312312<3>4", "a,==,b,==,0,1234,!=,432101312312312312,<,3,>,4,<EOF>", 32))

    def test_lexer33(self):
        self.assertTrue(TestLexer.test("*and<=>mod<\\<=9u9283287402342093809uifojfoijoifjoierjiesrjo", "*,and,<=,>,mod,<,Error Token \\", 33))

    def test_lexer34(self):
        self.assertTrue(TestLexer.test("/*thsegergesgis isgserges            s aergsergergesg cmtregserg*/", "<EOF>", 34))

    def test_lexer35(self):
        self.assertTrue(TestLexer.test("//hjhjhusrgergergserhu/*youergergsegrare lgsegergive */", "<EOF>", 35))

    def test_lexer36(self):
        self.assertTrue(TestLexer.test("//heergergergsellewo mwfwfywef f              fawf234242 riwfwfewfawfsadfsdafsadvwaeend \n a_____seurirui283743287482374832748da", "as_____deurirui283743287482374832748a,<EOF>", 36))

    def test_lexer37(self):
        self.assertTrue(TestLexer.test("/*helwefwflodfsd fsfsd  f  fwewefewe   wfrdssafend \n nothinfweafwfsdghjhj \n love */ nfwefwfwfwfweftp", "nfwefwfwfwfweftp,<EOF>", 37))

    def test_lexer38(self):
        self.assertTrue(TestLexer.test("awefwefwfwfassf fwfwfwfwewefwefaso WEWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD589539485934859348________________owoad ", "awefwefwfwfassf,fwfwfwfwewefwefaso,WEWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD589539485934859348________________owoad,<EOF>", 38))

    def test_lexer39(self):
        self.assertTrue(TestLexer.test("hello 332323232332323232 qeqeqeqeqeqe wfwefwfwefwf regergergerg", "hello,332323232332323232,qeqeqeqeqeqe,wfwefwfwefwf,regergergerg,<EOF>", 39))

    def test_lexer40(self):
        self.assertTrue(TestLexer.test("thefweffffffew23423432_____342483284728374____u thefweffffffew23423432_____342483284728374____u aefweffffffew23423432_____342483284728374____bc () ", "thefweffffffew23423432_____342483284728374____u,thefweffffffew23423432_____342483284728374____u,aefweffffffew23423432_____342483284728374____bc,(,),<EOF>", 40))

    def test_lexer41(self):
        self.assertTrue(TestLexer.test("0123322232323 100000000 00132323232 19348984932849394298493289432940", "0,123322232323,100000000,0,0,132323232,19348984932849394298493289432940,<EOF>", 41))

    def test_lexer42(self):
        self.assertTrue(TestLexer.test("0.454574857487584 0399656565656565655 23434343434430_32121212129 0.3e53243242342342345","0.454574857487584,0,399656565656565655,2343434343443032121212129,0.3e53243242342342345,<EOF>", 42))

    def test_lexer43(self):
        self.assertTrue(TestLexer.test("5.e52323423 6132131231231. 5.e-8","5.e52323423,6132131231231.,5.e-8,<EOF>", 43))

    def test_lexer44(self):
        self.assertTrue(TestLexer.test("anwe3287492387jafjfijwei_____D then false", "anwe3287492387jafjfijwei_____D,then,false,<EOF>", 44))

    def test_lexer45(self):
        self.assertTrue(TestLexer.test("sTRIfwfwefwefwefwefewfewfwefewfng False", "sTRIfwfwefwefwefwefewfewfwefewfng,False,<EOF>", 45))

    def test_lexer46(self):
        self.assertTrue(TestLexer.test(""" ",rregrerggdriutiertueri___________s\\F12" """, """Illegal Escape In String: ,rregrerggdriutiertueri___________s\\F""", 46))

    def test_lexer47(self):
        input = "agrggrgere88jdjij + a23424234324324__________2x - 88888888888888888888888888888888 > 34829389238932892382"
        expect = "agrggrgere88jdjij,+,a23424234324324__________2x,-,88888888888888888888888888888888,>,34829389238932892382,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 47))

    def test_lexer48(self):
        input = "aafwjfuwjfwjefjwoefewi37424s<.>didididiedidewidewoidwidowioweiowifowfi"
        expect = "aafwjfuwjfwjefjwoefewi37424s,<,.,>,didididiedidewidewoidwidowioweiowifowfi,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 48))

    def test_lexer49(self):
        input = "[;]12kkkasijiasdijwefowiefoiwefuawfu__________7432432849238493284AFSFAFWEFWEFAWFWEF___________________________ANXNMXMM\t"
        expect = "[,;,],12,kkkasijiasdijwefowiefoiwefuawfu__________7432432849238493284AFSFAFWEFWEFAWFWEF___________________________ANXNMXMM,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 49))

    def test_lexer50(self):
        input = ":a:sxassa:,irejgwefowiefoiwefuawfu__________7432432849238493284AFSFAFWEFWEFAWFWEF___________________________ioj0990hiju."
        expect = ":,a,:,sxassa,:,,,irejgiojwefowiefoiwefuawfu__________7432432849238493284AFSFAFWEFWEFAWFWEF___________________________0990hiju,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 50))
        
    def test_lexer51(self):
        input = '''
            fwfwefwefwfwfwefwfwefwx: integer = 64234324234324324235;
            mefwefwr42342ss: function integer(n: integer){
                return n/50432424234324 * 213123123131312;
            }
            main: function void () {
                delwerwrwerwerewrwerwta: integer = mess(7);
                printInteger(wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
            }
        '''
        expect = "fwfwefwefwfwfwefwfwefwx,:,integer,=,64234324234324324235,;,mefwefwr42342ss,:,function,integer,(,n,:,integer,),{,return,n,/,50432424234324,*,213123123131312,;,},main,:,function,void,(,),{,delwerwrwerwerewrwerwta,:,integer,=,mess,(,7,),;,printInteger,(,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,},<EOF>"
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
                wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: integer = add(10);
                printInteger(wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
            }
        '''
        expect = "add,:,function,integer,(,n,:,integer,),{,sum,:,integer,=,0,;,for,(,i,=,0,,,i,<=,n,,,i,+,1,),{,sum,=,sum,+,i,;,},return,sum,;,},main,:,function,void,(,),{,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,integer,=,add,(,10,),;,printInteger,(,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 52))

    def test_lexer53(self):
        input = '''
            x: integer = 65;
            fact: function integer(n: integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: integer){
                n = n + wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293;
            }
            main: function void () {
                wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: integer = fact(3);
                inc(x,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
                printInteger(x);
            }
        '''
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,integer,),{,n,=,n,+,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,;,},main,:,function,void,(,),{,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,integer,=,fact,(,3,),;,inc,(,x,,,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,printInteger,(,x,),;,},<EOF>"
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
            voidB: function void (out n: integer, wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: integer){
                n = n + voidA(wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
            }
            main: function void () {
                wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: integer = 5;
                voidB(x,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
                printInteger(x);
            }
        '''
        expect = "voidA,:,function,integer,(,n,:,integer,),{,return,n,%,10,;,},voidB,:,function,void,(,out,n,:,integer,,,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,integer,),{,n,=,n,+,voidA,(,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,},main,:,function,void,(,),{,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,integer,=,5,;,voidB,(,x,,,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,printInteger,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 56))

    def test_lexer57(self):
        input = '''
            main: function void () {
                wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: string = "dat";
                printString(wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
            }
        '''
        expect = "main,:,function,void,(,),{,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,string,=,dat,;,printString,(,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 57))

    def test_lexer58(self):
        input = '''
            main: function void () {
                wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: float = 3.45;
                printFloat(wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
            }
        '''
        expect = "main,:,function,void,(,),{,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,float,=,3.45,;,printFloat,(,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 58))

    def test_lexer59(self):
        input = '''
            main: function void () {
                wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293: boolean = true;
                printBoolean(wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293);
            }
        '''
        expect = "main,:,function,void,(,),{,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,:,boolean,=,true,;,printBoolean,(,wuuiweuiefuwifuiewfuwifuwiefuwiefuwifuwifuweufwie324824289482934832984293,),;,},<EOF>"
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
        input = """ "jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF\\e def" """
        expect = """Illegal Escape In String: jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF\\e"""
        self.assertTrue(TestLexer.test(input, expect, 62))
    
    def test_lexer63(self):
        input = """ "fwkefjwkjfkwjefkwjefkwfjkwef'c\\n def" """
        expect = """fwkefjwkjfkwjefkwjefkwfjkwef'c\\n def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 63))

    def test_lexer64(self):
        input = """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!^^wekfowefowekfokewfokewofkwekfewofewofkw^^!"""
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 64))

    def test_lexer65(self):
        input = "@______________43875938275983475023804930932sgZSDGWGREGER!@!@###@$!@$@#$@!$!@#$!@#$12^^^^^!"
        expect = "!,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 65))

    def test_lexer66(self):
        input = """a= "Hfewafwefafwafwae sfewafwefafwafwaaid: " fewafwefafwafwaIm fewafwefafwafwaSupfewafwefafwafwaer'Mfewafwefafwafwaan "s" testtt; __world = 5; imple = 8;"""
        expect = """a,=,Hfewafwefafwafwae sfewafwefafwafwaaid: ,fewafwefafwafwaIm,fewafwefafwafwaSupfewafwefafwafwaer,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 66))

    def test_lexer67(self):
        input = """a= "Heeeeeeeeeeeeeeeeedwddqe seeeeeeeeeeeeeeeeedwddqaideeeeeeeeeeeeeeeeedwddq:eeeeeeeeeeeeeeeeedwddq " Heeeeeeeeeeeeeeeeedwddqeleeeeeeeeeeeeeeeeedwddqlo " \n ";"""
        expect = """a,=,Heeeeeeeeeeeeeeeeedwddqe seeeeeeeeeeeeeeeeedwddqaideeeeeeeeeeeeeeeeedwddq:eeeeeeeeeeeeeeeeedwddq ,Heeeeeeeeeeeeeeeeedwddqeleeeeeeeeeeeeeeeeedwddqlo,Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 67))

    def test_lexer68(self):
        input = """opopweopworwpeorpweopaodfpasof = "opopweopworwpeorpweopaodfpasofello \n world !";"""
        expect = """opopweopworwpeorpweopaodfpasof,=,Unclosed String: opopweopworwpeorpweopaodfpasofello """
        self.assertTrue(TestLexer.test(input, expect, 68))

    def test_lexer69(self):
        input = '{1,"opopweopworwpeorpweopaodfpasofn\\t",3}'
        expect = "{,1,,,opopweopworwpeorpweopaodfpasofn\\t,,,3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 69))

    def test_lexer70(self):
        input = "{534583948593485932239322.534583948593485932239323, 534583948593485932239324.253458394859348593223932, 53458394859348593223932102e3}"
        expect = "{,534583948593485932239322.534583948593485932239323,,,534583948593485932239324.253458394859348593223932,,,53458394859348593223932102e3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 70))

    def test_lexer71(self):
        input = "a[43329384293849238239832984] = {13329384293849238239832984, 23329384293849238239832984,  33329384293849238239832984, 43329384293849238239832984}"
        expect = "a,[,43329384293849238239832984,],=,{,13329384293849238239832984,,,23329384293849238239832984,,,33329384293849238239832984,,,43329384293849238239832984,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 71))

    def test_lexer72(self):
        input = "==!=!&&||+-/"
        expect = "==,!=,!,&&,||,+,-,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 72))

    def test_lexer73(self):
        input = "v[512343542345345345] a12343542345345345;"
        expect = "v,[,512343542345345345,],a12343542345345345,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 73))

    def test_lexer74(self):
        input = "a[312343542345345345 + x.foo(212343542345345345)] = a[b[212343542345345345]] + 312343542345345345;"
        expect = "a,[,312343542345345345,+,x,.,foo,(,212343542345345345,),],=,a,[,b,[,2,],],+,312343542345345345,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 74))

    def test_lexer75(self):
        input = "ppppppppppppppppppppppppppppp=ppppppppppppppppppppppppppppp*ppppppppppppppppppppppppppppp*mpppppppppppppppppppppppppppppPI;"
        expect = "ppppppppppppppppppppppppppppp,=,ppppppppppppppppppppppppppppp,*,ppppppppppppppppppppppppppppp,*,mpppppppppppppppppppppppppppppPI,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 75))

    def test_lexer76(self):
        input = "13239450930590359035930495034953049534039452382347853485/32394509305903590359304950349530495340394523823478534852"
        expect = "13239450930590359035930495034953049534039452382347853485,/,32394509305903590359304950349530495340394523823478534852,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 76))

    def test_lexer77(self):
        input = """ " \\h " """
        expect = """Illegal Escape In String:  \h"""
        self.assertTrue(TestLexer.test(input, expect, 77))

    def test_lexer78(self):
        input = """ " \\wfwefefefefafsfhmmbnbvn\\t" """
        expect = """ \\wfwefefefefafsfhmmbnbvn\\t,<EOF>"""
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
        input = "{Trueeeeeeeeeeeeeeeeeeeeee,}"
        expect = "{,Trueeeeeeeeeeeeeeeeeeeeee,,,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 81))

    def test_lexer82(self):
        input = "//{\"}"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 82))

    def test_lexer83(self):
        input = "/* jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKFxyz #{\"} */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 83))

    def test_lexer84(self):
        input = '''
                // witerituiertuiwetueirtu87483758347348_++++-+_-+--+--+-+-!@#$#$%%^&$%*(*&}>}{<?"
                fwefwfwfwfwfwfwfwefewf
        '''
        expect = "fwefwfwfwfwfwfwfwefewf,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 84))
    
    def test_lexer85(self):
        input = "{/* witerituiertuiwetueirtu87483758347348_++++-+_-+--+--+-+-!@#$#$%%^&$%*(*&}>}{<? */ 180, 20}"
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
        input = """fwifwiefiu7847284234892ffjwfj"-N)
                    " """
        expect = """fwifwiefiu7847284234892ffjwfj,Unclosed String: -N)"""
        self.assertTrue(TestLexer.test(input, expect, 89))

    def test_lexer90(self):
        input = """ "jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF\\x" """
        expect = """Illegal Escape In String: jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF\\x"""
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
        input = "jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF"
        expect = "jfkwjfwejfwekwfjwkfjkwefjwkefjwkefjkwefjwkefjkwejfkwejfkwefjwkefjewkfjewkfjweewr239289483294_______________________4328423492384932849238ASDFAFKSDKF,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 93))

    def test_lexer94(self):
        input = "fkwkflwkffkfkkfkfkfkfkfkfkowroiwr98r92rir2or230942049203942034920349320"
        expect = "fkwkflwkffkfkkfkfkfkfkfkfkowroiwr98r92rir2or230942049203942034920349320,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 94))

    def test_lexer95(self):
        input = "fwkefjwkjfkwjefkwjefkwfjkwef?svn"
        expect = "fwkefjwkjfkwjefkwjefkwfjkwef,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 95))

    def test_lexer96(self):
        input = "fkwkflwkffkfkkfkfkfkfkfkfkowroiwr98r92rir2or230942049203942034920349320 x;"
        expect = "fkwkflwkffkfkkfkfkfkfkfkfkowroiwr98r92rir2or230942049203942034920349320,x,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 96))

    def test_lexer97(self):
        input = """{         "1rrio3iru34ur34u________________92834928398r2938r923r8923rfiafi" ,      "rrio3iru34ur34u________________92834928398r2938r923r8923rfiafi2"     ,      "rrio3iru34ur34u________________92834928398r2938r923r8923rfiafi3"       }"""
        expect = """{,1rrio3iru34ur34u________________92834928398r2938r923r8923rfiafi,,,rrio3iru34ur34u________________92834928398r2938r923r8923rfiafi2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 97))
    
    def test_lexer98(self):
        input = "3249284923849284923823983298239r.00000000000000000000000000000000000000e34823748324923489238432984293843298429384"
        expect = "3249284923849284923823983298239r.00000000000000000000000000000000000000e34823748324923489238432984293843298429384,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 98))
    
    def test_lexer99(self):
        input = "29384203940932094092309403294092394324092340329403290232.e-7333333333333333893293829384923432080980283092840923333333333333333333333"
        expect = "29384203940932094092309403294092394324092340329403290232.e-7333333333333333893293829384923432080980283092840923333333333333333333333,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 99))
    
    def test_lexer100(self):
        self.assertTrue(TestLexer.test(""" fwefwefewfewfwfewfwef """, """fwefwefewfewfwfewfwef,<EOF>""", 100))











    
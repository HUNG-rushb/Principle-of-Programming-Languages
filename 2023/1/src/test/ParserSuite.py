# # 1913652
# # Trịnh Duy Hưng

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    

    # def test00(self):
    #     input = """
    #     fwefwfwffewfwf : function void (fwefwefwefwf n : integer, fwefwf : integer){
    #         nfewf = newfwfwf + defwfelta;
    #         iewfwf : integer;
    #         for(ifwefw = 1fwew, i < 132322230){
    #             writeInt(iwewafwef);
    #         } 
    #     }
    #     """
    #     expect = "Error on line 2 col 53: n"
    #     self.assertTrue(TestParser.test(input, expect, 200))

    # def test01(self):
    #     input = """
    #     xUOYPULUI,GGGERGERy,z2341FSGEWRRGFDFHDG : integer = 141234124,213423412412432,31234214,234123421424;
    #     """
    #     expect = "Error on line 2 col 94: ,"
    #     self.assertTrue(TestParser.test(input, expect, 201))

    # def test02(self):
    #     input = """
    #     maSin : function void() {
    #         for (iERGERWGERG = 1ERGEWRGERGERGE, GREGEGERWGERWGj < 252345324523510, GEHWRHTWRHTWRi + 624353253251) {
    #             writeInt(1354325325325);
    #         }
    #         printFloat(__________________________________________________________________WRJGOEIRJGOIEWJGIJEWIORJGOEWIJGOx);
    #     }
    #     """
    #     expect = "Error on line 3 col 32: ERGEWRGERGERGE"
    #     self.assertTrue(TestParser.test(input, expect,202))

    # def test03(self):
    #     input = """
    #     SDGDGDS : function void {
    #         for (iERGERWGERG = 1ERGEWRGERGERGE, GREGEGERWGERWGj < 252345324523510, GEHWRHTWRHTWRi + 624353253251) {
    #             writeInt(1354325325325);
    #         }
    #         printFloat(__________________________________________________________________WRJGOEIRJGOIEWJGIJEWIORJGOEWIJGOx);
    #     }
    #     """
    #     expect = "Error on line 2 col 32: {"
    #     self.assertTrue(TestParser.test(input, expect,203))

    # def test04(self):
    #     input = """SFGSDGSDGDS: function void() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,204))

    # def test05(self):
    #     input = r"""BBBBBBBBBBBBBBBBBBc, ddddddddddddddddddddddddddadDDDDDD: integer = 5, 6;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,205))

    # def test06(self):
    #     input = r"""c, ddddddddddddddddddddddddddadDDDDDD: string = "abc", "def";"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,206))

    # def test07(self):
    #     input = '''
    #         GHDHGDBFGBDFBGx: integer = 4787685785687;
    #         EWTRETEWT3452545345345: function integer(n5785687568568: integer){
    #             return n856875687568568568/5665785687585670 * 87985872;
    #         }
    #         E3535435345: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #             ierjiejiejgiejgeir8982943829420490: integer = RRTY67767(7678658756865);
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,207))

    def test08(self):
        input = '''
            adETWWERTEWRTd: function integer(RWTEWTEWTEWTEWRTEWn: integer){


                break;
                continue;

                suWTREWTWERTm: integer = 0;
                for (iERWTEWRTEWRT = 0, iETWTW<=n, iEWTWETEWT+1){
                    sERWTEWRTTRum = suEWTRWERTm + i;
                }
                return suWETEWRTEWTEWRTEWRTTWERTEWTWERm;
            }
            maTEWRTWERTEWRTEWRTEWRTERWTWETWTWERTRTRTin: function void () {
                ierjiejiejgiejgeir8982943829420490: integer = adTWERTEWRTEWEWTWERTd(REWTEWRTEWTWE10);
                printFloat(ierjiejiejgiejgeir8982943829420490);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,208))

    # def test09(self):
    #     input = '''
    #         xRWETEWRTEWRTEWRTEWRT: integer = 65;
    #         iiwiueriwuerw892384928__________________________: function integer(n: integer){
    #             if (nERWTWERTEWRTEWRTWER == 0ERWTEWRTEWRT) return WTERWTEWRTEWRTEWRT;
    #             else return nTEWRTEWRTEWRT * iiwiueriwuerw892384928__________________________(nWERTEWRTEWRTEWRTERWTER-1);
    #         }
    #         iTEWRTEWRTERTWERTWnc: function void (out n: integer, ierjiejiejgiejgeir8982943829420490: integer){
    #             nEWRTEWRTERTERW = TEWRTEWRTEWRn + ierjiejiejgiejgeir8982943829420490;
    #         }
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = iiwiueriwuerw892384928__________________________(3);
    #             inc(x,ierjiejiejgiejgeir8982943829420490);
    #             printFloat(x);
    #         }
    #     '''
    #     expect = "Error on line 4 col 45: ERWTEWRTEWRT"
    #     self.assertTrue(TestParser.test(input, expect,209))

    # def test10(self):
    #     input = '''
    #         EWRTEWRTEWRTERWTWERT: function void () {
    #             i324534253425345234523452353425: integer = 1324532453245324532450;
    #             while (i532453453453453253245!=3253453245324532450){
    #                 i34532453245 = i32453245 - 1324523453245345;
    #             }
    #             return  i324532453245;
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,210))

    # def test11(self):
    #     input = """
    #     mEWRTWERTWERTain : function void() {
    #         for (i4532453245234523453245324534534253425 = 34253245345341, j453245324555532453425 < 134534532450, i53245532453245 + 12390534205) {
    #         }
    #         printFloat(RGERWGEWRGERGx);
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,211))

    # def test12(self):
    #     input = """
    #     maEWRTEWRTEWTEWRTERWTERWTERWin : function void() {
    #         for (i2345324532453245324532 = 23534532453451, j34534532453245342532 < 15345324532453453253420, i532324532453245324 + 1555553425234) {
    #             printFloat(FWFERGREx)
    #         }
    #         printFloat(GERGEWGWEx);
    #     }
    #     """
    #     expect = "Error on line 5 col 12: }"
    #     self.assertTrue(TestParser.test(input, expect, 212))

    # def test13(self):
    #     input = """
    #     mERWERWGERGERWGERGERGERGERGain : function void() {
    #         for (iGERWGERWG = 1, jWGERGERWGERGERGERGERGERGERGERGERGERGEWRGEWRGERG < 11324210, iERGERGERGEWRGERWGERWGERGERWGER + 5787606971) {
    #             writeInt(aGWERGERGERWGERGEW);
    #         }
    #         printFloat();
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,213))
        
    # def test14(self):
    #     input = r"""c, ddddddddddddddddddddddddddadDDDDDD: float = 534253425321.2534532534253245342, 323523453252352345235245.3254234532453244e-10;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,214))

    # def test15(self):
    #     input = r"""c, ddddddddddddddddddddddddddadDDDDDD: boolean = true, false;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 215))

    # def test16(self):
    #     input = r"""c, ddddddddddddddddddddddddddadDDDDDD: array[132453245342,3245234532452] of integer = {13245325, 254352234534253425}, {253245324532453, foo(4)};"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,216))

    # def test17(self):
    #     input = r"""c, ddddddddddddddddddddddddddadDDDDDD: auto = 1532453245325, foo(4453253454);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,217))

    # def test18(self):
    #     input = '''
    #         FWEFWQETRTWETERT: function void () {
    #             i5363456: integer = 152254324532523450;
    #             while (i45235324532>205342534535425325){
    #                 iRWETWERTEW = iWERTWERT+ 23253252353252;
    #             }
    #             return  iRTREWTWERTWERT;
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,218))

    # def test19(self):
    #     input = '''
    #         voidA: function integer(n: integer){
    #             return n%10;
    #         }
    #         voidB: function void (out n: integer, ierjiejiejgiejgeir8982943829420490: integer){
    #             n = n + voidA(ierjiejiejgiejgeir8982943829420490);
    #         }
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = 5;
    #             voidB(x,ierjiejiejgiejgeir8982943829420490);
    #             printFloat(x);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 219))

    # def test20(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: string = "dat";
    #             printString(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 220))
    
    # def test21(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: float = 3.45;
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 221))

    # def test22(self):
    #     input = """
    #     GWERGEWRGEWGRGRGRGRGRG : function void() {
    #         for (i32452353254 = 13245234, j34523453245342 < 132452353250, i32453425345342 + 234535324532451) {
    #             writeInt(1532452345324532);
    #         }
    #         printFloat;
    #     }
    #     """
    #     expect = "Error on line 6 col 22: ;"
    #     self.assertTrue(TestParser.test(input, expect, 222))

    # def test23(self):
    #     input = """
    #     GERWGERWGEGERmain : void() {
    #         for (i32452345 = 123452345, j3245325 < 23245324523, i + 132532453245) {
    #             writeInt(123452345);
    #         }
    #         printFloat(x325452345);
    #     }
    #     """
    #     expect = "Error on line 2 col 28: void"
    #     self.assertTrue(TestParser.test(input, expect, 223))

    # def test24(self):
    #     input = """
    #     GWEGEWGERW : function void() {
    #         for (iEGREG = 1234532453425, iGGTRHDHDHDHHRTHERH + 1EWREWRGEWG) {
    #             writeInt(1REWTEWRTEWRT);
    #         }
    #         printFloat(xDFNER32234534);
    #     }
    #     """
    #     expect = "Error on line 3 col 64: EWREWRGEWG"
    #     self.assertTrue(TestParser.test(input, expect, 224))

    # def test25(self):
    #     input = """
    #     SDFGDFGGSDFGDSFG : function() {
    #         for (i23454325 = 1, j2345324534253534253453245 < 1234532453240, i 532453253254324+ 1) {
    #             writeInt(15324532452354);
    #         }
    #         printFloat(x3254325325432);
    #     }
    #     """
    #     expect = "Error on line 2 col 35: ("
    #     self.assertTrue(TestParser.test(input, expect, 225))

    # def test26(self):
    #     input = r"""A532453245325235, B2345324523542352: float = 435325235321, 2353253253254325235232;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 226))

    # def test27(self):
    #     input = r"""A23542353253245: function integer() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 227))

    # def test28(self):
    #     input = r"""A32452352353245: function integer() inherit TT34TERWTERTWERTEWTWETEWTE {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 228))

    # def test29(self):
    #     input = r""" 
    #         GESGERGERGERG: function void(out n324532453245325: integer) {
    #             n235325  = n34253245325+ 15234532454235252523;
    #             return n34253425234532453453245;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 229))

    # def test30(self):
    #     input = '''
    #         SGERGEWGRW: function void () {
    #             ierjiejiejgiejgeir8982943829420490: boolean = true;
    #             printBoolean(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 230))

    # def test31(self):
    #     input = '''
    #         WERGEWGEWGERGWRGGWER: function void () {
    #             b: array [54353254523] of integer;
    #             b[424523453245] = 323452345235;
    #             printFloat(b[25423525234]);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 231))

    # def test32(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = 3+34*30/5*16/4*2/2+19%4+2%2;
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 232))

    # def test33(self):
    #     input = '''
    #         main: function void () {
    #             i: integer = 10;
    #             do{
    #                 i = i - 1;
    #             }
    #             while (i!=0);
    #             return  i;
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 233))

    # def test34(self):
    #     input = '''
    #         main: function void () {
    #             i: integer = -10;
    #             do{
    #                 i = i - 1;
    #             }
    #             while (i!=0);
    #             return  i;
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 234))

    # def test35(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: float = 130.34e2;
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 235))

    # def test36(self):
    #     input = """
    #     main : function void() {
    #         for (i = 1, j < 10) {
    #             writeInt(1);
    #         }
    #     }
    #     """
    #     expect = "Error on line 3 col 30: )"
    #     self.assertTrue(TestParser.test(input, expect, 236))

    # def test37(self):
    #     input = """
    #     main : function void() {
    #         if(true){
    #             for (i = 1, i < 10, i+1) {
    #                 writeInt(i);
    #         }
    #         }else{
    #             printFloat(0);
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 237))

    # def test38(self):
    #     input = """
    #     main : function void() {
    #         if(true){
    #             for (i = 1, i < 10, i+1) {
    #                 writeInt(i);
    #         }
    #         }else{
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 238))

    # def test39(self):
    #     input = """
    #     main : function void() {
    #         if(true){
    #             for (i = 1, i < 10, i+1) {
    #                 writeInt(i);
    #         }
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 239))
    
    # def test40(self):
    #     input = """
    #     main : function void() {
    #         if(true){
    #         }else{
    #             printFloat(0);
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 240))
    # def test41(self):
    #     input = r"""
    #     learningtofly: function integer() {
    #         return -----foo(1_2 + 2 || 4 :: 5);
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 241))

    # def test42(self):
    #     input = r"""x:integer = a + b * c - d / e % f;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 242))

    # def test43(self):
    #     input = r"""x:float=1E-4+10.0;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 243))

    # def test44(self):
    #     input = r"""
    #     boo: boolean =  a && b || c && !d;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 244))

    # def test45(self):
    #     input = r"""
        
    #         newStr: string = "Hello "::"World!";
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 245))

    # def test46(self):
    #     input = r"""
    #     main: function void(){
    #         eq = a == b;
    #         neq = a != b;
    #         lt = a < b;
    #         le = a <= b;
    #         gt = a > b;
    #         ge = a >= b;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 246))

    # def test47(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: string = "true";
    #             printString(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 247))

    # def test48(self):
    #     input = '''
    #         voidA: function integer(n: integer) inherit voidB{
    #             return n%10;
    #         }
    #         voidB: function void (out n: integer, ierjiejiejgiejgeir8982943829420490: integer){
    #             n = n + voidA(ierjiejiejgiejgeir8982943829420490);
    #         }
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = 5;
    #             voidB(x,ierjiejiejgiejgeir8982943829420490);
    #             printFloat(x);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 248))

    # def test49(self):
    #     input = '''
    #         voidA: function integer(n: integer) inherit voidB{
    #             return n%10;
    #         }
    #         voidB: function void (out n: integer){
    #             n = n + 24;
    #         }
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = 5;
    #             voidB(x,ierjiejiejgiejgeir8982943829420490);
    #             printFloat(x);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 249))

    # def test50(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: boolean = !true&&!false||true||false||!false;
    #             printBoolean(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 250))

    # def test51(self):
    #     input = """
    #     iiwiueriwuerw892384928__________________________ : function integer(n: integer) {
    #         if(n==0) return 1;
    #         else return n*iiwiueriwuerw892384928__________________________(n-1);
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 251))

    # def test52(self):
    #     input = """
    #     ierjiejiejgiejgeir8982943829420490: integer = 3;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 252))

    # def test53(self):
    #     input = """True : string = "It's true!" 
    #     false : string = "it's not true..." """
    #     expect = "Error on line 2 col 8: false"
    #     self.assertTrue(TestParser.test(input, expect, 253))

    # def test54(self):
    #     input = """
    #     cEWRTEWRTEWRTEWRTEWRTE, ddddddddddddddEWTEWRTEWRTddddddddddddadDDDDDD, c: integer = 3, 4, 6;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 254))

    # def test55(self):
    #     input = """
    #     TTTERWTWERTEWRTEWRTc, ddddddddddddddddEEWRTERTddddddddddadDDDDDD, c, d: integer = 3, 4, 6;
    #     """
    #     expect = "Error on line 2 col 97: ;"
    #     self.assertTrue(TestParser.test(input, expect, 255))

    # def test56(self):
    #     input = """
    #     ERWTEWRTEWRTEW : void() {
    #         for (iERTEWRTE = 1, j < 10, i + 1) {
    #             writeInt(EWRTEWRTEWTEWRTEWRT);
    #         }
    #         printFloat(xEWRTEWRTEWRT);
    #     }
    #     """
    #     expect = "Error on line 2 col 25: void"
    #     self.assertTrue(TestParser.test(input, expect, 256))

    # def test57(self):
    #     input = r"""
    #     maRTEWRTWERTEWRTEWRTEWTREWTTTin: function void() {
    #         WERTWETREWRTa : integer = 3TERTEWTREWR;
    #         EWRTEWRTEWRTEb : integer = aTWERTEWRTEWRTEWRT;
    #         RWTEWRTEWRTa = bEWTEWRTEWRTEWR;
    #         EWRTEWRTERWTEWRb = foo(a&&b);
    #     }
    #     """
    #     expect = "Error on line 3 col 39: TERTEWTREWR"
    #     self.assertTrue(TestParser.test(input, expect, 257))

    # def test58(self):
    #     input = r"""
    #     aEWRTERWTEWRTEWT : integer = f0EWRTEWRTEWRTERTEWRTEWRTEWRT0(22-foo(a + too(a)));
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 258))

    # def test59(self):
    #     input = r"""
    #     aEWRTEWRTEWRT :integer = ERWTETEWRTb = f00(2TT2-foo(a + too(a)));
    #     """
    #     expect = "Error on line 2 col 45: ="
    #     self.assertTrue(TestParser.test(input, expect, 259))

    # def test60(self):
    #     input = """
    #     main : function void() {
    #         TREWRTEWRTEWRTEWTEWRc, ddddddddddddddddddddddddddadDDDDDD : integer = round(123.0e2), randomInt();
    #         suEWRTEWRTEWRTm : integer = aEWRTEWRT + bWETEWRTWETRWERTEWTEWTEW + arr[0,0];
    #         print(WERTEWRTWEa, suTEWRTEWRTEWRTm);
    #         return ;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 260))

    # def test61(self):
    #     input = r"""
    #     EWTEWRWERTWEa :integer = f00(b=22-foo(a + too(a)));
    #     """
    #     expect = "Error on line 2 col 38: ="
    #     self.assertTrue(TestParser.test(input, expect, 261))

    # def test62(self):
    #     input = r"""
    #     xEEWRTEWRTWRTEWTEWT :boolean = aETEWRT = EWTEWTbEWRTEWT = cWERTEWTEWRTEWRTEWRTEWTWERT;
    #     """
    #     expect = "Error on line 2 col 47: ="
    #     self.assertTrue(TestParser.test(input, expect, 262))

    # def test63(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: string;
    #             ierjiejiejgiejgeir8982943829420490 = "abcd"::"298";
    #             printBoolean(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 263))

    # def test64(self):
    #     input = '''
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: boolean = true;
    #             temp: boolean = !ierjiejiejgiejgeir8982943829420490||false||!false;
    #             printBoolean(temp);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 264))

    # def test65(self):
    #     input = r"""
    #     learningtoESGERGSERGfly: function integer() {
    #         aEGRGEGSEGs, n : string = "q4GRGEGERGS23 \\", "dwaf"::"dwad";
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 265))

    # def test66(self):
    #     input = '''
    #         main: function void () {
    #             uyututytDEGEGEGa,c: boolean = true,!false;
    #             printBoolean(_56765756756756a);
    #             printBoolean(34t3t34t3t3tc);
    #         }
    #     '''
    #     expect = "Error on line 5 col 31: t3t34t3t3tc"
    #     self.assertTrue(TestParser.test(input, expect, 266))

    # def test67(self):
    #     input = """
    #     x23432423234 : array [2, 3] of integer
    #     """
    #     expect = "Error on line 3 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 267))

    # def test68(self):
    #     input = """
    #     x32424242 : array [23423232, 32344543534] of float;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 268))

    # def test69(self):
    #     input = """
    #     x23423423423423 : array [2, 3234234, 2342424, 5] of integer;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 269))

    # def test70(self):
    #     input = r"""
    #     learningtofly: function integer() {
    #         return !343434234324232_23_12-3_6-2;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 270))

    # def test71(self):
    #     input = r"""
    #     wewrwerwra = foo(4) = 23423423423423c = 23432424234d;
    #     """
    #     expect = "Error on line 2 col 19: ="
    #     self.assertTrue(TestParser.test(input, expect, 271))

    # def test72(self):
    #     input = r"""
    #     bwefwefwfewfwef : integer = 5;
    #     awfwefwef : integer = b = 324242346;
    #     """
    #     expect = "Error on line 3 col 32: ="
    #     self.assertTrue(TestParser.test(input, expect, 272))

    # def test73(self):
    #     input = r"""
    #     RGSGSGSERGERG: function void() {
    #         if (aEGRWGERGEGEG&&B) {
    #             GEGEGEGERGEGa = ERGERGSEGEGb;
    #             ERGERERTRTc = ERWGEGEWRGERGd;
    #         } else  
    #             cEGRGEWRGEGEGERG = 43535353453453451;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 273))

    # def test74(self):
    #     input = r"""
    #     GERGSGSEGSGSER: function void() {
    #         if (a&&B) {
    #             aERGERGERGERG = bERERGERGERGERGERG;
    #             GERGERGERGc = EGERGERGEGd;
    #         } else {} // empty
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 274))

    # def test75(self):
    #     input = '''
    #         EGEGEGEGEGEG: function void () {
    #             aERGEGEGERGE,c: string = "true","!false";
    #             printString(GERGEGERGERa);
    #             printString(cEGERGERGEGERG);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 275))

    # def test76(self):
    #     input = '''
    #         maEGEGEGEGin: function void () {
    #             ERGEGEGa,ERGEGEc: string = "trGERGEGERGEue","!ERGERGERGERGEGERGse";
    #             vERGERGE: string = EGREGa::GGGGGGGGGGGGGGGGGGGGGGGGGGGc;
    #             printString(GERGERGa);
    #             printString(vEGEG);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 276))

    # def test77(self):
    #     input = '''
    #         EGEGmaiEGEGERGERGEGEEGn: function void () {
    #             a,c: string = "true","det/tsef";
    #             v: string = a::c;
    #             printString(a);
    #             printString(v);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 277))
    
    # def test78(self):
    #     input = '''
    #         FWFWEFWEFAWF: function integer(n___________: integer){
    #             return n+23423423454353454+2;
    #         }
    #         maiWFAWFWEFAWFn: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = voidA(voidA(34));
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 278))

    # def test79(self):
    #     input = """
    #     _____________________________ : auto = 0.0;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 279))

    # def test80(self):
    #     input = """
    #     xWEFAWFAWEFAWEF : auto = 0.0;
    #     yWAFWFAWF : auto = true;
    #     zAEWFAWEFWAEFWAEFWEFWEF : auto = "ThWAEFAWEFs is aWFWAEFAWEFAWFWstrWFWEFAWFing";
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 280))

    # def test81(self):
    #     input = """
    #     xFWFWEFWEF,FWFAWEFAWFWy,z234224,y4234234,t2342424,n4234234234324 : auto = 2343242341,2234234,324234,423423424,2342342345,234234234236;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 281))

    # def test82(self):
    #     input = """
    #     x23424Q24Q24Q2Q24Q24Q234Q224Q : array [] of integer;
    #     """
    #     expect = "Error on line 2 col 47: ]"
    #     self.assertTrue(TestParser.test(input, expect, 282))

    # def test83(self):
    #     input = r"""
    #     RETERT434353534534534: function void() {
    #         if (a32423423242&&FEWFWEFEWFEWFEWFWEFEWFWEB) {
    #             a5454545 = 7567567b;
    #             cQ2RQ2R2R4 = dRWEKRJIWE89E8R9W8R9;
    #             return False;
    #         } else 
    #             break;
    #         return ;
    #     }
    #     """
    #     expect = "Error on line 4 col 34: b"
    #     self.assertTrue(TestParser.test(input, expect, 283))

    # def test84(self):
    #     input = r"""
    #     WERTT53453453453535345345: function void() {
    #         for (iTWETWERTERWTEWT = 11234213421431234124141341, iEWTREWTWE <= 112342134123412340, 1234124 + i1241241234124)
    #         {
    #             aEWRTEWRTWET = WERTEWTEWRTEWRT + 143143412412;
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 284))

    # def test85(self):
    #     input = """
    #     QWDQWDWQDWQ: function void() {
    #         while (i______________________JGOEWJROIGJEWOIRGJOWEG != 121421410 + 1654748754622)
    #             aFEWFEWFEWFWEFWEFEF : integer = DQWDQ5;
    #     }
    #     """
    #     expect = "Error on line 4 col 36: :"
    #     self.assertTrue(TestParser.test(input, expect, 285))

    # def test86(self):
    #     input = """
    #     CECECESF : function void() {
    #         {
    #             aFEWFFWEFWEFWFEWFWE : integer = 13242142141245;
    #             bFEWFWEFWE = GGEGTRHRHT* 2213423412424_0123412342134213 -367354646262345153 ;




    #             for (i324532532532 = bWEFWEFWEFWEFEWFEWEWFEWF, i253453245 > 134252346 , i234532453245342-123453245234523)
    #             print(Array[0, i]);
    #         }
    #         return ;
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 286))

    # def test87(self):
    #     input = '''
    #         DDWDWDQWDQDQ: function string (s: string){
    #             i2345325325: integer = 432532453245342;
    #             while (i23453223453245345>0){
    #                 s2345342534 = s325432453245::"q325432453453245ua";
    #             }
    #             return s32453245345324;
    #         }
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: string = "3245342532453245235av";
    #             ierjiejiejgiejgeir8982943829420490 = voidA(ierjiejiejgiejgeir8982943829420490);
    #             printString(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 287))

    # def test88(self):
    #     input = '''
    #         voidAB: function integer(n: integer){
    #             return n+4+2;
    #         }
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = voidA(23);
    #             ierjiejiejgiejgeir8982943829420490 = ierjiejiejgiejgeir8982943829420490/2 + ierjiejiejgiejgeir8982943829420490/2/3;
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 288))

    # def test89(self):
    #     input = '''
    #         voidA: function integer(n: array[2353255] of integer){
    #             return n[4235432453425];
    #         }
    #         main: function void () {
    #             ierjiejiejgiejgeir8982943829420490: integer = 323453254+-4235324523--5325324;
    #             ierjiejiejgiejgeir8982943829420490 = ierjiejiejgiejgeir8982943829420490*2;
    #             printFloat(ierjiejiejgiejgeir8982943829420490);
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 289))

    # def test90(self):
    #     input = '''
    #         YUTR78578568756858756: function void () {
    #             for (i7809870 = 17890870, i879879789087 < 789870987910, i789087908 + 780987087087087871) {
    #                 if (478907*78907807802 > i78908708708){
    #                     writeInt(i789087078);
    #                     continue;
    #                 }
    #             }
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 290))

    # def test91(self):
    #     input = '''
    #         I5I687658568568: function void () {
    #             for (iWEEEEEEEEEEE = 18696789679, iWEWWWEWE < 17696796796796790, iWEREWREW + 7987967896791) {
    #                 if (467979*29679679679679 > 90069){
    #                     writeInt(7896789679);
    #                     break;
    #                 }
    #             }
    #         }
    #     '''
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 291))

    # def test92(self):
    #     input = '''
    #         SEGERGERGEGEGE: function void () {
    #             for (iGSDVSFDVSDFBBSBSBEBBSR = 1FWFWFAWFAF0, iGSDVSFDVSDFBBSBSBEBBSR >= 054325453245, iGSDVSFDVSDFBBSBSBEBBSR - 13453253252345325) {
    #                 if (WFWFWAFWEFWEFWEF4*2 > i324321412412411234){
    #                     writeInt(iTRSHSSTHSDG*232424234234);
    #                     break;
    #                 }
    #             }
    #             return;
    #         }
    #     '''
    #     expect = "Error on line 3 col 48: FWFWFAWFAF0"
    #     self.assertTrue(TestParser.test(input, expect, 292))

    # def test93(self):
    #     input = """
    #     iiwiueriwuerw892384928__________________________ : function integer(n: integer) {
    #         if(n==0) return 1;
    #         else return n*iiwiueriwuerw892384928__________________________(n-1);
    #     }
    #     main: function void () {
    #         ierjiejiejgiejgeir8982943829420490 : integer;
    #         ierjiejiejgiejgeir8982943829420490 = iiwiueriwuerw892384928__________________________(5)*iiwiueriwuerw892384928__________________________(4)*iiwiueriwuerw892384928__________________________(3);
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 293))

    # def test94(self):
    #     input = """
    #     iiwiueriwuerw892384928__________________________ : function integer(n: integer) {
    #         if(n==0) return 1;
    #         else return n*iiwiueriwuerw892384928__________________________(n-1);
    #     }
    #     main: function void () {
    #         ierjiejiejgiejgeir8982943829420490 : integer;
    #         ierjiejiejgiejgeir8982943829420490 =  -iiwiueriwuerw892384928__________________________(5);
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 294))

    # def test95(self):
    #     input = """
    #     inc : function void (out n : integer, ierjiejiejgiejgeir8982943829420490 : integer){
    #         n = n + 2342423424;
    #     }
    #     ierjiejiejgiejgeir8982943829420490 = inc(5,1);
    #     """
    #     expect = "Error on line 5 col 43: ="
    #     self.assertTrue(TestParser.test(input, expect, 295))

    # def test96(self):
    #     input = """
    #     inc : function integer (out n : integer, ierjiejiejgiejgeir8982943829420490 : integer){
    #         n = n + ierjiejiejgiejgeir8982943829420490;
    #         return n;
    #     }
    #     main: function void () {
    #     ierjiejiejgiejgeir8982943829420490 = inc(5;1);
    #     }
    #     """
    #     expect = "Error on line 7 col 50: ;"
    #     self.assertTrue(TestParser.test(input, expect, 296))

    # def test97(self):
    #     input = """
    #     fwfwefaf : function void (rytrytr645645654 n : integer, uiou : integer){
    #         n3424242 = n + wfwfwfwf;
    #     }
    #     main: function void() {
    #         deasdaioulta = wf(5,1);
    #         iuouououo(x, wfwfwfwf);
    #         printFloat(x);
    #     }
    #     """
    #     expect = "Error on line 2 col 51: n"
    #     self.assertTrue(TestParser.test(input, expect, 297))

    # def test98(self):
    #     input = """erwrwrwera: integer = 3;eeqweqeqb,c:string = "aqweqeqebc","dqweqeqeef";"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 298))

    # def test99(self):
    #     input = """effwfw, rwefwe, twefw, fwefwf: integer = 635453,3453535, 3534;"""
    #     expect = "Error on line 1 col 61: ;"
    #     self.assertTrue(TestParser.test(input, expect, 299))
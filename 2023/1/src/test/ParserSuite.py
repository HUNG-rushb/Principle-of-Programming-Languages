# # 1913652
# # Trịnh Duy Hưng

# import unittest
# from TestUtils import TestParser

# class ParserSuite(unittest.TestCase):

#     def test_0(self):
#         input = """
#             Class Doadag: Anidadsmal { }
#             Class Snfffsdake: Dqwwde { }
#             Class bfwefeuttdqwerfqdqwly {
#                 __swdqfqwdqwtr__() {
#                     Var a, b, c, d, e: Int = 1,2,4,5,6;
#                     Val $effffffffff: Int;
#                 }
#             }
#             """
#         expect = "Error on line 7 col 24: $effffffffff"
#         self.assertTrue(TestParser.test(input, expect, 200))

#     def test_1(self):
#         input = """
#             Class DFVDWDosadfwqg: DFCVBBBBBBBBBBBBBBBAniqvsdvmal {
#                 $hungyeuquynhquatriquadat() {
#                     awefdcvvv = asuidfuw[71223][24132];
#                 }
#             }
#             Class kitty: hyeergere {
#                 $fwefwefwfc() {
#                     Return Self.wuefwiu1237wfbhwbfw;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))

#     def test_2(self):
#         input = """
#             Class dfasvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv {
#                 getWife() {
#                     Var hung: Boolean = true;
#                 }
#                 main() {
#                     Var quynh: Float;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))

#     def test_3(self):
#         input = """
#             Class calsclasclaslcascl {
#                 getMoney() {
#                     Var b: Float = 0.3;
#                     Var b: Float = 0.3;
#                     Var b: Float = 0.3;
#                     Var b: Float = 0.3;
#                     Var b: Float = 0.3;
#                 }
#                 funjccnskjddjskcsdcvc() {
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
#                     Elseif (12 >= g) {
#                         Self.insert("String");
#                     }
#                     Elseif (12 >= g) {
#                         Self.insert("String");
#                     }
#                     Elseif (12 >= g) {
#                         Self.insert("String");
#                     }
#                     Elseif (12 >= g) {
#                         Self.insert("String");
#                     }
#                     Else {
#                         ___________________ = _______________________________________________________________________;
#                         Hung = Vi;
#                     }
#                 }

#                 setcvsdvdsvdvAge(okokokok: Boolean) {
#                     Self.agbseegree = agesrgsfdsde;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 203))

#     def test_4(self):
#         input = """ 
#             Class meomeoemeoemoeemoeo: Cat {
#                 Var truefalse: Boolean;
#                 Var $a, c, d: Float = .e41231, 234322., 712328.333333339;
#                 Var a: Array[Int, 8] = Array(10907090.1232, 3.6123, 34e5, 23243e4, 12332432.723E4 , 32144E512311111, 23E4623887, 12132.7E4);
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 204))

#     def test_5(self):
#         input = """
#             Class fffffffsdfasfwwf {
#                 wewgwfwef(awefwfs: Boolean; bwwebhbhds: Float) {
#                     Foreach (iokosofd In 846 .. 240000 By isdfav <= 9999) {
#                         sfsdfum = sudsfgwerm + rraya[isdafhsf];
#                     }
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 205))

#     def test_6(self):
#         input = """
#             Class Quynh {
#                 fsadf(iuiwer884: Float; b3342: Float) {
#                     Return iuiwer884 || b3342 < cwef.refer(afwedew,sdv2) && 23324 + 134235.4;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 206))

#     def test_7(self):
#         input = """
#             Class WestSide {
#                 MainMenu(quynh: Boolean; hung: Int) {
#                     Self.arr[5784378] = hung.cubu() + quynh.dep();
#                 }
#             }
#             Class DELLL {
#                 Hybrid(){
#                     Return 61236712;
#                 }
#             }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 207))

#     def test_8(self):
#         input = """
#                 Class MyClass {
#                     Var beRot: NguoiYeu;

#                     Var maicuoiluonnha: Int = 0;

#                     $cuoiluonnha() {
#                         Out.print(Self.beRot);
#                     }

#                     adsad(_age: Int) {
#                         Self.maicuoiluonnha = _age;
#                     }
#                 }

#                 Class MyClass {
#                     Var beRot: NguoiYeu;

#                     Var maicuoiluonnha: Int = 0;

#                     $cuoiluonnha() {
#                         Out.print(Self.beRot);
#                     }

#                     adsad(_age: Int) {
#                         Self.maicuoiluonnha = _age;
#                     }
#                 }

#                 Class MyClass {
#                     Var beRot: NguoiYeu;

#                     Var maicuoiluonnha: Int = 0;

#                     $cuoiluonnha() {
#                         Out.print(Self.beRot);
#                     }

#                     adsad(_age: Int) {
#                         Self.maicuoiluonnha = _age;
#                     }
#                 }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 208))
    
#     def test_9(self):
#         input = """
#             Class $HungYeuQuynhlamnha {
#             }

#         """
#         expect = "Error on line 2 col 18: $HungYeuQuynhlamnha"
#         self.assertTrue(TestParser.test(input, expect, 209))
    
#     def test_10(self):
#         input = """
#             Class father {
#                 get(){

#                 }
#             }
#             Class son: father {
#                 ok() {
#                     Return super::laugh();
#                 }
#             }
#         """
#         expect = "Error on line 9 col 34: laugh"
#         self.assertTrue(TestParser.test(input, expect, 210))
    
#     def test_11(self):
#         input = """
#             Class hungyeuquynh {
#                 cuoi() {
#                     Foreach (i In 0 .. 999 By pi <= i) {
#                         gf.bf();
#                     }

#                     Return true;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 211))
    
#     def test_12(self):
#         input = """
#             Class Shen {
#                 $_____twilieye() {
#                     Return false;
#                 }
#             }

#             Class Program {
#                 main_main() {
#                     agfASFFFFFFEERSWQf = (myConst + okokokoko) && (x + y + z);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 212))

#     def test_13(self):
#         input = """
#             Class myHippo {
#                 cat(hung: Array[Int, 99]) {
#                     Return hung[0]
#                 }
#             }
#         """
#         expect = "Error on line 5 col 16: }"
#         self.assertTrue(TestParser.test(input, expect,213))

#     def test_14(self):
#         input = """
#             Class testing____testing {
#                 Constructor(hungyeuquynh: Array[Float, 9]) {
#                     Self.hung = hungyeuquynh[1];
#                     Self.love = hungyeuquynh[2];
#                     Self.quynh = hungyeuquynh[2][1];
#                     Self.hung = hungyeuquynh[1];
#                     Self.love = hungyeuquynh[2];
#                     Self.quynh = hungyeuquynh[2][1];
#                     Self.hung = hungyeuquynh[1];
#                     Self.love = hungyeuquynh[2];
#                     Self.quynh = hungyeuquynh[2][1];
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,214))

#     def test_15(self):
#         input = """
#             Class CuoiLuonNha {
#                 Destructor() {
#                     bunbo.Delete().All(0);
#                     love.hung_quynh();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,215))

#     def test_16(self):
#         input = """
#             Class wedding {
#                 anni() {
#                     t = Rhungquynh::$cuoiluonnha()[57] >= 78;
#                     Return Self.love;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,216))

#     def test_17(self):
#         input = """
#             Class Program {
#                 Hung_Quynh() {
#                     Return Self.cuoiluon();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,217))

#     def test_18(self):
#         input = """
#             Class gaugaugagua {
#                 gotobed() {

#                 }

#                 Constructor() {
#                     Self.create = okokok;
#                 }

#                 Destructor() {
#                     Mew.delete();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,218))

#     def test_19(self):
#         input = """
#             Class quynh {
#                 Var beRot: Array[Float, -20] = true;
#             }
#         """
#         expect = "Error on line 3 col 40: -"
#         self.assertTrue(TestParser.test(input, expect,219))

#     def test_20(self):
#         input = """
#             Class ari {
#                 Constructor(a, b : Int)
#                 {
#                     hungyeuquynhlamnha.print("Contructor");
#                 }
#                 Destructor()
#                 {
#                     hungyeuquynhlamnha.print("Destructor");
#                 }
#                 $_getMethod() {
#                     Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
#                 }
#             }
#             Class Program {
#                 Constructor(a, b : Int)
#                 {
#                     hungyeuquynhlamnha.print("Contructor");
#                 }
#                 Destructor()
#                 {
#                     hungyeuquynhlamnha.print("Destructor");
#                 }
#                 main() {
#                     a = (myConst + b) && a + b + abcde;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,220))

#     def test_21(self):
#         input = """
#             Class P423423ro2342gra234213m {
#                 ma234729891in() {
#                     dasd.print("lo cc");
#                 }
#             }
#             Class iden31235351435 {

#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,221))

#     def test_22(self):
#         input = """
#             Class jztr {
#                 func(s: Boolean; r: Float) {
#                     Return ojojojojojjoo.Str(s + r);
#                 }
#             }
#             Class Program {
#                 jztr() {

#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,222))

#     def test_23(self):
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

#     def test_24(self):
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

#     def test_25(self):
#         input = """
#             Class Program {
#                 main() {
#                     Var a,b: Array[Float, 3.9];
#                 }
#             }
#             Class nicebutt {
#                 attr(wefwef, w234efwef: Int) {
#                     Return wefwef[4] != we343fwef[1].name;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 42: 3.9"
#         self.assertTrue(TestParser.test(input, expect,225))

#     def test_26(self):
#         input = """
#             Class parent {


#                 Var lname, fname: String = "";
#                 $getName() {
#                     Return Self.name[2];
#                 }
#                 setName(name: Int) {
#                     lname = name[0];
#                 }
#             }
#         """
#         expect = "Error on line 5 col 45: ;"
#         self.assertTrue(TestParser.test(input, expect,226))

#     def test_27(self):
#         input = """
#             Class Progfasdfram {
#                 masafasdfin() {
#                     Return New objdsfasdfect();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,227))

#     def test_28(self):
#         input = """
#             Class twitter {
#                 main(a: Boolean; b: Boolean) {
#                     Return New Bull().dsaf().Cicke();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,228))

#     def test_29(self):
#         input = """
#             Class fasdfasdf {
#                 Constructor(){Return eeeeeeeeeeeeeeeeeeeeeeee;}
#             }
#             Class dsbisubviweuhfw {

#                 Return statements;
#             }
#         """
#         expect = "Error on line 7 col 16: Return"
#         self.assertTrue(TestParser.test(input, expect,229))

#     def test_30(self):
#         input = """
#             Class fwefwefaf {
#                 maffwefgergergwain() {

#                 }
#             }
#             Class fawfadsfd {



#                 Destructor(param: Int, param_2: String) {

#                 }
#             }
#         """
#         expect = "Error on line 11 col 27: param"
#         self.assertTrue(TestParser.test(input, expect,230))

#     def test_31(self):
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
#         expect = "Error on line 7 col 32: ,"
#         self.assertTrue(TestParser.test(input, expect,231))

#     def test_32(self):
#         input = """
#             Class eqwego678dhgf {
#                 main() {
#                     Foreach (rtyre564tsg In 1 .. 111111110 + 5 By adfacv[i] >= 234) {
#                         If (a[ifaf][1123] != b[11]) {
#                             Return;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,232))

#     def test_33(self):
#         input = """
#             Class aloaloalo {
#                 main() {
#                     Var name: Int;
#                 }
#             }
#             Class wfsadfsdadf {
#                 function() {
#                     Var name: Int;




#                     Hung.Main()::$dollar();
#                 }
#             }
#         """
#         expect = "Error on line 14 col 31: ::"
#         self.assertTrue(TestParser.test(input, expect,233))

#     def test_34(self):
#         input = """
#             Class ok {
#                 $maiereewrwn() {

#                 }
#             }
#             Class l1l1l1l1l {
#                 adfasdfwerw(s1, s2, s3: String) {
#                     Return Str.concat(s13213, s12412, afw1231s3);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,234))

#     def test35(self):
#         input = """
#             Class giraffe {
#                 giraffe() {
#                     Return New giraffe().giraffe();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,235))

#     def test36(self):
#         input = """
#             Class test25fsfasldfk {
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 Var a: Int = 0;
#                 main() {
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                     a = New obj("string 1");
#                     Out.print(a.age);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,236))

#     def test_37(self):
#         input = """
#             Class Method {
#                 newMethod(a: String) {
#                     Return "This is a \\nstring"[1].getText();
#                 }
#             }
#         """
#         expect = "Error on line 4 col 50: ."
#         self.assertTrue(TestParser.test(input, expect,237))

#     def test_38(self):
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
#         expect = "Error on line 10 col 50: ."
#         self.assertTrue(TestParser.test(input, expect,238))

#     def test_39(self):
#         input = """
#             Class Program {
#                 main() {
#                 }
#             }
#             Class newClass {
#                 Val counqdqwdt: Int = 150324;
#                 Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
#                 Pr234234intO32ut() {
#                     Return Self.cou123nt * Self.ra213124te;
#                 }
#                 Val counqdqwdt: Int = 150324;
#                 Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
#                 Pr234234intO32ut() {
#                     Return Self.cou123nt * Self.ra213124te;
#                 }
#                 Val counqdqwdt: Int = 150324;
#                 Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
#                 Pr234234intO32ut() {
#                     Return Self.cou123nt * Self.ra213124te;
#                 }
#                 Val counqdqwdt: Int = 150324;
#                 Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
#                 Pr234234intO32ut() {
#                     Return Self.cou123nt * Self.ra213124te;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,239))

#     def test_40(self):
#         input = """
#             Class belrlrlrlrl {
#                 $ahahahahah() {
#                     Return Self.sousfwefwdsnd()[3029];
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,240))

#     def test_41(self):
#         input = """
#             Class eerrerrert {
#                 Var asdafd, bfasdf, cwefwefw: Float = 334, 4234, 54234;
#                 $prifwwfwnt() {
#                     Return Array(a,b,c);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,241))

#     def test_42(self):
#         input = """
#             Class sdfsaf {
#                 Var we: sdfsdddddddd;
#                 Var me: tyer43534terster = 0.2;
#                 $gsdafqe3432t() {
#                     Losdfgfsdcal.St4234ore.sieu3342thi();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,242))

#     def test_43(self):
#         input = """
#             Class Progrdfdafdsfam {
#                 msdfaain() {
#                 }
#             }
#             Ofsadfdsut.prwefwint(adsfa, b, 3);
#             Out.prinsdfs(a, b, 3);
#             Out.prinsdfat(a, b, 3);
#         """
#         expect = "Error on line 6 col 12: Ofsadfdsut"
#         self.assertTrue(TestParser.test(input, expect,243))

#     def test_44(self):
#         input = """
#             Class tfhs {
#                 assdwf() {
#                     If (afsadf == fsadfgwwbrtyu) {
#                         Foreach (i In 1 .. sadfwewefsdsadv By saudhuisadf) {
#                             Continue;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,244))

#     def test_45(self):
#         input = """
#             Class wopiolio {
#                 vmvzcvzda() {
#                     Dawfaweog.namfwewefe = Cafweat.nafwefwwafqweme +. "1asdfqq123adf$%^%$##$%$#%&^&^%^%<><<U><";
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,245))

#     def test_46(self):
#         input = """
#             Class Madfasdfsadeo: Dsdafasdfog {
#                 $gasdfasdfet() {
#                     Self.naasdfdsafme = Doasdfdsafg::nameasdfsdafsa;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 53: nameasdfsdafsa"
#         self.assertTrue(TestParser.test(input, expect,246))

#     def test_47(self):
#         input = """


#             If (a >= b) {
#                 Return Program;
#             }
#             Class Buffadadafalo: Anifr43t54gmals {
#                 asd434Doaasgafdfadssa.scofdfapeMethod();
#             }
#         """
#         expect = "Error on line 4 col 12: If"
#         self.assertTrue(TestParser.test(input, expect,247))

#     def test_48(self):
#         input = """
#             Foreach (i In 0 .. 9854 By 12313 * 2312 / 312 - adsfa.gdsfaset + adfweb.nadfsdfme) {
#                 Continue;
#                 Break;
#             }
#         """
#         expect = "Error on line 2 col 12: Foreach"
#         self.assertTrue(TestParser.test(input, expect,248))

#     def test_49(self):
#         input = """
#             Class FSDFAA {
#                 Return New BRETWERT(SGER5462A);
#             }
#         """
#         expect = "Error on line 3 col 16: Return"
#         self.assertTrue(TestParser.test(input, expect,249))

#     def test_50(self):
#         input = """
#             Class asdsDB: WEFWFAA {
#                 Var AWEFDa, FWEFWEFb: Float = 32312.5676, 2131235;
#                 Return SDGSSFGERa;
#             }
#         """
#         expect = "Error on line 4 col 16: Return"
#         self.assertTrue(TestParser.test(input, expect,250))

#     def test_51(self):
#         input = """
#             Class Program {
#                 func(){
#                     gjty4578_test();
#                 } 
#             }
            
#         """
#         expect = "Error on line 4 col 33: ("
#         self.assertTrue(TestParser.test(input, expect,251))

#     def test_52(self):
#         input = """
#             Class hungquynh {
#                 If (asdfasd <= 34738736)
#             }
#         """
#         expect = "Error on line 3 col 16: If"
#         self.assertTrue(TestParser.test(input, expect,252))

#     def test_53(self):
#         input = """



#             Self.fwefwafsd = 223948932.2398423;
#         """
#         expect = "Error on line 5 col 12: Self"
#         self.assertTrue(TestParser.test(input, expect,253))

#     def test_54(self):
#         input = """
#             Class Vwefwfds2213vsdvsf_____238dh823jksdaf {
#                 Val arr = Array[Array[Boolean, Vwefwfds2213vsdvsf_____238dh823jksdaf], Vwefwfds2213vsdvsf_____238dh823jksdaf];
#             }
#         """
#         expect = "Error on line 3 col 24: ="
#         self.assertTrue(TestParser.test(input, expect,254))

#     def test_55(self):
#         input = """
#             Class Program {
#                 main() {

#                 }
#             }
#             Class ___2342____dfasfokBdfsdfasdf {

#             }
#             Class ____Csadf {

#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,255))

#     def test_56(self):
#         input = """
#             Class Prog3432regwwer______________3498jsaa9ram {
#                 madsfasdfqin() {PdsfasdfaPL() {}}





#                 Var tu34_56h_(): Int;
#             }
#         """
#         expect = "Error on line 3 col 43: ("
#         self.assertTrue(TestParser.test(input, expect,256))

#     def test_57(self):
#         input = """
#             Class ER: Aw, Tfwefa_2387_______fwefu {
#             }
#         """
#         expect = "Error on line 2 col 24: ,"
#         self.assertTrue(TestParser.test(input, expect,257))

#     def test_58(self):
#         input = """
#             Class Bqwdasdasdffwqdewf {
#                 Var b, c : Int = 1384958670.44857682;
#             }
#         """
#         expect = "Error on line 3 col 52: ;"
#         self.assertTrue(TestParser.test(input, expect,258))

#     def test_59(self):
#         input = """
#             Class iwefwefadfd {
#                 fafwefew34343gsg() {
#                     adfsaa = Self.agewr2342a____________e + 3234.545 - 0b0 * Bweqrwe.fawfewer();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,259))

#     def test_60(self):
#         input = """
#             Class Prwefawf3453___wekwe9932ogram {
#                 maiawefawn() {
#                     a[0] = "Stri$@#^#&#%^ng 1" ==. "3425#@$strwfewang \\'";
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,260))

#     def test_61(self):
#         input = """
#             Class B {



#                 B435__.call();
#             }
#         """
#         expect = "Error on line 6 col 22: ."
#         self.assertTrue(TestParser.test(input, expect,261))

#     def test_62(self):
#         input = """
#             Class Progrwefwafadaam {
#                 Constructor(afawf, vdfvgeb: Boolean; c: Boolean) {
#                     awfwe = cafwef + 1234.234234;
#                     Return;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,262))

#     def test_63(self):
#         input = """
#             Class Cdafwe23423onstruc {
#                 Destruc________fwef3884___________() {
#                     Dawfewes.DeletefwefwAll();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,263))

#     def test_64(self):
#         input = """
#             Class efwerweafdfewC {



#                 Var a: Int = funewe44c();
#                 Val ergserg: fgergsf = "Hewfwaefllo";
#                 Val werqwea,b,c: Int = 0.433539, 1234.03432;
#             }
#         """
#         expect = "Error on line 6 col 38: ("
#         self.assertTrue(TestParser.test(input, expect,264))

#     def test_65(self):
#         input = """
#             Class Pwefwefasfrogram {
#                 mawefwaefin() {
#                     func_decwew23423___________________lare() {



#                         Return maiwefwen().twfwefqwefqwfxt();
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 59: ("
#         self.assertTrue(TestParser.test(input, expect,265))

#     def test_66(self):
#         input = """
#             Class wefewfwf {




#                 Var ewfweb: Ifwefwent = wfweA::$f()[1] + afew3242_384728g * 446533 + !weqrwy;

#                 Var wefwqea: Stuwefwqef34234 = New Teawfeach(New Stfwefwefdsu());

#                 Var td: Boolean = 34 >= yf && ut <= 3242352 || 7453 == !bwef - 3324323525;
#             }
#         """
#         expect = "Error on line 11 col 49: <="
#         self.assertTrue(TestParser.test(input, expect,266))

#     def test_67(self):
#         input = """
#             Class metfwefwefwhod {

#                 $getNwer2398239_______fwiui23ame() {
#                     quy.t1234(Bv.$t987);
#                 }
#             }
#         """
#         expect = "Error on line 5 col 33: $t987"
#         self.assertTrue(TestParser.test(input, expect,267))

#     def test_68(self):
#         input = """
#             Class Metawefeawfehod: Pafwefwafweram {
#                 mawfawef() {
#                     awaefaw = Twefaefw::$gew_efweft() + New Xwefafw().Gawefafd() - Awefaw.bwfaf().fwefaw2113432().t___324_();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,268))

#     def test_69(self):
#         input = """
#             Class werqwProgefwqefram {
#                 ____________________main() {






#                     a[1][2][3][4] = b[4][3].c(d[fwerwewef1]);
#                 }










#                 method () { }
#             }
#         """
#         expect = "Error on line 10 col 43: ."
#         self.assertTrue(TestParser.test(input, expect,269))

#     def test_70(self):
#         input = """
#             Class wqdqwdd234__________fwefE {
#                 $weaffwe324asdfas() {
#                     Return aewrw67dfh___________________[123][332][453] + hmmmmmm.bdasf()[412];
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,270))

#     def test_71(self):
#         input = """
#             Class aafefwea___34543faf {
#                 mawefawfin() {

#                 }
#             }
#             Class B {
#                 Constructor(aewf32,b324ffw,dagsdfw4223c: Float) {
#                     Return Self.aewew + gbsgdfgb + 564564;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,271))

#     def test_72(self):
#         input = """
#             Class efwefa {
#                 mafwefain() {





#                     Var $t: Float;
#                 }
#             }
#         """
#         expect = "Error on line 9 col 24: $t"
#         self.assertTrue(TestParser.test(input, expect,272))

#     def test_73(self):
#         input = """
#             Class wefwef_q3d2p {
#                 sexdfer() {
#                     Val _, _, _: String = 3, 4, 5;
#                     Val _, _, _: String = 3, 4, 5;
#                     Val _, _, _: String = 3, 4, 5;
#                     Val _, _, _: String = 3, 4, 5;
#                     Var aqwe, bewq, $i: Float = 1231.134120e+32178, 234.3E-123;
#                 }
#             }
#         """
#         expect = "Error on line 8 col 36: $i"
#         self.assertTrue(TestParser.test(input, expect,273))

#     def test_74(self):
#         input = """
#             Class _Rqwdqweq {
#                 Val $_____465y: Int = 12312412;
#                 _Fr3fwa() {
#                     Val _, __, ___: Boolean = 3342, 44231, 35459789;
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,274))

#     def test_75(self):
#         input = """

#             Class hungquynhnh {

#                 fff342411() {

#                     tr65.fkdfjdsak() {
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 7 col 37: {"
#         self.assertTrue(TestParser.test(input, expect,275))

#     def test_76(self):
#         input = """
#             Class qwefwe34234 {
#                 Var wefeewf: qfwf = New dqwdwq();
#                 mafwqfinStu() {
#                     Stazu[19] = za.za().za().za()[za5341];
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,276))

#     def test_77(self):
#         input = """
#             Class oweyfoadnak_____________ {
#                 Var _______________d_______________: Array[Array[Int, 3242376], 0b0];
#             }
#         """
#         expect = "Error on line 3 col 80: 0b0"
#         self.assertTrue(TestParser.test(input, expect,277))

#     def test_78(self):
#         input = """
#             Class fsfaewfwa {
#                 Var ffffffff____________: Array[String, 3] = Array(
#                                             Array(3,______________,5),
#                                             Array(____,2)
#                                         );
#                 fwafdasdf() {
#                     fwefa.print(________[wefadfa1][2234]);
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,278))

#     def test_79(self):
#         input = """
#             Class efewfwefsdfadf {
#                 Continue;
#                 Return;
#             }
#         """
#         expect = "Error on line 3 col 16: Continue"
#         self.assertTrue(TestParser.test(input, expect,279))

#     def test_80(self):
#         input = """
#             Class fwafdfew {
#                 fwefadfadf() {
#                     Foreach(a[0] In 00+04/0b0 .. b <= !c By get().count) {
#                         Continue;
#                     }
#                 }
#             }
#         """
#         expect = "Error on line 4 col 29: ["
#         self.assertTrue(TestParser.test(input, expect,280))

#     def test_81(self):
#         input = """
#             Class dfskjf_jdss {
#                 Rfsfsa() {
#                     Val $r: Int = 20;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 24: $r"
#         self.assertTrue(TestParser.test(input, expect,281))

#     def test_82(self):
#         input = """
#             Class aawefdsfsad {
#                 dessfrfdedad() {
#                     Val fwefdfadsfaefewrerq: Array[Array[Array[Float, 00],0x3_23],4];
#                 }
#             }
#         """
#         expect = "Error on line 4 col 70: 00"
#         self.assertTrue(TestParser.test(input, expect,282))

#     def test_83(self):
#         input = """
#             Class awfefdsaf {
                
#                 awfdfasdf() {
#                     Return ewfawefefafA::$naawefawefadsme() + twefwecsdfas();
#                 }
#             }
#         """
#         expect = "Error on line 5 col 74: ("
#         self.assertTrue(TestParser.test(input, expect,283))
    
#     def test_84(self):
#         input = """
#             Class testing {
#                 Var twe, FWE32y: Int = 1, 00;
#                 method(a,b,c:Int; r:Func) {
#                     If (0x0 + 2_13_123.645 > 0xAAAAAAAAAAAAAAAAAAAAAAAAA) {
#                         Foreach(index In 0x1 .. 12_3*45_35 By ug.gfsger(r)) {
#                             If (wthtrb / rtrwtwer) {
#                                 If (wefwe32 >= afnewaiufbwi) {
#                                     Break;
#                                 }
#                             }
#                         }
#                     }
#                     Elseif (tWFWA / 7_423.3243e-1231) {
#                         If (!FAWEF) { }
#                         Else { Return; }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,284))

#     def test_85(self):
#         input = """
#             Class name {
#                 method () {
#                     a = name::$age;
#                     b = name::$age().b();
#                     c = age;
#                     d = age();
#                 }
#             }
#         """
#         expect = "Error on line 7 col 27: ("
#         self.assertTrue(TestParser.test(input, expect,285))

#     def test86(self):
#         input = """
#             Class zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz {
#                 Var $_123a: Int = 00; 

#                 Mefwefwsdfthod () {
#                     Self.des(a,b,c);

#                     hung.dqw();

#                     If (asdf[213]) {
#                         Return qwdqd.fafewfawf(t); 
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,286))

#     def test87(self):
#         input = """
#             Class _____________ {
#                 afawefafd () {
#                     ygouygua = name::$age;
#                     2dwqewqf = efwfwfwfasdfwef;
#                     wefafwefafasde = $wfwwoeifjoiwaf();
#                 }
#             }
#         """
#         expect = "Error on line 5 col 21: dwqewqf"
#         self.assertTrue(TestParser.test(input, expect,287))

#     def test88(self):
#         input = """
#             Class fsafdsfawef {
#                 Val count: Int = 0;

#                 fasdvnhnyj() {
#                     Return Self.fwefad + Self.count(_________) - naeefwfme::$turn(_________) * fewfafe.$Age(_________);
#                 }
#             }
#         """
#         expect = "Error on line 6 col 103: $Age"
#         self.assertTrue(TestParser.test(input, expect,288))

#     def test89(self):
#         input = """
#             Class sfwefwef: ________________________ {
#                 __s432235324___tr__(asdasfqw: Boolean) {
#                     Self.____ = Self.count(___________) + __________________.$dollar();
#                 }
#             }
#         """  
#         expect = "Error on line 4 col 77: $dollar"
#         self.assertTrue(TestParser.test(input, expect,289))

#     def test90(self):
#         input = """
#             Class __________________________ {
#                 ____________dhafiawhu32AFDSAFEAWF5342387______________() {
#                     dwqudhqidhf = name[fewijidwid].fdshfaoifpppp;

#                 }
#             }
#         """
#         expect = "Error on line 4 col 50: ."
#         self.assertTrue(TestParser.test(input, expect,290))

#     def test_91(self):
#         input = """
#             Class Test{

#                 Test(){
#                     Var awdqe: Boolean= Self::ins;
#                     Var b21324: Float= Self::$afwfdsfsfa;
#                 }
#             }
#         """
#         expect = "Error on line 5 col 44: ::"
#         self.assertTrue(TestParser.test(input, expect, 291))

#     def test_92(self):
#         input = """
#             Class wefwef33 {
#                 Val bfwefassd: Int = 0x0;
#                 Val awefasdfa: Float = Self.ayurty.brtytr.afe2131c().t[00];
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,292))

#     def test_93(self):
#         input = """
#             Class dqwdqffr {
#                 __________453453() {
#                     Return _____________::hufawe::$bafawef::$__________________________________.faw7efhw236182;
#                 }
#             }
#         """
#         expect = "Error on line 4 col 42: hufawe"
#         self.assertTrue(TestParser.test(input, expect,293))

#     def test_94(self):
#         input = """

#             Class qwqwdqwd {


#                 ___________________________________() {

#                     awefd = khj::$bin()[0b101011];

#                     a = Main[0][1][2][1][2][1][2][1][2][1][2][1][2].get();
#                 }
#             }
#         """
#         expect = "Error on line 10 col 67: ."
#         self.assertTrue(TestParser.test(input, expect,294))

#     def test_95(self):
#         input = """
#             Class myClass {
#                 Val a__________________738f738f7hfa: Boolean = Main.a.get(_____________________[__________._________(_____________,_______________)]);
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,295))

#     def test_96(self):
#         input = """
            
#         """
#         expect = "Error on line 3 col 8: <EOF>"
#         self.assertTrue(TestParser.test(input, expect,296))

#     def test_97(self):
#         input = """
#             Class _97 {
#                 _metht5y5464_____od() {
#                     Name.a[0x0][oxo] = Self.gefwaft().swe3et.gewfwt();
#                     Name.a[00][oo] = Self.gefwaft().swe3et.gewfwt();
#                     Name.a[asdfhwe.fwefew(wduwe)][sdfasj.ergrgaf(__________________________________)] = Self.gefwaft().swe3et.gewfwt();
#                     Name.a[uihwwef][0x0] = Self.gefwaft().swe3et.gewfwt();
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,297))

#     def test_98(self):
#         input = """
#             Class Cfwefw {
#                 Var ______________________b________________: _____________________A__________________________;
#                 wfea__weuwufhw__________5235() {
#                     Return C::$fwefew + C.mcbnvb().aed[0xFECDA213];
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,298))

#     def test_99(self):
#         input = """
#             Class fewfasdf {
#                 $methowqfewfuykyud() {
#                     Foreach(i In -323432 .. -1.213e-313421 By -3432) {
#                         Foreach(j_______________________ In 00 .. -0xFF1235176 By 0b1101010101) {
#                             Var fwewefa: String = 0.2e213;
#                         }
#                     }
#                 }
#             }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,299))

import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_string_escape3(self):
        self.assertTrue(TestLexer.test(""" "This sentence contains new line\n." """, """Unclosed String: This sentence contains new line\n""", 1007))
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
#     def test_integer3(self):
#         self.assertTrue(TestLexer.test("123 _123 1_23 123 __123", "123,_123,123,123,__123,<EOF>", 101))
#     def test_block_comment7(self):
#         self.assertTrue(TestLexer.test("/* This is another block comment / */", "<EOF>", 101))

#     def test_1(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    
#     def test_2(self):
#         """test comment"""
#         self.assertTrue(TestLexer.test(
#             """
#             //abc
#             /* comment */ */            
#             """
#             , "*,/,<EOF>", 102))

#     def test_3(self):
#         """intlit floatlit"""
#         self.assertTrue(TestLexer.test(
#             """
#             1234 123
#             1_72
#             1_234_567
#             1.234 1.2e3 7E-10
#             1_234.567
#             e-10
#             """
#             , "1234,123,172,1234567,1.234,1.2e3,7E-10,1234.567,e,-,10,<EOF>", 103))

#     def test_5(self):
#         """intlit floatlit"""
#         self.assertTrue(TestLexer.test(
#             """
#             "This is a string containing tab \t"
#             "He asked me: \\"Where is John?\\""
#             """
#             , """This is a string containing tab \t,He asked me: \\"Where is John?\\",<EOF>""", 105))

#     def test_6(self):
#         """intlit floatlit"""
#         self.assertTrue(TestLexer.test(
#             """
#             auto break boolean do else
#             false float for function if
#             integer return string true while
#             void out continue of inherit
#             array
#             """
#             , """auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>""", 106))

#     def test_7(self):
#         """intlit floatlit"""
#         self.assertTrue(TestLexer.test(
#             """
#             + - * / %
#             ! && || ==
#             != < <= > >=
#             ::
#             """
#             , """+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>""", 107))

#     def test_8(self):
#         """intlit floatlit"""
#         self.assertTrue(TestLexer.test(
#             """
#             ( ) [ ] . , ; : { } =
#             """
#             , """(,),[,],.,,,;,:,{,},=,<EOF>""", 108))

#     def test_9(self):
#         """intlit floatlit"""
#         self.assertTrue(TestLexer.test(
#             """
#             x : integer = 65;
#             fact : function integer (n : integer ) {
#                 if (n == 0) return 1 ;
#                 else return n * fact (n - 1 ) ;
#             }
#             inc : function void (out n : integer , delta : integer ) {
#                 n = n + delta ;
#             }
#             main : function void () {
#                 delta : integer = fact (3) ;
#                 inc(x,delta) ;
#                 printInteger(x) ;
#             }
#             """
#             , """x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>""", 109))

#     def test_10(self):
#         """test comment"""
#         self.assertTrue(TestLexer.test(
#             """
#             //abc
#             /* commemts */
#             // eof
#             """
#             , "<EOF>", 110))
    
#     def test_11(self):
#         """test comment"""
#         self.assertTrue(TestLexer.test(
#             """
#             {1, 5, 7, 12} {"Kangxi", "Yongzheng", "Qianlong"}
#             """
#             , "{,1,,,5,,,7,,,12,},{,Kangxi,,,Yongzheng,,,Qianlong,},<EOF>", 111))

#     def test_12(self):
#         """test comment"""
#         self.assertTrue(TestLexer.test(
#             """
#             x : array [2, 3] of integer;
#             fact : function integer (n : integer ) {
#                 for (i = 1, i < 10, i + 1) {
#                     writeInt(i);
#                 }
#             }
#             main : function void () {
#                 r, s: integer;
#                 r = 2.0;
#                 a, b: array [5] of integer;
#                 s = r * r * myPI;
#                 a[0] = s;
#             }
#             """
#             , "x,:,array,[,2,,,3,],of,integer,;,fact,:,function,integer,(,n,:,integer,),{,for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},},main,:,function,void,(,),{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,integer,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>", 112))

#     def test_inline_comment(self):
#         self.assertTrue(TestLexer.test("// This is a comment", "<EOF>", 101))
#     def test_inline_comment2(self):
#         self.assertTrue(TestLexer.test("// This is a comment \n", "<EOF>", 101))
#     def test_inline_comment3(self):
#         self.assertTrue(TestLexer.test("// This is a comment with \"\\\" inside.", "<EOF>", 101))
#     def test_inline_comment4(self):
#         self.assertTrue(TestLexer.test("//*This is still a inline comment", "<EOF>", 101))
#     def test_inline_comment5(self):
#         self.assertTrue(TestLexer.test("//*This is still a inline comment*/", "<EOF>", 101))
#     def test_block_comment1(self):
#         self.assertTrue(TestLexer.test("/* This is a block comment */", "<EOF>", 102))
#     def test_block_comment2(self):
#         self.assertTrue(TestLexer.test("/* This is a block comment \nwith multiple lines */", "<EOF>", 102))
#     def test_block_comment3(self):
#         self.assertTrue(TestLexer.test("/* This is a block //comment */", "<EOF>", 102))
#     def test_block_comment4(self):
#         self.assertTrue(TestLexer.test("/* This is a block comment end with \"* /\" */", "<EOF>", 102))
#     def test_block_comment5(self):
#         self.assertTrue(TestLexer.test("/* This is a block comment \n//Inline Comment */", "<EOF>", 102))
#     def test_block_comment6(self):
#         self.assertTrue(TestLexer.test("/* This is a unclose block comment ", "/,*,This,is,a,unclose,block,comment,<EOF>", 102))
#     def test_block_comment7(self):
#         self.assertTrue(TestLexer.test("/* This is another block comment */ */", "*,/,<EOF>", 101))
#     def test_nested_comment1(self):
#         self.assertTrue(TestLexer.test("// A line comment // contains another line comment . ", "<EOF>", 101))
#     def test_nested_comment2(self):
#         self.assertTrue(TestLexer.test("/*a block cmt /*cover a block cmt*/ */ ", "*,/,<EOF>", 101))
#     def test_nested_comment3(self):
#         self.assertTrue(TestLexer.test("/*block comment 1*/\n/*block comment2*///inline comment", "<EOF>", 101))
    
#     def test_identifier(self):
#         self.assertTrue(TestLexer.test("my name is Hoa", "my,name,is,Hoa,<EOF>", 101))
#     def test_identifier2(self):
#         self.assertTrue(TestLexer.test("__", "__,<EOF>", 101))
#     def test_identifier3(self):
#         self.assertTrue(TestLexer.test("Ident 1 id1", "Ident,1,id1,<EOF>", 101))
#     # def test_identifier4(self):
#     #     self.assertTrue(TestLexer.test("1Cat+2_Dogs", "1,Cat,+,2,_Dogs,<EOF>", 101))
#     def test_identifier4(self):
#         self.assertTrue(TestLexer.test("X/123", "X,/,123,<EOF>", 101))
#     def test_identifier5(self):
#         self.assertTrue(TestLexer.test("_count 123number||sum", "_count,123,number,||,sum,<EOF>", 101))
#     def test_identifier6(self):
#         self.assertTrue(TestLexer.test("1day, I go to _school123_.;", "1,day,,,I,go,to,_school123_,.,;,<EOF>", 101))
     
#     def test_keyword1(self):
#         self.assertTrue(TestLexer.test("autobreakboolean", "autobreakboolean,<EOF>", 101))
#     def test_keyword2(self):
#         self.assertTrue(TestLexer.test("integer function void", "integer,function,void,<EOF>", 101))
        
#     def test_integer1(self):
#         self.assertTrue(TestLexer.test("0090", "0,0,90,<EOF>", 101))
#     def test_integer2(self):
#         self.assertTrue(TestLexer.test("-090x90", "-,0,90,x90,<EOF>", 101))
#     def test_integer3(self):
#         self.assertTrue(TestLexer.test("123 _123 1_23 123_ __123", "123,_123,123,123,__123,<EOF>", 101))
#     def test_integer4(self):
#         self.assertTrue(TestLexer.test("123*901/10", "123,*,901,/,10,<EOF>", 101))
#     def test_integer5(self):
#         self.assertTrue(TestLexer.test("1_23__456_", "123456,<EOF>", 101))
#     def test_integer6(self):
#         self.assertTrue(TestLexer.test("5 + 100/20", "5,+,100,/,20,<EOF>", 101))
#     def test_integer7(self):
#         self.assertTrue(TestLexer.test("-1000-10+-100/1", "-,1000,-,10,+,-,100,/,1,<EOF>", 101))
#     def test_integer8(self):
#         self.assertTrue(TestLexer.test("80 < 120 && (3-7) >= 7", "80,<,120,&&,(,3,-,7,),>=,7,<EOF>", 101))
#     def test_integer9(self):
#         self.assertTrue(TestLexer.test("5!=8 || 12%4 == 0", "5,!=,8,||,12,%,4,==,0,<EOF>", 101))
#     def test_integer10(self):
#         self.assertTrue(TestLexer.test("x00_0 010 1000x", "x00_0,0,10,1000,x,<EOF>", 101))
    
#     def test_float1(self):
#         self.assertTrue(TestLexer.test("1.2e10", "1.2e10,<EOF>", 101))
#     def test_float2(self):
#         self.assertTrue(TestLexer.test(" 7.5 0.6 ", "7.5,0.6,<EOF>", 101))
#     def test_float3(self):
#         self.assertTrue(TestLexer.test(" 5.1+1e5 ","5.1,+,1e5,<EOF>",101))
#     def test_float4(self):
#         self.assertTrue(TestLexer.test(" 6.8+9.2 ","6.8,+,9.2,<EOF>",101))
#     def test_float5(self):
#         self.assertTrue(TestLexer.test(" -1.3+1e3 ","-,1.3,+,1e3,<EOF>",101))
#     def test_float6(self):
#         self.assertTrue(TestLexer.test(" .6 ",".,6,<EOF>",101))
#     def test_float7(self):
#         self.assertTrue(TestLexer.test(" 7E15 ","7E15,<EOF>",101))
#     def test_float8(self):
#         self.assertTrue(TestLexer.test(" 1.0e ","1.0,e,<EOF>",101))
#     def test_float9(self):
#         self.assertTrue(TestLexer.test("4.1e3 ","4.1e3,<EOF>",101))
#     def test_float10(self):
#         self.assertTrue(TestLexer.test(" 5e-8+6 ","5e-8,+,6,<EOF>",101))
#     def test_float11(self):
#         self.assertTrue(TestLexer.test(" 10.0e-2.2e-3 ","10.0e-2,.2e-3,<EOF>",101))
   
#     def test_string(self):
#         self.assertTrue(TestLexer.test(""""Hello World !" ""","""Hello World !,<EOF>""",101))
#     def test_string2(self):
#         self.assertTrue(TestLexer.test(""""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture." ""","""1 Cat + 2 Dogs :: 12 Birds, 3 Spiders in the picture.,<EOF>""",101))
#     def test_string3(self):
#         self.assertTrue(TestLexer.test(""""Hello World !\"\n\"The result is: \"2 ""","""Hello World !,The result is: ,2,<EOF>""",101))
#     # def test_string4(self):
#     #     self.assertTrue(TestLexer.test(""""abc" ""","""abc,<EOF>""",101))
#     def test_string9(self):
#         self.assertTrue(TestLexer.test(""" "%^&*(\t"|"|b6783\\")&* ""","""%^&*(	,Error Token |""",101))
    
#     def test_string_comment(self):
#         self.assertTrue(TestLexer.test(""" "Hello /*My*/ World" ""","""Hello /*My*/ World,<EOF>""",101))
#     ## chỗ này có lỗi ko? nếu có là unclosed string hay error token # 
#     # def test_string_comment2(self):
#     #     self.assertTrue(TestLexer.test(""" "Hello World/* " */  ""","""Hello World/* ,*,/,<EOF>""",101))
#     def test_string_comment3(self):
#         self.assertTrue(TestLexer.test(""" "Hello //My World" ""","""Hello //My World,<EOF>""",101))
    
#     def test_string_escape(self):
#         self.assertTrue(TestLexer.test(""""This is a string containing tab \t." """, """This is a string containing tab \t.,<EOF>""", 101))
#     def test_string_escape2(self):
#         self.assertTrue(TestLexer.test(""""He asked me: \"Where is John?\"" """, """He asked me: \"Where is John?\",<EOF>""", 101))
#     ## He asked me: "Where is John?" lồng string trong string
#     def test_string_escape3(self):
#         self.assertTrue(TestLexer.test(""""This sentence contains new line\n." """, """Unclosed String: \"This sentence contains new line\n""", 101))
#     def test_string_escape4(self):
#         self.assertTrue(TestLexer.test(""""Print it ( a line char \\n )" """, """Print it ( a line char \\n ),<EOF>""", 101))
#     def test_string_escape5(self):
#         self.assertTrue(TestLexer.test(""""There is a backspace \b. before here." """, """There is a backspace \b. before here.,<EOF>""", 101))
#     def test_string_escape6(self):
#         self.assertTrue(TestLexer.test(""""Multiple chars \\\\" """, """Multiple chars \\\\,<EOF>""", 101))
#     def test_string_escape7(self):
#         self.assertTrue(TestLexer.test(""""He asked me: \\"Where is John?\\"" """, """He asked me: \\"Where is John?\\",<EOF>""", 101))
#     def test_string_escape8(self):
#         self.assertTrue(TestLexer.test("""" Print integer number by \"printInt(anArg: int)\"" """, """ Print integer number by ,printInt,(,anArg,:,int,),,<EOF>""", 1001))
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
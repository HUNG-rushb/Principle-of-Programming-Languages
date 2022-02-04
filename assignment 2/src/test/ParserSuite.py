# 1913652
# Trịnh Duy Hưng

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_0(self):
        input = """
            Class Doadag: Anidadsmal { }
            Class Snfffsdake: Dqwwde { }
            Class bfwefeuttdqwerfqdqwly {
                __swdqfqwdqwtr__() {
                    Var a, b, c, d, e: Int = 1,2,4,5,6;
                    Val $effffffffff: Int;
                }
            }
            """
        expect = "Error on line 7 col 24: $effffffffff"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_1(self):
        input = """
            Class DFVDWDosadfwqg: DFCVBBBBBBBBBBBBBBBAniqvsdvmal {
                $hungyeuquynhquatriquadat() {
                    awefdcvvv = asuidfuw[71223][24132];
                }
            }
            Class kitty: hyeergere {
                $fwefwefwfc() {
                    Return Self.wuefwiu1237wfbhwbfw;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        input = """
            Class dfasvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv {
                getWife() {
                    Var hung: Boolean = true;
                }
                main() {
                    Var quynh: Float;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        input = """
            Class calsclasclaslcascl {
                getMoney() {
                    Var b: Float = 0.3;
                    Var b: Float = 0.3;
                    Var b: Float = 0.3;
                    Var b: Float = 0.3;
                    Var b: Float = 0.3;
                }
                funjccnskjddjskcsdcvc() {
                    If (a >= b) {
                        Var a: Int = 0;
                        a = a + 3;
                    }
                    Elseif (b >= c) {
                        Self.getName(a >= b);
                    }
                    Elseif (12 >= g) {
                        Self.insert("String");
                    }
                    Elseif (12 >= g) {
                        Self.insert("String");
                    }
                    Elseif (12 >= g) {
                        Self.insert("String");
                    }
                    Elseif (12 >= g) {
                        Self.insert("String");
                    }
                    Elseif (12 >= g) {
                        Self.insert("String");
                    }
                    Else {
                        ___________________ = _______________________________________________________________________;
                        Hung = Vi;
                    }
                }

                setcvsdvdsvdvAge(okokokok: Boolean) {
                    Self.agbseegree = agesrgsfdsde;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        input = """ 
            Class meomeoemeoemoeemoeo: Cat {
                Var truefalse: Boolean;
                Var $a, c, d: Float = .e41231, 234322., 712328.333333339;
                Var a: Array[Int, 8] = Array(10907090.1232, 3.6123, 34e5, 23243e4, 12332432.723E4 , 32144E512311111, 23E4623887, 12132.7E4);
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        input = """
            Class fffffffsdfasfwwf {
                wewgwfwef(awefwfs: Boolean; bwwebhbhds: Float) {
                    Foreach (iokosofd In 846 .. 240000 By isdfav <= 9999) {
                        sfsdfum = sudsfgwerm + rraya[isdafhsf];
                    }
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_6(self):
        input = """
            Class Quynh {
                fsadf(iuiwer884: Float; b3342: Float) {
                    Return iuiwer884 || b3342 < cwef.refer(afwedew,sdv2) && 23324 + 134235.4;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7(self):
        input = """
            Class WestSide {
                MainMenu(quynh: Boolean; hung: Int) {
                    Self.arr[5784378] = hung.cubu() + quynh.dep();
                }
            }
            Class DELLL {
                Hybrid(){
                    Return 61236712;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8(self):
        input = """
                Class MyClass {
                    Var beRot: NguoiYeu;

                    Var maicuoiluonnha: Int = 0;

                    $cuoiluonnha() {
                        Out.print(Self.beRot);
                    }

                    adsad(_age: Int) {
                        Self.maicuoiluonnha = _age;
                    }
                }

                Class MyClass {
                    Var beRot: NguoiYeu;

                    Var maicuoiluonnha: Int = 0;

                    $cuoiluonnha() {
                        Out.print(Self.beRot);
                    }

                    adsad(_age: Int) {
                        Self.maicuoiluonnha = _age;
                    }
                }

                Class MyClass {
                    Var beRot: NguoiYeu;

                    Var maicuoiluonnha: Int = 0;

                    $cuoiluonnha() {
                        Out.print(Self.beRot);
                    }

                    adsad(_age: Int) {
                        Self.maicuoiluonnha = _age;
                    }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    
    def test_9(self):
        input = """
            Class $HungYeuQuynhlamnha {
            }

        """
        expect = "Error on line 2 col 18: $HungYeuQuynhlamnha"
        self.assertTrue(TestParser.test(input, expect, 209))
    
    def test_10(self):
        input = """
            Class father {
                get(){

                }
            }
            Class son: father {
                ok() {
                    Return super::laugh();
                }
            }
        """
        expect = "Error on line 9 col 34: laugh"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test_11(self):
        input = """
            Class hungyeuquynh {
                cuoi() {
                    Foreach (i In 0 .. 999 By pi <= i) {
                        gf.bf();
                    }

                    Return true;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_12(self):
        input = """
            Class Shen {
                $_____twilieye() {
                    Return false;
                }
            }

            Class Program {
                main_main() {
                    agfASFFFFFFEERSWQf = (myConst + okokokoko) && (x + y + z);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_13(self):
        input = """
            Class myHippo {
                cat(hung: Array[Int, 99]) {
                    Return hung[0]
                }
            }
        """
        expect = "Error on line 5 col 16: }"
        self.assertTrue(TestParser.test(input, expect,213))

    def test_14(self):
        input = """
            Class testing____testing {
                Constructor(hungyeuquynh: Array[Float, 9]) {
                    Self.hung = hungyeuquynh[1];
                    Self.love = hungyeuquynh[2];
                    Self.quynh = hungyeuquynh[2][1];
                    Self.hung = hungyeuquynh[1];
                    Self.love = hungyeuquynh[2];
                    Self.quynh = hungyeuquynh[2][1];
                    Self.hung = hungyeuquynh[1];
                    Self.love = hungyeuquynh[2];
                    Self.quynh = hungyeuquynh[2][1];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,214))

    def test_15(self):
        input = """
            Class CuoiLuonNha {
                Destructor() {
                    bunbo.Delete().All(0);
                    love.hung_quynh();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,215))

    def test_16(self):
        input = """
            Class wedding {
                anni() {
                    t = Rhungquynh::$cuoiluonnha()[57] >= 78;
                    Return Self.love;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,216))

    def test_17(self):
        input = """
            Class Program {
                Hung_Quynh() {
                    Return Self.cuoiluon();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,217))

    def test_18(self):
        input = """
            Class gaugaugagua {
                gotobed() {

                }

                Constructor() {
                    Self.create = okokok;
                }

                Destructor() {
                    Mew.delete();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,218))

    def test_19(self):
        input = """
            Class quynh {
                Var beRot: Array[Float, -20] = true;
            }
        """
        expect = "Error on line 3 col 40: -"
        self.assertTrue(TestParser.test(input, expect,219))

    def test_20(self):
        input = """
            Class ari {
                Constructor(a, b : Int)
                {
                    hungyeuquynhlamnha.print("Contructor");
                }
                Destructor()
                {
                    hungyeuquynhlamnha.print("Destructor");
                }
                $_getMethod() {
                    Return 12 + 1.2 - c + !b >= 8 || 4 || (a + b);
                }
            }
            Class Program {
                Constructor(a, b : Int)
                {
                    hungyeuquynhlamnha.print("Contructor");
                }
                Destructor()
                {
                    hungyeuquynhlamnha.print("Destructor");
                }
                main() {
                    a = (myConst + b) && a + b + abcde;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,220))

    def test_21(self):
        input = """
            Class P423423ro2342gra234213m {
                ma234729891in() {
                    dasd.print("lo cc");
                }
            }
            Class iden31235351435 {

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,221))

    def test_22(self):
        input = """
            Class jztr {
                func(s: Boolean; r: Float) {
                    Return ojojojojojjoo.Str(s + r);
                }
            }
            Class Program {
                jztr() {

                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,222))

    def test_23(self):
        input = """
            Class Program {
                main(){}
            }

            Class class1 {
                Var name: String;
            }
            Class class2 {
                Val $height: Float = 1.75;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,223))

    def test_24(self):
        input = """
            Class obj {
                Var _obj: Int = 0, 9;
            }
            Class Program {
                main() {
                    func(Array("a", "b", "c"));
                    Return Self.arr;
                }
            }
        """
        expect = "Error on line 3 col 33: ,"
        self.assertTrue(TestParser.test(input, expect,224))

    def test_25(self):
        input = """
            Class Program {
                main() {
                    Var a,b: Array[Float, 3.9];
                }
            }
            Class nicebutt {
                attr(wefwef, w234efwef: Int) {
                    Return wefwef[4] != we343fwef[1].name;
                }
            }
        """
        expect = "Error on line 4 col 42: 3.9"
        self.assertTrue(TestParser.test(input, expect,225))

    def test_26(self):
        input = """
            Class parent {


                Var lname, fname: String = "";
                $getName() {
                    Return Self.name[2];
                }
                setName(name: Int) {
                    lname = name[0];
                }
            }
        """
        expect = "Error on line 5 col 45: ;"
        self.assertTrue(TestParser.test(input, expect,226))

    def test_27(self):
        input = """
            Class Progfasdfram {
                masafasdfin() {
                    Return New objdsfasdfect();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,227))

    def test_28(self):
        input = """
            Class twitter {
                main(a: Boolean; b: Boolean) {
                    Return New Bull().dsaf().Cicke();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,228))

    def test_29(self):
        input = """
            Class fasdfasdf {
                Constructor(){Return eeeeeeeeeeeeeeeeeeeeeeee;}
            }
            Class dsbisubviweuhfw {

                Return statements;
            }
        """
        expect = "Error on line 7 col 16: Return"
        self.assertTrue(TestParser.test(input, expect,229))

    def test_30(self):
        input = """
            Class fwefwefaf {
                maffwefgergergwain() {

                }
            }
            Class fawfadsfd {



                Destructor(param: Int, param_2: String) {

                }
            }
        """
        expect = "Error on line 11 col 27: param"
        self.assertTrue(TestParser.test(input, expect,230))

    def test_31(self):
        input = """
            Class Dog {
                Var name: Int;



                Var age: Int = 2, 6, 4;
            }
            Class Program {
                main() {

                }
            }
        """
        expect = "Error on line 7 col 32: ,"
        self.assertTrue(TestParser.test(input, expect,231))

    def test_32(self):
        input = """
            Class eqwego678dhgf {
                main() {
                    Foreach (rtyre564tsg In 1 .. 111111110 + 5 By adfacv[i] >= 234) {
                        If (a[ifaf][1123] != b[11]) {
                            Return;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,232))

    def test_33(self):
        input = """
            Class aloaloalo {
                main() {
                    Var name: Int;
                }
            }
            Class wfsadfsdadf {
                function() {
                    Var name: Int;




                    Hung.Main()::$dollar();
                }
            }
        """
        expect = "Error on line 14 col 31: ::"
        self.assertTrue(TestParser.test(input, expect,233))

    def test_34(self):
        input = """
            Class ok {
                $maiereewrwn() {

                }
            }
            Class l1l1l1l1l {
                adfasdfwerw(s1, s2, s3: String) {
                    Return Str.concat(s13213, s12412, afw1231s3);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,234))

    def test35(self):
        input = """
            Class giraffe {
                giraffe() {
                    Return New giraffe().giraffe();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,235))

    def test36(self):
        input = """
            Class test25fsfasldfk {
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                Var a: Int = 0;
                main() {
                    a = New obj("string 1");
                    Out.print(a.age);
                    a = New obj("string 1");
                    Out.print(a.age);
                    a = New obj("string 1");
                    Out.print(a.age);
                    a = New obj("string 1");
                    Out.print(a.age);
                    a = New obj("string 1");
                    Out.print(a.age);
                    a = New obj("string 1");
                    Out.print(a.age);
                    a = New obj("string 1");
                    Out.print(a.age);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,236))

    def test_37(self):
        input = """
            Class Method {
                newMethod(a: String) {
                    Return "This is a \\nstring"[1].getText();
                }
            }
        """
        expect = "Error on line 4 col 50: ."
        self.assertTrue(TestParser.test(input, expect,237))

    def test_38(self):
        input = """
            Class Program {

                Var a, b, c: Int = 1, 2, 3 >= 9 + 5;

                main() {

                    If (a >= b) {

                        Foreach (i In 0 .. c[5][3].length By 1) {
                            If (c[i]) {
                                Continue;
                            }
                            Else {
                                Break;
                            }
                        }
                    }
                }
            }
        """
        expect = "Error on line 10 col 50: ."
        self.assertTrue(TestParser.test(input, expect,238))

    def test_39(self):
        input = """
            Class Program {
                main() {
                }
            }
            Class newClass {
                Val counqdqwdt: Int = 150324;
                Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
                Pr234234intO32ut() {
                    Return Self.cou123nt * Self.ra213124te;
                }
                Val counqdqwdt: Int = 150324;
                Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
                Pr234234intO32ut() {
                    Return Self.cou123nt * Self.ra213124te;
                }
                Val counqdqwdt: Int = 150324;
                Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
                Pr234234intO32ut() {
                    Return Self.cou123nt * Self.ra213124te;
                }
                Val counqdqwdt: Int = 150324;
                Val sudwedm, rate: Float = 10123.23523, 312454.4234234;
                Pr234234intO32ut() {
                    Return Self.cou123nt * Self.ra213124te;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,239))

    def test_40(self):
        input = """
            Class belrlrlrlrl {
                $ahahahahah() {
                    Return Self.sousfwefwdsnd()[3029];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,240))

    def test_41(self):
        input = """
            Class eerrerrert {
                Var asdafd, bfasdf, cwefwefw: Float = 334, 4234, 54234;
                $prifwwfwnt() {
                    Return Array(a,b,c);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,241))

    def test_42(self):
        input = """
            Class sdfsaf {
                Var we: sdfsdddddddd;
                Var me: tyer43534terster = 0.2;
                $gsdafqe3432t() {
                    Losdfgfsdcal.St4234ore.sieu3342thi();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,242))

    def test_43(self):
        input = """
            Class Progrdfdafdsfam {
                msdfaain() {
                }
            }
            Ofsadfdsut.prwefwint(adsfa, b, 3);
            Out.prinsdfs(a, b, 3);
            Out.prinsdfat(a, b, 3);
        """
        expect = "Error on line 6 col 12: Ofsadfdsut"
        self.assertTrue(TestParser.test(input, expect,243))

    def test_44(self):
        input = """
            Class tfhs {
                assdwf() {
                    If (afsadf == fsadfgwwbrtyu) {
                        Foreach (i In 1 .. sadfwewefsdsadv By saudhuisadf) {
                            Continue;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,244))

    def test_45(self):
        input = """
            Class wopiolio {
                vmvzcvzda() {
                    Dawfaweog.namfwewefe = Cafweat.nafwefwwafqweme +. "1asdfqq123adf$%^%$##$%$#%&^&^%^%<><<U><";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,245))

    def test_46(self):
        input = """
            Class Madfasdfsadeo: Dsdafasdfog {
                $gasdfasdfet() {
                    Self.naasdfdsafme = Doasdfdsafg::nameasdfsdafsa;
                }
            }
        """
        expect = "Error on line 4 col 53: nameasdfsdafsa"
        self.assertTrue(TestParser.test(input, expect,246))

    def test_47(self):
        input = """


            If (a >= b) {
                Return Program;
            }
            Class Buffadadafalo: Anifr43t54gmals {
                asd434Doaasgafdfadssa.scofdfapeMethod();
            }
        """
        expect = "Error on line 4 col 12: If"
        self.assertTrue(TestParser.test(input, expect,247))

    def test_48(self):
        input = """
            Foreach (i In 0 .. 9854 By 12313 * 2312 / 312 - adsfa.gdsfaset + adfweb.nadfsdfme) {
                Continue;
                Break;
            }
        """
        expect = "Error on line 2 col 12: Foreach"
        self.assertTrue(TestParser.test(input, expect,248))

    def test_49(self):
        input = """
            Class FSDFAA {
                Return New BRETWERT(SGER5462A);
            }
        """
        expect = "Error on line 3 col 16: Return"
        self.assertTrue(TestParser.test(input, expect,249))

    def test_50(self):
        input = """
            Class asdsDB: WEFWFAA {
                Var AWEFDa, FWEFWEFb: Float = 32312.5676, 2131235;
                Return SDGSSFGERa;
            }
        """
        expect = "Error on line 4 col 16: Return"
        self.assertTrue(TestParser.test(input, expect,250))

    def test_51(self):
        input = """
            Class Program {
                func(){
                    gjty4578_test();
                } 
            }
            
        """
        expect = "Error on line 4 col 33: ("
        self.assertTrue(TestParser.test(input, expect,251))

    def test_52(self):
        input = """
            Class hungquynh {
                If (asdfasd <= 34738736)
            }
        """
        expect = "Error on line 3 col 16: If"
        self.assertTrue(TestParser.test(input, expect,252))

    def test_53(self):
        input = """



            Self.fwefwafsd = 223948932.2398423;
        """
        expect = "Error on line 5 col 12: Self"
        self.assertTrue(TestParser.test(input, expect,253))

    def test_54(self):
        input = """
            Class Vwefwfds2213vsdvsf_____238dh823jksdaf {
                Val arr = Array[Array[Boolean, Vwefwfds2213vsdvsf_____238dh823jksdaf], Vwefwfds2213vsdvsf_____238dh823jksdaf];
            }
        """
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.test(input, expect,254))

    def test_55(self):
        input = """
            Class Program {
                main() {

                }
            }
            Class ___2342____dfasfokBdfsdfasdf {

            }
            Class ____Csadf {

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,255))

    def test_56(self):
        input = """
            Class Prog3432regwwer______________3498jsaa9ram {
                madsfasdfqin() {PdsfasdfaPL() {}}





                Var tu34_56h_(): Int;
            }
        """
        expect = "Error on line 3 col 43: ("
        self.assertTrue(TestParser.test(input, expect,256))

    def test_57(self):
        input = """
            Class ER: Aw, Tfwefa_2387_______fwefu {
            }
        """
        expect = "Error on line 2 col 24: ,"
        self.assertTrue(TestParser.test(input, expect,257))

    def test_58(self):
        input = """
            Class Bqwdasdasdffwqdewf {
                Var b, c : Int = 1384958670.44857682;
            }
        """
        expect = "Error on line 3 col 52: ;"
        self.assertTrue(TestParser.test(input, expect,258))

    def test_59(self):
        input = """
            Class iwefwefadfd {
                fafwefew34343gsg() {
                    adfsaa = Self.agewr2342a____________e + 3234.545 - 0b0 * Bweqrwe.fawfewer();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,259))

    def test_60(self):
        input = """
            Class Prwefawf3453___wekwe9932ogram {
                maiawefawn() {
                    a[0] = "Stri$@#^#&#%^ng 1" ==. "3425#@$strwfewang \\'";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,260))

    def test_61(self):
        input = """
            Class B {



                B435__.call();
            }
        """
        expect = "Error on line 6 col 22: ."
        self.assertTrue(TestParser.test(input, expect,261))

    def test_62(self):
        input = """
            Class Progrwefwafadaam {
                Constructor(afawf, vdfvgeb: Boolean; c: Boolean) {
                    awfwe = cafwef + 1234.234234;
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,262))

    def test_63(self):
        input = """
            Class Cdafwe23423onstruc {
                Destruc________fwef3884___________() {
                    Dawfewes.DeletefwefwAll();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,263))

    def test_64(self):
        input = """
            Class efwerweafdfewC {



                Var a: Int = funewe44c();
                Val ergserg: fgergsf = "Hewfwaefllo";
                Val werqwea,b,c: Int = 0.433539, 1234.03432;
            }
        """
        expect = "Error on line 6 col 38: ("
        self.assertTrue(TestParser.test(input, expect,264))

    def test_65(self):
        input = """
            Class Pwefwefasfrogram {
                mawefwaefin() {
                    func_decwew23423___________________lare() {



                        Return maiwefwen().twfwefqwefqwfxt();
                    }
                }
            }
        """
        expect = "Error on line 4 col 59: ("
        self.assertTrue(TestParser.test(input, expect,265))

    def test_66(self):
        input = """
            Class wefewfwf {




                Var ewfweb: Ifwefwent = wfweA::$f()[1] + afew3242_384728g * 446533 + !weqrwy;

                Var wefwqea: Stuwefwqef34234 = New Teawfeach(New Stfwefwefdsu());

                Var td: Boolean = 34 >= yf && ut <= 3242352 || 7453 == !bwef - 3324323525;
            }
        """
        expect = "Error on line 11 col 49: <="
        self.assertTrue(TestParser.test(input, expect,266))

    def test_67(self):
        input = """
            Class metfwefwefwhod {

                $getNwer2398239_______fwiui23ame() {
                    quy.t1234(Bv.$t987);
                }
            }
        """
        expect = "Error on line 5 col 33: $t987"
        self.assertTrue(TestParser.test(input, expect,267))

    def test_68(self):
        input = """
            Class Metawefeawfehod: Pafwefwafweram {
                mawfawef() {
                    awaefaw = Twefaefw::$gew_efweft() + New Xwefafw().Gawefafd() - Awefaw.bwfaf().fwefaw2113432().t___324_();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,268))

    def test_69(self):
        input = """
            Class werqwProgefwqefram {
                ____________________main() {






                    a[1][2][3][4] = b[4][3].c(d[fwerwewef1]);
                }










                method () { }
            }
        """
        expect = "Error on line 10 col 43: ."
        self.assertTrue(TestParser.test(input, expect,269))

    def test_70(self):
        input = """
            Class wqdqwdd234__________fwefE {
                $weaffwe324asdfas() {
                    Return aewrw67dfh___________________[123][332][453] + hmmmmmm.bdasf()[412];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,270))

    def test_71(self):
        input = """
            Class aafefwea___34543faf {
                mawefawfin() {

                }
            }
            Class B {
                Constructor(aewf32,b324ffw,dagsdfw4223c: Float) {
                    Return Self.aewew + gbsgdfgb + 564564;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,271))

    def test_72(self):
        input = """
            Class efwefa {
                mafwefain() {





                    Var $t: Float;
                }
            }
        """
        expect = "Error on line 9 col 24: $t"
        self.assertTrue(TestParser.test(input, expect,272))

    def test_73(self):
        input = """
            Class wefwef_q3d2p {
                sexdfer() {
                    Val _, _, _: String = 3, 4, 5;
                    Val _, _, _: String = 3, 4, 5;
                    Val _, _, _: String = 3, 4, 5;
                    Val _, _, _: String = 3, 4, 5;
                    Var aqwe, bewq, $i: Float = 1231.134120e+32178, 234.3E-123;
                }
            }
        """
        expect = "Error on line 8 col 36: $i"
        self.assertTrue(TestParser.test(input, expect,273))

    def test_74(self):
        input = """
            Class _Rqwdqweq {
                Val $_____465y: Int = 12312412;
                _Fr3fwa() {
                    Val _, __, ___: Boolean = 3342, 44231, 35459789;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,274))

    def test_75(self):
        input = """

            Class hungquynhnh {

                fff342411() {

                    tr65.fkdfjdsak() {
                    }
                }
            }
        """
        expect = "Error on line 7 col 37: {"
        self.assertTrue(TestParser.test(input, expect,275))

    def test_76(self):
        input = """
            Class qwefwe34234 {
                Var wefeewf: qfwf = New dqwdwq();
                mafwqfinStu() {
                    Stazu[19] = za.za().za().za()[za5341];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,276))

    def test_77(self):
        input = """
            Class oweyfoadnak_____________ {
                Var _______________d_______________: Array[Array[Int, 3242376], 0b0];
            }
        """
        expect = "Error on line 3 col 80: 0b0"
        self.assertTrue(TestParser.test(input, expect,277))

    def test_78(self):
        input = """
            Class fsfaewfwa {
                Var ffffffff____________: Array[String, 3] = Array(
                                            Array(3,______________,5),
                                            Array(____,2)
                                        );
                fwafdasdf() {
                    fwefa.print(________[wefadfa1][2234]);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,278))

    def test_79(self):
        input = """
            Class efewfwefsdfadf {
                Continue;
                Return;
            }
        """
        expect = "Error on line 3 col 16: Continue"
        self.assertTrue(TestParser.test(input, expect,279))

    def test_80(self):
        input = """
            Class fwafdfew {
                fwefadfadf() {
                    Foreach(a[0] In 00+04/0b0 .. b <= !c By get().count) {
                        Continue;
                    }
                }
            }
        """
        expect = "Error on line 4 col 29: ["
        self.assertTrue(TestParser.test(input, expect,280))

    def test_81(self):
        input = """
            Class dfskjf_jdss {
                Rfsfsa() {
                    Val $r: Int = 20;
                }
            }
        """
        expect = "Error on line 4 col 24: $r"
        self.assertTrue(TestParser.test(input, expect,281))

    def test_82(self):
        input = """
            Class aawefdsfsad {
                dessfrfdedad() {
                    Val fwefdfadsfaefewrerq: Array[Array[Array[Float, 00],0x3_23],4];
                }
            }
        """
        expect = "Error on line 4 col 70: 00"
        self.assertTrue(TestParser.test(input, expect,282))

    def test_83(self):
        input = """
            Class awfefdsaf {
                
                awfdfasdf() {
                    Return ewfawefefafA::$naawefawefadsme() + twefwecsdfas();
                }
            }
        """
        expect = "Error on line 5 col 74: ("
        self.assertTrue(TestParser.test(input, expect,283))
    
    def test_84(self):
        input = """
            Class testing {
                Var twe, FWE32y: Int = 1, 00;
                method(a,b,c:Int; r:Func) {
                    If (0x0 + 2_13_123.645 > 0xAAAAAAAAAAAAAAAAAAAAAAAAA) {
                        Foreach(index In 0x1 .. 12_3*45_35 By ug.gfsger(r)) {
                            If (wthtrb / rtrwtwer) {
                                If (wefwe32 >= afnewaiufbwi) {
                                    Break;
                                }
                            }
                        }
                    }
                    Elseif (tWFWA / 7_423.3243e-1231) {
                        If (!FAWEF) { }
                        Else { Return; }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,284))

    def test_85(self):
        input = """
            Class name {
                method () {
                    a = name::$age;
                    b = name::$age().b();
                    c = age;
                    d = age();
                }
            }
        """
        expect = "Error on line 7 col 27: ("
        self.assertTrue(TestParser.test(input, expect,285))

    def test86(self):
        input = """
            Class zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz {
                Var $_123a: Int = 00; 

                Mefwefwsdfthod () {
                    Self.des(a,b,c);

                    hung.dqw();

                    If (asdf[213]) {
                        Return qwdqd.fafewfawf(t); 
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,286))

    def test87(self):
        input = """
            Class _____________ {
                afawefafd () {
                    ygouygua = name::$age;
                    2dwqewqf = efwfwfwfasdfwef;
                    wefafwefafasde = $wfwwoeifjoiwaf();
                }
            }
        """
        expect = "Error on line 5 col 21: dwqewqf"
        self.assertTrue(TestParser.test(input, expect,287))

    def test88(self):
        input = """
            Class fsafdsfawef {
                Val count: Int = 0;

                fasdvnhnyj() {
                    Return Self.fwefad + Self.count(_________) - naeefwfme::$turn(_________) * fewfafe.$Age(_________);
                }
            }
        """
        expect = "Error on line 6 col 103: $Age"
        self.assertTrue(TestParser.test(input, expect,288))

    def test89(self):
        input = """
            Class sfwefwef: ________________________ {
                __s432235324___tr__(asdasfqw: Boolean) {
                    Self.____ = Self.count(___________) + __________________.$dollar();
                }
            }
        """  
        expect = "Error on line 4 col 77: $dollar"
        self.assertTrue(TestParser.test(input, expect,289))

    def test90(self):
        input = """
            Class __________________________ {
                ____________dhafiawhu32AFDSAFEAWF5342387______________() {
                    dwqudhqidhf = name[fewijidwid].fdshfaoifpppp;

                }
            }
        """
        expect = "Error on line 4 col 50: ."
        self.assertTrue(TestParser.test(input, expect,290))

    def test_91(self):
        input = """
            Class Test{

                Test(){
                    Var awdqe: Boolean= Self::ins;
                    Var b21324: Float= Self::$afwfdsfsfa;
                }
            }
        """
        expect = "Error on line 5 col 44: ::"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = """
            Class wefwef33 {
                Val bfwefassd: Int = 0x0;
                Val awefasdfa: Float = Self.ayurty.brtytr.afe2131c().t[00];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,292))

    def test_93(self):
        input = """
            Class dqwdqffr {
                __________453453() {
                    Return _____________::hufawe::$bafawef::$__________________________________.faw7efhw236182;
                }
            }
        """
        expect = "Error on line 4 col 42: hufawe"
        self.assertTrue(TestParser.test(input, expect,293))

    def test_94(self):
        input = """

            Class qwqwdqwd {


                ___________________________________() {

                    awefd = khj::$bin()[0b101011];

                    a = Main[0][1][2][1][2][1][2][1][2][1][2][1][2].get();
                }
            }
        """
        expect = "Error on line 10 col 67: ."
        self.assertTrue(TestParser.test(input, expect,294))

    def test_95(self):
        input = """
            Class myClass {
                Val a__________________738f738f7hfa: Boolean = Main.a.get(_____________________[__________._________(_____________,_______________)]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,295))

    def test_96(self):
        input = """
            
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect,296))

    def test_97(self):
        input = """
            Class _97 {
                _metht5y5464_____od() {
                    Name.a[0x0][oxo] = Self.gefwaft().swe3et.gewfwt();
                    Name.a[00][oo] = Self.gefwaft().swe3et.gewfwt();
                    Name.a[asdfhwe.fwefew(wduwe)][sdfasj.ergrgaf(__________________________________)] = Self.gefwaft().swe3et.gewfwt();
                    Name.a[uihwwef][0x0] = Self.gefwaft().swe3et.gewfwt();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,297))

    def test_98(self):
        input = """
            Class Cfwefw {
                Var ______________________b________________: _____________________A__________________________;
                wfea__weuwufhw__________5235() {
                    Return C::$fwefew + C.mcbnvb().aed[0xFECDA213];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,298))

    def test_99(self):
        input = """
            Class fewfasdf {
                $methowqfewfuykyud() {
                    Foreach(i In -323432 .. -1.213e-313421 By -3432) {
                        Foreach(j_______________________ In 00 .. -0xFF1235176 By 0b1101010101) {
                            Var fwewefa: String = 0.2e213;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect,299))

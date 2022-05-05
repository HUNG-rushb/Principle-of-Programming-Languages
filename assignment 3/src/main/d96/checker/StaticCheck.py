"""
1913652
Trịnh Duy Hưng
"""

from ast import Expression, Raise
from lib2to3.pgen2.grammar import opmap_raw
from msilib.schema import Class
from pydoc import classname
from xml.dom.expatbuilder import parseString

from attr import astuple
from matplotlib.pyplot import vlines


from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
import json

class Type:
    def NONE(self): return "<3...None"

    def INT(self): return "<3...INT"

    def FLOAT(self): return "<3...FLOAT"

    def STRING(self): return "<3...STRING"

    def BOOLEAN(self): return "<3...BOOLEAN"

    def ARRAY(self, type, size): return "<3...ARRAY" + "**" + type + "**" + str(size)

    def CLASS(self, name): return "<3...CLASS " + name

    def VOID(self): return "<3...VOID"

    def NULL(self): return "<3...NULL"

    # def NEW(self, type): return "<3...NEW" + " " + type
    def NEW(self): return "<3...NEW" 

    def SELF(self): return "<3...SELF"


class Kind:

    def STATIC(self): return "<3...STATIC"

    def INSTANCE(self): return "<3...INSTANCE"


def toJSON(data, place, typ = None) :
    if typ == 't':
        try:
            print(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            print(e)
    else:
        f = open('./main/d96/checker/' + place + '.json', 'w', encoding='utf-8')
        try:
            f.write(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            f.write(e)
        finally:
            f.close()

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

#  ! ██████  ██       ██████  ██████   █████  ██      
# ! ██       ██      ██    ██ ██   ██ ██   ██ ██      
# ! ██   ███ ██      ██    ██ ██████  ███████ ██      
# ! ██    ██ ██      ██    ██ ██   ██ ██   ██ ██      
# !  ██████  ███████  ██████  ██████  ██   ██ ███████
class GlobalScope(BaseVisitor, Utils):
    def visitProgram(self, ast: Program, classStore):
        for decl in ast.decl:
            self.visit(decl, classStore)
        
        # return classStore

    # newEnviroment = {
    #     'overall' : classStore,
    #     'class' : classStore[className]
    # }

    def visitClassDecl(self, ast: ClassDecl, classStore):
        className = ast.classname.name

        if className in classStore:
            raise Redeclared(Class(), className)
        
        memList = ast.memlist
        
        if ast.parentname != None:
            parentName = ast.parentname.name

            # 'overall': {'A': {'parent': '', 
            # 'attributes': {'a': {'type': '<3...INT', 'value': None, 'init': '<3...INT', 'const': False, 'kind': '<3...INSTANCE'}}, 
            # 'methods': {}}}
            if parentName not in classStore:
                raise Undeclared(Class(), parentName)
        else:
            parentName = ''

        classStore[className] = {
            'parent': parentName,
            'attributes': {},
            'methods': {}
        }

        newClassEnviroment = {
            'overall' : classStore,
            'class' : classStore[className]
        }

        for mem in memList:
            self.visit(mem, newClassEnviroment)
        
        # 2.11 No entry point
        # if ('Program' not in classStore) or ('main' not in classStore['Program']):
        #     raise NoEntryPoint()
        # elif :


  
    # kind: SIKind  # Instance or Static
    # decl: StoreDecl  # VarDecl for mutable or ConstDecl for immutable
    def visitAttributeDecl(self, ast: AttributeDecl, classStore):
        self.visit(ast.decl, classStore)

    # variable: Id
    # varType: Type
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast: VarDecl, classStore):
        varName = ast.variable.name
        
        # Attribute of Class's scope
        # if "class" in classStore[]:
        if classStore["class"] is not None and len(classStore) == 2:
            if varName in classStore['class']["attributes"]:
                raise Redeclared(Attribute(), varName) 
            
            varType = self.visit(ast.varType, classStore)
            varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()

            if ast.varInit is None:
                varInit = None
            else:
                varInit = self.visit(ast.varInit, classStore)
                
                if varInit != varType:
                    if varType == Type().FLOAT() and varInit == Type().INT():
                        varInit = Type().FLOAT()
                    else:
                        raise TypeMismatchInStatement(ast)

            classStore['class']["attributes"][varName] = {
                'type': varType,
                # 'value': None,
                'init': varInit,
                'const': False,
                'kind': varKind,
            }

        # Variable in method's scope
        # elif "method" in classStore:
        elif classStore["method"] is not None and len(classStore) == 4:
            # if varName in classStore['body']['variables']:
            if varName in classStore['body'][0]:
                raise Redeclared(Variable(), varName)

            varType = self.visit(ast.varType, classStore)
            varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()
            
            if ast.varInit is None:
                varInit = None
            else:
                varInit = self.visit(ast.varInit, classStore)
                
                if varInit != varType:
                    if varType == Type().FLOAT() and varInit == Type().INT():
                        varInit = Type().FLOAT()
                    else:
                        raise TypeMismatchInStatement(ast)

            # classStore['body']['variables'][varName] = {
            classStore['body'][0][varName] = {
                'type': varType,
                # 'value': None,
                'init': varInit,
                'const': False,
                'kind': varKind,
            }


    # constant: Id
    # constType: Type
    # value: Expr = None # None if there is no initial
    def visitConstDecl(self, ast: ConstDecl, classStore):
        varName = ast.constant.name
        
        # Attribute of Class's scope
        # if "class" in classStore[]:
        if classStore["class"] is not None and len(classStore) == 2:
            if varName in classStore['class']["attributes"]:
                raise Redeclared(Constant(), varName)

            varType = self.visit(ast.constType, classStore)
            varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()

            if ast.value == None:
                raise IllegalConstantExpression(ast.value)
            else:
                varInit = self.visit(ast.value, classStore)

                if varInit != varType:
                    if varType == Type().FLOAT() and varInit == Type().INT():
                        varInit = Type().FLOAT()
                    else:
                        raise TypeMismatchInConstant(ast) 

            classStore['class']["attributes"][varName] = {
                'type': varType,
                # 'value': None,
                'init': varInit,
                'const': True,
                'kind': varKind,
            }
        
         # Variable in method's scope
         # elif "method" in classStore:
        elif classStore["method"] is not None and len(classStore) == 4:
            # if varName in classStore['body']['variables']:
            if varName in classStore['body'][0]:
                raise Redeclared(Constant(), varName)

            varType = self.visit(ast.constType, classStore)
            varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()

            if ast.value == None:
                raise IllegalConstantExpression(ast.value)
            else:
                varInit = self.visit(ast.value, classStore)

                if varInit != varType:
                    if varType == Type().FLOAT() and varInit == Type().INT():
                        varInit = Type().FLOAT()
                    else:
                        raise TypeMismatchInConstant(ast) 

            # classStore['body']['variables'][varName] = {
            classStore['body'][0][varName] = {
                'type': varType,
                # 'value': None,
                'init': varInit,
                'const': True,
                'kind': varKind,
            }



    # kind: SIKind
    # name: Id
    # param: List[VarDecl]
    # body: Block
    def visitMethodDecl(self, ast: MethodDecl, classStore):
        methodName = ast.name.name

        if methodName in classStore['class']["methods"]:
            raise Redeclared(Method(), methodName)

        methodKind = Kind().STATIC() if methodName[0] == '$' else Kind().INSTANCE()
        methodParams = ast.param
        # methodBody = ast.body

        classStore['class']['methods'][methodName] = {
            'type': Type().VOID(),
            'kind': methodKind,
            # 'body': {
            #     "variables": {}
            # },
            'body': [],
            'params': {}
        }

        # Visit Params 
        newMethodEnviroment = {
            'overall' : classStore['overall'],
            'class' : classStore['class'],
            'method': classStore['class']['methods'][methodName]['params']
        }

        for param in methodParams:
            self.visitParam(param, newMethodEnviroment)

        # Visit Block 
        newMethodEnviromentBlock = {
            'overall' : classStore['overall'],
            'class' : classStore['class'],
            'method': classStore['class']['methods'][methodName]['params'],
            'body': classStore['class']['methods'][methodName]['body']
        }

        self.visit(ast.body, newMethodEnviromentBlock)

    # param: List[VarDecl]

    # variable: Id
    # varType: Type
    # varInit: Expr = None  # None if there is no initial
    def visitParam(self, ast: VarDecl, classStore):
        varName = ast.variable.name

        if varName in classStore["method"]:
            raise Redeclared(Variable(), varName)

        varType = self.visit(ast.varType, classStore)
        varKind = Kind().INSTANCE()

        classStore['method'][varName] = {
            'type': varType,
            # 'value': None,
            'const': False,
            'kind': varKind
        }


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    # ! inst: List[Inst]
    def visitBlock(self, ast: Block, classStore):
        blockInst = ast.inst
        
        classStore["body"].insert(0, {})

        for inst in blockInst:
            self.visit(inst, classStore)
    

    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast: BinaryOp, classStore):
        operand = ast.op
        left = self.visit(ast.left, classStore)
        right = self.visit(ast.right, classStore)

        if operand in ["+", "-", "*", "/", "%"]:
            if (left == Type().INT() or left[0] == Type().INT()) \
                and (right == Type().INT() or right[0] == Type().INT()):
                return Type().INT()
            elif (left == Type().FLOAT() or left == Type().INT() or left[0] == Type().FLOAT() or left[0] == Type().INT()) \
                and (right == Type().FLOAT() or right == Type().INT() or right[0] == Type().FLOAT() or right[0] == Type().INT()):

                if operand == "%" and (left == Type().FLOAT() or right == Type().FLOAT() \
                     or left[0] == Type().FLOAT() or right[0] == Type().FLOAT()):
                    raise TypeMismatchInExpression(ast)
                else:
                    return Type().FLOAT()
            else:
                raise TypeMismatchInExpression(ast)

        # 5.2 và 5.3
        elif operand in ["&&", "||", "==.", "+."]: 
            if ((left == Type().BOOLEAN() or left[0] == Type().BOOLEAN())\
                 and (right == Type().BOOLEAN() or right[0] == Type().BOOLEAN()) and operand in ["&&", "||"]) \
                    or ((left == Type().STRING() or left == Type().STRING()) \
                        and (right == Type().STRING() or right[0] == Type().STRING()) and operand in ["==.", "+."]):
                print(1234)
                return Type().BOOLEAN()
            else:
                raise TypeMismatchInExpression(ast)
                
        elif operand in ["==", "!=", ">", "<", "<=", ">="]:
            if ((left == Type().INT() or left[0] == Type().INT()) and (right == Type().INT() or right[0] == Type().INT())) \
                or ((left == Type().BOOLEAN() or left[0] == Type().BOOLEAN()) and (right == Type().BOOLEAN() or right[0] == Type().BOOLEAN()) and operand in ["==", "!="]) \
                or ((left == Type().FLOAT() or left[0] == Type().FLOAT()) and (right == Type().FLOAT() or right[0] == Type().FLOAT()) and operand in [">", "<", "<=", ">="]):
                return Type().BOOLEAN()
            else:
                raise TypeMismatchInExpression(ast)


    # op: str
    # body: Expr
    def visitUnaryOp(self, ast: UnaryOp, classStore):
        operand = ast.op
        body = self.visit(ast.body, classStore)

        if operand == '!' and (body == Type().BOOLEAN() or body[0] == Type().BOOLEAN()):
            return Type().BOOLEAN()
        elif operand == '-' and (body != Type().INT() or body[0] != Type().INT()) \
            and (body != Type().FLOAT() or body[0] != Type().FLOAT()):
            if body == Type().INT():
                return Type().INT()
            else:
                return Type().FLOAT()
        else:
            raise TypeMismatchInExpression(ast)

    


    #     name: str
    def visitId(self, ast: Id, classStore):
        name = ast.name

        # if "class" in classStore[]:
        if classStore["class"] is not None and len(classStore) == 2:
            # print(12340000)
            if name not in classStore["class"]["attributes"]:
                raise Undeclared(Attribute(), name)

            return (classStore["class"]["attributes"][name]["type"], classStore["class"]["attributes"][name]["const"])

        # elif "method" in classStore:
        elif classStore["method"] is not None and len(classStore) == 4:
            # print(1234)
            if name in classStore["class"]["attributes"]:
                # print(12312000)
                return (classStore["class"]["attributes"][name]["type"], classStore["class"]["attributes"][name]["const"])
            # elif name in classStore["body"]["variables"]:
            else:
                found = False
                for scope in classStore["body"]:
                    if name in scope:
                        found = True
                        return (scope[name]["type"], scope[name]["const"])

                if found == False:
                    raise Undeclared(Variable(), name)

        # elif "method" in classStore:
        # elif classStore["for_***"] is not None and len(classStore) > 4:
        # # elif "for_***" in classStore:
        #     print(123987981473198)
        elif classStore["if_***"] is not None and len(classStore) > 4:
        # elif "for_***" in classStore:
            print(123987981473198)



       
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ast: Assign, classStore):
        print(123123)
        LHS = self.visit(ast.lhs, classStore)

        # LHS is const 
        if hasattr(ast.lhs, 'name') and LHS[1] == True:
            raise CannotAssignToConstant(ast)

        expr = self.visit(ast.exp, classStore)

        if LHS != expr:
            raise TypeMismatchInStatement(ast)

    # !!!!!!!!!!!!!!!!!!!!!!!!!
    # expr: Expr
    # thenStmt: Stmt
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast: If, classStore):
        # classStore['if_***'] = classStore["body"]

        ifExpr = self.visit(ast.expr, classStore)
        
        if hasattr(ast.expr, 'name'): 
            if ifExpr[0] != Type().BOOLEAN():
                raise TypeMismatchInExpression(ast.expr)
        else:
            if ifExpr != Type().BOOLEAN():
                raise TypeMismatchInExpression(ast.expr)

        # if ifExpr != Type().BOOLEAN() or ifExpr[0] != Type().BOOLEAN():
        #     raise TypeMismatchInExpression(ast.expr)

        # ifThen = self.visit(ast.thenStmt, classStore)
        self.visit(ast.thenStmt, classStore)

        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, classStore)

        
        

    # !!!!!!!!!!!!!!!!!!!!!!!!!
    # id: Id
    # expr1: Expr
    # expr2: Expr 
    # loop: Stmt
    # expr3: Expr = None
    def visitFor(self, ast: For, classStore):
        # print(classStore)
        iterName = ast.id.name

        found = False
        for scope in classStore["body"]:
            if iterName in scope:
                found = True
        if found == False:
            raise Undeclared(Variable(), iterName)

        expression_1 = self.visit(ast.expr1, classStore)
        expression_2 = self.visit(ast.expr2, classStore)
        expression_3 = Type().INT() if ast.expr3 == None else self.visit(ast.expr3, classStore)

        if hasattr(ast.expr1, "name"):
            if expression_1[0] != Type().INT():
                print(213123)
                raise TypeMismatchInStatement(ast)
        else:
            if expression_1 != Type().INT():
                print(11111)
                raise TypeMismatchInStatement(ast)

        if hasattr(ast.expr2, "name"):
            if expression_2[0] != Type().INT():
                print(3)
                raise TypeMismatchInStatement(ast)
        else:
            if expression_2 != Type().INT():
                print(4)
                raise TypeMismatchInStatement(ast)

        if hasattr(ast.expr3, "name") and ast.expr3 != None:
            if expression_3[0] != Type().INT():
                raise TypeMismatchInStatement(ast)
        else:
            if expression_3 != Type().INT():
                raise TypeMismatchInStatement(ast)

        loopStmt = self.visit(ast.loop, classStore)
        




    def visitBreak(self, ast: Break, classStore):
        print(classStore)
        if 'for' in classStore:
            pass
        else:
            raise MustInLoop(ast)

    def visitContinue(self, ast: Continue, classStore):
        if 'for' in classStore:
            pass
        else:
            raise MustInLoop(ast)

    # expr: Expr = None
    def visitReturn(self, ast: Return, classStore):
        expression = self.visit(ast.expr, classStore)
        return expression

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # obj: Expr
    # method: Id
    # param: List[Expr]
    # dog.bark()
    def visitCallStmt(self, ast: CallStmt, classStore):
        objCall = self.visit(ast.obj, classStore)
        methodCall = self.visit(ast.method, classStore)
        paramCall = self.visit(ast.param, classStore)
        print(12313)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # obj: Expr
    # method: Id
    # param: List[Expr]
    def visitCallExpr(self, ast: CallExpr, classStore):
        print(33428)
        














    # classname: Id
    # param: List[Expr]
    def visitNewExpr(self, ast: NewExpr, classStore):
        className = ast.classname.name

        if className not in classStore['overall']:
            raise Undeclared(Class(), className)

        if "Constructor" not in classStore['overall'][className]["methods"]:
            raise Undeclared(SpecialMethod(), "Constructor")

        methodParams = ast.param
        listCopyConstrutorParams =  list(classStore['overall'][className]["methods"]["Constructor"]["params"])

        if len(methodParams) != len(listCopyConstrutorParams):
            raise TypeMismatchInExpression(ast)

        i = 0
        for param in methodParams:
            current = listCopyConstrutorParams[i]

            # Param is ID 
            if hasattr(param, "name"):
                if self.visit(param, classStore)[0] != classStore['overall'][className]["methods"]["Constructor"]["params"][current]["type"]:
                    # print(797889)
                    raise TypeMismatchInExpression(ast)
            # Param is literal 
            elif self.visit(param, classStore) != classStore['overall'][className]["methods"]["Constructor"]["params"][current]["type"]:
                    raise TypeMismatchInExpression(ast)
            i += 1

        # return Type().NEW()
        return Type().CLASS(className)


    

    


    

            
         
    def visitIntLiteral(self, ast: IntLiteral, classStore):
        return Type().INT()

    def visitFloatLiteral(self, ast: FloatLiteral, classStore):
        return Type().FLOAT()

    def visitStringLiteral(self, ast: StringLiteral, classStore):
        return Type().STRING()

    def visitBooleanLiteral(self, ast: BooleanLiteral, classStore):
        return Type().BOOLEAN()

    def visitNullLiteral(self, ast: NullLiteral, classStore):
        return Type().NULL()
        
    def visitSelfLiteral(self, ast: SelfLiteral, classStore):
        return Type().SELF()

    # ! value: List[Expr]
    # ! value: List[Expr]
    # ! value: List[Expr]
    def visitArrayLiteral(self, ast: ArrayLiteral, classStore):
        arrayValue = ast.value
        arraySize = len(arrayValue)
 
        if arraySize == 0:
            return "<3...ARRAY"

        elif arraySize > 0:
            temp = self.visit(arrayValue[0], classStore)
            for value in arrayValue:
                current = self.visit(value, classStore)

                if temp != current:
                    raise IllegalArrayLiteral(ast)
            
            return Type().ARRAY(temp, arraySize)

    

    def visitClassType(self, ast: ClassType, classStore):
        className = ast.classname.name

        if className not in classStore['overall']:
            raise Undeclared(Class(), className)
        
        return Type().CLASS(className)
        

        
    def visitIntType(self, ast: IntType, classStore):
        return Type().INT()

    def visitFloatType(self, ast: FloatType, classStore):
        return Type().FLOAT()

    def visitBoolType(self, ast: BoolType, classStore):
        return Type().BOOLEAN()

    def visitStringType(self, ast: StringType, classStore):
        return Type().STRING()

    # size: int
    # eleType: Type
    def visitArrayType(self, ast: ArrayType, classStore):
        arrayType = self.visit(ast.eleType, classStore)
        arraySize = ast.size

        return Type().ARRAY(arrayType, arraySize)

    def visitVoidType(self, ast: VoidType, classStore):
        return Type().VOID()

# ! ██ ███    ██ ██ ████████ 
# ! ██ ████   ██ ██    ██    
# ! ██ ██ ██  ██ ██    ██    
# ! ██ ██  ██ ██ ██    ██    
# ! ██ ██   ████ ██    ██   


# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# ! ██      ███████ █████   ██      █████   █████   ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)


#   decl: List[ClassDecl]
    def visitProgram(self, ast: Program, classStore):
        classStore = {}
        # classStore2 = {}
        # print(ast.decl)

        # classStore = GlobalScope().visitProgram(ast, classStore)
        GlobalScope().visitProgram(ast, classStore)
        toJSON(classStore, 'global_scope')

        # classStore = ValidateInit().visitProgram(ast, classStore)
        # toJSON(classStore, 'validate_init')
        # return []

        # for decl in ast.decl:
        #     self.visit(decl, classStore)
        return []

#     classname: Id
#     memlist: List[MemDecl]
#     parentname: Id = None
    def visitClassDecl(self, ast: ClassDecl, classStore):
        className = self.visit(ast.classname, classStore)

        


#     name: str
    def visitId(self, ast: Id, classStore):
        #  return {'name':ast.name, "type":Type.UNDEFINE}
         return 
        
        
        

       
    

    def visitBinaryOp(self, ast: BinaryOp, classStore):
        return None

    def visitUnaryOp(self, ast: UnaryOp, classStore):
        return None

    def visitCallExpr(self, ast: CallExpr, classStore):
        return None

    def visitNewExpr(self, ast: NewExpr, classStore):
        return None

    def visitArrayCell(self, ast: ArrayCell, classStore):
        return None

    def visitFieldAccess(self, ast: FieldAccess, classStore):
        return None

    def visitFloatLiteral(self, ast: FloatLiteral, classStore):
        return None

    def visitStringLiteral(self, ast: StringLiteral, classStore):
        return None

    def visitBooleanLiteral(self, ast: BooleanLiteral, classStore):
        return None

    def visitNullLiteral(self, ast: NullLiteral, classStore):
        return None

    def visitSelfLiteral(self, ast: SelfLiteral, classStore):
        return None

    def visitArrayLiteral(self, ast: ArrayLiteral, classStore):
        return None

    def visitVarDecl(self, ast: VarDecl, classStore):
        return None


    def visitAssign(self, ast: Assign, classStore):
        return None

    def visitIf(self, ast: If, classStore):
        return None

    def visitFor(self, ast: For, classStore):
        return None

    def visitBreak(self, ast: Break, classStore):
        return None

    def visitContinue(self, ast: Continue, classStore):
        return None

    def visitReturn(self, ast: Return, classStore):
        return None

    def visitCallStmt(self, ast: CallStmt, classStore):
        return None


    def visitBlock(self, ast: Block, classStore):
        return None

    def visitConstDecl(self, ast: ConstDecl, classStore):
        return None

    def visitInstance(self, ast: Instance, classStore):
        return None

    def visitBlock(self, ast: Block, classStore):
        return None

    def visitStatic(self, ast: Static, classStore):
        return None

    def visitMethodDecl(self, ast: MethodDecl, classStore):
        return None

    def visitAttributeDecl(self, ast: AttributeDecl, classStore):
        return None

    def visitClassType(self, ast: ClassType, classStore):
        return None
        
    # Primitive Type 
    def visitIntType(self, ast: IntType, classStore):
        return Type.INT

    def visitFloatType(self, ast: FloatType, classStore):
        return Type.FLOAT

    def visitBoolType(self, ast: BoolType, classStore):
        return Type.BOOLEAN

    def visitStringType(self, ast: StringType, classStore):
        return Type.STRING

    def visitArrayType(self, ast: ArrayType, classStore):
        return Type.ARRAY

    def visitVoidType(self, ast: VoidType, classStore):
        return Type.VOID


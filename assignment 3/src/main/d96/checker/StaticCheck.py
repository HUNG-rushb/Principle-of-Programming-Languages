"""
1913652
Trịnh Duy Hưng
"""

from msilib.schema import Class
from pydoc import classname

from numpy import var
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


# from enum import Enum
import json

# class Type(Enum):
#     UNDEFINE = 0
#     INT = 1
#     FLOAT = 2
#     BOOLEAN = 3
#     STRING = 4
#     ARRAY = 5
#     CLASS = 6
#     VOID = 7

# class Kind(Enum):
#     STATIC = 0
#     INSTANCE = 1

class Type:

    def NONE(self): return "<3...None"

    def INT(self): return "<3...INT"

    def FLOAT(self): return "<3...FLOAT"

    def STRING(self): return "<3...STRING"

    def BOOLEAN(self): return "<3...BOOLEAN"

    def ARRAY(self, type, size): return "<3...ARRAY" + " " + type + " " + str(size)

    def CLASS(self, name): return "<3...CLASS " + name

    def VOID(self): return "<3...VOID"

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
        
        return classStore

    def visitClassDecl(self, ast: ClassDecl, classStore):
        className = ast.classname.name

        if className in classStore:
            raise Redeclared(Class(), className)
        

        memList = ast.memlist
        
        if ast.parentname != None:
            parentName = ast.parentname.name

            if parentName not in classStore:
                raise Undeclared(Class(), parentName)
        else:
            parentName = ''

        classStore[className] = {
            'parent': parentName,
            'attributes': {},
            'methods': {}
        }

        for mem in memList:
            self.visit(mem, classStore[className])
        
        # 2.11 No entry point
        # if ('Program' not in classStore) or ('main' not in classStore['Program']):
        #     raise NoEntryPoint()
        # elif :


  

    def visitAttributeDecl(self, ast: AttributeDecl, classStore):
        # self.visit(ast.decl, classStore['attributes'], "attr")
        self.visit(ast.decl, classStore['attributes'])

    # variable: Id
    # varType: Type
    # varInit: Expr = None  # None if there is no initial
    # def visitVarDecl(self, ast: VarDecl, classStore, typeP):
    def visitVarDecl(self, ast: VarDecl, classStore):
        varName = ast.variable.name

        if varName in classStore:
            # raise Redeclared(Attribute(), varName) if typeP == "attr" else Redeclared(Variable(), varName)
            raise Redeclared(Attribute(), varName) 

        varType = self.visit(ast.varType, classStore)
        varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()

        if ast.varInit == None:
            varInit = None
        else:
            varInit = self.visit(ast.varInit, classStore)

        classStore[varName] = {
            'type': varType,
            'value': None,
            'init': varInit,
            'const': False,
            'kind': varKind,
        }

    # constant: Id
    # constType: Type
    # value: Expr = None # None if there is no initial
    def visitConstDecl(self, ast: ConstDecl, classStore):
        varName = ast.constant.name
        
        if varName in classStore:
            raise Redeclared(Constant(), varName)

        varType = self.visit(ast.constType, classStore)
        varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()

        if ast.value == None:
            varInit = None
        else:
            varInit = self.visit(ast.value, classStore)

        classStore[varName] = {
            'type': varType,
            'value': None,
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

        if methodName in classStore:
            raise Redeclared(Method(), methodName)

        methodKind = Kind().STATIC() if methodName[0] == '$' else Kind().INSTANCE()
        methodParams = ast.param

        classStore['methods'][methodName] = {
            'type': Type().VOID(),
            'kind': methodKind,
            'body': [{}],
            'params': {}
        }

        for param in methodParams:
            self.visitParam(param, classStore['methods'][methodName]['params'])

    def visitParam(self, ast: VarDecl, classStore):
        varName = ast.variable.name
        varType = self.visit(ast.varType, classStore)
        varKind = Kind().INSTANCE()

        classStore[varName] = {
            'type': varType,
            'value': None,
            'const': False,
            'kind': varKind
        }


    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast: BinaryOp, classStore):
        # operand = ast.op
        left = self.visit(ast.left, classStore)
        right = self.visit(ast.right, classStore)

        if left == Type().INT() and right == Type().INT():
            return Type().INT()
        elif left == Type().FLOAT() and right == Type().FLOAT():
            return Type().FLOAT()
        

    # op: str
    # body: Expr
    def visitUnaryOp(self, ast: UnaryOp, classStore):
        # operand = ast.op
        body = self.visit(ast.body, classStore)

        if body == Type().INT():
            return Type().INT()
        elif body == Type().FLOAT():
            return Type().FLOAT()


    def visitIntLiteral(self, ast: IntLiteral, classStore):
        return Type().INT()

    def visitFloatLiteral(self, ast: FloatLiteral, classStore):
        return Type().FLOAT()

    def visitStringLiteral(self, ast: StringLiteral, classStore):
        return Type().STRING()

    def visitBooleanLiteral(self, ast: BooleanLiteral, classStore):
        return Type().BOOLEAN()

    def visitSelfLiteral(self, ast: SelfLiteral, classStore):
        return Type().SELF()

    def visitArrayLiteral(self, ast: ArrayLiteral, classStore):
        return Type().ARRAY()

    

    def visitClassType(self, ast: ClassType, classStore):
        return Type().CLASS(ast.classname.name)
        
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
class ValidateInit(BaseVisitor, Utils):
    def visitProgram(self, ast: Program, classStore):
        for decl in ast.decl:
            self.visit(decl, classStore)
        
        return classStore

    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None  # None if there is no parent
    def visitClassDecl(self, ast: ClassDecl, classStore):
        className = ast.classname.name
        memList = ast.memlist
        
        for mem in memList:
            self.visit(mem, classStore[className])

    def visitAttributeDecl(self, ast: AttributeDecl, classStore):
        self.visit(ast.decl, classStore['attributes'])

    # variable: Id
    # varType: Type
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast: VarDecl, classStore):
        varName = ast.variable.name

        if ast.varInit == None:
            return
        else:
            varInit = self.visit(ast.varInit, classStore)

        classStore[varName].update({
            'init': varInit
        })

    # constant: Id
    # constType: Type
    # value: Expr = None # None if there is no initial
    def visitConstDecl(self, ast: ConstDecl, classStore):
        constName = ast.constant.name

        if ast.value == None:
            return
        else:
            constInit = self.visit(ast.value, classStore)

        classStore[constName].update({
            'init': constInit
        })

    # def visitMethodDecl(self, ast: MethodDecl, classStore):
    #     return None

    # def visitParam(self, ast: VarDecl, classStore):
    #     return None


    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast: BinaryOp, classStore):
        # operand = ast.op
        left = self.visit(ast.left, classStore)
        right = self.visit(ast.right, classStore)

        if left == Type.INT() and right == Type.INT():
            print(123)
            return Type.INT()
        

    # op: str
    # body: Expr
    def visitUnaryOp(self, ast: UnaryOp, classStore):
        operand = ast.op
        body = self.visit(ast.body, classStore)

        return None

    def visitCallExpr(self, ast: CallExpr, classStore):
        return None

    def visitNewExpr(self, ast: NewExpr, classStore):
        return None





    def visitArrayCell(self, ast: ArrayCell, classStore):
        return None

    def visitFieldAccess(self, ast: FieldAccess, classStore):
        return None





    def visitIntLiteral(self, ast: IntLiteral, classStore):
        print("\n", 123, "\n")
        return Type().INT()

    def visitFloatLiteral(self, ast: FloatLiteral, classStore):
        return Type().FLOAT()

    def visitStringLiteral(self, ast: StringLiteral, classStore):
        return Type().STRING()

    def visitBooleanLiteral(self, ast: BooleanLiteral, classStore):
        return Type().BOOLEAN()

    def visitSelfLiteral(self, ast: SelfLiteral, classStore):
        return Type().SELF()

    def visitArrayLiteral(self, ast: ArrayLiteral, classStore):
        return Type().ARRAY()

    


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

   

    def visitInstance(self, ast: Instance, classStore):
        return None

    def visitBlock(self, ast: Block, classStore):
        return None

    def visitStatic(self, ast: Static, classStore):
        return None


    def visitClassType(self, ast: ClassType, classStore):
        return Type().CLASS(ast.classname.name)

    # Primitive Type 
    def visitIntType(self, ast: IntType, classStore):
        return Type().INT()

    def visitFloatType(self, ast: FloatType, classStore):
        return Type().FLOAT()

    def visitBoolType(self, ast: BoolType, classStore):
        return Type().BOOLEAN()

    def visitStringType(self, ast: StringType, classStore):
        return Type().STRING()

    def visitArrayType(self, ast: ArrayType, classStore):
        return Type().ARRAY()

    def visitVoidType(self, ast: VoidType, classStore):
        return Type().VOID()

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

        classStore = GlobalScope().visitProgram(ast, classStore)
        toJSON(classStore, 'global_scope')

        # classStore = ValidateInit().visitProgram(ast, classStore)
        # toJSON(classStore, 'validate_init')
        # return []

        # for decl in ast.decl:
        #     self.visit(decl, classStore)

#     classname: Id
#     memlist: List[MemDecl]
#     parentname: Id = None
    def visitClassDecl(self, ast: ClassDecl, classStore):
        className = self.visit(ast.classname, classStore)

        # attrDecl = []
        # methodDecl = []
        # for mem in ast.memlist:
        #     if isinstance(mem, AttributeDecl):
        #         attrDecl.append(mem)
        #     else:
        #         methodDecl.append(mem)

        if ast.parentname != None:
            parentName = self.visit(ast.parentname, classStore)
            # print(parentName)
        else:
            parentName = None
        # -----------------------------------------------------------------
        # First ever class can not have inheritance
        if len(classStore) == 0 and parentName != None:
            raise Undeclared(Class(), parentName["name"])
        
        # Store not empty
        elif len(classStore) > 0:

            # Loop through store and check name 
            for current_classDecl in classStore:
                if current_classDecl['ClassName'] == className["name"]:
                    raise Redeclared(Class(), className["name"])

       
        newClass = {}
        newClass['ClassName'] = className['name']
        newClass['Attributes'] = []
        newClass['Methos'] = []

        classStore.insert(0, newClass)


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


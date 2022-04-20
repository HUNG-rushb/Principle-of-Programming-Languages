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


from enum import Enum
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

    def INT(self): return "<3...INT"

    def FLOAT(self): return "<3...FLOAT"

    def STRING(self): return "<3...STRING"

    def BOOLEAN(self): return "<3...BOOLEAN"

    def ARRAY(self): return "<3...ARRAY"

    def CLASS(self): return "<3...CLASS"

    def VOID(self): return "<3...VOID"


class Kind:

    def STATIC(self): return "<3...STATIC"

    def INSTANCE(self): return "<3...INSTANCE"


def toJSON(data, typ = None):
    if typ == 't':
        try:
            print(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            print(e)
    else:
        f = open('./main/d96/checker/param.json', 'w', encoding='utf-8')
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


# {
#     "super": {
#         "parent": "",
#         "attribute": {
#             "$s": {
#                 "type": "<FLOAT>",
#                 "init": null,
#                 "const": false,
#                 "kind": "<STATIC>"
#             }
#         },
#         "method": {}
#     },
#     "A": {
#         "parent": "",
#         "attribute": {
#             "z": {
#                 "type": "<INT>",
#                 "init": "<INT>",
#                 "const": false,
#                 "kind": "<INSTANCE>"
#             }
#         },
#         "method": {
#             "getA": {
#                 "type": "<VOID>",
#                 "kind": "<INSTANCE>",
#                 "body": [
#                     {
#                         "a": {
#                             "type": "<INT>",
#                             "kind": "<INSTANCE>",
#                             "init": null,
#                             "const": false
#                         },
#                         "t": {
#                             "type": "<CLASS>(super)",
#                             "kind": "<INSTANCE>",
#                             "const": false,
#                             "init": "<NULL>"
#                         },
#                         "b": {
#                             "type": "<FLOAT>",
#                             "kind": "<INSTANCE>",
#                             "const": false,
#                             "init": "<FLOAT>"
#                         }
#                     }
#                 ],
#                 "param": {
#                     "a": {
#                         "type": "<INT>",
#                         "kind": "<INSTANCE>",
#                         "init": null,
#                         "const": false
#                     },
#                     "b": {
#                         "type": "<INT>",
#                         "kind": "<INSTANCE>",
#                         "init": null,
#                         "const": false
#                     }
#                 }
#             }
#         }
#     }
# }
class GlobalScope(BaseVisitor, Utils):

#   decl: List[ClassDecl]
    def visitProgram(self, ast: Program, classStore):
        for decl in ast.decl:
            self.visit(decl, classStore)
        
        return classStore

#     classname: Id
#     memlist: List[MemDecl]
#     parentname: Id = None
    def visitClassDecl(self, ast: ClassDecl, classStore):
        className = ast.classname.name
        memList = ast.memlist
        
        if ast.parentname != None:
            parentName = ast.parentname.name
        else:
            parentName = ''

        classStore[className] = {
            'parent': parentName,
            'attributes': {},
            'methods': {}
        }

        for mem in memList:
            self.visit(mem, classStore[className])



    def visitMethodDecl(self, ast: MethodDecl, classStore):
        methodName = ast.name.name
        methodKind = self.visit(ast.kind, classStore)
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



    def visitAttributeDecl(self, ast: AttributeDecl, classStore):
        self.visit(ast.decl, classStore['attributes'])

    def visitVarDecl(self, ast: VarDecl, classStore):
        varName = ast.variable.name
        varType = self.visit(ast.varType, classStore)
        varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()

        classStore[varName] = {
            'type': varType,
            'value': None,
            'const': False,
            'kind': varKind
        }

    # constant: Id
    # constType: Type
    # value: Expr = None # None if there is no initial
    def visitConstDecl(self, ast: ConstDecl, classStore):
        varName = ast.constant.name
        varType = self.visit(ast.constType, classStore)
        varKind = Kind().STATIC() if varName[0] == '$' else Kind().INSTANCE()

        classStore[varName] = {
            'type': varType,
            'value': None,
            'const': True,
            'kind': varKind
        }



#     name: str
    def visitId(self, ast: Id, classStore):
        #  return {'name':ast.name, "type":Type.UNDEFINE}
         return 
        
        
        

       
    def visitClassType(self, ast: ClassType, classStore):
        return None

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








# [
# 	{
# 		"className": <classname>
# 		"attributes": [
# 			{"a": int}
# 			{"b": float}
# 			{"c": string}
# 		]
# 		"methods": [
# 			{
# 				"methodname": <methodName>
# 				"type": Method || SpecialMethod
# 				"params": [
# 					{<paramName>: <type>}
# 				]
# 				"body": [
# 					{<variableName>: <type>}
# 				]
# 			}
# 		]
# 	}
# ]


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
        # print(ast.decl)

        classStore = GlobalScope().visitProgram(ast, classStore)
        toJSON(classStore)

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
        
        
        

       
    def visitClassType(self, ast: ClassType, classStore):
        return None

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

#     def visitFuncDecl(self, ast, c):
#         return None list(map(lambda x: self.visit(x, (c, True)), ast.body.stmt))
#
#     def visitCallExpr(self, ast, c):
#         at = [self.visit(x, (c[0], False)) for x in ast.param]
#
#         res = self.lookup(ast.method.name, c[0], lambda x: x.name)
#         if res is None or not type(res.mtype) is MType:
#             raise Undeclared(Function(), ast.method.name)
#         elif len(res.mtype.partype) != len(at):
#             if c[1]:
#                 raise TypeMismatchInStatement(ast)
#             else:
#                 raise TypeMismatchInExpression(ast)
#         else:
#             return None res.mtype.rettype
#
#     def visitIntLiteral(self, ast, c):
#         return None IntType()


# if ast.parentname == None:
#             self.visit(ast.classname, classStore)
#             for memdecl in ast.memlist:
#                 self.visit(memdecl, classStore)
#         else:
#             if parentName == classname:
#                 raise Redeclared(Class(), classname)
#             else:
#                 print('...')
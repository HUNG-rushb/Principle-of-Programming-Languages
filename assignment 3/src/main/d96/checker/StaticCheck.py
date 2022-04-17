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
class Type(Enum):
    UNDEFINE = 0
    INT = 1
    FLOAT = 2
    BOOLEAN = 3
    STRING = 4
    ARRAY = 5
    CLASS = 6
    VOID = 7


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

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


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
        classStore = []
        # print(ast.decl)

        for decl in ast.decl:
            self.visit(decl, classStore)

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
        else:
            parentName = None
        # -----------------------------------------------------------------
        # First ever class can not have inheritance
        if len(classStore) == 0 and parentName != None:
            return Undeclared(Class(), parentName)
        
        # Not the first ever class declared 
        elif len(classStore) > 0:
            for current_classDecl in classStore:
                if current_classDecl['ClassName'] == className['name']:
                    raise Redeclared(Class(), className["name"])
            


            
        

      
       
        newClass = {}
        newClass['ClassName'] = className['name']
        newClass['Attributes'] = []
        newClass['Methos'] = []

        classStore.insert(0, newClass)


#     name: str
    def visitId(self, ast: Id, classStore):
         return {'name':ast.name, "type":Type.UNDEFINE}
        
        
        

       
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
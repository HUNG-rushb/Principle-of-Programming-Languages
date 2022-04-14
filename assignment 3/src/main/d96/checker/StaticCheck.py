"""
1913652
Trịnh Duy Hưng
"""
from msilib.schema import Class
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
    def visitProgram(self, ast: Program, varList):
        # return  [self.visit(x,c) for x in ast.decl]
        varList = [[{}], [{}]]
        for decl in ast.decl:
            self.visit(decl, varList)

#     classname: Id
#     memlist: List[MemDecl]
#     parentname: Id = None
    def visitClassDecl(self, ast: ClassDecl, varList):
        className = ast.classname.name
        parentName = ast.parentName.name

        if className in varList:
            raise Redeclared(Class(),)

#     name: str
    def visitId(self, ast: Id, varList):

        for index in varList:
            if ast.Id in index:
                return index[ast.Id]
        


    def visitClassType(self, ast: ClassType, varList):
        return None

    def visitBinaryOp(self, ast: BinaryOp, varList):
        return None

    def visitUnaryOp(self, ast: UnaryOp, varList):
        return None

    def visitCallExpr(self, ast: CallExpr, varList):
        return None

    def visitNewExpr(self, ast: NewExpr, varList):
        return None

    def visitArrayCell(self, ast: ArrayCell, varList):
        return None

    def visitFieldAccess(self, ast: FieldAccess, varList):
        return None

    def visitFloatLiteral(self, ast: FloatLiteral, varList):
        return None

    def visitStringLiteral(self, ast: StringLiteral, varList):
        return None

    def visitBooleanLiteral(self, ast: BooleanLiteral, varList):
        return None

    def visitSelfLiteral(self, ast: SelfLiteral, varList):
        return None

    def visitArrayLiteral(self, ast: ArrayLiteral, varList):
        return None

    def visitAssign(self, ast: Assign, varList):
        return None

    def visitIf(self, ast: If, varList):
        return None

    def visitFor(self, ast: For, varList):
        return None

    def visitBreak(self, ast: Break, varList):
        return None

    def visitContinue(self, ast: Continue, varList):
        return None

    def visitReturn(self, ast: Return, varList):
        return None

    def visitCallStmt(self, ast: CallStmt, varList):
        return None

    def visitVarDecl(self, ast: VarDecl, varList):
        return None

    def visitBlock(self, ast: Block, varList):
        return None

    def visitConstDecl(self, ast: ConstDecl, varList):
        return None

    def visitInstance(self, ast: Instance, varList):
        return None

    def visitBlock(self, ast: Block, varList):
        return None

    def visitStatic(self, ast: Static, varList):
        return None

    def visitMethodDecl(self, ast: MethodDecl, varList):
        return None

    def visitAttributeDecl(self, ast: AttributeDecl, varList):
        return None

    # Primitive Type 
    def visitIntType(self, ast: IntType, varList):
        return Type.INT

    def visitFloatType(self, ast: FloatType, varList):
        return Type.FLOAT

    def visitBoolType(self, ast: BoolType, varList):
        return Type.BOOLEAN

    def visitStringType(self, ast: StringType, varList):
        return Type.STRING

    def visitArrayType(self, ast: ArrayType, varList):
        return Type.ARRAY

    def visitVoidType(self, ast: VoidType, varList):
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

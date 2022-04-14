
"""
 * @author nhphung
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

    def visitProgram(self, ast: Program, c):
        # return  [self.visit(x,c) for x in ast.decl]
        c = {}
        for decl in ast.decl:
            self.visit(decl, c)

#     classname: Id
#     memlist: List[MemDecl]
#     parentname: Id = None
    def visitClassDecl(self, ast: ClassDecl, c):
        self.visit(ast.classname, c)

#     name: str
    def visitId(self, ast: Id, c):
        if ast.name in c:
            raise Redeclared(Class(), ast.name)
        c[ast.name] = Type.CLASS

    def visitClassType(self, ast: ClassType, c):
        return None

    def visitBinaryOp(self, ast: BinaryOp, c):
        return None

    def visitUnaryOp(self, ast: UnaryOp, c):
        return None

    def visitCallExpr(self, ast: CallExpr, c):
        return None

    def visitNewExpr(self, ast: NewExpr, c):
        return None

    def visitArrayCell(self, ast: ArrayCell, c):
        return None

    def visitFieldAccess(self, ast: FieldAccess, c):
        return None

    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return None

    def visitStringLiteral(self, ast: StringLiteral, c):
        return None

    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return None

    def visitSelfLiteral(self, ast: SelfLiteral, c):
        return None

    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        return None

    def visitAssign(self, ast: Assign, c):
        return None

    def visitIf(self, ast: If, c):
        return None

    def visitFor(self, ast: For, c):
        return None

    def visitBreak(self, ast: Break, c):
        return None

    def visitContinue(self, ast: Continue, c):
        return None

    def visitReturn(self, ast: Return, c):
        return None

    def visitCallStmt(self, ast: CallStmt, c):
        return None

    def visitVarDecl(self, ast: VarDecl, c):
        return None

    def visitBlock(self, ast: Block, c):
        return None

    def visitConstDecl(self, ast: ConstDecl, c):
        return None

    def visitInstance(self, ast: Instance, c):
        return None

    def visitBlock(self, ast: Block, c):
        return None

    def visitStatic(self, ast: Static, c):
        return None

    def visitMethodDecl(self, ast: MethodDecl, c):
        return None

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        return None

    def visitIntType(self, ast: IntType, c):
        return None

    def visitFloatType(self, ast: FloatType, c):
        return None

    def visitBoolType(self, ast: BoolType, c):
        return None

    def visitStringType(self, ast: StringType, c):
        return None

    def visitArrayType(self, ast: ArrayType, c):
        return None

    def visitVoidType(self, ast: VoidType, c):
        return None

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

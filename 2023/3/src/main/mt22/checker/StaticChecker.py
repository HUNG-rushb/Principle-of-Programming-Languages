# 1913652
# Trịnh Duy Hưng
from AST import *
from Visitor import Visitor
from StaticError import *
import json

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

def toJSON(data, place, typ = None) :
    if typ == 't':
        try:
            print(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            print(e)
    else:
        f = open('./main/mt22/checker/' + place + '.json', 'w', encoding='utf-8')
        try:
            f.write(json.dumps(data, sort_keys=False, indent=4))
        except Exception as e:
            f.write(e)
        finally:
            f.close()


class Type:
    def NONE(self): return "<3...None"

    def VOID(self): return "<3...VOID"

    def INT(self): return "<3...INT"

    def FLOAT(self): return "<3...FLOAT"

    def STRING(self): return "<3...STRING"

    def BOOLEAN(self): return "<3...BOOLEAN"

    def ARRAY(self, type, size): return "<3...ARRAY" + "**" + type + "**" + str(size)

    



# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# ! ██      ███████ █████   ██      █████   █████   ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
class StaticChecker(Visitor):

    global_envi = [
        Symbol("getInt", MType([], IntegerType())),
        Symbol("putIntLn", MType([IntegerType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, funcStore):
        print("00000000")
        print(ast)
     
        
        funcStore = {}

        for decl in ast.decls:
            print(1111111)
            self.visit(decl, funcStore)

        # if ('Program' not in classStore) or ('main' not in classStore['Program']):
        # if 'main' not in funcStore:
        #     raise NoEntryPoint()

        toJSON(funcStore, 'global_scope')
        return ""
        
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, funcStore):
        # varName = ast.name
        # varType = self.visit(ast.typ, funcStore)

        funcStore['global']['variable'] = {
            'type': 12,
            'init': None
        }

        print(22222222)
        # toJSON(funcStore, 'global')





    





    # def visitIntLiteral(self, ast: IntLiteral, classStore):
    #     return Type().INT()

    # def visitFloatLiteral(self, ast: FloatLiteral, classStore):
    #     return Type().FLOAT()

    # def visitStringLiteral(self, ast: StringLiteral, classStore):
    #     return Type().STRING()

    # def visitBooleanLiteral(self, ast: BooleanLiteral, classStore):
    #     return Type().BOOLEAN()







    def visitIntegerType(self, ast: IntegerType, funcStore):
        return Type().INT()

    def visitFloatType(self, ast: FloatType, funcStore):
        return Type().FLOAT()

    def visitBooleanType(self, ast: BooleanType, funcStore):
        return Type().BOOLEAN()

    def visitStringType(self, ast: StringType, funcStore):
        return Type().STRING()

    # size: int
    # eleType: Type
    def visitArrayType(self, ast: ArrayType, funcStore):
        arrayType = self.visit(ast.eleType, funcStore)
        arraySize = ast.size

        return Type().ARRAY(arrayType, arraySize)

    def visitVoidType(self, ast: VoidType, funcStore):
        return Type().VOID()







    # def visit(self, ast, param):
    #     return ast.accept(self, param)

    # def visitIntegerType(self, ast, param): pass
    # def visitFloatType(self, ast, param): pass
    # def visitBooleanType(self, ast, param): pass
    # def visitStringType(self, ast, param): pass

    # def visitArrayType(self, ast, param): pass
    # def visitAutoType(self, ast, param): pass
    # def visitVoidType(self, ast, param): pass

    # def visitBinExpr(self, ast, param): pass
    # def visitUnExpr(self, ast, param): pass
    # def visitId(self, ast, param): pass
    # def visitArrayCell(self, ast, param): pass
    # def visitIntegerLit(self, ast, param): pass
    # def visitFloatLit(self, ast, param): pass
    # def visitStringLit(self, ast, param): pass
    # def visitBooleanLit(self, ast, param): pass
    # def visitArrayLit(self, ast, param): pass
    # def visitFuncCall(self, ast, param): pass

    # def visitAssignStmt(self, ast, param): pass
    # def visitBlockStmt(self, ast, param): pass
    # def visitIfStmt(self, ast, param): pass
    # def visitForStmt(self, ast, param): pass
    # def visitWhileStmt(self, ast, param): pass
    # def visitDoWhileStmt(self, ast, param): pass
    # def visitBreakStmt(self, ast, param): pass
    # def visitContinueStmt(self, ast, param): pass
    # def visitReturnStmt(self, ast, param): pass
    # def visitCallStmt(self, ast, param): pass

    # def visitVarDecl(self, ast, param): pass
    # def visitParamDecl(self, ast, param): pass
    # def visitFuncDecl(self, ast, param): pass

    # def visitProgram(self, ast, param): pass
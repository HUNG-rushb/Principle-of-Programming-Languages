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
    def INT(self): return "<3...INT"

    def FLOAT(self): return "<3...FLOAT"

    def STRING(self): return "<3...STRING"

    def BOOLEAN(self): return "<3...BOOLEAN"

    def ARRAY(self, type, size): return "<3...ARRAY" + "__" + type + "__" + str(size)

    def AUTO(self): return "<3...AUTO"

    def VOID(self): return "<3...VOID"

# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# ! ██      ███████ █████   ██      █████   █████   ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
class StaticChecker(Visitor):

    global_envi = {}

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, funcStore):
        print(ast)

        funcStore = { 
            "Global_Variable": {},
            "Global_Function": {},
        }

        for decl in ast.decls:
            # if isinstance(decl, VarDecl):            
            #     funcStore['Global_Variable'][decl.name] = {}
            if isinstance(decl, FuncDecl):
                if decl.name in funcStore["Global_Function"]:
                    raise Redeclared(Function(), decl.name)
                funcStore['Global_Function'][decl.name] = {}

        toJSON(funcStore, 'first')

        
        

        for decl in ast.decls:
            self.visit(decl, funcStore)

        if 'main' not in funcStore['Global_Function'] or funcStore['Global_Function']['main']['returnType'] != Type().VOID() or len(funcStore['Global_Function']['main']['params']) > 0:
            raise NoEntryPoint()

        toJSON(funcStore, 'all')
        return ""
        
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, funcStore):
        varName = str(ast.name)
        varType = self.visit(ast.typ, funcStore)

        if ast.init is not None:
            varInit = self.visit(ast.init, funcStore)

            # if varInit != varType:
            #     if varType == Type().FLOAT() and varInit == Type().INT():
            #         varInit = Type().FLOAT()
            #     else:
            #         raise TypeMismatchInVarDecl(ast)
        else:
            varInit = None

        # Global
        if len(funcStore) == 2:
            if varName in funcStore["Global_Variable"]:
                raise Redeclared(Variable(), varName)

            funcStore['Global_Variable'][varName] = {
                'type': varType,
                'init': varInit,
            }
        # In function
        elif len(funcStore) == 3:
            if varName in funcStore['body'][0]:
                raise Redeclared(Variable(), varName)

            funcStore['body'][0][varName] = {
                'type': varType,
                'init': varInit,
            }




    # name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast: ParamDecl, funcStore): 
        paramName = str(ast.name)
        paramType = self.visit(ast.typ, funcStore)

        if paramName in funcStore["methodParams"]:
            raise Redeclared(Parameter(), paramName)

        if ast.out == False:
            out = False
        else:
            out = True

        if ast.inherit == False:
            inherit = False
        else:
            inherit = True


        funcStore['methodParams'][paramName] = {
            'type': paramType,
            'out': out,
            'inherit': inherit
        }

    # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast: FuncDecl, funcStore): 
        funcName = str(ast.name)
        returnType = self.visit(ast.return_type, funcStore)

        if ast.inherit is not None:
            inherit = str(ast.inherit)
        else:
            inherit = None

        

        # Create Function in store
        funcStore['Global_Function'][funcName] = {
                'returnType': returnType,
                'inherit': inherit,
                'body': [{}, {}],
                'params': {},
                # 'localVar': {}
        }

        # Visit Params 
        newMethodEnviroment = {
            'methodParams': funcStore['Global_Function'][funcName]['params']
        }

        for param in ast.params:
            self.visit(param, newMethodEnviroment)

        # Visit Block 
        newMethodEnviromentBlock = {
            'inherit': funcStore['Global_Function'][funcName]['inherit'],
            'methodParams': funcStore['Global_Function'][funcName]['params'],
            'body': funcStore['Global_Function'][funcName]['body'],
            # 'localVar': funcStore['Global_Function'][funcName]['localVar']
        }

        self.visit(ast.body, newMethodEnviromentBlock)
    
    #  body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast: BlockStmt, funcStore): 
        for stmt in ast.body:
            self.visit(stmt, funcStore)




    
    # op: str, left: Expr, right: Exp
    def visitBinExpr(self, ast: BinExpr, funcStore): pass

    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, funcStore): pass

    # name: str
    def visitId(self, ast: Id, funcStore): 
        return str(ast.name)

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast: ArrayCell, funcStore): pass



    def visitIntegerLit(self, ast: IntegerLit, funcStore):
        return Type().INT()

    def visitFloatLit(self, ast: FloatLit, funcStore):
        return Type().FLOAT()

    def visitStringLit(self, ast: StringLit, funcStore):
        return Type().STRING()

    def visitBooleanLit(self, ast: BooleanLit, funcStore):
        return Type().BOOLEAN()
    
    # explist: List[Expr]
    def visitArrayLit(self, ast: ArrayLit, funcStore):
        exprlist = []
        for expr in ast.explist:
            exprlist.append(self.visit(expr, funcStore))

        return exprlist



    # def visitFuncCall(self, ast, param): pass
# ----------------------------------------------------------------  
    def visitIntegerType(self, ast: IntegerType, funcStore):
        return Type().INT()

    def visitFloatType(self, ast: FloatType, funcStore):
        return Type().FLOAT()

    def visitBooleanType(self, ast: BooleanType, funcStore):
        return Type().BOOLEAN()

    def visitStringType(self, ast: StringType, funcStore):
        return Type().STRING()

    def visitAutoType(self, ast: AutoType, funcStore):
        return Type().AUTO()

    def visitVoidType(self, ast: VoidType, funcStore):
        return Type().VOID()

    # dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ast: ArrayType, funcStore):
        arrayType = self.visit(ast.typ, funcStore)
        arraySize = ''

        for size in ast.dimensions:
            arraySize = arraySize + '-' + str(size)

        return Type().ARRAY(arrayType, arraySize)



   









    

   





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


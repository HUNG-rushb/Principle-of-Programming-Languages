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
            if isinstance(decl, FuncDecl):
                funcName = str(decl.name)
                returnType = self.visit(decl.return_type, funcStore)

                if funcName in funcStore["Global_Function"] \
                    or funcName in funcStore["Global_Variable"] \
                    or  funcName in ["readInteger",\
                            "printInteger",\
                            "readFloat",\
                            "writeFloat",\
                            "readBoolean",\
                            "printBoolean",\
                            "readString",\
                            "printString",\
                            "super",\
                            "preventDefault"]:
                    raise Redeclared(Function(), decl.name)

                if decl.inherit is not None:
                    inherit = str(decl.inherit)
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

                for param in decl.params:
                    self.visit(param, newMethodEnviroment)

        toJSON(funcStore, 'first')

        for decl in ast.decls:
            self.visit(decl, funcStore)

        if 'main' not in funcStore['Global_Function'] \
            or funcStore['Global_Function']['main']['returnType'] != Type().VOID() \
                or len(funcStore['Global_Function']['main']['params']) > 0:
            raise NoEntryPoint()

        toJSON(funcStore, 'all')
        return ""
        
    
    # name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast: VarDecl, funcStore):
        varName = str(ast.name)
        varType = self.visit(ast.typ, funcStore)

        if ast.init is not None:
            varInit = self.visit(ast.init, funcStore)

            if varInit != varType:
                if varType == Type().FLOAT() and varInit == Type().INT():
                    varInit = Type().FLOAT()
                elif varType == Type().AUTO() or varType == Type().VOID():
                    varInit = varType
                else:
                    raise TypeMismatchInVarDecl(ast)
        else:
            if varType == Type().AUTO():
                raise Invalid(Variable(), varName)
            varInit = None

        # Global
        if len(funcStore) == 2:
            if varName in funcStore["Global_Variable"] \
                or varName in funcStore["Global_Function"] \
                or varName in ["readInteger",\
                            "printInteger",\
                            "readFloat",\
                            "writeFloat",\
                            "readBoolean",\
                            "printBoolean",\
                            "readString",\
                            "printString",\
                            "super",\
                            "preventDefault"]:
                raise Redeclared(Variable(), varName)

            funcStore['Global_Variable'][varName] = {
                'type': varType,
                'init': varInit,
            }
        # In function
        elif len(funcStore) == 5:
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
    
        # Visit Block 
        newMethodEnviromentBlock = {
            'Global_Variable': funcStore['Global_Variable'],
            'Global_Function': funcStore['Global_Function'],
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
    def visitBinExpr(self, ast: BinExpr, funcStore): 
        operand = str(ast.op)
        left = self.visit(ast.left, funcStore)
        right = self.visit(ast.right, funcStore)

        if operand in ["+", "-", "*", "/", "%"]:
            if left == Type().INT() and right == Type().INT():
                return Type().INT()
            elif (left == Type().FLOAT() or left == Type().INT()) \
                and (right == Type().FLOAT() or right == Type().INT()):

                if operand == "%" and (left == Type().FLOAT() or right == Type().FLOAT()):
                    raise TypeMismatchInExpression(ast)
                else:
                    return Type().FLOAT()
            else:
                raise TypeMismatchInExpression(ast)

        elif operand in ["&&", "||", "!"]: 
            if left == Type().BOOLEAN() and right == Type().BOOLEAN():
                return Type().BOOLEAN()
            else:
                raise TypeMismatchInExpression(ast)

        elif operand in ["::"]: 
            if left == Type().STRING() and right == Type().STRING():
                return Type().STRING()
            else:
                raise TypeMismatchInExpression(ast)
                
        elif operand in ["==", "!=", ">", "<", "<=", ">="]:
            if (left == Type().INT() and right == Type().INT()) \
                or (left == Type().BOOLEAN() and right == Type().BOOLEAN() and operand in ["==", "!="]) \
                or (left == Type().FLOAT()  and right == Type().FLOAT() and operand in [">", "<", "<=", ">="]):
                return Type().BOOLEAN()
            # else:
            #     raise TypeMismatchInExpression(ast)

    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, funcStore): 
        operand = str(ast.op)
        body = self.visit(ast.val, funcStore)

        if operand == '!' and body == Type().BOOLEAN() :
            return Type().BOOLEAN()
        elif operand == '-' and body != Type().INT() and body != Type().FLOAT():
            if body == Type().INT():
                return Type().INT()
            else:
                return Type().FLOAT()
        else:
            raise TypeMismatchInExpression(ast)

    def visitIntegerLit(self, ast: IntegerLit, funcStore):
        return Type().INT()

    def visitFloatLit(self, ast: FloatLit, funcStore):
        return Type().FLOAT()

    def visitStringLit(self, ast: StringLit, funcStore):
        return Type().STRING()

    def visitBooleanLit(self, ast: BooleanLit, funcStore):
        return Type().BOOLEAN()
    
    


# !----------------------------------------------------------------  
# !----------------------------------------------------------------  
# !----------------------------------------------------------------  
    # name: str
    def visitId(self, ast: Id, funcStore): 
        name = str(ast.name)
       
        if name in funcStore['Global_Variable']: 
            return funcStore['Global_Variable'][name]['type']
        elif name in funcStore['body'][0]: 
            return funcStore['body'][0][name]['type']
        elif name in funcStore['methodParams']:
            return funcStore['methodParams'][name]['type']
        else:
            raise Undeclared(Identifier(), name)
                
    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast: ArrayCell, funcStore): 
        name = str(ast.name)

        toJSON(funcStore, 'del')

        index_type = self.visit(ast.cell[0], funcStore)

        if index_type != Type().INT():
            raise TypeMismatchInExpression(ast)

        if len(funcStore) == 2:
            if name not in funcStore["Global_Variable"]:
                raise Undeclared(Identifier(), name)

            if funcStore["Global_Variable"][name]['type'].find('INT') != -1:
                return Type().INT()
            elif funcStore["Global_Variable"][name]['type'].find('FLOAT') != -1:
                return Type().FLOAT()
            elif funcStore["Global_Variable"][name]['type'].find('STRING') != -1:
                return Type().STRING()
            elif funcStore["Global_Variable"][name]['type'].find('BOOLEAN') != -1:
                return Type().BOOLEAN()

        # In function
        elif len(funcStore) == 5:
            if name not in funcStore['body'][0]:
                raise Undeclared(Identifier(), name)

            if funcStore['body'][0][name]['type'].find('INT') != -1:
                return Type().INT()
            elif funcStore['body'][0][name]['type'].find('FLOAT') != -1:
                return Type().FLOAT()
            elif funcStore['body'][0][name]['type'].find('STRING') != -1:
                return Type().STRING()
            elif funcStore['body'][0][name]['type'].find('BOOLEAN') != -1:
                return Type().BOOLEAN()

        



    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast: AssignStmt, funcStore):
        LHS = self.visit(ast.lhs, funcStore)
        rhs = self.visit(ast.rhs, funcStore)

        if LHS != rhs:
            raise TypeMismatchInStatement(ast)








    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast: IfStmt, funcStore): 
        cond = self.visit(ast.cond, funcStore)



        self.visit(ast.tstmt, funcStore)

        # if ast.fstmt is not None:
        #     return self.visit(ast.fstmt, funcStore)

    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast: ForStmt, funcStore): 
        
        cond = self.visit(ast.cond, funcStore)
        upd = self.visit(ast.upd, funcStore)

        funcStore_in_loop = {
            **funcStore,
            "in_loop": True
        }
        self.visit(ast.stmt, funcStore_in_loop)

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast: WhileStmt, funcStore): 
        cond = self.visit(ast.cond, funcStore)
        self.visit(ast.tstmt, funcStore)

    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast: DoWhileStmt, funcStore): 
        cond = self.visit(ast.cond, funcStore)
        self.visit(ast.stmt, funcStore)



    def visitBreakStmt(self, ast: BreakStmt, funcStore): 
        toJSON(funcStore, 'del')
        if 'in_loop' in funcStore:
            funcStore.pop('in_loop')
            pass
        else:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast: ContinueStmt, funcStore): 
        if 'in_loop' in funcStore:
            pass
        else:
            raise MustInLoop(ast)

    # expr: Expr or None = None
    def visitReturnStmt(self, ast: ReturnStmt, funcStore): 
        if ast.expr is not None:
            return self.visit(ast.expr, funcStore)
        else: 
            return Type().VOID()


    # name: str, args: List[Expr]
    def visitCallStmt(self, ast: CallStmt, funcStore): 
        name = str(ast.name)
        number_of_param = len(ast.args)

        if name in ["readInteger",\
                    "printInteger",\
                    "readFloat",\
                    "writeFloat",\
                    "readBoolean",\
                    "printBoolean",\
                    "readString",\
                    "printString",\
                    "super",\
                    "preventDefault"]:
            return Type().VOID()

        if name not in funcStore['Global_Function']:
            raise Undeclared(Function(), name)  
        elif number_of_param != len(funcStore['Global_Function'][name]["params"]):
            raise TypeMismatchInExpression(ast)
            
        return funcStore['Global_Function'][name]["returnType"]



   

# ----------------------------------------------------------------  
    # name: str, args: List[Expr]
    def visitFuncCall(self, ast: FuncCall, funcStore): 
        name = str(ast.name)
        number_of_param = len(ast.args)

        if name in ["readInteger",\
                    "printInteger",\
                    "readFloat",\
                    "writeFloat",\
                    "readBoolean",\
                    "printBoolean",\
                    "readString",\
                    "printString",\
                    "super",\
                    "preventDefault"]:
            return Type().VOID()

        if name not in funcStore['Global_Function']:
            raise Undeclared(Function(), name)  
        elif number_of_param != len(funcStore['Global_Function'][name]["params"]):
            raise TypeMismatchInExpression(ast)
            
        return funcStore['Global_Function'][name]["returnType"]

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

    # explist: List[Expr]
    def visitArrayLit(self, ast: ArrayLit, funcStore):
        # print(type(ast.explist[0]))
        if any(not isinstance(y, (type(ast.explist[0]))) for y in ast.explist):
            raise IllegalArrayLiteral(ast)

        return Type().ARRAY(self.visit(ast.explist[0], funcStore), '-' + str(len(ast.explist)))

   









    

   




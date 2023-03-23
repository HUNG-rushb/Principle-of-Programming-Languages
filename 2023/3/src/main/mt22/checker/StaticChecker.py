# 1913652
# Trịnh Duy Hưng
from Visitor import Visitor



# def toJSON(data, place, typ = None) :
#     if typ == 't':
#         try:
#             print(json.dumps(data, sort_keys=False, indent=4))
#         except Exception as e:
#             print(e)
#     else:
#         f = open('./main/d96/checker/' + place + '.json', 'w', encoding='utf-8')
#         try:
#             f.write(json.dumps(data, sort_keys=False, indent=4))
#         except Exception as e:
#             f.write(e)
#         finally:
#             f.close()


class Type:
    def NONE(self): return "<3...None"

    def VOID(self): return "<3...VOID"

    def INT(self): return "<3...INT"

    def FLOAT(self): return "<3...FLOAT"

    def STRING(self): return "<3...STRING"

    def BOOLEAN(self): return "<3...BOOLEAN"

    def ARRAY(self, type, size): return "<3...ARRAY" + "**" + type + "**" + str(size)

    # def CLASS(self, name): return "<3...CLASS " + name
    # def NULL(self): return "<3...NULL"



# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# ! ██      ███████ █████   ██      █████   █████   ██████  
# ! ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
# !  ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
class StaticChecker(Visitor):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, funcStore):
        funcStore = {}

        for decl in ast.decl:
            self.visit(decl, funcStore)

        # if ('Program' not in classStore) or ('main' not in classStore['Program']):
        if 'main' not in funcStore:
            raise NoEntryPoint()
        
    






    def visitIntLiteral(self, ast: IntLiteral, classStore):
        return Type().INT()

    def visitFloatLiteral(self, ast: FloatLiteral, classStore):
        return Type().FLOAT()

    def visitStringLiteral(self, ast: StringLiteral, classStore):
        return Type().STRING()

    def visitBooleanLiteral(self, ast: BooleanLiteral, classStore):
        return Type().BOOLEAN()







    def visitIntType(self, ast: IntType, funcStore):
        return Type().INT()

    def visitFloatType(self, ast: FloatType, funcStore):
        return Type().FLOAT()

    def visitBoolType(self, ast: BoolType, funcStore):
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
# 1912683
# Nguyen Thien Bao
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from functools import reduce
from AST import *

class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(list(map(lambda x: self.visit(x), ctx.vardecl())))
    
    def visitVardecl(self, ctx: D96Parser.VardeclContext):

        reversed = list(reversed(self.visit(ctx.idlist())))
        return reduce(lambda prev,current: VarDecl(current[1], current[0], self.visit(ctx.typ()), prev) ,reversed , None)
        
    def visitIdlist(self, ctx:  D96Parser.IdlistContext):
        return [self.visit(ctx.mem(0))] if ctx.getChildCount() == 1 else list(map(lambda x: self.visit(x), ctx.mem()))
       
    def visitMem(self, ctx: D96Parser.MemContext):
        return (True, ctx.ID().getText()) if ctx.STATIC() else (False, ctx.ID().getText())
       
    def visitTyp(self, ctx: D96Parser.TypContext):
        return IntType() if ctx.INT() else FloatType()

    
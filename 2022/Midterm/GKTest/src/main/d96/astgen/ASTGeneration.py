# 1912683
# Nguyen Thien Bao
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from functools import reduce
from AST import *

class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(list(map(lambda x: self.visit(x), ctx.vardecl())))
        # return Program(reduce(lambda x, y: x + self.visit(y), ctx.vardecl(), []))


    def visitVardecl(self, ctx: D96Parser.VardeclContext):
        return reduce(lambda prev, current: VarDecl(current[1], current[0], self.visit(ctx.typ()), prev),
                                list(reversed(self.visit(ctx.idlist()))), 
                                None)
        






    def visitIdlist(self, ctx:  D96Parser.IdlistContext):
        return [self.visit(ctx.mem(0))] if ctx.getChildCount() == 1 else list(map(lambda x: self.visit(x), ctx.mem()))
       
    def visitMem(self, ctx: D96Parser.MemContext):
        return (True, ctx.ID().getText()) if ctx.STATIC() else (False, ctx.ID().getText())
       







    def visitTyp(self, ctx: D96Parser.TypContext):
        return IntType() if ctx.INT() else FloatType()

    






























from functools import reduce
class ASTGeneration(D96Visitor):

    # program: exp EOF;
    def visitProgram(self,ctx:D96Parser.ProgramContext):
        return self.visit(ctx.exp())

    # exp: (term ASSIGN)* term;
    def visitExp(self,ctx:D96Parser.ExpContext):
        terms = list(map(lambda x: self.visit(x), ctx.term()))
        assigns = list(map(lambda x: x.getText(), ctx.ASSIGN()))
        exps = reversed(list(map(lambda op, operand: (op, operand), assigns, terms[:-1])))
        return reduce(lambda right, unaryLeft: Binary(unaryLeft[0], unaryLeft[1], right), exps, terms[-1])

    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:D96Parser.TermContext): 
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) if ctx.COMPARE() else self.visit(ctx.factor(0))

    # factor: operand (ANDOR operand)*; 
    def visitFactor(self,ctx:D96Parser.FactorContext):
        operands = list(map(lambda x: self.visit(x), ctx.operand()))
        andors = list(map(lambda x: x.getText(), ctx.ANDOR()))
        exps = list(map(lambda op, operand: (op, operand), andors, operands[1:]))
        return reduce(lambda left, unaryRight: Binary(unaryRight[0], left, unaryRight[1]), exps, operands[0])

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:D96Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == 'True')
        else:
            return self.visit(ctx.exp())









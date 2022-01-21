# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardclr.
    def visitVardclr(self, ctx:BKOOLParser.VardclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdclr.
    def visitFuncdclr(self, ctx:BKOOLParser.FuncdclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramdclr.
    def visitParamdclr(self, ctx:BKOOLParser.ParamdclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcall.
    def visitFuncall(self, ctx:BKOOLParser.FuncallContext):
        return self.visitChildren(ctx)



del BKOOLParser
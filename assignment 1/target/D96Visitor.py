# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declaration.
    def visitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_declaration.
    def visitVariable_declaration(self, ctx:D96Parser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_statements.
    def visitAssignment_statements(self, ctx:D96Parser.Assignment_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statements.
    def visitIf_statements(self, ctx:D96Parser.If_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forin_statements.
    def visitForin_statements(self, ctx:D96Parser.Forin_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodinvocation_statement.
    def visitMethodinvocation_statement(self, ctx:D96Parser.Methodinvocation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statements.
    def visitBreak_statements(self, ctx:D96Parser.Break_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statements.
    def visitContinue_statements(self, ctx:D96Parser.Continue_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statements.
    def visitReturn_statements(self, ctx:D96Parser.Return_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statements.
    def visitBlock_statements(self, ctx:D96Parser.Block_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_lit.
    def visitArray_lit(self, ctx:D96Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_val.
    def visitArray_val(self, ctx:D96Parser.Array_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_parameters.
    def visitList_parameters(self, ctx:D96Parser.List_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameters.
    def visitParameters(self, ctx:D96Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier_list.
    def visitIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value_list.
    def visitValue_list(self, ctx:D96Parser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_element_type.
    def visitArray_element_type(self, ctx:D96Parser.Array_element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_size.
    def visitArray_size(self, ctx:D96Parser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_type.
    def visitVariable_type(self, ctx:D96Parser.Variable_typeContext):
        return self.visitChildren(ctx)



del D96Parser
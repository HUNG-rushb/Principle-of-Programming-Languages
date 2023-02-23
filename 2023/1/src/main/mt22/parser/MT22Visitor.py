# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#main_function.
    def visitMain_function(self, ctx:MT22Parser.Main_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_declaration.
    def visitFunction_declaration(self, ctx:MT22Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_declaration_no_init.
    def visitVariable_declaration_no_init(self, ctx:MT22Parser.Variable_declaration_no_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_declaration_init.
    def visitVariable_declaration_init(self, ctx:MT22Parser.Variable_declaration_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_declaration_init_list.
    def visitVariable_declaration_init_list(self, ctx:MT22Parser.Variable_declaration_init_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment_statements.
    def visitAssignment_statements(self, ctx:MT22Parser.Assignment_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#method_invocation_statements.
    def visitMethod_invocation_statements(self, ctx:MT22Parser.Method_invocation_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_integer_function.
    def visitRead_integer_function(self, ctx:MT22Parser.Read_integer_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_integer_function.
    def visitPrint_integer_function(self, ctx:MT22Parser.Print_integer_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_float_function.
    def visitRead_float_function(self, ctx:MT22Parser.Read_float_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#write_float_function.
    def visitWrite_float_function(self, ctx:MT22Parser.Write_float_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_boolean_function.
    def visitRead_boolean_function(self, ctx:MT22Parser.Read_boolean_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_boolean_function.
    def visitPrint_boolean_function(self, ctx:MT22Parser.Print_boolean_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_string_function.
    def visitRead_string_function(self, ctx:MT22Parser.Read_string_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_string_function.
    def visitPrint_string_function(self, ctx:MT22Parser.Print_string_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#super_function.
    def visitSuper_function(self, ctx:MT22Parser.Super_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prevent_default_function.
    def visitPrevent_default_function(self, ctx:MT22Parser.Prevent_default_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_statements.
    def visitIf_statements(self, ctx:MT22Parser.If_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elseif_list_statements.
    def visitElseif_list_statements(self, ctx:MT22Parser.Elseif_list_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elseif_statement.
    def visitElseif_statement(self, ctx:MT22Parser.Elseif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#else_statement.
    def visitElse_statement(self, ctx:MT22Parser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_statements.
    def visitFor_statements(self, ctx:MT22Parser.For_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_statements.
    def visitWhile_statements(self, ctx:MT22Parser.While_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_statements.
    def visitDo_while_statements(self, ctx:MT22Parser.Do_while_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_statements.
    def visitBreak_statements(self, ctx:MT22Parser.Break_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_statements.
    def visitContinue_statements(self, ctx:MT22Parser.Continue_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_expr.
    def visitReturn_expr(self, ctx:MT22Parser.Return_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_statements.
    def visitReturn_statements(self, ctx:MT22Parser.Return_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_nothing_statements.
    def visitReturn_nothing_statements(self, ctx:MT22Parser.Return_nothing_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#global_statements.
    def visitGlobal_statements(self, ctx:MT22Parser.Global_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#global_statement.
    def visitGlobal_statement(self, ctx:MT22Parser.Global_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statements.
    def visitBlock_statements(self, ctx:MT22Parser.Block_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statements.
    def visitStatements(self, ctx:MT22Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_in_loop_statements.
    def visitBlock_in_loop_statements(self, ctx:MT22Parser.Block_in_loop_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#in_loop_statements.
    def visitIn_loop_statements(self, ctx:MT22Parser.In_loop_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#in_loop_statement.
    def visitIn_loop_statement(self, ctx:MT22Parser.In_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list_no_empty.
    def visitExpr_list_no_empty(self, ctx:MT22Parser.Expr_list_no_emptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr9.
    def visitExpr9(self, ctx:MT22Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr10.
    def visitExpr10(self, ctx:MT22Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#all_type.
    def visitAll_type(self, ctx:MT22Parser.All_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_types.
    def visitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_id_list.
    def visitVariable_id_list(self, ctx:MT22Parser.Variable_id_listContext):
        return self.visitChildren(ctx)



del MT22Parser
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


    # Visit a parse tree produced by D96Parser#class_declarations.
    def visitClass_declarations(self, ctx:D96Parser.Class_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_inheritance.
    def visitClass_inheritance(self, ctx:D96Parser.Class_inheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_dclr.
    def visitConstructor_dclr(self, ctx:D96Parser.Constructor_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_dclr.
    def visitDestructor_dclr(self, ctx:D96Parser.Destructor_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declaration.
    def visitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_declaration.
    def visitVariable_declaration(self, ctx:D96Parser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#no_value_assign_declare_list.
    def visitNo_value_assign_declare_list(self, ctx:D96Parser.No_value_assign_declare_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#no_value_assign_declare.
    def visitNo_value_assign_declare(self, ctx:D96Parser.No_value_assign_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declare_initiate_list.
    def visitDeclare_initiate_list(self, ctx:D96Parser.Declare_initiate_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_and_assign.
    def visitType_and_assign(self, ctx:D96Parser.Type_and_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#both_variable_declaration.
    def visitBoth_variable_declaration(self, ctx:D96Parser.Both_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#both_no_value_assign_declare_list.
    def visitBoth_no_value_assign_declare_list(self, ctx:D96Parser.Both_no_value_assign_declare_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#both_no_value_assign_declare.
    def visitBoth_no_value_assign_declare(self, ctx:D96Parser.Both_no_value_assign_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#both_declare_initiate_list.
    def visitBoth_declare_initiate_list(self, ctx:D96Parser.Both_declare_initiate_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#both_type_and_assign.
    def visitBoth_type_and_assign(self, ctx:D96Parser.Both_type_and_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#function_declaration.
    def visitFunction_declaration(self, ctx:D96Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_func_statement.
    def visitCall_func_statement(self, ctx:D96Parser.Call_func_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_func.
    def visitCall_func(self, ctx:D96Parser.Call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_func_header.
    def visitCall_func_header(self, ctx:D96Parser.Call_func_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_func_attr_list.
    def visitCall_func_attr_list(self, ctx:D96Parser.Call_func_attr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_func_attr.
    def visitCall_func_attr(self, ctx:D96Parser.Call_func_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_func_end.
    def visitCall_func_end(self, ctx:D96Parser.Call_func_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_statements.
    def visitAssignment_statements(self, ctx:D96Parser.Assignment_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statements.
    def visitIf_statements(self, ctx:D96Parser.If_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_list_statements.
    def visitElseif_list_statements(self, ctx:D96Parser.Elseif_list_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_statement.
    def visitElseif_statement(self, ctx:D96Parser.Elseif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_statement.
    def visitElse_statement(self, ctx:D96Parser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#by_expr.
    def visitBy_expr(self, ctx:D96Parser.By_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forin_statements.
    def visitForin_statements(self, ctx:D96Parser.Forin_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_attr_access.
    def visitInstance_attr_access(self, ctx:D96Parser.Instance_attr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method_access.
    def visitInstance_method_access(self, ctx:D96Parser.Instance_method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_attr_access.
    def visitStatic_attr_access(self, ctx:D96Parser.Static_attr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_access.
    def visitStatic_method_access(self, ctx:D96Parser.Static_method_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation.
    def visitMethod_invocation(self, ctx:D96Parser.Method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation_statement.
    def visitMethod_invocation_statement(self, ctx:D96Parser.Method_invocation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statements.
    def visitBreak_statements(self, ctx:D96Parser.Break_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statements.
    def visitContinue_statements(self, ctx:D96Parser.Continue_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_expr.
    def visitReturn_expr(self, ctx:D96Parser.Return_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statements.
    def visitReturn_statements(self, ctx:D96Parser.Return_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_class_statements.
    def visitBlock_class_statements(self, ctx:D96Parser.Block_class_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statements.
    def visitBlock_statements(self, ctx:D96Parser.Block_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statements_in_main.
    def visitBlock_statements_in_main(self, ctx:D96Parser.Block_statements_in_mainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements_class.
    def visitStatements_class(self, ctx:D96Parser.Statements_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements.
    def visitStatements(self, ctx:D96Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement_class.
    def visitStatement_class(self, ctx:D96Parser.Statement_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
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


    # Visit a parse tree produced by D96Parser#expr11.
    def visitExpr11(self, ctx:D96Parser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr12.
    def visitExpr12(self, ctx:D96Parser.Expr12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_expr.
    def visitIndex_expr(self, ctx:D96Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index.
    def visitIndex(self, ctx:D96Parser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_accesses.
    def visitInstance_accesses(self, ctx:D96Parser.Instance_accessesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_access.
    def visitInstance_access(self, ctx:D96Parser.Instance_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_accesses.
    def visitStatic_accesses(self, ctx:D96Parser.Static_accessesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_access.
    def visitStatic_access(self, ctx:D96Parser.Static_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_expr.
    def visitList_expr(self, ctx:D96Parser.List_exprContext):
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


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier_list.
    def visitIdentifier_list(self, ctx:D96Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_in_func_identifier_list.
    def visitVariable_in_func_identifier_list(self, ctx:D96Parser.Variable_in_func_identifier_listContext):
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


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_type.
    def visitVariable_type(self, ctx:D96Parser.Variable_typeContext):
        return self.visitChildren(ctx)



del D96Parser
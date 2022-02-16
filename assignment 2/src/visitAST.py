from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return None

    def visitClass_declarations(self, ctx: D96Parser.Class_declarationsContext):
        return None

    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        return None

    def visitClass_inheritance(self, ctx: D96Parser.Class_inheritanceContext):
        return None

    def visitConstructor_dclr(self, ctx: D96Parser.Constructor_dclrContext):
        return None

    def visitDestructor_dclr(self, ctx: D96Parser.Destructor_dclrContext):
        return None

    def visitMethod_declaration(self, ctx: D96Parser.Method_declarationContext):
        return None

    def visitVar_variable_declaration_noinit(self, ctx: D96Parser.Var_variable_declaration_noinitContext):
        return None

    def visitVar_variable_declaration(self, ctx: D96Parser.Var_variable_declarationContext):
        return None

    def visitVar_declare_initiate_list(self, ctx: D96Parser.Var_declare_initiate_listContext):
        return None

    def visitVar_type_and_assign(self, ctx: D96Parser.Var_type_and_assignContext):
        return None

    def visitVal_variable_declaration_noinit(self, ctx: D96Parser.Val_variable_declaration_noinitContext):
        return None

    def visitVal_variable_declaration(self, ctx: D96Parser.Val_variable_declarationContext):
        return None

    def visitVal_declare_initiate_list(self, ctx: D96Parser.Val_declare_initiate_listContext):
        return None

    def visitVal_type_and_assign(self, ctx: D96Parser.Val_type_and_assignContext):
        return None

    def visitVar_both_variable_declaration_noinnit(self, ctx: D96Parser.Var_both_variable_declaration_noinnitContext):
        return None

    def visitVar_both_variable_declaration(self, ctx: D96Parser.Var_both_variable_declarationContext):
        return None

    def visitVar_both_no_value_assign_declare_list(self, ctx: D96Parser.Var_both_no_value_assign_declare_listContext):
        return None

    def visitVar_both_no_value_assign_declare(self, ctx: D96Parser.Var_both_no_value_assign_declareContext):
        return None

    def visitVar_both_declare_initiate_list(self, ctx: D96Parser.Var_both_declare_initiate_listContext):
        return None

    def visitVar_both_type_and_assign(self, ctx: D96Parser.Var_both_type_and_assignContext):
        return None

    def visitVal_both_variable_declaration_noinnit(self, ctx: D96Parser.Val_both_variable_declaration_noinnitContext):
        return None

    def visitVal_both_variable_declaration(self, ctx: D96Parser.Val_both_variable_declarationContext):
        return None

    def visitVal_both_declare_initiate_list(self, ctx: D96Parser.Val_both_declare_initiate_listContext):
        return None

    def visitVal_both_type_and_assign(self, ctx: D96Parser.Val_both_type_and_assignContext):
        return None

    def visitFunction_declaration(self, ctx: D96Parser.Function_declarationContext):
        return None

    def visitCall_func_statement(self, ctx: D96Parser.Call_func_statementContext):
        return None

    def visitCall_func(self, ctx: D96Parser.Call_funcContext):
        return None

    def visitCall_func_header(self, ctx: D96Parser.Call_func_headerContext):
        return None

    def visitCall_func_attr_list(self, ctx: D96Parser.Call_func_attr_listContext):
        return None

    def visitCall_func_attr(self, ctx: D96Parser.Call_func_attrContext):
        return None

    def visitCall_func_end(self, ctx: D96Parser.Call_func_endContext):
        return None

    def visitAssignment_statements(self, ctx: D96Parser.Assignment_statementsContext):
        return None

    def visitLhs(self, ctx: D96Parser.LhsContext):
        return None

    def visitIf_condition(self, ctx: D96Parser.If_conditionContext):
        return None

    def visitIf_statements(self, ctx: D96Parser.If_statementsContext):
        return None

    def visitElseif_list_statements(self, ctx: D96Parser.Elseif_list_statementsContext):
        return None

    def visitElseif_statement(self, ctx: D96Parser.Elseif_statementContext):
        return None

    def visitElse_statement_or_none(self, ctx: D96Parser.Else_statement_or_noneContext):
        return None

    def visitElse_statement(self, ctx: D96Parser.Else_statementContext):
        return None

    def visitBy_expr(self, ctx: D96Parser.By_exprContext):
        return None

    def visitForin_statements(self, ctx: D96Parser.Forin_statementsContext):
        return None

    def visitInstance_attr_access(self, ctx: D96Parser.Instance_attr_accessContext):
        return None

    def visitInstance_method_access(self, ctx: D96Parser.Instance_method_accessContext):
        return None

    def visitStatic_attr_access(self, ctx: D96Parser.Static_attr_accessContext):
        return None

    def visitStatic_method_access(self, ctx: D96Parser.Static_method_accessContext):
        return None

    def visitMethod_invocation(self, ctx: D96Parser.Method_invocationContext):
        return None

    def visitMethod_invocation_statement(self, ctx: D96Parser.Method_invocation_statementContext):
        return None

    def visitBreak_statements(self, ctx: D96Parser.Break_statementsContext):
        return None

    def visitContinue_statements(self, ctx: D96Parser.Continue_statementsContext):
        return None

    def visitReturn_expr(self, ctx: D96Parser.Return_exprContext):
        return None

    def visitReturn_statements(self, ctx: D96Parser.Return_statementsContext):
        return None

    def visitBlock_class_statements(self, ctx: D96Parser.Block_class_statementsContext):
        return None

    def visitBlock_statements(self, ctx: D96Parser.Block_statementsContext):
        return None

    def visitStatements_class(self, ctx: D96Parser.Statements_classContext):
        return None

    def visitStatements(self, ctx: D96Parser.StatementsContext):
        return None

    def visitStatement_class(self, ctx: D96Parser.Statement_classContext):
        return None

    def visitStatement(self, ctx: D96Parser.StatementContext):
        return None

    def visitExpr(self, ctx: D96Parser.ExprContext):
        return None

    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        return None

    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        return None

    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        return None

    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        return None

    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        return None

    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        return None

    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        return None

    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        return None

    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        return None

    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        return None

    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        return None

    def visitExpr12(self, ctx: D96Parser.Expr12Context):
        return None

    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        return None

    def visitIndex_expr(self, ctx: D96Parser.Index_exprContext):
        return None

    def visitIndex(self, ctx: D96Parser.IndexContext):
        return None

    def visitInstance_accesses(self, ctx: D96Parser.Instance_accessesContext):
        return None

    def visitInstance_access(self, ctx: D96Parser.Instance_accessContext):
        return None

    def visitStatic_accesses(self, ctx: D96Parser.Static_accessesContext):
        return None

    def visitStatic_access(self, ctx: D96Parser.Static_accessContext):
        return None

    def visitList_expr(self, ctx: D96Parser.List_exprContext):
        return None

    def visitArray_lit(self, ctx: D96Parser.Array_litContext):
        return None

    def visitArray_val(self, ctx: D96Parser.Array_valContext):
        return None

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        return None

    def visitList_parameters(self, ctx: D96Parser.List_parametersContext):
        return None

    def visitParam(self, ctx: D96Parser.ParamContext):
        return None

    def visitIdentifier_list(self, ctx: D96Parser.Identifier_listContext):
        return None

    def visitVariable_in_func_identifier_list(self, ctx: D96Parser.Variable_in_func_identifier_listContext):
        return None

    def visitValue_list(self, ctx: D96Parser.Value_listContext):
        return None

    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        return None

    def visitArray_element_type(self, ctx: D96Parser.Array_element_typeContext):
        return None

    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        return None

    def visitVariable_type(self, ctx: D96Parser.Variable_typeContext):
        return None

    
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: global_statements EOF ;
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.global_statements))


    # global_statements: global_statement global_statements | global_statement ;
    def visitGlobal_statements(self, ctx:MT22Parser.Global_statementsContext):
        if ctx.getChildCount() == 1:
            global_statement = [self.visit(ctx.global_statement())]
            
            return global_statement 
        else:
            global_statement = [self.visit(ctx.global_statement())]
            global_statements = self.visit(ctx.global_statements())

            return  global_statement + global_statements 

    # global_statement: variable_declaration_no_init 
    #                 | variable_declaration_init 
    #                 | function_declaration
    #                 | main_function;
    def visitGlobal_statement(self, ctx:MT22Parser.Global_statementContext):
        if ctx.variable_declaration_no_init():
            # print('1')
            return self.visit(ctx.variable_declaration_no_init())
        elif ctx.variable_declaration_init():
            # print('2')
            return self.visit(ctx.variable_declaration_init())

        elif ctx.function_declaration():
            # print('3')
            return self.visit(ctx.function_declaration())
            
        elif ctx.main_function():
            # print('4')
            return self.visit(ctx.main_function())



    
    # main_function: MAIN COLON FUNCTION (all_type | VOID) LB RB block_statements;
    # function_declaration: VARIABLE_IDENTIFIERS COLON FUNCTION (all_type | VOID) LB 
    #                 param_list RB (INHERIT VARIABLE_IDENTIFIERS | ) block_statements;
    def visitMain_function(self, ctx:MT22Parser.Main_functionContext):
        MAIN = Id(ctx.MAIN().getText())


        return self.visitChildren(ctx)


    def visitFunction_declaration(self, ctx:MT22Parser.Function_declarationContext):
        VARIABLE_IDENTIFIERS = Id(ctx.VARIABLE_IDENTIFIERS().getText())



        return self.visitChildren(ctx)


    # class_declaration: CLASS VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance block_class_statements;
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        VARIABLE_IN_FUNC_IDENTIFIERS = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        class_inheritance = self.visit(ctx.class_inheritance())
        block_class_statements = self.visit(ctx.block_class_statements())

        return ClassDecl(VARIABLE_IN_FUNC_IDENTIFIERS, block_class_statements, class_inheritance)


    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        return self.visitChildren(ctx)


    def visitParam_list_no_empty(self, ctx:MT22Parser.Param_list_no_emptyContext):
        return self.visitChildren(ctx)


    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)



    def visitVariable_declaration_no_init(self, ctx:MT22Parser.Variable_declaration_no_initContext):
        return self.visitChildren(ctx)


    def visitVariable_declaration_init(self, ctx:MT22Parser.Variable_declaration_initContext):
        return self.visitChildren(ctx)


    def visitVariable_declaration_init_list(self, ctx:MT22Parser.Variable_declaration_init_listContext):
        return self.visitChildren(ctx)






    def visitAssignment_statements(self, ctx:MT22Parser.Assignment_statementsContext):
        return self.visitChildren(ctx)


    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    def visitMethod_invocation_statements(self, ctx:MT22Parser.Method_invocation_statementsContext):
        return self.visitChildren(ctx)


    def visitRead_integer_function(self, ctx:MT22Parser.Read_integer_functionContext):
        return self.visitChildren(ctx)


    def visitPrint_integer_function(self, ctx:MT22Parser.Print_integer_functionContext):
        return self.visitChildren(ctx)


    def visitRead_float_function(self, ctx:MT22Parser.Read_float_functionContext):
        return self.visitChildren(ctx)


    def visitWrite_float_function(self, ctx:MT22Parser.Write_float_functionContext):
        return self.visitChildren(ctx)


    def visitRead_boolean_function(self, ctx:MT22Parser.Read_boolean_functionContext):
        return self.visitChildren(ctx)


    def visitPrint_boolean_function(self, ctx:MT22Parser.Print_boolean_functionContext):
        return self.visitChildren(ctx)


    def visitRead_string_function(self, ctx:MT22Parser.Read_string_functionContext):
        return self.visitChildren(ctx)


    def visitPrint_string_function(self, ctx:MT22Parser.Print_string_functionContext):
        return self.visitChildren(ctx)


    def visitSuper_function(self, ctx:MT22Parser.Super_functionContext):
        return self.visitChildren(ctx)


    def visitPrevent_default_function(self, ctx:MT22Parser.Prevent_default_functionContext):
        return self.visitChildren(ctx)


    def visitIf_statements(self, ctx:MT22Parser.If_statementsContext):
        return self.visitChildren(ctx)


    def visitElseif_list_statements(self, ctx:MT22Parser.Elseif_list_statementsContext):
        return self.visitChildren(ctx)


    def visitElseif_statement(self, ctx:MT22Parser.Elseif_statementContext):
        return self.visitChildren(ctx)


    def visitElse_statement(self, ctx:MT22Parser.Else_statementContext):
        return self.visitChildren(ctx)


    def visitFor_statements(self, ctx:MT22Parser.For_statementsContext):
        return self.visitChildren(ctx)


    def visitWhile_statements(self, ctx:MT22Parser.While_statementsContext):
        return self.visitChildren(ctx)


    def visitDo_while_statements(self, ctx:MT22Parser.Do_while_statementsContext):
        return self.visitChildren(ctx)


    def visitBreak_statements(self, ctx:MT22Parser.Break_statementsContext):
        return self.visitChildren(ctx)


    def visitContinue_statements(self, ctx:MT22Parser.Continue_statementsContext):
        return self.visitChildren(ctx)


    def visitReturn_expr(self, ctx:MT22Parser.Return_exprContext):
        return self.visitChildren(ctx)


    def visitReturn_statements(self, ctx:MT22Parser.Return_statementsContext):
        return self.visitChildren(ctx)


    def visitReturn_nothing_statements(self, ctx:MT22Parser.Return_nothing_statementsContext):
        return self.visitChildren(ctx)


    


    def visitBlock_statements(self, ctx:MT22Parser.Block_statementsContext):
        return self.visitChildren(ctx)


    def visitBlock_statements_no_func_decl(self, ctx:MT22Parser.Block_statements_no_func_declContext):
        return self.visitChildren(ctx)


    def visitStatements(self, ctx:MT22Parser.StatementsContext):
        return self.visitChildren(ctx)


    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    def visitStatements_no_func_decl(self, ctx:MT22Parser.Statements_no_func_declContext):
        return self.visitChildren(ctx)


    def visitStatement_no_func_decl(self, ctx:MT22Parser.Statement_no_func_declContext):
        return self.visitChildren(ctx)


    def visitStatements_no_var_no_func(self, ctx:MT22Parser.Statements_no_var_no_funcContext):
        return self.visitChildren(ctx)


    def visitStatement_no_var_no_func(self, ctx:MT22Parser.Statement_no_var_no_funcContext):
        return self.visitChildren(ctx)


    def visitBlock_in_loop_statements(self, ctx:MT22Parser.Block_in_loop_statementsContext):
        return self.visitChildren(ctx)


    def visitIn_loop_statements(self, ctx:MT22Parser.In_loop_statementsContext):
        return self.visitChildren(ctx)


    def visitIn_loop_statement(self, ctx:MT22Parser.In_loop_statementContext):
        return self.visitChildren(ctx)


    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    def visitExpr_list_no_empty(self, ctx:MT22Parser.Expr_list_no_emptyContext):
        return self.visitChildren(ctx)


    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    def visitExpr9(self, ctx:MT22Parser.Expr9Context):
        return self.visitChildren(ctx)


    def visitExpr10(self, ctx:MT22Parser.Expr10Context):
        return self.visitChildren(ctx)


    def visitArray_init(self, ctx:MT22Parser.Array_initContext):
        return self.visitChildren(ctx)


    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visitChildren(ctx)


    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    def visitAll_type(self, ctx:MT22Parser.All_typeContext):
        return self.visitChildren(ctx)


    def visitAll_type_no_void(self, ctx:MT22Parser.All_type_no_voidContext):
        return self.visitChildren(ctx)


    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    def visitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        return self.visitChildren(ctx)


    def visitVariable_id_list(self, ctx:MT22Parser.Variable_id_listContext):
        return self.visitChildren(ctx)


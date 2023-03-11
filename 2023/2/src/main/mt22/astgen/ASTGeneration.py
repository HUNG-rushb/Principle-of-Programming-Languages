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



    
    # main_function: MAIN COLON FUNCTION (all_type | VOID) LB param_list RB (INHERIT VARIABLE_IDENTIFIERS | ) 
    # block_statements;
    def visitMain_function(self, ctx:MT22Parser.Main_functionContext):
        MAIN = Id(ctx.MAIN().getText())
        
        if ctx.all_type():
            return_type = self.visit(ctx.all_type())
        elif ctx.VOID():
            return_type = ctx.VOID().getText()

        param_list = self.visit(ctx.param_list())

        if ctx.INHERIT():
            inherit = self.visit(ctx.VARIABLE_IDENTIFIERS().getText())
        else:
            inherit = None
        
        body = self.visit(ctx.block_statements())

        return FuncDecl(MAIN, return_type,param_list, inherit,body)

    # function_declaration: VARIABLE_IDENTIFIERS COLON FUNCTION (all_type | VOID) LB param_list RB 
    # (INHERIT VARIABLE_IDENTIFIERS | ) block_statements;
    def visitFunction_declaration(self, ctx:MT22Parser.Function_declarationContext):
        VARIABLE_IDENTIFIERS = Id(ctx.VARIABLE_IDENTIFIERS(0).getText())
       
        if ctx.all_type():
            return_type = self.visit(ctx.all_type())
        elif ctx.VOID():
            return_type = ctx.VOID().getText()

        param_list = self.visit(ctx.param_list())

        if ctx.INHERIT():
            inherit = self.visit(ctx.VARIABLE_IDENTIFIERS(1).getText())
        else:
            inherit = None
        
        body = self.visit(ctx.block_statements())

        return FuncDecl(MAIN, return_type,param_list, inherit,body)





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










    # expr_list: expr_list_no_empty | ;
    # expr_list_no_empty: expr COMMA expr_list_no_empty | expr;
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
         if ctx.getChildCount() == 1:
            expr = [self.visit(ctx.expr_list_no_empty())]
            return expr 
        else: 
            return []


    def visitExpr_list_no_empty(self, ctx:MT22Parser.Expr_list_no_emptyContext):
        if ctx.getChildCount() == 1:
            expr = [self.visit(ctx.expr())]
            return expr 
        elif ctx.getChildCount() == 3:
            expr = [self.visit(ctx.expr())]
            expr_list_no_empty = self.visit(ctx.expr_list_no_empty())
            return expr + expr_list_no_empty 


    # expr: expr1 DOUBLECOLONOP expr1 | expr1;
    # expr1: expr2 (EQUALOP | NOTEQUALOP | LT | GT | LTE | GTE) expr2 | expr2;
    # expr2: expr2 (ANDOP | OROP) expr3 | expr3;
    # expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
    # expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
    # expr5: NOTOP expr5 | expr6;

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


    # expr6: MINUSOP expr6 | expr7;
    # // a[1]
    # expr7: expr7 LSB expr_list_no_empty RSB | expr8;
    # // foo()
    # expr8: VARIABLE_IDENTIFIERS LB expr_list RB | expr9;
    # expr9: literal | VARIABLE_IDENTIFIERS | expr10; 
    # expr10: LB expr RB;

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









    # variable_id_list: VARIABLE_IDENTIFIERS COMMA variable_id_list | VARIABLE_IDENTIFIERS | ;
    def visitVariable_id_list(self, ctx:MT22Parser.Variable_id_listContext):
        return self.visitChildren(ctx)


    # array_init: LCB expr_list_no_empty RCB;
    def visitArray_init(self, ctx:MT22Parser.Array_initContext):
        expr_list = self.visit(ctx.expr_list_no_empty())

    # array_lit: ARRAY LSB expr_list RSB ;
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        expr_list = self.visit(ctx.expr_list())
        return ArrayLit(expr_list)

    # literal:  INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit ;
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INTLIT():
            # a = ctx.INTLIT().getText()
            return IntegerLit(int(ctx.INTLIT().getText(), 10))
        elif ctx.FLOATLIT():
            a = ctx.FLOATLIT().getText()

            if (a[0] == '.'):
                a = '0' + a
                
            return FloatLit(float(a))
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())


     # array_type: ARRAY LSB expr_list_no_empty RSB OF atomic_types;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        dimensions = self.visit(ctx.expr_list_no_empty())
        typ = self.visit(ctx.atomic_types())
        return ArrayLit(dimensions, typ)

    # all_type: atomic_types | array_type | AUTO | VOID;
    def visitAll_type(self, ctx:MT22Parser.All_typeContext):
        if ctx.atomic_types():
            return  self.visit(ctx.atomic_types())
        elif ctx.array_type():
            return  self.visit(ctx.array_type())
        elif ctx.AUTO():
            return AutoType()
        elif ctx.VOID():
            return VoidType()

    # all_type_no_void: atomic_types | array_type | AUTO ;
    def visitAll_type_no_void(self, ctx:MT22Parser.All_type_no_voidContext):
        if ctx.atomic_types():
            return  self.visit(ctx.atomic_types())
        elif ctx.array_type():
            return  self.visit(ctx.array_type())
        elif ctx.AUTO():
            return AutoType()

    # atomic_types: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        if ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()


    


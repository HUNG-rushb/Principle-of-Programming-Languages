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

        return FuncDecl(MAIN, return_type, param_list, inherit,body)









    # param_list: param_list_no_empty | ;
    # param_list_no_empty: param COMMA param_list_no_empty | param;
    # param: (INHERIT | ) (OUT | ) VARIABLE_IDENTIFIERS COLON all_type;
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        if ctx.getChildCount() == 1:
            param_list_no_empty = [self.visit(ctx.param_list_no_empty())]
            return param_list_no_empty 
        else:
            return []

    def visitParam_list_no_empty(self, ctx:MT22Parser.Param_list_no_emptyContext):
        if ctx.getChildCount() == 3:     
            a = self.visit(ctx.param())
            param_list_no_empty = self.visit(ctx.param_list_no_empty())
            return [a] + param_list_no_empty
        elif ctx.getChildCount() == 1:
            param = self.visit(ctx.param())
            return [param]

    def visitParam(self, ctx:MT22Parser.ParamContext):
        name = ctx.VARIABLE_IDENTIFIERS().getText()
        typ = self.visit(ctx.all_type())

        if ctx.INHERIT():
            inherit = True
        else:
            inherit = False

        if ctx.OUT():
            out = True
        else:
            out = False

        return ParamDecl(name, typ, out, inherit)




   


    

   
    # variable_declaration_no_init: variable_id_list COLON all_type_no_void SEMICOLON;
    def visitVariable_declaration_no_init(self, ctx:MT22Parser.Variable_declaration_no_initContext):
        name = ctx.VARIABLE_IDENTIFIERS().getText()
        typ = self.visit(ctx.all_type_no_void())

        variable_id_list = self.visit(ctx.variable_id_list())
        variable_type = self.visit(ctx.all_type_no_void())
        result = []
        
        for i in variable_id_list:
            result += [VarDecl(i, variable_type, None)] 

        return result

    # variable_declaration_init:  VARIABLE_IDENTIFIERS variable_declaration_init_list (expr | array_init) SEMICOLON;
    def visitVariable_declaration_init(self, ctx:MT22Parser.Variable_declaration_initContext):
        result = []
        name = ctx.VARIABLE_IDENTIFIERS().getText()
        variable_declaration_init_list = self.visit(ctx.variable_declaration_init_list())
        if ctx.expr():
            value = self.visit(ctx.expr())
        else:
            value = self.visit(ctx.array_init())

        if len(variable_declaration_init_list) == 1:
            typ = variable_declaration_init_list.pop(0)
            result += [VarDecl(name, typ, value)]
        else:
            length = len(variable_declaration_init_list) // 2
            typ = variable_declaration_init_list.pop(length)

            variable_declaration_init_list.append(expr)
            variable_declaration_init_list.insert(0, name)

            length = len(variable_declaration_init_list) // 2
            id_half = variable_declaration_init_list[:length]
            init_value_half = variable_declaration_init_list[length:]

            for id_loop, expr_loop in zip(id_half, init_value_half):
                result += [VarDecl(id_loop, typ, expr_loop)]
            
        return result

        
    # variable_declaration_init_list: COMMA VARIABLE_IDENTIFIERS variable_declaration_init_list (expr | array_init) COMMA
    #                                 | COLON all_type_no_void EQUAL ;
    def visitVariable_declaration_init_list(self, ctx:MT22Parser.Variable_declaration_init_listContext):
        if ctx.getChildCount() == 5:
            name = ctx.VARIABLE_IDENTIFIERS().getText()
            variable_declaration_init_list = self.visit(ctx.variable_declaration_init_list())
            if ctx.expr():
                value = self.visit(ctx.expr())
            else:
                value = self.visit(ctx.array_init())

            return [name] + variable_declaration_init_list + [value]
        else: 
            return [self.visit(ctx.all_type_no_void())]













    # assignment_statements: lhs EQUAL expr SEMICOLON;
    # lhs: VARIABLE_IDENTIFIERS | VARIABLE_IDENTIFIERS LSB expr_list_no_empty RSB; 
    def visitAssignment_statements(self, ctx:MT22Parser.Assignment_statementsContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)


    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.getChildCount() == 4:
            name = ctx.VARIABLE_IDENTIFIERS().getText()     
            cell = self.visit(ctx.expr_list_no_empty())
            return ArrayCell(name, cell)
        elif ctx.getChildCount() == 1:
            return ctx.VARIABLE_IDENTIFIERS().getText()

    # method_invocation_statements: (VARIABLE_IDENTIFIERS LB expr_list RB 
    #                             | read_integer_function
    #                             | print_integer_function
    #                             | read_float_function
    #                             | write_float_function
    #                             | read_boolean_function
    #                             | print_boolean_function
    #                             | read_string_function
    #                             | print_string_function
    #                             | super_function
    #                             | prevent_default_function) SEMICOLON;
    def visitMethod_invocation_statements(self, ctx:MT22Parser.Method_invocation_statementsContext):
        if ctx.getChildCount() == 4:
            name = ctx.VARIABLE_IDENTIFIERS().getText()
            args = self.visit(ctx.expr_list())
            return CallStmt(name, args)
        elif ctx.read_integer_function():
            return self.visit(ctx.read_integer_function())
        elif ctx.print_integer_function():
           return self.visit(ctx.print_integer_function()) 
        elif ctx.read_float_function():
            return self.visit(ctx.read_float_function())
        elif ctx.write_float_function():
            return self.visit(ctx.write_float_function())
        elif ctx.read_boolean_function():
            return self.visit(ctx.read_boolean_function())
        elif ctx.print_boolean_function():
            return self.visit(ctx.print_boolean_function())
        elif ctx.read_string_function():
            return self.visit(ctx.read_string_function())
        elif ctx.print_string_function():
            return self.visit(ctx.print_string_function())
        elif ctx.super_function():
            return self.visit(ctx.super_function())
        elif ctx.prevent_default_function():
            return self.visit(ctx.prevent_default_function())















    # read_integer_function: READ_INTEGER LB expr_list RB;
    # print_integer_function: PRINT_INTEGER LB expr_list RB;
    def visitRead_integer_function(self, ctx:MT22Parser.Read_integer_functionContext):
        name = ctx.READ_INTEGER().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    def visitPrint_integer_function(self, ctx:MT22Parser.Print_integer_functionContext):
        name = ctx.PRINT_INTEGER().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    # read_float_function: READ_FLOAT LB expr_list RB;
    # write_float_function: WRITE_FLOAT LB expr_list RB;
    def visitRead_float_function(self, ctx:MT22Parser.Read_float_functionContext):
        name = ctx.READ_FLOAT().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    def visitWrite_float_function(self, ctx:MT22Parser.Write_float_functionContext):
        name = ctx.WRITE_FLOAT().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    # read_boolean_function: READ_BOOLEAN LB expr_list RB;
    # print_boolean_function: PRINT_BOOLEAN LB expr_list RB;
    def visitRead_boolean_function(self, ctx:MT22Parser.Read_boolean_functionContext):
        name = ctx.READ_BOOLEAN().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    def visitPrint_boolean_function(self, ctx:MT22Parser.Print_boolean_functionContext):
        name = ctx.PRINT_BOOLEAN().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    # read_string_function: READ_STRING LB expr_list RB;
    # print_string_function: PRINT_STRING LB expr_list RB;
    def visitRead_string_function(self, ctx:MT22Parser.Read_string_functionContext):
        name = ctx.READ_STRING().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    def visitPrint_string_function(self, ctx:MT22Parser.Print_string_functionContext):
        name = ctx.PRINT_STRING().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    # super_function: SUPER LB expr_list RB;
    # prevent_default_function: PREVENT_DEFAULT LB expr_list RB;
    def visitSuper_function(self, ctx:MT22Parser.Super_functionContext):
        name = ctx.SUPER().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)

    def visitPrevent_default_function(self, ctx:MT22Parser.Prevent_default_functionContext):
        name = ctx.PREVENT_DEFAULT().getText()
        args = self.visit(ctx.expr_list())
        return CallStmt(name, args)











    

    # if_statements: IF LB expr RB (block_statements | statement) elseif_list_statements ;
    def visitIf_statements(self, ctx:MT22Parser.If_statementsContext):
        cond = self.visit(ctx.expr())

        if ctx.block_statements():
            tstmt =  self.visit(ctx.block_statements())
        else: 
            tstmt = self.visit(ctx.statement())

        fstmt = self.visit(ctx.elseif_list_statements())

        return [IfStmt(cond, tstmt, fstmt)]

    # elseif_list_statements: elseif_statement | else_statement | ;
    def visitElseif_list_statements(self, ctx:MT22Parser.Elseif_list_statementsContext):
        if ctx.elseif_statement():
            return self.visit(ctx.elseif_statement())
        elif ctx.else_statement():
            return self.visit(ctx.else_statement())
        else: 
            return None

    # elseif_statement: ELSE IF LB expr RB (block_statements | statement) elseif_list_statements;
    def visitElseif_statement(self, ctx:MT22Parser.Elseif_statementContext):
        cond = self.visit(ctx.expr())

        if ctx.block_statements():
            tstmt =  self.visit(ctx.block_statements())
        else: 
            tstmt = self.visit(ctx.statement())

        fstmt = self.visit(ctx.elseif_list_statements())

        return IfStmt(cond, tstmt, fstmt)

    # else_statement: ELSE (block_statements | statement) | ;
    def visitElse_statement(self, ctx:MT22Parser.Else_statementContext):
        if ctx.getChildCount() == 2:
            if ctx.block_statements():
                return self.visit(ctx.block_statements())
            elif ctx.statement():
                return self.visit(ctx.statement())
        else:
            return []

        











    # for_statements: FOR LB VARIABLE_IDENTIFIERS EQUAL expr COMMA expr COMMA expr RB
    #            (block_statements_no_func_decl | statement_no_var_no_func);
    def visitFor_statements(self, ctx:MT22Parser.For_statementsContext):
        init = AssignStmt( ctx.VARIABLE_IDENTIFIERS().getText(), self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        upd  = self.visit(ctx.expr(2))
        if ctx.block_statements_no_func_decl():
            stmt =  self.visit(ctx.block_statements_no_func_decl())
        elif ctx.statement_no_var_no_func():
            stmt =  self.visit(ctx.statement_no_var_no_func())

        return ForStmt(init, cond, upd, stmt)






    # while_statements: WHILE LB expr RB (block_statements_no_func_decl | statement_no_var_no_func);
    def visitWhile_statements(self, ctx:MT22Parser.While_statementsContext):
        cond = self.visit(ctx.expr())
        
        if ctx.block_statements_no_func_decl():
            stmt =  self.visit(ctx.block_statements_no_func_decl())
        elif ctx.statement_no_var_no_func():
            stmt =  self.visit(ctx.statement_no_var_no_func())

        return WhileStmt(cond, stmt)




    # do_while_statements: DO block_statements_no_func_decl WHILE LB expr RB SEMICOLON;
    def visitDo_while_statements(self, ctx:MT22Parser.Do_while_statementsContext):
        cond = self.visit(ctx.expr())
        stmt =  self.visit(ctx.block_statements_no_func_decl())
        return DoWhileStmt(cond, stmt)

    







    # break_statements: BREAK SEMICOLON;
    # continue_statements: CONTINUE SEMICOLON;
    def visitBreak_statements(self, ctx:MT22Parser.Break_statementsContext):
        return BreakStmt()


    def visitContinue_statements(self, ctx:MT22Parser.Continue_statementsContext):
        return ContinueStmt()


    # return_expr: expr | ;
    # return_statements: RETURN return_expr SEMICOLON;
    # return_nothing_statements: RETURN SEMICOLON;
    def visitReturn_expr(self, ctx:MT22Parser.Return_exprContext):
        if ctx.getChildCount() == 1:
            expr = self.visit(ctx.expr())
            return expr 
        else:
            return None

    def visitReturn_statements(self, ctx:MT22Parser.Return_statementsContext):
        return ReturnStmt(self.visit(ctx.return_expr()))


    def visitReturn_nothing_statements(self, ctx:MT22Parser.Return_nothing_statementsContext):
        return ReturnStmt(None)


    





    

    # block_statements: LCB statements RCB;
    # block_statements_no_func_decl: LCB statements_no_func_decl RCB;
    def visitBlock_statements(self, ctx:MT22Parser.Block_statementsContext):
        return BlockStmt(self.visit(ctx.statements()))


    def visitBlock_statements_no_func_decl(self, ctx:MT22Parser.Block_statements_no_func_declContext):
        return BlockStmt(self.visit(ctx.statements_no_func_decl()))

    # statements: statement statements | statement | ;
    def visitStatements(self, ctx:MT22Parser.StatementsContext):
        if ctx.getChildCount() == 1:
            statement = self.visit(ctx.statement())
            return statement
        elif ctx.getChildCount() == 2:
            statement = self.visit(ctx.statement())
            statements = self.visit(ctx.statements())
            return statement + statements 
        else: 
            return []

    # statement:  variable_declaration_no_init 
    #             | variable_declaration_init 
    #             | function_declaration 
    #             | assignment_statements 
    #             | if_statements 
    #             | for_statements 
    #             | while_statements
    #             | do_while_statements
    #             | method_invocation_statements
    #             | return_statements 
    #             | return_nothing_statements
    #             | in_loop_statement
    #             | block_statements;
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        if ctx.variable_declaration_no_init():
            return self.visit(ctx.variable_declaration_no_init())
        elif ctx.variable_declaration_init():
            return self.visit(ctx.variable_declaration_init())
        elif ctx.function_declaration():
            return self.visit(ctx.function_declaration())
        elif ctx.assignment_statements():
            return self.visit(ctx.assignment_statements())
        elif ctx.if_statements():
            return self.visit(ctx.if_statements())
        elif ctx.for_statements():
            return self.visit(ctx.for_statements())
        elif ctx.while_statements():
            return self.visit(ctx.while_statements())
        elif ctx.do_while_statements():
            return self.visit(ctx.do_while_statements())
        elif ctx.method_invocation_statements():
            return self.visit(ctx.method_invocation_statements())
        elif ctx.return_statements():
            return self.visit(ctx.return_statements())
        elif ctx.return_nothing_statements():
            return self.visit(ctx.return_nothing_statements())
        elif ctx.in_loop_statement():
            return self.visit(ctx.in_loop_statement())
        elif ctx.block_statements():
            return self.visit(ctx.block_statements())








    # statements_no_func_decl: statement_no_func_decl statements_no_func_decl | statement_no_func_decl | ;
    def visitStatements_no_func_decl(self, ctx:MT22Parser.Statements_no_func_declContext):
        return self.visitChildren(ctx)

    # statement_no_func_decl:  variable_declaration_no_init 
    #                         | variable_declaration_init 
    #                         | assignment_statements 
    #                         | if_statements 
    #                         | for_statements 
    #                         | while_statements
    #                         | do_while_statements
    #                         | method_invocation_statements
    #                         | return_statements 
    #                         | return_nothing_statements
    #                         | in_loop_statement
    #                         | block_statements_no_func_decl;
    def visitStatement_no_func_decl(self, ctx:MT22Parser.Statement_no_func_declContext):
        return self.visitChildren(ctx)












    # statements_no_var_no_func: statement_no_var_no_func statements_no_var_no_func | statement_no_var_no_func | ;
    def visitStatements_no_var_no_func(self, ctx:MT22Parser.Statements_no_var_no_funcContext):
        return self.visitChildren(ctx)

    # statement_no_var_no_func: assignment_statements 
    #                         | if_statements 
    #                         | for_statements 
    #                         | while_statements
    #                         | do_while_statements
    #                         | method_invocation_statements
    #                         | return_statements 
    #                         | return_nothing_statements
    #                         | in_loop_statement
    #                         | block_statements;
    def visitStatement_no_var_no_func(self, ctx:MT22Parser.Statement_no_var_no_funcContext):
        return self.visitChildren(ctx)







    # def visitBlock_in_loop_statements(self, ctx:MT22Parser.Block_in_loop_statementsContext):
    #     return self.visitChildren(ctx)


    # def visitIn_loop_statements(self, ctx:MT22Parser.In_loop_statementsContext):
    #     return self.visitChildren(ctx)

    # in_loop_statement: break_statements | continue_statements;
    def visitIn_loop_statement(self, ctx:MT22Parser.In_loop_statementContext):
        if ctx.break_statements():
            return self.visit(ctx.break_statements())
        elif ctx.continue_statements():
            return self.visit(ctx.continue_statements())










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

    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 3:
            operand = ctx.DOUBLECOLONOP().getText()
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))

            return BinaryOp(operand, left, right)
        else:  
            return self.visit(ctx.expr1())


    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            if ctx.EQUALOP():
                operand = ctx.EQUALOP().getText()
            elif ctx.NOTEQUALOP():
                operand = ctx.NOTEQUALOP().getText()
            elif ctx.LT():
                operand = ctx.LT().getText()
            elif ctx.GT():
                operand = ctx.GT().getText()
            elif ctx.LTE():
                operand = ctx.LTE().getText()
            else:
                operand = ctx.GTE().getText()

            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))

            return BinaryOp(operand, left, right)
        else:  
            return self.visit(ctx.expr2())

    # expr2: expr2 (ANDOP | OROP) expr3 | expr3;
    # expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            if ctx.ANDOP():
                operand = ctx.ANDOP().getText()
            else:
                operand = ctx.OROP().getText()

            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())

            return BinaryOp(operand, left, right)
        else:  
            return self.visit(ctx.expr3())

    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            if ctx.PLUSOP():
                operand = ctx.PLUSOP().getText()
            else:
                operand = ctx.MINUSOP().getText()

            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())

            return BinaryOp(operand, left, right)
        else:  
            return self.visit(ctx.expr4())

    # expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
    # expr5: NOTOP expr5 | expr6;
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            if ctx.MULTIPLYOP():
                operand = ctx.MULTIPLYOP().getText()
            elif ctx.DIVIDEOP():
                operand = ctx.DIVIDEOP().getText()
            else:
                operand = ctx.MODULOOP().getText()

            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())

            return BinaryOp(operand, left, right)
        else:  
            return self.visit(ctx.expr5())

    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            operand = ctx.NOTOP().getText()
            body = self.visit(ctx.expr5())
            return UnaryOp(operand, body)
        else:  
            return self.visit(ctx.expr6())

    # expr6: MINUSOP expr6 | expr7;
    # expr7: expr7 LSB expr_list_no_empty RSB | expr8;
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            operand = ctx.MINUSOP().getText()
            body = self.visit(ctx.expr6())

            return UnaryOp(operand, body)
        else:  
            return self.visit(ctx.expr7())

    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.getChildCount() == 4:
            name = self.visit(ctx.expr7())
            expr_list_no_empty = self.visit(ctx.expr_list_no_empty())

            return ArrayCell(name, expr_list_no_empty)
        else:  
            return self.visit(ctx.expr8())

    # expr8: VARIABLE_IDENTIFIERS LB expr_list RB | expr9;
    # expr9: literal | VARIABLE_IDENTIFIERS | expr10; 
    # expr10: LB expr RB;
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if ctx.getChildCount() == 4:
            name = ctx.VARIABLE_IDENTIFIERS().getText()
            expr_list = self.visit(ctx.expr_list())

            return FuncCall(name, expr_list)
        else:  
            return self.visit(ctx.expr9())

    def visitExpr9(self, ctx:MT22Parser.Expr9Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.VARIABLE_IDENTIFIERS():
            return Id(ctx.VARIABLE_IDENTIFIERS().getText())
        else:  
            return self.visit(ctx.expr10())


    def visitExpr10(self, ctx:MT22Parser.Expr10Context):
        return self.visit(ctx.expr())









    # variable_id_list: VARIABLE_IDENTIFIERS COMMA variable_id_list | VARIABLE_IDENTIFIERS | ;
    def visitVariable_id_list(self, ctx:MT22Parser.Variable_id_listContext):
        if ctx.getChildCount() == 3:     
            a = Id(ctx.VARIABLE_IDENTIFIERS().getText())
            identifier_list = self.visit(ctx.identifier_list())
            return [a] + identifier_list
        elif ctx.getChildCount() == 1:
            a = Id(ctx.VARIABLE_IDENTIFIERS().getText())
            return [a]
        else: 
            return []


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


    


from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    # Program 
    # program: class_declarations EOF;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(self.visit(ctx.class_declarations()))

    # Class declaration
    # class_declarations: class_declaration class_declarations | class_declaration ;
    def visitClass_declarations(self, ctx: D96Parser.Class_declarationsContext):
        if ctx.getChildCount() == 1:
            class_declaration = [self.visit(ctx.class_declaration())]
            
            return class_declaration 
        else:
            class_declaration = [self.visit(ctx.class_declaration())]
            class_declarations = self.visit(ctx.class_declarations())

            return  class_declaration + class_declarations 
    
    # class_inheritance: COLON VARIABLE_IN_FUNC_IDENTIFIERS | ;
    def visitClass_inheritance(self, ctx: D96Parser.Class_inheritanceContext):
        if ctx.getChildCount() == 2:
            return Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        else:
            return None

    # class_declaration: CLASS VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance block_class_statements;
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        VARIABLE_IN_FUNC_IDENTIFIERS = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        class_inheritance = self.visit(ctx.class_inheritance())
        block_class_statements = self.visit(ctx.block_class_statements())

        return ClassDecl(VARIABLE_IN_FUNC_IDENTIFIERS, block_class_statements, class_inheritance)

    



    # Constructor Destructor
    # constructor_dclr: CONSTRUCTOR LB list_parameters RB block_statements;
    def visitConstructor_dclr(self, ctx: D96Parser.Constructor_dclrContext):
        si = Instance() 
        name = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())

        return MethodDecl(si, name, list_parameters, block_statements)

    # destructor_dclr: DESTRUCTOR LB RB block_statements;
    def visitDestructor_dclr(self, ctx: D96Parser.Destructor_dclrContext):
        si = Instance()
        name = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())
        
        return MethodDecl(si, name, list_parameters, block_statements)




    #  Method declaration
    # method_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
    def visitMethod_declaration(self, ctx: D96Parser.Method_declarationContext):
        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            name = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            si = Instance()
        else:
            name = Id(ctx.DOLLAR_IDENTIFIERS().getText())
            si = Static()

        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())
       
        return MethodDecl(si, name, list_parameters, block_statements)





    #  STATEMENTS ------------------------------------------------------------------------------------------------------

    # Variable declaration ****************************************************************************
    # variable_declaration: (VAR | VAL) (declare_initiate_list | no_value_assign_declare_list) SEMICOLON;
    def visitVar_variable_declaration(self, ctx: D96Parser.Var_variable_declarationContext):
        if ctx.VAR():
            variable = Id()
            varType = Type()
            
            return VarDecl(variable, varType, )
        else:
            return ConstDecl()

    # no_value_assign_declare_list: no_value_assign_declare no_value_assign_declare_list| no_value_assign_declare;
    def visitVar_no_value_assign_declare_list(self, ctx: D96Parser.Var_no_value_assign_declare_listContext):
        if ctx.getChildCount() == 1:
            no_value_assign_declare = [self.visit(ctx.no_value_assign_declare())]

            return no_value_assign_declare 
        else:
            no_value_assign_declare = [self.visit(ctx.no_value_assign_declare())]
            no_value_assign_declare_list = self.visit(ctx.no_value_assign_declare_list())

            return [self.visit(ctx.no_value_assign_declare())] + no_value_assign_declare_list 

    # no_value_assign_declare: VARIABLE_IN_FUNC_IDENTIFIERS COMMA | VARIABLE_IN_FUNC_IDENTIFIERS | COLON variable_type;
    def visitVar_no_value_assign_declare(self, ctx: D96Parser.Var_no_value_assign_declareContext):
        return

    # declare_initiate_list: VARIABLE_IN_FUNC_IDENTIFIERS type_and_assign expr
    #                             | variable_in_func_identifier_list COLON variable_type;
    def visitVar_declare_initiate_list(self, ctx: D96Parser.Var_declare_initiate_listContext):
        return

    # type_and_assign: COMMA VARIABLE_IN_FUNC_IDENTIFIERS type_and_assign expr COMMA
    #                     | COLON variable_type ASSIGNOP;
    def visitVar_type_and_assign(self, ctx: D96Parser.Var_type_and_assignContext):
        return






    def visitVal_variable_declaration(self, ctx: D96Parser.Val_variable_declarationContext):
        return None

    def visitVal_no_value_assign_declare_list(self, ctx: D96Parser.Val_no_value_assign_declare_listContext):
        return None

    def visitVal_no_value_assign_declare(self, ctx: D96Parser.Val_no_value_assign_declareContext):
        return None

    def visitVal_declare_initiate_list(self, ctx: D96Parser.Val_declare_initiate_listContext):
        return None

    def visitVal_type_and_assign(self, ctx: D96Parser.Val_type_and_assignContext):
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




    def visitVal_both_variable_declaration(self, ctx: D96Parser.Val_both_variable_declarationContext):
        return None

    def visitVal_both_no_value_assign_declare_list(self, ctx: D96Parser.Val_both_no_value_assign_declare_listContext):
        return None

    def visitVal_both_no_value_assign_declare(self, ctx: D96Parser.Val_both_no_value_assign_declareContext):
        return None

    def visitVal_both_declare_initiate_list(self, ctx: D96Parser.Val_both_declare_initiate_listContext):
        return None

    def visitVal_both_type_and_assign(self, ctx: D96Parser.Val_both_type_and_assignContext):
        return None














    # Function declaration
    # function_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
    def visitFunction_declaration(self, ctx: D96Parser.Function_declarationContext):
        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            name = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            si = Instance()
        else:
            name = Id(ctx.DOLLAR_IDENTIFIERS().getText())
            si = Static()

        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())
       
        return MethodDecl(si, name, list_parameters, block_statements)













    # call_func_statement: call_func_header call_func_attr_list call_func_end SEMICOLON;
    def visitCall_func_statement(self, ctx: D96Parser.Call_func_statementContext):
        return

    # call_func: call_func_header call_func_attr_list call_func_end;
    def visitCall_func(self, ctx: D96Parser.Call_funcContext):
        call_func_header = self.visit(ctx.call_func_header())
        call_func_attr_list = self.visit(ctx.call_func_attr_list())
        call_func_end = self.visit(ctx.call_func_end())
        return CallStmt()

    # call_func_header: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) (index_operators | ) (DOUBLECOLONOP DOLLAR_IDENTIFIERS | );
    def visitCall_func_header(self, ctx: D96Parser.Call_func_headerContext):
        return

    # call_func_attr_list: call_func_attr call_func_attr_list | call_func_attr | ;
    def visitCall_func_attr_list(self, ctx: D96Parser.Call_func_attr_listContext):
        return
        
    # call_func_attr: DOT (VARIABLE_IN_FUNC_IDENTIFIERS | VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB);                 
    def visitCall_func_attr(self, ctx: D96Parser.Call_func_attrContext):
        return
                   
    # call_func_end: DOT VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB;
    def visitCall_func_end(self, ctx: D96Parser.Call_func_endContext):
        VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
        value_list = self.visit(ctx.value_list())
        return VARIABLE_IN_FUNC_IDENTIFIERS + value_list
        










    # Assignment statement
    # assignment_statements: lhs ASSIGNOP expr SEMICOLON;
    def visitAssignment_statements(self, ctx: D96Parser.Assignment_statementsContext):
        lhs = Expr(self.visit(ctx.lhs()))
        expr = Expr(self.visit(ctx.expr()))

        return  Assign(lhs, expr)
        
    # lhs: (VARIABLE_IN_FUNC_IDENTIFIERS 
    #         | instance_attr_access 
    #         | static_attr_access 
    #         ) (index_operators | );
    def visitLhs(self, ctx: D96Parser.LhsContext):
        return
        








    # If statements 
    # if_condition: LB expr RB;
    def visitIf_condition(self, ctx: D96Parser.If_conditionContext):
        return self.visit(ctx.expr())

    # if_statements: IF LB expr RB block_statements (elseif_list_statements else_statement | elseif_list_statements | else_statement | );
    def visitIf_statements(self, ctx: D96Parser.If_statementsContext):
        return
        
    # elseif_list_statements: elseif_statement elseif_list_statements |  elseif_statement;
    def visitElseif_list_statements(self, ctx: D96Parser.Elseif_list_statementsContext):
        return
        
    # elseif_statement: ELSEIF LB expr RB block_statements;
    def visitElseif_statement(self, ctx: D96Parser.Elseif_statementContext):
        return
    
    # else_statement_or_none: else_statement | ; 
    def visitElse_statement_or_none(self, ctx: D96Parser.Else_statement_or_noneContext):
        return

    # else_statement: ELSE block_statements;
    def visitElse_statement(self, ctx: D96Parser.Else_statementContext):
        return
        






    # For In statement
    # by_expr: (BY expr) | ;
    def visitBy_expr(self, ctx: D96Parser.By_exprContext):
        return
        
    # forin_statements: FOREACH LB (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) 
    #                     IN expr DOUBLEDOTOP expr by_expr RB block_statements;
    def visitForin_statements(self, ctx: D96Parser.Forin_statementsContext):
        return






    # Member access
    # instance_attr_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS;
    def visitInstance_attr_access(self, ctx: D96Parser.Instance_attr_accessContext):
        return
        
    # instance_method_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;
    def visitInstance_method_access(self, ctx: D96Parser.Instance_method_accessContext):
        return
        
    # static_attr_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS;
    def visitStatic_attr_access(self, ctx: D96Parser.Static_attr_accessContext):
        return
        
    # static_method_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;
    def visitStatic_method_access(self, ctx: D96Parser.Static_method_accessContext):
        return
        






    # Method invocation statement
    # method_invocation: instance_method_access | static_method_access;
    def visitMethod_invocation(self, ctx: D96Parser.Method_invocationContext):
        return
        
    # method_invocation_statement: method_invocation SEMICOLON;
    def visitMethod_invocation_statement(self, ctx: D96Parser.Method_invocation_statementContext):
        return







    # Break statement
    # break_statements: BREAK SEMICOLON;
    def visitBreak_statements(self, ctx: D96Parser.Break_statementsContext):
        return Break()
        
    # Continue statement
    # continue_statements: CONTINUE SEMICOLON;
    def visitContinue_statements(self, ctx: D96Parser.Continue_statementsContext):
        return Continue()
        
    # Return statement
    # return_expr: expr | ;
    def visitReturn_expr(self, ctx: D96Parser.Return_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr())
        else:
            return [] 
        
    # return_statements: RETURN return_expr SEMICOLON;
    def visitReturn_statements(self, ctx: D96Parser.Return_statementsContext):
        return_expr = Expr(self.visit(ctx.return_expr()))
        return Return(return_expr)
        









    # Block statements ---------------------------------------------------------------------------------
    
    #*************************************************************************************
    # block_class_statements: LCB statements_class RCB;
    def visitBlock_class_statements(self, ctx: D96Parser.Block_class_statementsContext):
        return self.visit(ctx.statements_class())
        
    # block_statements: LCB statements RCB;
    def visitBlock_statements(self, ctx: D96Parser.Block_statementsContext):
        return self.visit(ctx.statements())







    # statements_class: statement_class statements_class | statement_class | ;
    def visitStatements_class(self, ctx: D96Parser.Statements_classContext):
        if ctx.getChildCount() == 1:
            statement_class = self.visit(ctx.statement_class())
            # return Block([], statement_class) 
            return [statement_class]

        elif ctx.getChildCount() == 2:
            statement_class = self.visit(ctx.statement_class())
            statements_class = self.visit(ctx.statements_class())
            return [statement_class] + statements_class 

        else: 
            return []
        
    # statements: statement statements | statement | ;
    def visitStatements(self, ctx: D96Parser.StatementsContext):
        if ctx.getChildCount() == 1:
            statement = [self.visit(ctx.statement())]
            return [statement] 

        elif ctx.getChildCount() == 2:
            statement = [self.visit(ctx.statement())]
            statements = self.visit(ctx.statements())
            return [statement] + statements 

        else: 
            return Block([])
        





        
    # statement_class: var_both_variable_declaration
    #                 | val_both_variable_declaration
    #                 | function_declaration
    #                 | constructor_dclr
    #                 | destructor_dclr ;
    def visitStatement_class(self, ctx: D96Parser.Statement_classContext):
        if ctx.var_both_variable_declaration():
            return self.visit(ctx.var_both_variable_declaration())
        elif ctx.val_both_variable_declaration():
            return self.visit(ctx.val_both_variable_declaration())
        elif ctx.function_declaration():
            return self.visit(ctx.function_declaration())
        elif ctx.constructor_dclr():
            return self.visit(ctx.constructor_dclr())
        else:
            return self.visit(ctx.destructor_dclr())
        
    # no function declaration
    #  no $
# statement: var_variable_declaration 
#             | val_variable_declaration 
#             | assignment_statements 
#             | if_statements 
#             | forin_statements 
#             | call_func_statement
#             | method_invocation_statement
#             | break_statements
#             | continue_statements
#             | return_statements ;
    def visitStatement(self, ctx: D96Parser.StatementContext):
        if ctx.var_variable_declaration():
            self.visit(ctx.var_variable_declaration())
        elif ctx.val_variable_declaration():
            self.visit(ctx.val_variable_declaration())
        elif ctx.assignment_statements():
            self.visit(ctx.assignment_statements())
        elif ctx.if_statements():
            self.visit(ctx.if_statements())
        elif ctx.forin_statements():
            self.visit(ctx.forin_statements())
        elif ctx.call_func_statement():
            self.visit(ctx.call_func_statement())
        elif ctx.method_invocation_statement():
            self.visit(ctx.method_invocation_statement())
        elif ctx.break_statements():
            self.visit(ctx.break_statements())
        elif ctx.continue_statements():
            self.visit(ctx.continue_statements())
        else:
            self.visit(ctx.return_statements())
        


















































    # EXPRESSIONS ----------------------------------------------------------------------------------
    # Ưu tiên gọi access trước

    # expr: expr1 (STRCONCATOP | STREQUALOP) expr1 | expr1;
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount() == 3:
            if ctx.STRCONCATOP():
                operand = ctx.STRCONCATOP().getText()
            else:
                operand = ctx.STREQUALOP().getText()

            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))

            return BinaryOp(operand, left, right)
            
        else:  
            return self.visit(ctx.expr1(0))
            
        
    # expr1: expr2 (EQUALOP | NOTEQUALOP | LT | GT | LTE | GTE) expr2 | expr2;
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
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
            return self.visit(ctx.expr2(0))
        
    # expr2: expr2 (ANDOP | OROP) expr3 | expr3;
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            if ctx.ANDOP():
                operand = ctx.ANDOP().getText()
            else:
                operand = ctx.OROP().getText()

            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())

            return BinaryOp(operand, left, right)
            
        else:  
            return self.visit(ctx.expr3(0))
        
    # expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            if ctx.PLUSOP():
                operand = ctx.PLUSOP().getText()
            else:
                operand = ctx.MINUSOP().getText()

            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())

            return BinaryOp(operand, left, right)
            
        else:  
            return self.visit(ctx.expr4(0))
        
    # expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
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
            return self.visit(ctx.expr5(0))
        
    # expr5: NOTOP expr5 | expr6;
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            operand = ctx.NOTOP().getText()
            body = self.visit(ctx.expr5())

            return UnaryOp(operand, body)
            
        else:  
            return self.visit(ctx.expr6())
        
    # expr6: MINUSOP expr6 | expr7;
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            operand = ctx.MINUSOP().getText()
            body = self.visit(ctx.expr6())

            return UnaryOp(operand, body)
            
        else:  
            return self.visit(ctx.expr7())
        
    # expr7: expr7 index_operators | expr8;
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.getChildCount() == 2:
            expr7 = self.visit(ctx.expr7())
            index_operators = self.visit(ctx.index_operators())

            return ArrayCell(expr7, index_operators)
            
        else:  
            return self.visit(ctx.expr8())
        
    # expr8: expr8 instance_accesses | expr9;
    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount() == 2:
            obj = self.visit(ctx.expr7())
            fieldname = self.visit(ctx.instance_accesses())

            return FieldAccess(obj, fieldname)
            
        else:  
            return self.visit(ctx.expr9())
        
    # expr9: VARIABLE_IN_FUNC_IDENTIFIERS static_accesses | expr10;
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount() == 2:
            operand = ctx.MINUSOP().getText()
            body = self.visit(ctx.expr6())

            return UnaryOp(operand, body)
            
        else:  
            return self.visit(ctx.expr10())
        
    # expr10: NEW expr LB list_expr RB | expr11;
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.getChildCount() == 2:
            operand = ctx.MINUSOP().getText()
            body = self.visit(ctx.expr6())

            return UnaryOp(operand, body)
            
        else:  
            return self.visit(ctx.expr11())
        
    # expr11: literal 
    #         | VARIABLE_IN_FUNC_IDENTIFIERS 
    #         | SELF 
    #         | expr12; 
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.getChildCount() == 2:
            operand = ctx.MINUSOP().getText()
            body = self.visit(ctx.expr6())

            return UnaryOp(operand, body)
            
        else:  
            return self.visit(ctx.expr12())
        
    # expr12: LB expr RB;
    def visitExpr12(self, ctx: D96Parser.Expr12Context):
        return self.visit(ctx.expr())
        








    # a[1][2]
    # index_operators: index_operators LSB expr RSB  | LSB expr RSB ;
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount() == 1:
            expr = [self.visit(ctx.expr())]
            return expr 
        else:
            expr = [self.visit(ctx.expr())]
            index_operators = self.visit(ctx.index_operators())
            return [self.visit(ctx.expr())] + index_operators 
        
        
    # index_expr: index | index index_operators;
    def visitIndex_expr(self, ctx: D96Parser.Index_exprContext):
        if ctx.getChildCount() == 1:
            index = [self.visit(ctx.index())]

            return index 
        # else:
        #     expr = [self.visit(ctx.expr())]
        #     index_operators = self.visit(ctx.index_operators())

        #     return [self.visit(ctx.expr())] + index_operators 
        
    # index: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)
    #         | (expr instance_attr_access (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)) | ;
    def visitIndex(self, ctx: D96Parser.IndexContext):
        return
        







        
    # Instance, Static accesses
    # instance_accesses: instance_access instance_accesses | instance_access;
    def visitInstance_accesses(self, ctx: D96Parser.Instance_accessesContext):
        if ctx.getChildCount() == 1:
            instance_access = [self.visit(ctx.instance_access())]
            return instance_access 
        else:
            instance_access = [self.visit(ctx.instance_access())]
            instance_accesses = self.visit(ctx.instance_accesses())
            return [self.visit(ctx.instance_access())] + instance_accesses
    
    # *********************************************************************************************************************
    # instance_access:  DOT VARIABLE_IN_FUNC_IDENTIFIERS
    #                 | DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;
    def visitInstance_access(self, ctx: D96Parser.Instance_accessContext):
        if ctx.getChildCount() == 2:
            VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            return Id(VARIABLE_IN_FUNC_IDENTIFIERS) 
            
        # else:
        #     VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
        #     list_expr = self.visit(ctx.list_expr())
        #     return VARIABLE_IN_FUNC_IDENTIFIERS  + list_expr
        


    # static_accesses: static_access static_accesses | static_access;
    def visitStatic_accesses(self, ctx: D96Parser.Static_accessesContext):
        if ctx.getChildCount() == 1:
            static_access = [self.visit(ctx.static_access())]
            return static_access 
        else:
            static_access = [self.visit(ctx.static_access())]
            static_accesses = self.visit(ctx.static_accesses())
            return [self.visit(ctx.static_access())] + static_accesses
        
    # static_access:  DOUBLECOLONOP DOLLAR_IDENTIFIERS
    #                 | DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;
    def visitStatic_access(self, ctx: D96Parser.Static_accessContext):
        if ctx.getChildCount() == 2:
            DOLLAR_IDENTIFIERS = ctx.DOLLAR_IDENTIFIERS().getText()
            return DOLLAR_IDENTIFIERS 
            
        else:
            DOLLAR_IDENTIFIERS = ctx.DOLLAR_IDENTIFIERS().getText()
            list_expr = self.visit(ctx.list_expr())
            return DOLLAR_IDENTIFIERS  + list_expr 

        
        
    # Expression list 
    # list_expr: expr COMMA list_expr | expr | ;
    def visitList_expr(self, ctx: D96Parser.List_exprContext):
        if ctx.getChildCount() == 1:
            expr = [self.visit(ctx.expr())]
            return expr 

        elif ctx.getChildCount() == 3:
            expr = [self.visit(ctx.expr())]
            list_expr = self.visit(ctx.list_expr())
            return expr  + list_expr 

        else: 
            return []
        









        
    # --------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------

    # Array literal
    # array_lit: ARRAY LB array_val RB;
    def visitArray_lit(self, ctx: D96Parser.Array_litContext):
        return self.visit(ctx.array_val())
        
    # array_val: expr COMMA array_val | expr | ;
    def visitArray_val(self, ctx: D96Parser.Array_valContext):
        if ctx.getChildCount() == 3:
            expr = self.visit(ctx.expr())
            array_val = self.visit(ctx.array_val())

            return expr + array_val

        elif ctx.getChildCount() == 1:
            expr = self.visit(ctx.expr())
            return expr 

        else: 
            return []
        
    # Literals
    # literal: INTLIT_IN_ARRAY | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit; *********************************************************************************8
    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.array_type():
            return ArrayType()
        





    # List of parameters
    # list_parameters: param SEMICOLON list_parameters | param | ;
    def visitList_parameters(self, ctx: D96Parser.List_parametersContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        elif ctx.getChildCount() == 2:
            param = self.visit(ctx.param())
            list_parameters = self.visit(ctx.list_parameters())
            return param + list_parameters
        else:
            return []
        
        
        
    # param: identifier_list COLON variable_type;
    def visitParam(self, ctx: D96Parser.ParamContext):
        identifier_list = self.visit(ctx.identifier_list())
        variable_type = self.visit(ctx.variable_type())
        result = []
        
        for i in identifier_list:
            result += [VarDecl(i, variable_type, None)]

        return result






    # Identifiers list
    # identifier_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA identifier_list 
    #                 | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | ;
    def visitIdentifier_list(self, ctx: D96Parser.Identifier_listContext):
        if ctx.getChildCount() == 3:
            if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
                a = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            else:
                a = Id(ctx.DOLLAR_IDENTIFIERS().getText())

            identifier_list = self.visit(ctx.identifier_list())

            return [a] + identifier_list

        elif ctx.getChildCount() == 1:
            if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
                a = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            else:
                a = Id(ctx.DOLLAR_IDENTIFIERS().getText())

            return [a]

        else: 
            return []
        
    # variable_in_func_identifier_list: VARIABLE_IN_FUNC_IDENTIFIERS COMMA variable_in_func_identifier_list 
    #                                         | VARIABLE_IN_FUNC_IDENTIFIERS | ;
    def visitVariable_in_func_identifier_list(self, ctx: D96Parser.Variable_in_func_identifier_listContext):
        if ctx.getChildCount() == 3:
            VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            variable_in_func_identifier_list = self.visit(ctx.variable_in_func_identifier_list())

            return VARIABLE_IN_FUNC_IDENTIFIERS + variable_in_func_identifier_list

        elif ctx.getChildCount() == 1:
            VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            return VARIABLE_IN_FUNC_IDENTIFIERS 

        else: 
            return []
        

    # Value list
    # value_list: (literal | expr) COMMA value_list | (literal | expr) | ;
    def visitValue_list(self, ctx: D96Parser.Value_listContext):
        if ctx.getChildCount() == 1:
            if ctx.literal():
                return self.visit(ctx.literal())
            else:
                return self.visit(ctx.expr())

        elif ctx.getChildCount() == 2:
            if ctx.literal():
                a = self.visit(ctx.literal())
            else:
                a = self.visit(ctx.expr())

            value_list = self.visit(ctx.value_list())

            return a + value_list

        else:
            return []
        

    # Array type
    # array_type: ARRAY LSB array_element_type COMMA INTLIT_IN_ARRAY RSB;
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        # array_element_type = Type(self.visit(ctx.array_element_type()))
        array_element_type = self.visit(ctx.array_element_type())
        size = int(self.visit(ctx.INTLIT_IN_ARRAY().getText()))
        return ArrayType(size, array_element_type)
        
        
    # array_element_type: array_type | INT | FLOAT | BOOLEAN | STRING;
    def visitArray_element_type(self, ctx: D96Parser.Array_element_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        

    # Primitive type
    # primitive_type: BOOLEAN | INT | FLOAT | STRING;
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        
    # Variable type
    # variable_type: primitive_type | array_type | VARIABLE_IN_FUNC_IDENTIFIERS;
    def visitVariable_type(self, ctx: D96Parser.Variable_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())             
        elif ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            return ClassType(Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()))

        
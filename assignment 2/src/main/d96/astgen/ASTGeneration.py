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
        name = Id(ctx.CONSTRUCTOR().getText())
        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())

        return [MethodDecl(si, name, list_parameters, block_statements)]

    # destructor_dclr: DESTRUCTOR LB list_parameters RB block_statements;
    def visitDestructor_dclr(self, ctx: D96Parser.Destructor_dclrContext):
        si = Instance()
        name = Id(ctx.DESTRUCTOR().getText())
        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())
        
        return [MethodDecl(si, name, list_parameters, block_statements)]

    #  STATEMENTS ------------------------------------------------------------------------------------------------------
    #! Variable declaration ****************************************************************************
    #! Variable declaration ****************************************************************************

    # var_variable_declaration_noinit: VAR variable_in_func_identifier_list COLON variable_type SEMICOLON;
    def visitVar_variable_declaration_noinit(self, ctx: D96Parser.Var_variable_declaration_noinitContext):
        identifier_list = self.visit(ctx.variable_in_func_identifier_list())
        variable_type = self.visit(ctx.variable_type())
        result = []
        
        # print(identifier_list)
        for i in identifier_list:
            if isinstance(variable_type, ClassType):
                init =  NullLiteral()
            else:
                init = None

            result += [VarDecl(i, variable_type, init)]

        return result
    
    # var_variable_declaration: VAR VARIABLE_IN_FUNC_IDENTIFIERS var_declare_initiate_list expr SEMICOLON;
    def visitVar_variable_declaration(self, ctx: D96Parser.Var_variable_declarationContext):
        result = []

        id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        var_declare_initiate_list = self.visit(ctx.var_declare_initiate_list())
        expr = self.visit(ctx.expr())
        

        if len(var_declare_initiate_list) == 1:
            declare_type = var_declare_initiate_list.pop(0)

            if id.name[0] == '$':
                result += [VarDecl(id, declare_type, expr)]
            else:
                result += [VarDecl(id, declare_type, expr)]
        else:
            list_length = len(var_declare_initiate_list) // 2
            # list_length = var_declare_initiate_list.length // 2
            
            declare_type = var_declare_initiate_list.pop(list_length)

            var_declare_initiate_list.append(expr)
            var_declare_initiate_list.insert(0, id)

            # print(var_declare_initiate_list)
            
            list_length = len(var_declare_initiate_list) // 2
            # list_length = var_declare_initiate_list.length // 2

            id_half = var_declare_initiate_list[:list_length]
            init_value_half = var_declare_initiate_list[list_length:]

            for id_loop, expr_loop in zip(id_half, init_value_half):
                if id_loop.name[0] == '$':
                    result += [VarDecl(id_loop, declare_type, expr_loop)]
                else:
                    result += [VarDecl(id_loop, declare_type, expr_loop)]
            
        return result

    # var_declare_initiate_list: COMMA VARIABLE_IN_FUNC_IDENTIFIERS var_declare_initiate_list expr COMMA
    #                             | COLON variable_type ASSIGNOP;
    def visitVar_declare_initiate_list(self, ctx: D96Parser.Var_declare_initiate_listContext):
        if ctx.getChildCount() == 5:
            id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            var_declare_initiate_list = self.visit(ctx.var_declare_initiate_list())
            expr = self.visit(ctx.expr())

            return [id] + var_declare_initiate_list + [expr]

        else: 
            return [self.visit(ctx.variable_type())]



    # val_variable_declaration_noinit: VAL variable_in_func_identifier_list COLON variable_type SEMICOLON;
    def visitVal_variable_declaration_noinit(self, ctx: D96Parser.Val_variable_declaration_noinitContext):
        identifier_list = self.visit(ctx.variable_in_func_identifier_list())
        variable_type = self.visit(ctx.variable_type())

        result = []
        
        for i in identifier_list:
            if isinstance(variable_type, ClassType):
                
                init =  NullLiteral()
            else:
                init = None

            result += [ConstDecl(i, variable_type, init)]


        return result

    
    # val_variable_declaration: VAL VARIABLE_IN_FUNC_IDENTIFIERS val_declare_initiate_list expr SEMICOLON; 
    def visitVal_variable_declaration(self, ctx: D96Parser.Val_variable_declarationContext):
        val_declare_initiate_list = self.visit(ctx.val_declare_initiate_list())
        expr = self.visit(ctx.expr())
        result = []
        id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())

        if len(val_declare_initiate_list) == 1:
            declare_type = val_declare_initiate_list.pop(0)

            if id.name[0] == '$':
                result += [ConstDecl(id, declare_type, expr)]
            else:
                result += [ConstDecl(id, declare_type, expr)]
        else:
            length = len(val_declare_initiate_list) // 2
            declare_type = val_declare_initiate_list.pop(length)
            val_declare_initiate_list.append(expr)
            val_declare_initiate_list.insert(0, id)

            length = len(val_declare_initiate_list) // 2
            id_half = val_declare_initiate_list[:length]
            init_value_half = val_declare_initiate_list[length:]

            for id_loop, expr_loop in zip(id_half, init_value_half):
                if id_loop.name[0] == '$':
                    result += [ConstDecl(id_loop, declare_type, expr_loop)]
                else:
                    result += [ ConstDecl(id_loop, declare_type, expr_loop)]
            
        return result

    # val_declare_initiate_list: COMMA VARIABLE_IN_FUNC_IDENTIFIERS val_declare_initiate_list expr COMMA
    #                             | COLON variable_type ASSIGNOP;
    def visitVal_declare_initiate_list(self, ctx: D96Parser.Val_declare_initiate_listContext):
        if ctx.getChildCount() == 5:
            id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            val_declare_initiate_list = self.visit(ctx.val_declare_initiate_list())
            expr = self.visit(ctx.expr())

            return [id] + val_declare_initiate_list + [expr]

        else: 
            return [self.visit(ctx.variable_type())]









    # var_both_variable_declaration_noinnit: VAR identifier_list COLON variable_type SEMICOLON;
    def visitVar_both_variable_declaration_noinnit(self, ctx: D96Parser.Var_both_variable_declaration_noinnitContext):
        identifier_list = self.visit(ctx.identifier_list())
        variable_type = self.visit(ctx.variable_type())
        result = []
        
        for i in identifier_list:
            # result += [VarDecl(i, variable_type, None)]
            if isinstance(variable_type, ClassType):
                init =  NullLiteral()
            else:
                init = None

            if i.name[0] == '$':
                typee = Static()
            else:
                typee = Instance()
            
            result += [AttributeDecl(typee, VarDecl(i, variable_type, init))] 

        return result

    # var_both_variable_declaration: VAR (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) var_both_declare_initiate_list expr SEMICOLON;
    def visitVar_both_variable_declaration(self, ctx: D96Parser.Var_both_variable_declarationContext):
        var_both_declare_initiate_list = self.visit(ctx.var_both_declare_initiate_list())
        expr = self.visit(ctx.expr())
        result = []

        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        else:
            id = Id(ctx.DOLLAR_IDENTIFIERS().getText())
        

        if len(var_both_declare_initiate_list) == 1:
            declare_type = var_both_declare_initiate_list.pop(0)

            if id.name[0] == '$':
                result += [AttributeDecl(Static(), VarDecl(id, declare_type, expr))]
            else:
                result += [AttributeDecl(Instance(), VarDecl(id, declare_type, expr))]
        else:
            length = len(var_both_declare_initiate_list) // 2
            declare_type = var_both_declare_initiate_list.pop(length)
            var_both_declare_initiate_list.append(expr)
            var_both_declare_initiate_list.insert(0, id)

            length = len(var_both_declare_initiate_list) // 2
            id_half = var_both_declare_initiate_list[:length]
            init_value_half = var_both_declare_initiate_list[length:]

            for id_loop, expr_loop in zip(id_half, init_value_half):
                if id_loop.name[0] == '$':
                    result += [AttributeDecl(Static(), VarDecl(id_loop, declare_type, expr_loop))]
                else:
                    result += [AttributeDecl(Instance(), VarDecl(id_loop, declare_type, expr_loop))]
            
        return result

    # var_both_declare_initiate_list: COMMA (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) var_both_declare_initiate_list expr COMMA
    #                             | COLON variable_type ASSIGNOP;
    def visitVar_both_declare_initiate_list(self, ctx: D96Parser.Var_both_declare_initiate_listContext):
        if ctx.getChildCount() == 5:
            if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
                id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            else:
                id = Id(ctx.DOLLAR_IDENTIFIERS().getText())

            var_both_declare_initiate_list = self.visit(ctx.var_both_declare_initiate_list())
            expr = self.visit(ctx.expr())

            return [id] + var_both_declare_initiate_list + [expr]

        else: 
            return [self.visit(ctx.variable_type())]



    # val_both_variable_declaration_noinnit: VAL identifier_list COLON variable_type SEMICOLON;
    def visitVal_both_variable_declaration_noinnit(self, ctx: D96Parser.Val_both_variable_declaration_noinnitContext):
        identifier_list = self.visit(ctx.identifier_list())
        variable_type = self.visit(ctx.variable_type())
        result = []
        
        for i in identifier_list:
            # result += [ConstDecl(i, variable_type, None)]
            if isinstance(variable_type, ClassType):
                init =  NullLiteral()
            else:
                init = None

            if i.name[0] == '$':
                typee = Static()
            else:
                typee = Instance()

            result += [AttributeDecl(typee, ConstDecl(i, variable_type, init))]


        return result

    # val_both_variable_declaration: VAL (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) val_both_declare_initiate_list expr SEMICOLON;
    def visitVal_both_variable_declaration(self, ctx: D96Parser.Val_both_variable_declarationContext):
        val_both_declare_initiate_list = self.visit(ctx.val_both_declare_initiate_list())

        # print(val_both_declare_initiate_list)

        expr = self.visit(ctx.expr())
        result = []

        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        else:
            id = Id(ctx.DOLLAR_IDENTIFIERS().getText())

        if len(val_both_declare_initiate_list) == 1:
            declare_type = val_both_declare_initiate_list.pop(0)

            if id.name[0] == '$':
                result += [AttributeDecl(Static(), ConstDecl(id, declare_type, expr))]
            else:
                result += [AttributeDecl(Instance(), ConstDecl(id, declare_type, expr))]
        else:
            length = len(val_both_declare_initiate_list) // 2
            declare_type = val_both_declare_initiate_list.pop(length)
            val_both_declare_initiate_list.append(expr)
            val_both_declare_initiate_list.insert(0, id)

            length = len(val_both_declare_initiate_list) // 2
            id_half = val_both_declare_initiate_list[:length]
            init_value_half = val_both_declare_initiate_list[length:]

            for id_loop, expr_loop in zip(id_half, init_value_half):
                if id_loop.name[0] == '$':
                    result += [AttributeDecl(Static(), ConstDecl(id_loop, declare_type, expr_loop))]
                else:
                    result += [AttributeDecl(Instance(), ConstDecl(id_loop, declare_type, expr_loop))]
            
        return result

    # val_both_declare_initiate_list:  COMMA (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) val_both_declare_initiate_list expr COMMA
    #                             | COLON variable_type ASSIGNOP;
    def visitVal_both_declare_initiate_list(self, ctx: D96Parser.Val_both_declare_initiate_listContext):
        # print('val_both_declare_initiate_list')
        
        if ctx.getChildCount() == 5:
            if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
                id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            else:
                id = Id(ctx.DOLLAR_IDENTIFIERS().getText())
            
            # print(id)
            
            val_both_declare_initiate_list = self.visit(ctx.val_both_declare_initiate_list())
            expr = self.visit(ctx.expr())

            return [id] + val_both_declare_initiate_list + [expr]

        else: 
            return [self.visit(ctx.variable_type())]


    # *******************************************************************************************

    # ! Function declaration
    # function_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
    def visitFunction_declaration(self, ctx: D96Parser.Function_declarationContext):
        # if ctx.list_parameters():
        #     list_parameters = self.visit(ctx.list_parameters())
        # else:
        #     list_parameters == []
        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())

        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            
            name_id = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            name = Id(name_id)

            if (name_id == 'main' and list_parameters == []):
            # if (name_id == 'main' and ctx.getChildCount() == 4):
                # print('ok')
                parent = ctx.parentCtx

                while (not isinstance(parent, D96Parser.Class_declarationContext)):
                    parent = parent.parentCtx

                if (parent.VARIABLE_IN_FUNC_IDENTIFIERS().getText() == 'Program'):
                    return [MethodDecl(Static(), name, list_parameters, block_statements)]

            si = Instance()
        else:
            name = Id(ctx.DOLLAR_IDENTIFIERS().getText())
            si = Static()

        return [MethodDecl(si, name, list_parameters, block_statements)]





    # # ! Call Func
    # # ! Call Func
    # # ! Call Func

    # # a.b.c.d()
    # # CallExpr(FieldAccess.......)

    # # call_func_statement: call_func SEMICOLON;
    # def visitCall_func_statement(self, ctx: D96Parser.Call_func_statementContext):
    #     return self.visit(ctx.call_func())

    # # call_func: call_func_header call_func_attr_list call_func_end;
    # # call_func: call_func_header call_func_attr_list DOT VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB;
    # def visitCall_func(self, ctx: D96Parser.Call_funcContext):
    #     obj =  self.visit(ctx.call_func_header())

    #     method = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
    #     param = self.visit(ctx.value_list())
    #     return CallExpr(obj, method, param)

    # # call_func_header: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) (index_operators | ) (DOUBLECOLONOP DOLLAR_IDENTIFIERS | );
    # def visitCall_func_header(self, ctx: D96Parser.Call_func_headerContext):
    #     return

    # # call_func_attr_list: call_func_attr call_func_attr_list | call_func_attr | ;
    # def visitCall_func_attr_list(self, ctx: D96Parser.Call_func_attr_listContext):
    #     return
        
    # # call_func_attr: DOT (VARIABLE_IN_FUNC_IDENTIFIERS | VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB);                 
    # def visitCall_func_attr(self, ctx: D96Parser.Call_func_attrContext):
    #     return
                   
    # # # call_func_end: DOT VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB;
    # # def visitCall_func_end(self, ctx: D96Parser.Call_func_endContext):
    # #     VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
    # #     value_list = self.visit(ctx.value_list())
    # #     return VARIABLE_IN_FUNC_IDENTIFIERS + value_list
        


    # ! Assignment statement
    # assignment_statements: lhs ASSIGNOP expr SEMICOLON;
    def visitAssignment_statements(self, ctx: D96Parser.Assignment_statementsContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())

        return  [Assign(lhs, expr)]
        
    # lhs: scalar_variable | expr7; 
    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.scalar_variable():           
            return self.visit(ctx.scalar_variable())

        elif ctx.expr7():
            return self.visit(ctx.expr7())

    # scalar_variable: VARIABLE_IN_FUNC_IDENTIFIERS 
    #         | instance_attr_access 
    #         | static_attr_access;
    def visitScalar_variable(self, ctx: D96Parser.Scalar_variableContext):
        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():           
            return Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())

        elif ctx.instance_attr_access():
            return self.visit(ctx.instance_attr_access())
        
        else:
            return self.visit(ctx.static_attr_access())

        
    # ! If statements 
    # *************************************************************************************************
    # if_statements: IF LB expr RB block_statements elseif_list_statements;
    def visitIf_statements(self, ctx: D96Parser.If_statementsContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.block_statements())
        elseStmt = self.visit(ctx.elseif_list_statements())
        
        return [If(expr, thenStmt, elseStmt)]

    # elseif_list_statements: elseif_statement  
    #                     | else_statement 
    #                     | ;
    def visitElseif_list_statements(self, ctx: D96Parser.Elseif_list_statementsContext):
        if ctx.elseif_statement():           
            return self.visit(ctx.elseif_statement())

        elif ctx.else_statement():
            return self.visit(ctx.else_statement())

        else: 
            return None 

    # elseif_statement: ELSEIF LB expr RB block_statements elseif_list_statements;
    def visitElseif_statement(self, ctx: D96Parser.Elseif_statementContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.block_statements())
        elseif_list_statements = self.visit(ctx.elseif_list_statements())
        
        return If(expr, thenStmt, elseif_list_statements)

    # else_statement: ELSE block_statements | ;
    def visitElse_statement(self, ctx: D96Parser.Else_statementContext):
        if ctx.getChildCount() == 2: 
            return self.visit(ctx.block_statements())
        else:
            return None
        
    
    # ! For In statement
    # by_expr: (BY expr) | ;
    def visitBy_expr(self, ctx: D96Parser.By_exprContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.expr())
        else:
            return IntLiteral(int('1'))
        
    # forin_statements: FOREACH LB (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) 
    #                     IN expr DOUBLEDOTOP expr by_expr RB block_statements;
    def visitForin_statements(self, ctx: D96Parser.Forin_statementsContext):
        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            id = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            expr1 = self.visit(ctx.expr(0))
            expr2 = self.visit(ctx.expr(1))
            loop = self.visit(ctx.block_statements())
            expr3 = self.visit(ctx.by_expr())
            return [For(id, expr1, expr2, loop, expr3)]
        else:
            id = Id(ctx.DOLLAR_IDENTIFIERS().getText())
            expr1 = self.visit(ctx.expr(0))
            expr2 = self.visit(ctx.expr(1))
            loop = self.visit(ctx.block_statements())
            expr3 = self.visit(ctx.by_expr())
            return [For(id, expr1, expr2, loop, expr3)]

    # ! Member access
    #***************************************************************************************
    # instance_attr_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS;
    def visitInstance_attr_access(self, ctx: D96Parser.Instance_attr_accessContext):
        obj = self.visit(ctx.expr())
        fieldname = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        return FieldAccess(obj, fieldname)
        
    # instance_method_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;
    def visitInstance_method_access(self, ctx: D96Parser.Instance_method_accessContext):
        obj = self.visit(ctx.expr())
        method = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        param = self.visit(ctx.list_expr())
        return [CallStmt(obj, method, param)]
        
    
    # static_attr_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS;
    def visitStatic_attr_access(self, ctx: D96Parser.Static_attr_accessContext):
        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            obj = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())

            fieldname = Id(ctx.DOLLAR_IDENTIFIERS(0).getText())
            return FieldAccess(obj, fieldname)
        else:
            obj = Id(ctx.DOLLAR_IDENTIFIERS(0).getText())
            fieldname = Id(ctx.DOLLAR_IDENTIFIERS(1).getText())
            return FieldAccess(obj, fieldname)
        
    # static_method_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;
    def visitStatic_method_access(self, ctx: D96Parser.Static_method_accessContext):
        if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            obj = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())

            method = Id(ctx.DOLLAR_IDENTIFIERS(0).getText())
            param = self.visit(ctx.list_expr())
            return [CallStmt(obj, method, param)]
        else:
            obj = Id(ctx.DOLLAR_IDENTIFIERS(0).getText())
            method = Id(ctx.DOLLAR_IDENTIFIERS(1).getText())
            param = self.visit(ctx.list_expr())
            return [CallStmt(obj, method, param)]
        


    # Method invocation statement
    # method_invocation: instance_method_access | static_method_access;
    def visitMethod_invocation(self, ctx: D96Parser.Method_invocationContext):
        if ctx.instance_method_access():
            return self.visit(ctx.instance_method_access())
        else:
            return self.visit(ctx.static_method_access())
        
    # method_invocation_statement: method_invocation SEMICOLON;
    def visitMethod_invocation_statement(self, ctx: D96Parser.Method_invocation_statementContext):
        return self.visit(ctx.method_invocation())


    # Break statement
    # break_statements: BREAK SEMICOLON;
    def visitBreak_statements(self, ctx: D96Parser.Break_statementsContext):
        return [Break()]
        
    # Continue statement
    # continue_statements: CONTINUE SEMICOLON;
    def visitContinue_statements(self, ctx: D96Parser.Continue_statementsContext):
        return [Continue()]
        
    # Return statement
    # return_expr: expr | ;
    def visitReturn_expr(self, ctx: D96Parser.Return_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr())
        else:
            return None
        
    # return_statements: RETURN return_expr SEMICOLON;
    def visitReturn_statements(self, ctx: D96Parser.Return_statementsContext):
        return_expr = self.visit(ctx.return_expr())
        return [Return(return_expr)]


    # Block statements ---------------------------------------------------------------------------------
    # Block statements ---------------------------------------------------------------------------------
    # Block statements ---------------------------------------------------------------------------------

    # block_class_statements: LCB statements_class RCB;
    def visitBlock_class_statements(self, ctx: D96Parser.Block_class_statementsContext):
        return self.visit(ctx.statements_class())
        
    # block_statements: LCB statements RCB;
    def visitBlock_statements(self, ctx: D96Parser.Block_statementsContext):
        return Block(self.visit(ctx.statements()))


    # statements_class: statement_class statements_class | statement_class | ;
    def visitStatements_class(self, ctx: D96Parser.Statements_classContext):
        if ctx.getChildCount() == 1:
            statement_class = self.visit(ctx.statement_class())
            # return Block([], statement_class) 
            return statement_class

        elif ctx.getChildCount() == 2:
            statement_class = self.visit(ctx.statement_class())
            statements_class = self.visit(ctx.statements_class())
            return statement_class + statements_class 

        else: 
            return []
        
    # statements: statement statements | statement | ;
    def visitStatements(self, ctx: D96Parser.StatementsContext):
        if ctx.getChildCount() == 1:
            statement = self.visit(ctx.statement())
            return statement 

        elif ctx.getChildCount() == 2:
            statement = self.visit(ctx.statement())
            statements = self.visit(ctx.statements())
            return statement + statements 

        else: 
            return []

#   ! Tat ca statement can tra ve []
        
#    statement_class: var_both_variable_declaration
#                 | val_both_variable_declaration
#                 | var_both_variable_declaration_noinnit
#                 | val_both_variable_declaration_noinnit
#                 | function_declaration
#                 | constructor_dclr
#                 | destructor_dclr ;
    def visitStatement_class(self, ctx: D96Parser.Statement_classContext):
        if ctx.var_both_variable_declaration():
            return self.visit(ctx.var_both_variable_declaration())
        elif ctx.val_both_variable_declaration():
            return self.visit(ctx.val_both_variable_declaration())

        elif ctx.var_both_variable_declaration_noinnit():
            return self.visit(ctx.var_both_variable_declaration_noinnit())
        elif ctx.val_both_variable_declaration_noinnit():
            return self.visit(ctx.val_both_variable_declaration_noinnit())

        elif ctx.function_declaration():
            return self.visit(ctx.function_declaration())
            
        elif ctx.constructor_dclr():
            return self.visit(ctx.constructor_dclr())
        else:
            return self.visit(ctx.destructor_dclr())
        
# no function declaration
# no $
# statement: var_variable_declaration 
#             | val_variable_declaration 
#             | var_variable_declaration_noinit 
#             | val_variable_declaration_noinit 
#             | assignment_statements 
#             | val_variable_declaration 
#             | assignment_statements 
#             | if_statements 
#             | forin_statements 
#             | method_invocation_statement
#             | break_statements
#             | continue_statements
#             | return_statements ;
    def visitStatement(self, ctx: D96Parser.StatementContext):
        if ctx.var_variable_declaration():
            # print('1')
            return self.visit(ctx.var_variable_declaration())
        elif ctx.val_variable_declaration():
            # print('2')
            return self.visit(ctx.val_variable_declaration())

        elif ctx.var_variable_declaration_noinit():
            # print('3')
            return self.visit(ctx.var_variable_declaration_noinit())
            
        elif ctx.val_variable_declaration_noinit():
            # print('4')
            return self.visit(ctx.val_variable_declaration_noinit())

        elif ctx.assignment_statements():
            # print('5')
            return self.visit(ctx.assignment_statements())
        elif ctx.if_statements():
            # print('6')
            return self.visit(ctx.if_statements())
        elif ctx.forin_statements():
            # print('7')
            return self.visit(ctx.forin_statements())
        # elif ctx.call_func_statement():
        #     # print('8')
        #     return self.visit(ctx.call_func_statement())
        elif ctx.method_invocation_statement():
            # print('9')
            return self.visit(ctx.method_invocation_statement())
        elif ctx.break_statements():
            # print('10')
            return self.visit(ctx.break_statements())
        elif ctx.continue_statements():
            # print('11')
            return self.visit(ctx.continue_statements())
        else:
            # print('12')
            return self.visit(ctx.return_statements())

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
            return self.visit(ctx.expr3())
        
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
            return self.visit(ctx.expr4())
        
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
            return self.visit(ctx.expr5())
        
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
            obj = self.visit(ctx.expr8())

            # return list tuple
            # (id, param, flag)
            instance_accesses = self.visit(ctx.instance_accesses())
            
            # a.b.c().d.e()
            for a in instance_accesses:
                if a[-1] == 0:
                    obj = FieldAccess(obj, a[0])
                else:
                    obj = CallExpr(obj, a[0], a[1])

            return obj
        else:  
            return self.visit(ctx.expr9())
    
    # expr9: static_access | expr10;
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.static_access():
            return self.visit(ctx.static_access())
            
        else:  
            return self.visit(ctx.expr10())
    
    # expr10: NEW VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB | expr11;
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.getChildCount() == 5:
            classname = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            param = self.visit(ctx.list_expr())

            return NewExpr(classname, param)
            
        else:  
            return self.visit(ctx.expr11())
    
    
    # expr11: literal 
    #         | VARIABLE_IN_FUNC_IDENTIFIERS 
    #         | SELF 
    #         | expr12; 
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            return Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        elif ctx.SELF():
            return SelfLiteral()
        else:  
            return self.visit(ctx.expr12())
        
    # expr12: LB expr RB;
    def visitExpr12(self, ctx: D96Parser.Expr12Context):
        return self.visit(ctx.expr())
        



    # a[1][2]...
    # index_operators: LSB expr RSB index_operators | LSB expr RSB ;
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount() == 3:
            expr = [self.visit(ctx.expr())]
            return expr 
        else:
            expr = [self.visit(ctx.expr())]
            index_operators = self.visit(ctx.index_operators())
            return expr + index_operators 
        
        
    # # ! index_expr: index | index index_operators;
    # def visitIndex_expr(self, ctx: D96Parser.Index_exprContext):
    #     if ctx.getChildCount() == 1:
    #         index = [self.visit(ctx.index())]
    #         return index 

    #     else:
    #         expr = [self.visit(ctx.expr())]
    #         index_operators = self.visit(ctx.index_operators())
    #         return expr + index_operators 
        
    # # ! index: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)
    # #         | (expr instance_attr_access (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)) 
    # #         | ;
    # def visitIndex(self, ctx: D96Parser.IndexContext):
    #     return
        


    
    # Instance, Static accesses
    # instance_accesses: instance_access instance_accesses | instance_access;
    def visitInstance_accesses(self, ctx: D96Parser.Instance_accessesContext):
        if ctx.getChildCount() == 1:
            instance_access = [self.visit(ctx.instance_access())]
            return instance_access 
        else:
            instance_access = [self.visit(ctx.instance_access())]
            instance_accesses = self.visit(ctx.instance_accesses())
            return instance_access + instance_accesses
    
    
    # instance_access:  DOT VARIABLE_IN_FUNC_IDENTIFIERS
    #                 | DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;
    def visitInstance_access(self, ctx: D96Parser.Instance_accessContext):
        if ctx.getChildCount() == 2:
            VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            return (Id(VARIABLE_IN_FUNC_IDENTIFIERS), [], 0)
            
        else:
            VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            list_expr = self.visit(ctx.list_expr())
            return (Id(VARIABLE_IN_FUNC_IDENTIFIERS), list_expr, 1)
        


    # static_accesses: static_access static_accesses | static_access;
    # def visitStatic_accesses(self, ctx: D96Parser.Static_accessesContext):
    #     if ctx.getChildCount() == 1:
    #         static_access = [self.visit(ctx.static_access())]
    #         return static_access 
    #     else:
    #         static_access = [self.visit(ctx.static_access())]
    #         static_accesses = self.visit(ctx.static_accesses())
    #         return static_access + static_accesses
        
    # static_access:  DOUBLECOLONOP DOLLAR_IDENTIFIERS
    #                 | DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;
    # def visitStatic_access(self, ctx: D96Parser.Static_accessContext):
    #     if ctx.getChildCount() == 2:
    #         DOLLAR_IDENTIFIERS = ctx.DOLLAR_IDENTIFIERS().getText()
    #         return DOLLAR_IDENTIFIERS 
            
    #     else:
    #         DOLLAR_IDENTIFIERS = ctx.DOLLAR_IDENTIFIERS().getText()
    #         list_expr = self.visit(ctx.list_expr())
    #         return DOLLAR_IDENTIFIERS + list_expr 

    # static_access: VARIABLE_IN_FUNC_IDENTIFIERS (DOUBLECOLONOP DOLLAR_IDENTIFIERS
    #             | DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB);
    def visitStatic_access(self, ctx: D96Parser.Static_accessContext):
        if ctx.getChildCount() == 3:
            obj = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            fieldname = Id(ctx.DOLLAR_IDENTIFIERS().getText())
            return FieldAccess(obj, fieldname) 
            
        else:
            obj = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            method = Id(ctx.DOLLAR_IDENTIFIERS().getText())
            param = self.visit(ctx.list_expr())
            return CallExpr(obj, method, param)

    # Expression list 
    # list_expr: expr COMMA list_expr | expr | ;
    def visitList_expr(self, ctx: D96Parser.List_exprContext):
        if ctx.getChildCount() == 1:
            expr = [self.visit(ctx.expr())]
            return expr 

        elif ctx.getChildCount() == 3:
            expr = [self.visit(ctx.expr())]
            list_expr = self.visit(ctx.list_expr())
            return expr + list_expr 

        else: 
            return []

        
    # --------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------

    # Array literal
    # array_lit: ARRAY LB array_val RB;
    def visitArray_lit(self, ctx: D96Parser.Array_litContext):
        value = self.visit(ctx.array_val())
        return ArrayLiteral(value)
        
    # array_val: expr COMMA array_val | expr | ;
    def visitArray_val(self, ctx: D96Parser.Array_valContext):
        if ctx.getChildCount() == 3:
            expr = self.visit(ctx.expr())
            array_val = self.visit(ctx.array_val())

            return [expr] + array_val

        elif ctx.getChildCount() == 1:
            expr = self.visit(ctx.expr())
            return [expr] 

        else: 
            return []
        
    # !Literals
    # literal: INTLIT_IN_ARRAY | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit; 
    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INTLIT():
            a = ctx.INTLIT().getText()

            if (len(a) == 1):
                return IntLiteral(int(a, 10))
                
            else:
                if (a[1] == 'b' or a[1] == 'B'):
                    return IntLiteral(int(a, 2))
                elif (a[1] == 'x' or a[1] == 'X'):
                    return IntLiteral(int(a, 16))
                elif (a[0] != '0'):
                    return IntLiteral(int(a, 10))
                else:
                    return IntLiteral(int(a, 8))
                
        elif ctx.INTLIT_IN_ARRAY():
            a = ctx.INTLIT_IN_ARRAY().getText()

            if (len(a) == 1):
                return IntLiteral(int(a, 10))
                
            else:
                if (a[1] == 'b' or a[1] == 'B'):
                    return IntLiteral(int(a, 2))
                elif (a[1] == 'x' or a[1] == 'X'):
                    return IntLiteral(int(a, 16))
                elif (a[0] != '0'):
                    return IntLiteral(int(a, 10))
                else:
                    return IntLiteral(int(a, 8))
        
        elif ctx.FLOATLIT():
            a = ctx.FLOATLIT().getText()

            if (a[0] == '.'):
                a = '0' + a
                
            return FloatLiteral(float(a))

        elif ctx.BOOLLIT():
            # a = ctx.BOOLLIT().getText()

            # if a == 'True':
            #     return BooleanLiteral(bool(a))
            # else:
            #     return BooleanLiteral(ctx.BOOLLIT().getText() == "True")
            
            return BooleanLiteral(ctx.BOOLLIT().getText() == "True")
        elif ctx.STRINGLIT():
            a = str(ctx.STRINGLIT().getText())
            return StringLiteral(a)

        elif ctx.array_lit():
            return self.visit(ctx.array_lit())

    # List of parameters
    # list_parameters: param SEMICOLON list_parameters | param | ;
    def visitList_parameters(self, ctx: D96Parser.List_parametersContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        elif ctx.getChildCount() == 3:
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
            a = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            variable_in_func_identifier_list = self.visit(ctx.variable_in_func_identifier_list())
            return [a] + variable_in_func_identifier_list

        elif ctx.getChildCount() == 1:
            a = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
            return [a]

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
        
        array_element_type = self.visit(ctx.array_element_type())

        a = ctx.INTLIT_IN_ARRAY().getText()

        if (len(a) == 1):
            size = int(a, 10)
            
        else:
            if (a[1] == 'b' or a[1] == 'B'):
                size = int(a, 2)
            elif (a[1] == 'x' or a[1] == 'X'):
                size = int(a, 16)
            elif (a[0] != '0'):
                size = int(a, 10)
            else:
                size = int(a, 8)

        # size = int(ctx.INTLIT_IN_ARRAY().getText())

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

        
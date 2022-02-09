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
    def visitClassDeclartions(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 1:
            class_declaration = [self.visit(ctx.class_declaration())]
            return class_declaration 
        else:
            class_declaration = [self.visit(ctx.class_declaration())]
            class_declarations = self.visit(ctx.class_declarations())
            return [self.visit(ctx.class_declaration())] + class_declarations 

    # class_declaration: CLASS VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance block_class_statements;
    def visitClassDeclartion(self, ctx: D96Parser.ProgramContext):
        VARIABLE_IN_FUNC_IDENTIFIERS = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        class_inheritance = self.visit(ctx.class_inheritance())
        block_class_statements = self.visit(ctx.block_class_statements())

        return ClassDecl(VARIABLE_IN_FUNC_IDENTIFIERS, block_class_statements, class_inheritance)

    # class_inheritance: COLON VARIABLE_IN_FUNC_IDENTIFIERS | ;
    def visitClassInheritance(self, ctx: D96Parser.ProgramContext):
        return Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())

    # Constructor Destructor
    # constructor_dclr: CONSTRUCTOR LB list_parameters RB block_statements;
    def visitConstructorDeclaration(self, ctx: D96Parser.ProgramContext):
        si = Instance() 
        name = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())

        return MethodDecl(si, name, list_parameters, block_statements)

    # destructor_dclr: DESTRUCTOR LB RB block_statements;
    def visitDestructorDeclaration(self, ctx: D96Parser.ProgramContext):
        si = Instance()
        name = Id(ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText())
        list_parameters = self.visit(ctx.list_parameters())
        block_statements = self.visit(ctx.block_statements())
        
        return MethodDecl(si, name, list_parameters, block_statements)

    #  Method declaration
    # method_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
    def visitMethodDeclaration(self, ctx: D96Parser.ProgramContext):
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
    def visitVariableDeclaration(self, ctx: D96Parser.ProgramContext):

        return VarDecl()

    # no_value_assign_declare_list: no_value_assign_declare no_value_assign_declare_list| no_value_assign_declare;
    def visitNoValueAssignDeclareList(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 1:
            no_value_assign_declare = [self.visit(ctx.no_value_assign_declare())]
            return no_value_assign_declare 
        else:
            no_value_assign_declare = [self.visit(ctx.no_value_assign_declare())]
            no_value_assign_declare_list = self.visit(ctx.no_value_assign_declare_list())
            return [self.visit(ctx.no_value_assign_declare())] + no_value_assign_declare_list 

    # no_value_assign_declare: VARIABLE_IN_FUNC_IDENTIFIERS COMMA | VARIABLE_IN_FUNC_IDENTIFIERS | COLON variable_type;
    def visitNoValueAssignDeclare(self, ctx: D96Parser.ProgramContext):
        return

    # declare_initiate_list: VARIABLE_IN_FUNC_IDENTIFIERS type_and_assign expr
    #                             | variable_in_func_identifier_list COLON variable_type;
    def visitDeclareInitiateList(self, ctx: D96Parser.ProgramContext):
        return

    # type_and_assign: COMMA VARIABLE_IN_FUNC_IDENTIFIERS type_and_assign expr COMMA
    #                     | COLON variable_type ASSIGNOP;
    def visitTypeAndAssign(self, ctx: D96Parser.ProgramContext):
        return


    # Both declaration
    # both_variable_declaration: (VAR | VAL) (both_declare_initiate_list | both_no_value_assign_declare_list) SEMICOLON;
    def visitBothDeclaration(self, ctx: D96Parser.ProgramContext):
        return

    # both_no_value_assign_declare_list: both_no_value_assign_declare both_no_value_assign_declare_list| both_no_value_assign_declare;
    def visitBothNoValueAssignDeclareList(self, ctx: D96Parser.ProgramContext):
        return

    # both_no_value_assign_declare: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | COLON variable_type;
    def visitBothNoValueAssignDeclare(self, ctx: D96Parser.ProgramContext):
        return

    # both_declare_initiate_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) both_type_and_assign expr
    #                             | variable_in_func_identifier_list COLON variable_type;
    def visitBothDeclareInitiateList(self, ctx: D96Parser.ProgramContext):
        return

    # both_type_and_assign: COMMA (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) both_type_and_assign expr COMMA
    #                         | COLON variable_type ASSIGNOP;
    def visitBothTypeAndAssign(self, ctx: D96Parser.ProgramContext):
        return

    # Function declaration
    # function_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
    def visitFunctionDeclaration(self, ctx: D96Parser.ProgramContext):
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
    def visitCallFuncStatement(self, ctx: D96Parser.ProgramContext):
        return

    # call_func: call_func_header call_func_attr_list call_func_end;
    def visitCallFunc(self, ctx: D96Parser.ProgramContext):
        call_func_header = self.visit(ctx.call_func_header())
        call_func_attr_list = self.visit(ctx.call_func_attr_list())
        call_func_end = self.visit(ctx.call_func_end())
        return CallStmt()

    # call_func_header: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) (index_operators | ) (DOUBLECOLONOP DOLLAR_IDENTIFIERS | );
    def visitCallFuncHeader(self, ctx: D96Parser.ProgramContext):
        return

    # call_func_attr_list: call_func_attr call_func_attr_list | call_func_attr | ;
    def visitCallFuncAttributeList(self, ctx: D96Parser.ProgramContext):
        return
        
    # call_func_attr: DOT (VARIABLE_IN_FUNC_IDENTIFIERS | VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB);                 
    def visitCallFuncAttribute(self, ctx: D96Parser.ProgramContext):
        return
                   
    # call_func_end: DOT VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB;
    def visitCallFuncEnd(self, ctx: D96Parser.ProgramContext):
        VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
        value_list = self.visit(ctx.value_list())
        return VARIABLE_IN_FUNC_IDENTIFIERS + value_list
        


















    # Assignment statement
    # assignment_statements: lhs ASSIGNOP expr SEMICOLON;
    def visitAssignmentStatements(self, ctx: D96Parser.ProgramContext):
        lhs = Expr(self.visit(ctx.lhs()))
        expr = Expr(self.visit(ctx.expr()))

        return  Assign(lhs, expr)
        
    # lhs: (VARIABLE_IN_FUNC_IDENTIFIERS 
    #         | instance_attr_access 
    #         | static_attr_access 
    #         ) (index_operators | );
    def visitLHS(self, ctx: D96Parser.ProgramContext):
        return
        
















    # If statements 
    # if_condition: LB expr RB;
    def visitIfCondition(self, ctx: D96Parser.ProgramContext):
        return self.visit(ctx.expr())

    # if_statements: IF LB expr RB block_statements (elseif_list_statements else_statement | elseif_list_statements | else_statement | );
    def visitIfStatements(self, ctx: D96Parser.ProgramContext):
        return
        
    # elseif_list_statements: elseif_statement elseif_list_statements |  elseif_statement;
    def visitElseIfListStatements(self, ctx: D96Parser.ProgramContext):
        return
        
    # elseif_statement: ELSEIF LB expr RB block_statements;
    def visitElseIfStatement(self, ctx: D96Parser.ProgramContext):
        return
    
    # else_statement_or_none: else_statement | ; 
    def visitElseStatementOrNone(self, ctx: D96Parser.ProgramContext):
        return

    # else_statement: ELSE block_statements;
    def visitElseStatement(self, ctx: D96Parser.ProgramContext):
        return
        

































    # For In statement
    # by_expr: (BY expr) | ;
    def visitByExpr(self, ctx: D96Parser.ProgramContext):
        return
        
    # forin_statements: FOREACH LB (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) 
    #                     IN expr DOUBLEDOTOP expr by_expr RB block_statements;
    def visitForInStatement(self, ctx: D96Parser.ProgramContext):
        return













    # Member access
    # instance_attr_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS;
    def visitInstanceAttrAccess(self, ctx: D96Parser.ProgramContext):
        return
        
    # instance_method_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;
    def visitInstanceMethodAccess(self, ctx: D96Parser.ProgramContext):
        return
        
    # static_attr_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS;
    def visitStaticAttrAccess(self, ctx: D96Parser.ProgramContext):
        return
        
    # static_method_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;
    def visitStaticMethodAccess(self, ctx: D96Parser.ProgramContext):
        return
        








    # Method invocation statement
    # method_invocation: instance_method_access | static_method_access;
    def visitMethodInvocation(self, ctx: D96Parser.ProgramContext):
        return
        
    # method_invocation_statement: method_invocation SEMICOLON;
    def visitMethodInvocationStatement(self, ctx: D96Parser.ProgramContext):
        return









    # Break statement
    # break_statements: BREAK SEMICOLON;
    def visitBreakStatement(self, ctx: D96Parser.ProgramContext):
        return Break()
        
    # Continue statement
    # continue_statements: CONTINUE SEMICOLON;
    def visitContinueStatement(self, ctx: D96Parser.ProgramContext):
        return Continue()
        
    # Return statement
    # return_expr: expr | ;
    def visitReturnExpr(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr())

        else:
            return [] 
        
    # return_statements: RETURN return_expr SEMICOLON;
    def visitReturnStatement(self, ctx: D96Parser.ProgramContext):
        return_expr = Expr(self.visit(ctx.return_expr()))
        return Return(return_expr)
        









    # Block statements ---------------------------------------------------------------------------------
    # block_class_statements: LCB statements_class RCB;
    def visitBlockClassStatements(self, ctx: D96Parser.ProgramContext):
        return self.vist(ctx.statements_class())
        
    # block_statements: LCB statements RCB;
    def visitBlockStatements(self, ctx: D96Parser.ProgramContext):
        return self.vist(ctx.statements())
        
    # statements_class: statement_class statements_class | statement_class | ;
    def visitStatemetsClass(self, ctx: D96Parser.ProgramContext):
        return
        
    # statements: statement statements | statement | ;
    def visitStatements(self, ctx: D96Parser.ProgramContext):
        return
        
    # statement_class: both_variable_declaration
    #                 | function_declaration
    #                 | constructor_dclr
    #                 | destructor_dclr ;
    def visitStatementClass(self, ctx: D96Parser.ProgramContext):
        return
        
    # no function declaration
    #  no $
    # statement: variable_declaration 
    #             | assignment_statements 
    #             | if_statements 
    #             | forin_statements 
    #             | call_func_statement
    #             | method_invocation_statement
    #             | break_statements
    #             | continue_statements
    #             | return_statements ;
    def visitStatement(self, ctx: D96Parser.ProgramContext):
        return
        


















    # EXPRESSIONS ----------------------------------------------------------------------------------
    # a.b[1]              a.b()[1]           a.b[1]            a.b()[1].b()[1]
    # a::b[1]             a::b()[1]          a::b[1]           a::b()[1]::b()[1]  
    # Ưu tiên gọi access trước

    # expr: expr1 (STRCONCATOP | STREQUALOP) expr1 | expr1;
    def visitExpr(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr1: expr2 (EQUALOP | NOTEQUALOP | LT | GT | LTE | GTE) expr2 | expr2;
    def visitExpr1(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr2: expr2 (ANDOP | OROP) expr3 | expr3;
    def visitExpr2(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
    def visitExpr3(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
    def visitExpr4(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr5: NOTOP expr5 | expr6;
    def visitExpr5(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr6: MINUSOP expr6 | expr7;
    def visitExpr6(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr7: expr7 index_operators | expr8;
    def visitExpr7(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr8: expr8 instance_accesses | expr9;
    def visitExpr8(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr9: VARIABLE_IN_FUNC_IDENTIFIERS static_accesses | expr10;
    def visitExpr9(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr10: NEW expr LB list_expr RB | expr11;
    def visitExpr10(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr11: literal 
    #         | VARIABLE_IN_FUNC_IDENTIFIERS 
    #         | SELF 
    #         | expr12; 
    def visitExpr11(self, ctx: D96Parser.ProgramContext):
        return
        
    # expr12: LB expr RB;
    def visitExpr12(self, ctx: D96Parser.ProgramContext):
        return
        
    # a[1][2]
    # index_operators: index_operators LSB expr RSB  | LSB expr RSB ;
    def visitIndexOperators(self, ctx: D96Parser.ProgramContext):
        return
        
    # index_expr: index | index index_operators;
    def visitIndexExpr(self, ctx: D96Parser.ProgramContext):
        return
        
    # index: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)
    #         | (expr instance_attr_access (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)) | ;
    def visitIndex(self, ctx: D96Parser.ProgramContext):
        return
        
    # Instance, Static accesses
    # instance_accesses: instance_access instance_accesses | instance_access;
    def visitInstanceAccesses(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 1:
            instance_access = [self.visit(ctx.instance_access())]
            return instance_access 
        else:
            instance_access = [self.visit(ctx.instance_access())]
            instance_accesses = self.visit(ctx.instance_accesses())
            return [self.visit(ctx.instance_access())] + instance_accesses
        
    # instance_access:  DOT VARIABLE_IN_FUNC_IDENTIFIERS
    #                 | DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;
    def visitInstanceAccess(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 2:
            VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            return VARIABLE_IN_FUNC_IDENTIFIERS 
            
        else:
            VARIABLE_IN_FUNC_IDENTIFIERS = ctx.VARIABLE_IN_FUNC_IDENTIFIERS().getText()
            list_expr = self.visit(ctx.list_expr())
            return VARIABLE_IN_FUNC_IDENTIFIERS  + list_expr
        
    # static_accesses: static_access static_accesses | static_access;
    def visitStaticAccesses(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 1:
            static_access = [self.visit(ctx.static_access())]
            return static_access 
        else:
            static_access = [self.visit(ctx.static_access())]
            static_accesses = self.visit(ctx.static_accesses())
            return [self.visit(ctx.static_access())] + static_accesses
        
    # static_access:  DOUBLECOLONOP DOLLAR_IDENTIFIERS
    #                 | DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;
    def visitStaticAccess(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 2:
            DOLLAR_IDENTIFIERS = ctx.DOLLAR_IDENTIFIERS().getText()
            return DOLLAR_IDENTIFIERS 
            
        else:
            DOLLAR_IDENTIFIERS = ctx.DOLLAR_IDENTIFIERS().getText()
            list_expr = self.visit(ctx.list_expr())
            return DOLLAR_IDENTIFIERS  + list_expr 

        
        
    # Expression list 
    # list_expr: expr COMMA list_expr | expr | ;
    def visitListExpr(self, ctx: D96Parser.ProgramContext):
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
    def visitArrayLiteral(self, ctx: D96Parser.ProgramContext):
        return self.visit(ctx.array_val())
        
    # array_val: expr COMMA array_val | expr | ;
    def visitArrayValue(self, ctx: D96Parser.ProgramContext):
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
    def visitLiteral(self, ctx: D96Parser.ProgramContext):
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
    def visitListParams(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        elif ctx.getChildCount() == 2:
            param = self.visit(ctx.param())
            list_parameters = self.visit(ctx.list_parameters())
            return param + list_parameters
        else:
            return []
        
        
    # param: identifier_list COLON variable_type;
    def visitParam(self, ctx: D96Parser.ProgramContext):
        identifier_list = self.visit(ctx.identifier_list())
        variable_type = self.visit(ctx.variable_type())
        return identifier_list + variable_type

    # Identifiers list
    # identifier_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA identifier_list 
    #                 | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | ;
    def visitIDList(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 3:
            if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
                a = self.visit(ctx.VARIABLE_IN_FUNC_IDENTIFIERS())
            else:
                a = self.visit(ctx.DOLLAR_IDENTIFIERS())

            identifier_list = self.visit(ctx.identifier_list())

            return a + identifier_list

        elif ctx.getChildCount() == 1:
            if ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
                a = self.visit(ctx.VARIABLE_IN_FUNC_IDENTIFIERS())
            else:
                a = self.visit(ctx.DOLLAR_IDENTIFIERS())

            return a 

        else: 
            return []
        
    # variable_in_func_identifier_list: VARIABLE_IN_FUNC_IDENTIFIERS COMMA variable_in_func_identifier_list 
    #                                         | VARIABLE_IN_FUNC_IDENTIFIERS | ;
    def visitVariableInFuncIDList(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 3:
            VARIABLE_IN_FUNC_IDENTIFIERS = self.visit(ctx.VARIABLE_IN_FUNC_IDENTIFIERS())
            variable_in_func_identifier_list = self.visit(ctx.variable_in_func_identifier_list())

            return VARIABLE_IN_FUNC_IDENTIFIERS + variable_in_func_identifier_list

        elif ctx.getChildCount() == 1:
            VARIABLE_IN_FUNC_IDENTIFIERS = self.visit(ctx.VARIABLE_IN_FUNC_IDENTIFIERS())
            return VARIABLE_IN_FUNC_IDENTIFIERS 

        else: 
            return []
        

    # Value list
    # value_list: (literal | expr) COMMA value_list | (literal | expr) | ;
    def visitValueList(self, ctx: D96Parser.ProgramContext):
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
    def visitArrayType(self, ctx: D96Parser.ProgramContext):
        array_element_type = self.visit(ctx.identifier_list())
        INTLIT_IN_ARRAY = self.visit(ctx.INTLIT_IN_ARRAY())
        return array_element_type + INTLIT_IN_ARRAY
        
    # array_element_type: array_type | INT | FLOAT | BOOLEAN | STRING;
    def visitArrayElementType(self, ctx: D96Parser.ProgramContext):
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
        

    # Primitive type
    # primitive_type: BOOLEAN | INT | FLOAT | STRING;
    def visitPrimitiveType(self, ctx: D96Parser.ProgramContext):
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
    def visitVariableType(self, ctx: D96Parser.ProgramContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        elif ctx.VARIABLE_IN_FUNC_IDENTIFIERS():
            return self.visit(ctx.VARIABLE_IN_FUNC_IDENTIFIERS())

        



































# class ASTGenerator(CSELVisitor):
#     # program: decl+ EOF;
#     # Visit a parse tree produced by CSELParser#program.
#     def visitProgram(self, ctx:CSELParser.ProgramContext):
#         result = []
        
#         for vd in ctx.decl():
#             result += self.visit(vd)
            
#         return Program(result)

#     # cseltype: INT | FLOAT | BOOLEAN;
#     # Visit a parse tree produced by CSELParser#cseltype.
#     def visitCseltype(self, ctx:CSELParser.CseltypeContext):
#         if ctx.INT():
#             return IntType()
#         elif ctx.FLOAT():
#             return FloatType()
#         elif ctx.BOOLEAN():
#             return BooleanType()

#     # decl: vardecl decltail | constdecl decltail | funcdecl decltail;
#     # Visit a parse tree produced by CSELParser#decl.
#     def visitDecl(self, ctx:CSELParser.DeclContext):
#         if ctx.vardecl():
#             varDecl = self.visit(ctx.vardecl())
#             declTail = self.visit(ctx.decltail())
#             return varDecl + declTail
#         elif ctx.funcdecl():
#             funcDecl = self.visit(ctx.funcdecl())
#             declTail = self.visit(ctx.decltail())
#             return funcDecl + declTail
#         elif ctx.constdecl():
#             constDecl = self.visit(ctx.constdecl())
#             declTail = self.visit(ctx.decltail())
#             return constDecl + declTail
            
        

#     # decltail: vardecl decltail | constdecl decltail | funcdecl decltail | ; 
#     # Visit a parse tree produced by CSELParser#decltail.
#     def visitDecltail(self, ctx:CSELParser.DecltailContext):
#         if ctx.vardecl():
#             varDecl = self.visit(ctx.vardecl())
#             declTail = self.visit(ctx.decltail())
#             return varDecl + declTail
#         elif ctx.funcdecl():
#             funcDecl = self.visit(ctx.funcdecl())
#             declTail = self.visit(ctx.decltail())
#             return funcDecl + declTail
#         elif ctx.constdecl():
#             constDecl = self.visit(ctx.constdecl())
#             declTail = self.visit(ctx.decltail())
#             return constDecl + declTail
#         else:
#             return []

#     # vardecl: LET single_vardecls SEMI;
#     # Visit a parse tree produced by CSELParser#vardecl.
#     def visitVardecl(self, ctx:CSELParser.VardeclContext):
#         return self.visit(ctx.single_vardecls())

#     # single_vardecls: single_vardecl single_vardecltail;
#     # Visit a parse tree produced by CSELParser#single_vardecls.
#     def visitSingle_vardecls(self, ctx:CSELParser.Single_vardeclsContext):
#         singleVar = self.visit(ctx.single_vardecl())
#         singleVarTail = self.visit(ctx.single_vardecltail())
#         return singleVar + singleVarTail

#     # single_vardecl: ID COLON cseltype;
#     # Visit a parse tree produced by CSELParser#single_vardecl.
#     def visitSingle_vardecl(self, ctx:CSELParser.Single_vardeclContext):
#         ids = ctx.ID().getText()
#         typee = self.visit(ctx.cseltype())
#         result = []
        
#         for a in ids:
#             result.append(VarDecl(Id(a), typee))
            
#         return result

#     # single_vardecltail: COMMA single_vardecl single_vardecltail | ;
#     # Visit a parse tree produced by CSELParser#single_vardecltail.
#     def visitSingle_vardecltail(self, ctx:CSELParser.Single_vardecltailContext):
#         if ctx.getChildCount() == 3:
#             singleVar = self.visit(ctx.single_vardecl())
#             singleVarTail = self.visit(ctx.single_vardecltail())
#             return singleVar + singleVarTail
#         else: 
#             return []

#     # constdecl: CONST single_constdecl SEMI;
#     # Visit a parse tree produced by CSELParser#constdecl.
#     def visitConstdecl(self, ctx:CSELParser.ConstdeclContext):
#         return self.visit(ctx.single_constdecl())

#     # single_constdecl: ID COLON cseltype EQ expr;
#     # Visit a parse tree produced by CSELParser#single_constdecl.
#     def visitSingle_constdecl(self, ctx:CSELParser.Single_constdeclContext):
#         ids = ctx.ID().getText()
#         typee = self.visit(ctx.cseltype())
#         value = self.visit(ctx.expr())
#         result = []
        
#         for a in ids:
#             result.append(ConstDecl(Id(a), typee, value))
            
#         return result

#     # expr: INTLIT | FLOATLIT | BOOLEANLIT;
#     # Visit a parse tree produced by CSELParser#expr.
#     def visitExpr(self, ctx:CSELParser.ExprContext):
#         if ctx.INTLIT():
#             return IntLit(int(ctx.INTLIT().getText()))
#         elif ctx.FLOATLIT():
#             return FloatLit(float(ctx.FLOATLIT().getText()))
#         else:
#             return BooleanLit(ctx.BOOLEANLIT().getText() == 'True')

#     # funcdecl: FUNCTION ID LR paramlist RR SEMI;
#     # Visit a parse tree produced by CSELParser#funcdecl.
#     def visitFuncdecl(self, ctx:CSELParser.FuncdeclContext):
#         id = ctx.ID().getText()
#         paramList = self.visit(ctx.paramlist())
        
#         return [FuncDecl(Id(id), paramList)]

#     # paramlist: single_vardecls | ;
#     # Visit a parse tree produced by CSELParser#paramlist.
#     def visitParamlist(self, ctx:CSELParser.ParamlistContext):
#         if ctx.getChildCount() == 1:
#             return self.visit(ctx.single_vardecls())
#         else:
#             return []















    # def visitProgram(self, ctx: D96Parser.ProgramContext):
    #     return Program([FuncDecl(Id("main"),
    #                              [],
    #                              self.visit(ctx.mptype()),
    #                              Block([], [self.visit(ctx.body())] if ctx.body() else []))])

    # def visitMptype(self, ctx: D96Parser.MptypeContext):
    #     if ctx.INTTYPE():
    #         return IntType()
    #     else:
    #         return VoidType()

    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))

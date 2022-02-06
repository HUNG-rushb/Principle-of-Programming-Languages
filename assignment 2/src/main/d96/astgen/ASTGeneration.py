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
            return self.visit(ctx.class_declaration())
        else:
            return self.visit(ctx.class_declaration()) + self.visit(ctx.class_declarations())

    # class_declaration: CLASS VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance block_class_statements;
    def visitClassDeclartion(self, ctx: D96Parser.ProgramContext):
        return

    # class_inheritance: COLON VARIABLE_IN_FUNC_IDENTIFIERS | ;
    def visitClassInheritance(self, ctx: D96Parser.ProgramContext):
        return

    # Constructor Destructor
    # constructor_dclr: CONSTRUCTOR LB list_parameters RB block_statements;
    def visitConstructorDeclaration(self, ctx: D96Parser.ProgramContext):
        return

    # destructor_dclr: DESTRUCTOR LB RB block_statements;
    def visitDestructorDeclaration(self, ctx: D96Parser.ProgramContext):
        return

    #  Method declaration
    # method_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
    def visitMethodDeclaration(self, ctx: D96Parser.ProgramContext):
        return

    #  STATEMENTS ------------------------------------------------------------------------------------------------------

    # Variable declaration
    # variable_declaration: (VAR | VAL) (declare_initiate_list | no_value_assign_declare_list) SEMICOLON;
    def visitVariableDeclaration(self, ctx: D96Parser.ProgramContext):
        return

    # no_value_assign_declare_list: no_value_assign_declare no_value_assign_declare_list| no_value_assign_declare;
    def visitNoValueAssignDeclareList(self, ctx: D96Parser.ProgramContext):
        return

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
        return

    # call_func_statement: call_func_header call_func_attr_list call_func_end SEMICOLON;
    def visitCallFuncStatement(self, ctx: D96Parser.ProgramContext):
        return

    # call_func: call_func_header call_func_attr_list call_func_end;
    def visitCallFunc(self, ctx: D96Parser.ProgramContext):
        return

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
        return
        


    # Assignment statement
    # assignment_statements: lhs ASSIGNOP expr SEMICOLON;
    def visitAssignmentStatements(self, ctx: D96Parser.ProgramContext):
        return
        
    # lhs: (VARIABLE_IN_FUNC_IDENTIFIERS 
    #         | instance_attr_access 
    #         | static_attr_access 
    #         ) (index_operators | );
    def visitLHS(self, ctx: D96Parser.ProgramContext):
        return
        
    # If statements 
    # if_condition: LB expr RB;
    def visitIfCondition(self, ctx: D96Parser.ProgramContext):
        return

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
        return
        
    # Continue statement
    # continue_statements: CONTINUE SEMICOLON;
    def visitContinueStatement(self, ctx: D96Parser.ProgramContext):
        return
        
    # Return statement
    # return_expr: expr | ;
    def visitReturnExpr(self, ctx: D96Parser.ProgramContext):
        return
        
    # return_statements: RETURN return_expr SEMICOLON;
    def visitReturnStatement(self, ctx: D96Parser.ProgramContext):
        return
        

    # Block statements ---------------------------------------------------------------------------------
    # block_class_statements: LCB statements_class RCB;
    def visitBlockClassStatements(self, ctx: D96Parser.ProgramContext):
        return
        
    # block_statements: LCB statements RCB;
    def visitBlockStatements(self, ctx: D96Parser.ProgramContext):
        return
        
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
        return
        
    # instance_access:  DOT VARIABLE_IN_FUNC_IDENTIFIERS
    #                 | DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;
    def visitInstanceAccess(self, ctx: D96Parser.ProgramContext):
        return
        
    # static_accesses: static_access static_accesses | static_access;
    def visitStaticAccesses(self, ctx: D96Parser.ProgramContext):
        return
        
    # static_access:  DOUBLECOLONOP DOLLAR_IDENTIFIERS
    #                 | DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;
    def visitStaticAccess(self, ctx: D96Parser.ProgramContext):
        return
        
    # Expression list 
    # list_expr: expr COMMA list_expr | expr | ;
    def visitListExpr(self, ctx: D96Parser.ProgramContext):
        return
        
    # --------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------

    # Array literal
    # array_lit: ARRAY LB array_val RB;
    def visitArrayLiteral(self, ctx: D96Parser.ProgramContext):
        return
        
    # array_val: expr COMMA array_val | expr | ;
    def visitArrayValue(self, ctx: D96Parser.ProgramContext):
        return
        
    # Literals
    # literal: INTLIT_IN_ARRAY | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit;
    def visitLiteral(self, ctx: D96Parser.ProgramContext):
        return
        
    # List of parameters
    # list_parameters: param SEMICOLON list_parameters | param | ;
    def visitListParams(self, ctx: D96Parser.ProgramContext):
        return
        
    # param: identifier_list COLON variable_type;
    def visitParam(self, ctx: D96Parser.ProgramContext):
        return
        
    # Identifiers list
    # identifier_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA identifier_list 
    #                 | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | ;
    def visitIDList(self, ctx: D96Parser.ProgramContext):
        return
        
    # variable_in_func_identifier_list: VARIABLE_IN_FUNC_IDENTIFIERS COMMA variable_in_func_identifier_list 
    #                                         | VARIABLE_IN_FUNC_IDENTIFIERS | ;
    def visitVariableInFuncIDList(self, ctx: D96Parser.ProgramContext):
        return
        

    # Value list
    # value_list: (literal | expr) COMMA value_list | (literal | expr) | ;
    def visitValueList(self, ctx: D96Parser.ProgramContext):
        return
        

    # Array type
    # array_type: ARRAY LSB array_element_type COMMA INTLIT_IN_ARRAY RSB;
    def visitArrayType(self, ctx: D96Parser.ProgramContext):
        return
        
    # array_element_type: array_type | INT | FLOAT | BOOLEAN | STRING;
    def visitArrayElementType(self, ctx: D96Parser.ProgramContext):
        return
        

    # Primitive type
    # primitive_type: BOOLEAN | INT | FLOAT | STRING;
    def visitPrimitiveType(self, ctx: D96Parser.ProgramContext):
        return
        
    # Variable type
    # variable_type: primitive_type | array_type | VARIABLE_IN_FUNC_IDENTIFIERS;
    def visitVariableType(self, ctx: D96Parser.ProgramContext):
        return
        















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

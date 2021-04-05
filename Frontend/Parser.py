from Frontend.Lexer import LexTokens

class AST:
    

    def __init__(self, id, num = -1):
        self.name = id
        self.tok = num
        self.children = []
        self.parent = None
    
    def addNode(self, node):
        node.set_parent(self)
        self.children.append(node)
    
    def get_parent(self):
        return self.parent
    def set_parent(self, parent):
        self.parent = parent
    
    



class Parser:

    def consume(self):
        #print(self.stream[self.cur_lexeme_pos])
        self.cur_lexeme_pos = self.cur_lexeme_pos + 1

    def match(self, x):
        if self.stream[self.cur_lexeme_pos][0] == x:
            node = AST(self.stream[self.cur_lexeme_pos][1], self.stream[self.cur_lexeme_pos][0])
            self.NodePtr.addNode(node)
            self.consume()
            
        else:
            a = 1/0 #Raise an Error


    def __init__(self, tok_stream):
        self.stream = tok_stream
        self.cur_lexeme_pos = 0
        self.cur_lookahead_pos = 1
        self.pTree = []
        self.ast = AST("PROGRAM")
        self.NodePtr = self.ast

    def value(self):
        if(self.stream[self.cur_lexeme_pos][0] == LexTokens.Prob_val):
            self.match(LexTokens.Prob_val)

    def equation(self):
        equ = AST("RHS")
        
        if(self.stream[self.cur_lexeme_pos][0] == LexTokens.Equ_):
            
            self.match(LexTokens.Equ_)
            self.NodePtr.addNode(equ)
            self.NodePtr = equ
            self.value()

        else:
            
            self.match(LexTokens.Is_tok)
            self.NodePtr.addNode(equ)
            self.NodePtr = equ
            self.value()
        self.NodePtr = self.NodePtr.get_parent()
        
            
    def evalVar(self):
        
        if(self.stream[self.cur_lexeme_pos][0] == LexTokens.Var_Symbol):
            self.match(LexTokens.Var_Symbol)
            self.evalVar() 
            
        elif(self.stream[self.cur_lexeme_pos][0] == LexTokens.And_Tok):
            
            self.match(LexTokens.And_Tok)
            self.evalVar()
            
        elif(self.stream[self.cur_lexeme_pos][0] == LexTokens.Or_Tok):
            self.match(LexTokens.Or_Tok)
            self.evalVar()  
        elif(self.stream[self.cur_lexeme_pos][0] == LexTokens.Not_Tok):
            op = AST("UNARY")
            self.NodePtr.addNode(op)
            self.NodePtr = op
            self.match(LexTokens.Not_Tok)
            self.evalVar()  
            self.NodePtr = self.NodePtr.get_parent()
           
        

    def prob(self):
        self.match(LexTokens.L_Paren)
        var = AST("VAR")
        self.NodePtr.addNode(var)
        self.NodePtr = var
        self.evalVar()
        self.NodePtr = self.NodePtr.get_parent()
        self.match(LexTokens.R_Paren)
        self.equation()
    

    def expr(self):
        
        if(self.stream[self.cur_lexeme_pos][0] == LexTokens.Prob_P):
            
            self.match(LexTokens.Prob_P)
            
            self.prob()
        elif(self.stream[self.cur_lexeme_pos][0] == LexTokens.Prob_word):
            
            self.match(LexTokens.Prob_word)
            self.prob()




    def dump_AST(self, node):
        print(node.name, end="")
        
        if(node.parent != None):
            print(" PARENT is", node.parent.name)
        for children in node.children:
            self.dump_AST(children)

        

    def prog(self):

        while self.cur_lexeme_pos < len(self.stream):
            expr = AST("EXPR")
            self.NodePtr.addNode(expr)
            self.NodePtr = expr
            self.expr()
            self.NodePtr = self.NodePtr.get_parent()

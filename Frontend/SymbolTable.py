from Frontend.Lexer import LexTokens
#from Frontend.Parser import *



class SymbolTable:

    def __init__(self, parsed):
        self.symbols = {}
        self.parsetree = parsed 
        self.last_referenced = None
        self.traverseTree(parsed)
        self.op = None

    def declared(self, var):
        return var in self.symbols

    
    def check_symbol(self, var):
        if self.declared(var):
            pass
            #print("Already Declared")
        else:
            #self.symbols[var] = (True, -1)
            self.last_referenced = var
        pass
    def assign(self, var_name, val):
        self.symbols[var_name]= val
    """
    Takes in Node representing the right side of a =

    """
    def deduce(self, node, op = False):
        accumulate = 0
        
        for expressions in node.children:
            print(expressions.name, end="")
            if expressions.tok == LexTokens.Prob_val:
                if op:
                    print(expressions)
                    assert(False)
                    accumulate = 1 - float(expressions.name)
                    
                else:
                    accumulate = float(expressions.name)
            if expressions.tok == LexTokens.Var_Symbol:
                #assert(self.declared(expressions.name))
                pass
            if expressions.tok == LexTokens.Prob_P:
                pass
                #accumulate += self.deduce(expressions)
            if expressions.tok == LexTokens.Not_Tok:
                self.deduce(expressions, True)
        print("\nnewline")
                
           
            
            
            
            
        
        
        print("ACCUM = ",accumulate)
        pass
    def get_probability(self, node):
        for child in node.chilren:
            print(child.name)

    def unary_eval(self, node):
        print(node.children[1].name)
        #return 1 - self.symbols[node.chilren[1].name]

    def simplifyRight(self, rightNode):
        accumulate = 0
        for nodes in rightNode.children:
            if nodes.tok == LexTokens.Prob_val:
                accumulate += float(nodes.name)
            if nodes.tok == LexTokens.Prob_P:
                self.get_probability(nodes)
        return accumulate

    def traverseTree(self, tree):
        if(tree.tok == LexTokens.Var_Symbol):
            self.check_symbol(tree.name)
        #if(tree.tok == LexTokens.Prob_val):
            #self.assign(self.last_referenced, tree.name)
        if(tree.name == "UNARY"):
            pass#self.unary_eval(tree)   
        if tree.name == "RHS":
            self.assign(self.last_referenced, self.simplifyRight(tree))
            pass
            #self.deduce(tree)
        for nodes in tree.children:
            self.traverseTree(nodes)

        

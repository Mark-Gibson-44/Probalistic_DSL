import re

#from SymbolTable import * 
query_regexes = ["^[a-zA-Z]$", "^\!$", "^|$"]

def isToken(lexeme):
    for i in range(len (query_regexes)):
        match = re.search(query_regexes[i], lexeme)
        if(bool(match)):
            return (True, i)
    return (False, -1)

class Node:

    def __init__(self, id, tok):
        self.id = id
        self.tok = tok
        self.leaves = []
    
    def addNode(self, id, num = -1):
        leaf = Node(id, num)
        leaf.append(leaf)


class Query:

    def __init__(self, var_table):
        self.queryData = var_table
        self.queryLexed = []
        self.queryParsed = []
        self.queryOp = None
        #self.ptr
        self.unary_ops = {
            '&': lambda x, y : x * y,
            '|': lambda x, y : x + y
        }
    
    def lex_query(self, query):
        curchar = 0
        lookahead = 1
        cur_str = ""
        for char in query:
            if char == " ":
                continue
            cur_str = cur_str + char
            if isToken(cur_str)[0]:
                
                self.queryLexed.append((isToken(cur_str)[1], cur_str))
                cur_str = ""
    def parse_query(self, tok_stream):
        #print(tok_stream)
        lookahead = 1
        current = 0
        """
        for toks in tok_stream:
            if(toks[0] == 0):
                self.queryVar(toks[1])
            elif(toks[0] < 0):
                self.queryOp = toks[1]
        
        """
        while(lookahead < len(tok_stream)):
            #print(tok_stream[current])
            
            if(tok_stream[lookahead][0] > 1):
                
                self.unaryExpr(tok_stream[lookahead][1], tok_stream[current][1], tok_stream[lookahead + 1][1])
                current  = lookahead + 1
                
            elif(tok_stream[current][0] == 1):
                self.queryExpr(tok_stream[current][1], tok_stream[lookahead][1])
                current = lookahead + 1
            else:
                
                self.queryVar(tok_stream[current][1])
                current = current + 1
            lookahead = current + 1
        self.queryLexed = []
        
        """
        Set up Parse Tree To determine precedence
        """
 

    def queryExpr(self, op, var):
        print(op)
        if op == "!":
            op = None
            print( 1 - self.queryData[var])
        
    def unaryExpr(self, op, left, right):
        
        
        print(self.unary_ops[op](self.queryData[left], self.queryData[right]))

    def queryVar(self, var):
        assert(self.queryData[var])
        if(self.queryOp != None):
            print(self.queryExpr(var))
        else:
            print(self.queryData[var])

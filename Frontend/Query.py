import re
from Parser import AST 
from SymbolTable import * 
query_regexes = ["^[a-zA-z]$", "^\!$", "^|$"]

def isToken(lexeme):
    for i in range(len (query_regexes)):
        match = re.search(query_regexes[i], lexeme)
        if(bool(match)):
            return (True, i)
    return (False, -1)



class Query:

    def __init__(self, var_table):
        self.queryData = var_table
        self.queryLexed = []
        self.queryParsed = []
        self.queryOp = None

    def lex_query(self, query):
        curchar = 0
        lookahead = 1
        cur_str = ""
        for char in query:
            if char == " ":
                continue
            cur_str = cur_str + char
            if isToken(cur_str)[0]:
                #print(cur_str)
                self.queryLexed.append((isToken(cur_str)[1], cur_str))
                cur_str = ""
    def parse_query(self, tok_stream):
        lookahead = 1
        current = 0
        for toks in tok_stream:
            if(toks[0] == 0):
                self.queryVar(toks[1])
            elif(toks[0] == 1):
                self.queryOp = toks[1]
            
        """
        Set up Parse Tree To determine precedence
        """
    def queryExpr(self, var):
        if self.queryOp == "!":
            self.queryOp = None
            return 1 - self.queryData[var]

    def queryVar(self, var):
        if(self.queryOp != None):
            print(self.queryExpr(var))
        else:
            print(self.queryData[var])


            
    def eval_query(self, parsed_query):
        accumulate = 0
        
        


        return accumulate

            
                
                

#q = Query(22)
#q.lex_query("X | B")
l = Lexer()
l.lex("Frontend/test.txt")
p = Parser(l.Tok_list)
p.prog()
st = SymbolTable(p.ast)

q = Query(st.symbols)
q.lex_query("!x")
q.parse_query(q.queryLexed)
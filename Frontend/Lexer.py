import re
import enum




class LexTokens(enum.Enum):
    Prob_P = 1
    L_Paren = 2
    R_Paren = 3
    Var_Symbol = 4
    Equ_ = 5
    Prob_word = 6
    Is_tok = 7
    And_Tok = 8
    Or_Tok = 9
    Not_Tok = 10
    Dependence = 11
    Prob_val = 12


regexes = ["^P$", "^\($", "^\)$", "^[a-zA-Z]$", "^=$", "^probability$", "^is$", "^\&$", "^U$", "^\!$", "^\|$", "^0\.[0-9][0-9]*$"]

def isToken(lexeme):
    for i in range(len (regexes)):
        match = re.search(regexes[i], lexeme)
        if(bool(match)):
            return (True, i)
    return (False, -1)

class Lexer:
    
    def __init__(self):
        self.Tok_list = []
        self.cur_char = ''
        self.cur_word = ""

        
    def log(self):
        for tok in self.Tok_list:
            print(tok)
    def lex(self, File):
        f = open(File)
        
        for line in f:
            for char in line:
                if(char == " " or char == "\n" or char == "\t"):
                    continue
                self.cur_word = self.cur_word + char
                matched, tok = isToken(self.cur_word)
                if(matched):
                    
                    self.Tok_list.append((LexTokens(tok+1), self.cur_word))
                    self.cur_word = ""
                if(self.cur_word != ""):
                    pass#raise Exception
        
    def lex_Repl(self, line):
        for char in line:
            if(char == " " or char == "\n" or char == "\t"):
                continue
            self.cur_word = self.cur_word + char
            matched, tok = isToken(self.cur_word)
            if(matched):
                    
                self.Tok_list.append((LexTokens(tok+1), self.cur_word))
                self.cur_word = ""
            if(char == "Q"):
                exit()
        

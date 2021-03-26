from pytest import *
import sys
sys.path.append("..")

from Lexer import *



exp_tok = [LexTokens.Prob_P, LexTokens.L_Paren,LexTokens.Var_Symbol, LexTokens.R_Paren, LexTokens.Equ_, LexTokens.Prob_val]

def test_lex_tokens():
    l = Lexer()
    l.lex("./Tok_test.txt")
    for i in range(len(l.Tok_list)):
        assert(l.Tok_list[i][0] == exp_tok[i])


    
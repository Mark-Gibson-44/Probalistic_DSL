import argparse

from Frontend.Lexer import Lexer
from Frontend.Parser import Parser
from Frontend.SymbolTable import SymbolTable
from Frontend.Query import Query


#argParsing = argparse.ArgumentParser(description='CL Flags')
#argParsing.add_argument('-R', metavar='R', type=None, nargs=True,
#                    help='Launch Repl')

#args = argParsing.parse_args()
#print(args)


if __name__ == "__main__":
    l = Lexer()
    l.lex("Frontend/test.txt")


    p = Parser(l.Tok_list)
    p.prog()
    st = SymbolTable(p.ast)

    q = Query(st.symbols)
    query = input()
    while(query != 'Q'):
        q.lex_query(query)
        q.parse_query(q.queryLexed)
        query = input()

import sys
from antlr4 import *
from misterLexer import misterLexer
from misterParser import misterParser
from maquinaVirtual import *
 
def main(argv):
    input = FileStream(argv[1])
    lexer = misterLexer(input)
    stream = CommonTokenStream(lexer)
    parser = misterParser(stream)
    tree = parser.programa()
    print(parser.quadList)
    #print(parser.dirPrincipal)
    #if parser._syntaxErrors == 0:
    	#maquina = maquinaVirtual(parser.dirPrincipal, parser.quadList, , , , , , )
if __name__ == '__main__':
    main(sys.argv)
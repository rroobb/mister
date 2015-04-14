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
if __name__ == '__main__':
    main(sys.argv)
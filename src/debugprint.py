import sys
def echo():
    print('nameCheck present')
def p(data):
    if '--debug' in sys.argv or '-d' in sys.argv: print(data)
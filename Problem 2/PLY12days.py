""" This will parse the data from the unix command echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n"
which is:
Header1 is this
Header2 and that

Data 1.0
Data 2.0
"""

tokens = ('ON', 'DAY', 'ORDINAL')
literals = ['.', ':'  ]

# Tokens
t_ON  = r'^On\sthe'
t_DAY = r'day\sof\sChristmas\s'

# def t_INTEGER(t):
#     r'\d+'
#     try:
#         t.value = int(t.value)
#     except ValueError:
#         print("Integer value too large %d", t.value)
#         t.value = 0
#     return t


def t_ORDINAL(t):
    r'\w*\s'
    ordinals = ['first', 'second', 'third', 'fourth',
                'fifth', 'sixth', 'seventh', 'eighth']
    if t.value[:-1] in ordinals:
        return t
    else:
        return ""

# Ignored characters
t_ignore = " \r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : ON
             | DAY
             | ORDINAL
             | day
             | empty
    '''
    print(t[1])

def p_day(t):
    'day : ON ORDINAL DAY'
    t[0] = t[2]

def p_empty(t):
    'empty : '
    pass

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n" | grep -v '^\s*$' | python PLYstarter.py | sed "s/_~_/ which is a float./"

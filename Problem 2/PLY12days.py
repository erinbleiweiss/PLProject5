
qty = {
    'partridge in a pear tree': 0,
    'turtle': 0,
    'french': 0,
    'calling': 0,
    'golden': 0,
    'geese': 0,
    'swans': 0,
    'maids': 0,
    'ladies': 0,
    'lords': 0,
    'pipers': 0,
    'drummers': 0
}

tokens = ('MY', 'WORD', 'ORDINAL', 'NUMBER', 'PARTRIDGE', 'AND')
literals = ['.', ':', ','  ]

# Tokens
ordinals = ['first', 'second', 'third', 'fourth',
            'fifth', 'sixth', 'seventh', 'eighth',
            'ninth', 'tenth', 'eleventh', 'twelfth']

numbers = {'A': 1,
           'Two': 2,
           'Three': 3,
           'Four': 4,
           'Five': 5,
           'Six': 6,
           'Seven': 7,
           'Eight': 8,
           'Nine': 9,
           'Ten': 10,
           'Eleven': 11,
           'Twelve': 12}


def t_MY(t):
    r'^My.*$'
    return t


def t_PARTRIDGE(t):
    r'partridge.*tree'
    return t

def t_AND(t):
    r'\band\b'
    return t

def t_WORD(t):
    r'\b[\w-]+\b'
    if t.value in ordinals:
        t.value = t.value.capitalize()
        t.type = "ORDINAL"
    elif t.value in numbers:
        t.value = numbers[t.value]
        t.type = "NUMBER"
    return t


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
def get_total():
    count = 0
    for gift in qty:
        count += qty[gift]
    return count

print("Cumulative Twelve Days of Christmas Gifts")

def p_start(t):
    '''start : MY
             | WORD
             | ORDINAL
             | NUMBER
             | day
             | partridge
             | gift
             | empty
    '''


def p_day(t):
    'day : WORD WORD ORDINAL WORD WORD WORD ","'
    print "\n{0} {1}: ".format(t[3], t[4])

def p_partridge(t):
    'partridge : NUMBER PARTRIDGE "."'
    number = t[1]
    qty[t[2]] += number
    number = qty[t[2]]
    if number > 1:
        t[2] = 'partridges in a pear tree'
    print "{0} {1}".format(number, t[2])
    print "Total gifts: {0}".format(get_total())

def p_gift(t):
    'gift : NUMBER WORD WORD'
    number = t[1]
    qty[t[2]] += number
    number = qty[t[2]]
    print "{0} {1} {2}".format(number, t[2], t[3])

def p_gift_and(t):
    'gift : NUMBER WORD WORD AND'
    number = t[1]
    qty[t[2]] += number
    number = qty[t[2]]
    print "{0} {1} {2}".format(number, t[2], t[3])

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


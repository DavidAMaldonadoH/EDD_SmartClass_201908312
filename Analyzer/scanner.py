import ply.lex as lex
import re
#List of tokens
tokens = [
    'LQUESTION',
    'RQUESTION',
    'DOLAR',
    'IGUAL',
    'ENTERO',
    'CADENA',
    'ID'
]

reserved = {
    'elements'   : 'ELEMENTS',
    'element'    : 'ELEMENT',
    'type'       : 'TYPE',
    'item'       : 'ITEM',
}

tokens += list(reserved.values())

#Tokens
t_LQUESTION  = r'\¿'
t_RQUESTION  = r'\?'
t_DOLAR      = r'\$'
t_IGUAL      = r'='

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t 

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),'ID') # Check for reserved words
    return t

# Ignored characters
t_ignore = ' \t\r\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
lexer = lex.lex(reflags=re.IGNORECASE)
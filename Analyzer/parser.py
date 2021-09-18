import ply.yacc as yacc

from Analyzer.scanner import tokens

elementos = []

def p_init(t):
    'init : LQUESTION ELEMENTS RQUESTION elementos LQUESTION DOLAR ELEMENTS RQUESTION'
    t[0] = t[4]
    for item in t[0]:
        elementos.append(item)

def p_elementos_lista(t):
    'elementos : elementos elemento'
    t[0] = t[1]
    t[0].append(t[2])

def p_elementos_elemento(t):
    'elementos : elemento'
    t[0] = [t[1]]

def p_elemento(t):
    'elemento : LQUESTION ELEMENT TYPE IGUAL CADENA RQUESTION datos LQUESTION DOLAR ELEMENT RQUESTION'
    t[0] = t[7]
    t[0].update({'type': t[5].lower()})

def p_datos(t):
    'datos : datos dato'
    t[0] = t[1]
    t[0].update(t[2])

def p_datos_dato(t):
    'datos : dato'
    t[0] = dict()
    t[0].update(t[1])

def p_dato(t):
    '''dato : LQUESTION ITEM ID IGUAL CADENA DOLAR RQUESTION
            | LQUESTION ITEM ID IGUAL ENTERO DOLAR RQUESTION'''
    t[0] = {t[3].lower() : t[5]}

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

parser = yacc.yacc()

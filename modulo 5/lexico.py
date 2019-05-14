import ply.lex as lex

class Lexico():
    def __init__(self):
        self._tokens = list()
        tokens = (
        'INT',
        'FLOAT',
        'OR',
        'AND',
        'PLUS',
        'MINUS',
        'MULTIPL',
        'DIVI',
        'ASIGNACION',
        'COMPARACION',
        'MENOR_QUE',
        'MENOR_O_IGUAL_QUE',
        'MAYOR_QUE',
        'MAYOR_O_IGUAL_QUE',
        'DIFERENTE',
        'PAREN_DER',
        'PAREN_IZQ',
        'LLAVE_DER',
        'LLAVE_IZQ',
        'PUNTO_Y_COMA',
        'IF',
        'WHILE',
        'RETURN',
        'ELSE',
        'INT_TYPE',
        'FLOAT_TYPE',
        'CADENA',
        'COMA',
        'ID'

        )

        t_INT = r'\d+'
        t_FLOAT = r'\d+\.\d+'
        t_OR = r'\|{2}'
        t_AND = r'&&'
        t_MULTIPL = r'\*'
        t_DIVI = r'/'
        t_ASIGNACION = r'\='
        t_MENOR_QUE = r'<'
        t_MENOR_O_IGUAL_QUE = r'<='
        t_MAYOR_QUE = r'>'
        t_MAYOR_O_IGUAL_QUE = r'>'
        t_DIFERENTE = r'!='
        t_PAREN_DER = r'\)'
        t_PAREN_IZQ = r'\('
        t_LLAVE_DER = r'\}'
        t_LLAVE_IZQ = r'\{'
        t_PUNTO_Y_COMA = r'\;'
        t_PLUS = r'\+'
        t_MINUS = r'-'
        t_COMA = r','
   
        def t_IF(t):
          r'if'
          return t
        def t_WHILE(t):
          r'while'
          return t
        def t_RETURN(t):
          r'return'
          return t
        def t_ELSE(t):
          r'else'
          return t
        def t_INT_TYPE(t):
          r'int'
          return t
        def t_FLOAT_TYPE(t):
          r'float'
          return t
        #def t_CADENA(t):
          #r'\"^[a-z\s]{0,255}$/i\"'
          #return t
        def t_ID(t):
          r'\w+(_\d\w)*'
          return t
       
        def t_COMPARACION(t):
          r'=='
          return t
        
        def t_newline(t):
          r'\n+'
          t.lexer.lineno += len(t.value)

        def t_error(t):
          t.lexer.skip(1)

        lex.lex()
        leer = open ('informacion.txt', 'r')
        cadena = leer.read()
        leer.close()
        lex.input(cadena)
        while 1:
          tok = lex.token()
          if not tok:
            break
          self._tokens.append([tok.type,tok.value])
        self._tokens.append(['$',''])
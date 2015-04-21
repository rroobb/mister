grammar mister;

options {
  language=Python;
}

//=======================================================
// Reglas de gramatica
//=======================================================

programa: programaAux1 programaAux3 EOF
    ;

programaAux1: v_vars programaAux1
    | c_class programaAux1
    |
    ;

programaAux3: FUNCION programaAux5
    ;

programaAux5: ENTERO programaAux6
    | DECIMAL programaAux7
    | TEXTO programaAux7
    | NADA programaAux7
    ;

programaAux6: INICIO func 
    | programaAux7
    ;

programaAux7: ID func programaAux3
    ;
    
programaAux4: tipo
    | NADA
    ;

v_vars: varsAux1 v_varsDefinicion
    ;

varsAux1: ID
    | tipo
    | l_list
    ;
	
v_varsDefinicion: varsAux4 PUNTOYCOMA
	;

varsAux2: IGUAL varsAux3
    |
    ;

varsAux3: expresion
    | cteL
    ;

varsAux4: ID varsAux2 varsAux5
    ;

varsAux5: COMA ID varsAux2 varsAux5
    |
    ;
	
v_varsAtrib: varsAtribAux1 v_varsDefinicion
    ;

varsAtribAux1: tipo
    | l_list
    ;

tipo: ENTERO
    | DECIMAL
    | TEXTO
    ;

l_list: LISTA tipo CTENTERO
    ;

cteL: CORCHETE1 valor cteLAux1 CORCHETE2
    ;

cteLAux1: COMA valor cteLAux1
    |
    ;

valor: CTENTERO
    | CTEDECIMAL
    | compuesto valorAux1
    | CTETEXTO
    ;

valorAux1: llamarFunc
    |
    ;

parametros: PARENTESIS1 parametrosAux1 PARENTESIS2
    ;
    
parametrosAux1: parametrosAux2 ID parametrosAux3
    |
    ;

parametrosAux2: tipo
    | l_list
    ;
    
parametrosAux3: COMA parametrosAux2 ID parametrosAux3
    |
    ;


func: parametros LLAVE1 funcAux1 funcAux2 funcAux3 LLAVE2
    ;

funcAux1: v_vars funcAux1
    |
    ;
    
funcAux2: estatuto funcAux2
    |
    ;
    
funcAux3: RETORNAR expresion PUNTOYCOMA
    |
    ;
    
expresion: declaracion expresionAux1
    ;
    
expresionAux1: expresionAux2 expresion
    |
    ;
    
expresionAux2: Y
    | O
    ;
    
estatuto: asignacion
    | condicion
    | expresion PUNTOYCOMA
    | escritura
    | ciclo
    | lectura
    ;

declaracion: exp declaracionAux2
    ;
    
declaracionAux1: MAYOR
    | MENOR
    | DIFERENTE
    | MAYORIGUAL
    | MENORIGUAL
    | IDENTICO
    ;

declaracionAux2: declaracionAux1 exp
	|
	;
    
exp: termino expAux1
    ;
    
expAux1: SUMA termino expAux1
    | RESTA termino expAux1
    |
    ;

llamarFunc: PARENTESIS1 llamarFuncAux1 PARENTESIS2
    ;
    
llamarFuncAux1: expresion llamarFuncAux2
    | REFERENCIA ID llamarFuncAux2
    |
    ;
    
llamarFuncAux2: COMA llamarFuncAux3 llamarFuncAux2
    |
    ;
    
llamarFuncAux3: expresion
    | REFERENCIA ID
    ;

termino: factor terminoAux1
    ;

terminoAux1: MULTIPLICACION factor terminoAux1
    | DIVISION factor terminoAux1
    |
    ;
    
factor: PARENTESIS1 expresion PARENTESIS2
    | valor
    | factorAux1 valor
    ;

factorAux1: SUMA
    | RESTA
    ;
    
compuesto: ID compuestoAux1
    ;
    
compuestoAux1: PUNTO ID compuestoAux2
    |
    ;

compuestoAux2: PUNTO CTENTERO
    |
    ;

asignacion: ASIGNAR compuesto IGUAL asignacionAux1 PUNTOYCOMA
    ;

asignacionAux1: expresion
    | cteL
    ;
    
condicion: SI PARENTESIS1 expresion PARENTESIS2 bloque condicionAux1
    ;
   
condicionAux1: SINO bloque
    |
    ;

bloque: LLAVE1 estatuto bloqueAux1 LLAVE2
    ;

bloqueAux1: estatuto bloqueAux1
    |
    ;
    
ciclo: MIENTRAS PARENTESIS1 expresion PARENTESIS2 bloque
    ;

escritura: IMPRIMIR PARENTESIS1 expresion escrituraAux1 PARENTESIS2 PUNTOYCOMA
    ;
    
escrituraAux1: COMA expresion escrituraAux1
    |
    ;
    
lectura: LEER PARENTESIS1 ID PARENTESIS2 PUNTOYCOMA
    ;
    
c_class: CLASE ID classAux1 LLAVE1 classAux2 classAux3 LLAVE2 PUNTOYCOMA
    ;
    
classAux1: HEREDA ID
    |
    ;
    
classAux2: atrib
    |
    ;
    
classAux3: metod
    |
    ;
    
atrib: ATRIBUTOS DOSPUNTOS atribAux1
    ;
    
atribAux1: atribAux2 v_varsAtrib atribAux3
    ;
    
atribAux2: PUBLICO
    | PRIVADO
    ;
    
atribAux3: atribAux1
    |
    ;
    
metod: METODOS DOSPUNTOS metodAux1
    ;
    
metodAux1: FUNCION metodAux2 ID func metodAux3
    ;
    
metodAux2: tipo
    | NADA
    ;
    
metodAux3: metodAux1
    |
    ;

//=============================================
//Tokens
//=============================================


INICIO:                  'INICIO' ;
SI:                      'SI' ;
SINO:                    'SINO' ;
MIENTRAS:                'MIENTRAS' ;
LEER:                    'LEER' ;
IMPRIMIR:                'IMPRIMIR' ;
FUNCION:                 'FUNCION' ;
ENTERO:                  'ENTERO' ;
DECIMAL:                 'DECIMAL' ;
TEXTO:                   'TEXTO' ;
RETORNAR:                'RETORNAR' ;
LISTA:                   'LISTA' ;
CLASE:                  'CLASE' ;
ATRIBUTOS:              'ATRIBUTOS' ;
METODOS:                'METODOS' ;
HEREDA:                 'HEREDA' ;
NADA:                   'NADA' ;
PRIVADO:                'PRIVADO' ;
PUBLICO:                'PUBLICO' ;
ASIGNAR:                 'ASIGNAR';
Y:                       '&&' ;
REFERENCIA:              '&' ;
O:                       '||' ;
IDENTICO:                '==';
IGUAL:                   '=' ;
COMA:                    ',' ;
SUMA:                    '+' ;
RESTA:                   '-' ;
DIVISION:                '/' ;
MULTIPLICACION:          '*' ;
DIFERENTE:               '!=';
MAYORIGUAL:              '>=';
MENORIGUAL:              '<=';
MENOR:                   '<' ;
MAYOR:                   '>' ;
PARENTESIS1:             '(' ;
PARENTESIS2:             ')' ;
LLAVE1:                  '{' ;
LLAVE2:                  '}' ;
CORCHETE1:               '[' ;
CORCHETE2:               ']' ;
PUNTOYCOMA:              ';' ;
DOSPUNTOS:               ':' ;
PUNTO:                   '.' ;
ID:                      [a-zA-Z][a-zA-Z0-9]* ;
CTENTERO:                  '-'?DIGIT+ ;
CTEDECIMAL:                '-'?DIGIT+'.'DIGIT+ ;
CTETEXTO:                  '"' ( WS | ~('"'|'\\') )* '"' ;
WS                      : 
                        ( ' '
                        | '\t'
                        | '\r'    
                        | '\n'    
                        )
                        -> skip
                        ;
fragment DIGIT : '0'..'9' ;
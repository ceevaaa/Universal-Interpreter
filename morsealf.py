#En kort = 1 enhetsintervall
#Paus mellan tecken = 1 enhetsintervall
#En long = 3 enhetsintervall
#Avstånd mellan enskilda bokstävet = 3 enhetsintervall
#Paus mellan ord = 5 enhetsintervall

def signtomorse(sign):
    """Converts a letter/number to morsecode"""
    code = tomorse[str.upper(sign)]
    return(code + "   ")

def morsetosign(morse):
    """Converts morse to signs"""
    text = tosign[morse]
    return(text)

tomorse = {
    'A' : '. _'            ,
    'B' : '_ . . .'        ,
    'C' : '_ . _ .'        ,
    'D' : '_ . .'          ,
    'E' : '.'              ,
    'F' : '. . _ .'        ,
    'G' : '_ _ .'          ,
    'H' : '. . . .'        ,
    'I' : '. .'            ,
    'J' : '. _ _ _'        ,
    'K' : '_ . _'          ,
    'L' : '. _ . .'        ,
    'M' : '_ _'            ,
    'N' : '_ .'            ,
    'O' : '_ _ _'          ,
    'P' : '. _ _ .'        ,
    'Q' : '_ _ . _'        ,
    'R' : '. _ .'          ,
    'S' : '. . .'          ,
    'T' : '_'              ,
    'U' : '. . _'          ,
    'V' : '. . . _'        ,
    'W' : '. _ _'          ,
    'X' : '_ . . _'        ,
    'Y' : '_ . _ _'        ,
    'Z' : '_ _ . .'        ,
    'Å' : '. _ _ . _'      ,
    'Ä' : '. _ . _'        ,
    'Ö' : '_ _ _ .'        ,
    'É' : '. . _ . .'      ,
    'Ñ' : '_ _ . _ _'      ,
    'Ñ' : '_ _ . _ _'      ,
    'Ü' : '. . _ _'        ,
    'Û' : '. . _ _'        ,
    'CH': '_ _ _ _'        ,
    'Š' : '_ _ _ _'        ,
    'ß' : '. . . _ _ . .'  ,
    'Ç' : '_ . _ . .'      ,
    'Ŝ' : '_ . _ . .'      ,
    '1' : '. _ _ _ _'      ,
    '2' : '. . _ _ _'      ,
    '3' : '. . . _ _'      ,
    '4' : '. . . . _'      ,
    '5' : '. . . . .'      ,
    '6' : '_ . . . .'      ,
    '7' : '_ _ . . .'      ,
    '8' : '_ _ _ . .'      ,
    '9' : '_ _ _ _ .'      ,
    '0' : '_ _ _ _ _'      ,
    '?' : '. . _ _ . .'    ,  # Frågetecken
    '!' : '. . _ _ .'      ,  # Utropstecken [1]
    ',' : '_ _ . . _ _'    ,  # Kommatecken
    '.' : '. _ . _ . _'    ,  # Punkt-tecken
    '=' : '_ . . . _'      ,  # Åtskillnadstecken
    '-' : '_ . . . . _'    ,  # Bindestreck, minustecken
    '(' : '_ . _ _ .'      ,  # Vänsterparentes
    ')' : '_ . _ _ . _'    ,  # Högerparentes
    '¤' : '. . . . . . . .',  # Felskrivningstecken (våglinje, bytt till ¤ av mig)
    '+' : '. _ . _ .'      ,  # Procedurtecken "Slut på meddelandet"
    'Æ' : '. . . _ . _'    ,  # Procedurtecken "Slut på sändningen"
    '@' : '. _ _ . _ .'    ,  # Texttecken "Snabel-A". Infördes 2004
    '/' : '_ . . _ .'      ,  # Bråkstreck
    '%' : '. _ _ . .'      ,  # Procent-tecken
    '"' : '. _ . . _ .'    ,  # Citat-tecken
    ';' : '_ . _ . _ .'    ,  # Semikolon
    ':' : '_ _ _ . . .'    ,  # Kolon
    '§' : '. . . _ .'      ,  # Procedurtecken "Förstått"
    '¿' : '. . _ . _'      ,  # Inleder frågesats i spanska och portugisiska
    '~' : '_ . _ . _'      ,  # Procedurtecken "Lystring"
    "'" : '. _ _ _ _ .'    ,  # Apostrof
    '#' : '. _ . . _'      ,  # Skillnadstecken. Kan förenklat symboliseras med //
    '&' : '. _ . . .'      ,  # "Ampersand"
    '$' : '. . . _ . . _'  ,  # SX, "S crossed"
    '√' : '. _ . . .'      ,  # Väntatecken  (sqrt)
    '*' : '. .   . .'      ,  # Upprepningstecken
    '¡' : '_ _ . . . _'}      # Inleder utropssats i spanska och portugisiska

tosign = {
     '. _'            : 'A' ,
     '_ . . .'        : 'B' ,
     '_ . _ .'        : 'C' ,
     '_ . .'          : 'D' ,
     '.'              : 'E' ,
     '. . _ .'        : 'F' ,
     '_ _ .'          : 'G' ,
     '. . . .'        : 'H' ,
     '. .'            : 'I' ,
     '. _ _ _'        : 'J' ,
     '_ . _'          : 'K' ,
     '. _ . .'        : 'L' ,
     '_ _'            : 'M' ,
     '_ .'            : 'N' ,
     '_ _ _'          : 'O' ,
     '. _ _ .'        : 'P' ,
     '_ _ . _'        : 'Q' ,
     '. _ .'          : 'R' ,
     '. . .'          : 'S' ,
     '_'              : 'T' ,
     '. . _'          : 'U' ,
     '. . . _'        : 'V' ,
     '. _ _'          : 'W' ,
     '_ . . _'        : 'X' ,
     '_ . _ _'        : 'Y' ,
     '_ _ . .'        : 'Z' ,
     '. _ _ . _'      : 'Å' ,
     '. _ . _'        : 'Ä' ,
     '_ _ _ .'        : 'Ö' ,
     '. . _ . .'      : 'É' ,
     '_ _ . _ _'      : 'Ñ' ,
     '_ _ . _ _'      : 'Ñ' ,
     '. . _ _'        : 'Ü' ,
     '. . _ _'        : 'Û' ,
     '_ _ _ _'        : 'CH',
     '_ _ _ _'        : 'Š' ,
     '. . . _ _ . .'  : 'ß' ,
     '_ . _ . .'      : 'Ç' ,
     '_ . _ . .'      : 'Ŝ' ,
     '. _ _ _ _'      : '1' ,
     '. . _ _ _'      : '2' ,
     '. . . _ _'      : '3' ,
     '. . . . _'      : '4' ,
     '. . . . .'      : '5' ,
     '_ . . . .'      : '6' ,
     '_ _ . . .'      : '7' ,
     '_ _ _ . .'      : '8' ,
     '_ _ _ _ .'      : '9' ,
     '_ _ _ _ _'      : '0' ,
     '. . _ _ . .'    : '?' ,
     '. . _ _ .'      : '!' ,
     '_ _ . . _ _'    : ',' ,
     '. _ . _ . _'    : '.' ,
     '_ . . . _'      : '=' ,
     '_ . . . . _'    : '-' ,
     '_ . _ _ .'      : '(' ,
     '_ . _ _ . _'    : ')' ,
     '. . . . . . . .': '¤' ,
     '. _ . _ .'      : '+' ,
     '. . . _ . _'    : 'Æ' ,
     '. _ _ . _ .'    : '@' ,
     '_ . . _ .'      : '/' ,
     '. _ _ . .'      : '%' ,
     '. _ . . _ .'    : '"' ,
     '_ . _ . _ .'    : ';' ,
     '_ _ _ . . .'    : ':' ,
     '. . . _ .'      : '§' ,
     '. . _ . _'      : '¿' ,
     '_ . _ . _'      : '~' ,
     '. _ _ _ _ .'    : "'" ,
     '. _ . . _'      : '#' ,
     '. _ . . .'      : '&' ,
     '. . . _ . . _'  : '$' ,
     '. _ . . .'      : '√' ,
     '. .   . .'      : '*' ,
     '_ _ . . . _'    : '¡' }

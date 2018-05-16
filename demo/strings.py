
# -*- coding: utf-8 -*-

def infinitivo(verbo):
    # Toma una cadena que se asume es un verbo
    # y devuelve una cadena que es el verbo en infinitivo
    return verbo.upper() + "R"

nc = ["hombre", "mujer", "libro"]
vi = ["camina", "bebe", "corre"]
vt = ["ama", "invita", "lee"]
d = ["un", "una", "toda", "todo"]
c = ["y", "o", "si ... entonces"]
np = ["pedro", "maria", "juan", "javier", "jose"]


words = raw_input("Ingrese su frase: ")
words1 = words.lower()
words2 = words1.split(' ')
print "La frase en minusculas es: ", words2

# Elimina la preposicion "a"
for w in words2:
    if w == 'a':
        print "Se elimino una a"
        words2.remove(w)

print "La lista de palabras es ", words2
print "La longitud es: ", len(words2)

# crear una lista de categorias con base en word2
categorias = []

for w in words2:
    if w in nc:
        categorias.append('nc')
    elif w in vi:
        categorias.append('vi')
    elif w in vt:
        categorias.append('vt')
    elif w in d:
        categorias.append('d')
    elif w in c:
        categorias.append('c')
    elif w in np:
        categorias.append('np')


print "La lista de categorias es: ", categorias
print "La longitud es: ", len(categorias)

# Decir que la frase no sirve si hay palabras por fuera del rango
if len(categorias) < len(words2):
    print "No puedo computar esta frase (no conozco todas las palabras)"
else:
    # crear un diccionario de categorias
    traducciones = []
    for i in range(len(words2)):
        if categorias[i] == 'nc':
            print "El sustantivo es: ", words2[i]
            sust = infinitivo(words2[i])
            print "El sustantivo es: ", sust
            traducciones.append(lambda x: str(sust) + "(" + str(x) + ")")
        elif categorias[i] == 'np':
            inicial = words2[i][0].lower()
            print "La inicial del nombre es: ", inicial
            traducciones.append(lambda X, inicial=inicial: X(inicial))
        elif categorias[i] == 'vi':
            print "El verbo es: ", words2[i]
            infini = infinitivo(words2[i])
            print "El infinitivo es: ", infini
            traducciones.append(lambda x: str(infini) + "(" + str(x) + ")")
        elif categorias[i] == 'vt':
            print "El verbo es: ", words2[i]
            infini = infinitivo(words2[i])
            print "El infinitivo es: ", infini
            traducciones.append(\
            lambda XX:(lambda x:(XX(lambda y: (str(infini) + "(" + str(x) + "," + str(y) + ")")))))

    n = len(traducciones)
    formula = traducciones[n - 1]
    for i in range(0, n-1):
        j = (n - 2) - i
        print "Operando con palabra " + str(j) + "esima"
        formula = traducciones[j](formula)

    print "La formula en primer orden es: ",
    print formula



print("©Maria Jose & Javier")

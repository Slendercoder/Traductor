
# -*- coding: utf-8 -*-
def infinitivo(verbo):
    # Toma una cadena que se asume es un verbo
    # y devuelve una cadena que es el verbo en infinitivo
    return verbo.upper() + "R"

#lista de palabras de cada categoria.
nc = ["hombre", "mujer", "libro", "animal", "niño","niña","fruta","amigo","amiga","profesor","profesora","edificio","perro", "pajaro","gato","pais","ciudad"]
vi = ["camina", "bebe", "corre", "duerme","nada","sonrie", "vive", "baila", "come","canta","estornuda","fracasa","grita","llora","patina","pelea","respira","trabaja"]
vt = ["ama", "invita", "lee", "compra", "estudia", "escribe","quiere","alimenta","asusta","dice","engaña", "evita", "llama","mira","olvida","necesita","molesta","perdona","visita", "viaja"]
d1 = ["un", "una"]
d2 = ["toda", "todo"]
c = ["y", "o", "si", "entonces"]
np = ["pedro", "maria", "juan", "javier","abel", "mario","valerie", "jose", "angela", "natalia", "rupaul", "carlos", "fernando", "alejandro", "miguel","esteban", "gabriela","oscar","samuel","victor","edgar", "carlos","eduardo", "sergio", "nicolas", "nathalia","camilo","sebastian","isabella","luisa","sara","rodrigo","angel", "daniel", "manuel","andres","felipe","david", "kevin","cristhian","edwin", "julian", "maría", "josé", "juana", "bart", "lisa"]

#pide al usuario una frase y la pasa a minusculas y las divide en una lista.
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
    elif w in d1:
        categorias.append('d1')
    elif w in d2:
        categorias.append('d2')
    elif w in c:
        categorias.append('c')
    elif w in np:
        categorias.append('np')


print "La lista de categorias es: ", categorias
print "La longitud es: ", len(categorias)

# Revisar si hay dos "np"s seguidos y unirlos en uno solo
indices_para_eliminar = []

for i in range(0, len(categorias) - 1):
    if categorias[i] == 'np':
        if categorias[i+1] == 'np':
            print "Hay dos np seguidos en " + str(i) + " y en " + str(i+1)
            indices_para_eliminar.append(i+1)

print "Indices para eliminar ", indices_para_eliminar

#elimiar indices_para_eliminar de words2 y categorias
for t in indices_para_eliminar and categorias :
    if t == 'np':
        print "Se elimino un ", t
        categorias.remove(t)

aux = []
for t in range(len(words2)):
    if t not in indices_para_eliminar:
        aux.append(words2[t])

words2 = aux

print "La lista de palabras es ", words2
print "La longitud es: ", len(words2)

print "La lista de categorias es: ", categorias
print "La longitud es: ", len(categorias)


# Decir que la frase no sirve si hay palabras por fuera del rango
if len(categorias) < len(words2):
    print "No puedo computar esta frase (no conozco todas las palabras)"
else:
    # crear un diccionario de categorias, dónde a cada categoria se le
    # asigna su debida expresión lógica.
    traducciones = []
    for i in range(len(words2)):
        if categorias[i] == 'nc':
            sust = words2[i].lower()
            print "El sustantivo es: ", sust
            traducciones.append(lambda x, sust=sust: str(sust) + "(" + str(x) + ")")
        elif categorias[i] == 'np':
            inicial = words2[i][0].lower()
            print "La inicial del nombre es: ", inicial
            traducciones.append(lambda X, inicial=inicial: X(inicial))
        elif categorias[i] == 'vi':
            print "El verbo es: ", words2[i]
            infini = infinitivo(words2[i])
            print "El infinitivo es: ", infini
            traducciones.append(lambda x, infini=infini: str(infini) + "(" + str(x) + ")")
        elif categorias[i] == 'vt':
            print "El verbo es: ", words2[i]
            infini = infinitivo(words2[i])
            print "El infinitivo es: ", infini
            traducciones.append(\
            lambda XX:(lambda x:(XX(lambda y, infini=infini: (str(infini) + "(" + str(x) + "," + str(y) + ")")))))
        elif categorias[i] == 'd1':
            print "Hay un determinante: ", words2[i]
            traducciones.append(\
            lambda X:(lambda Y:("∃x (" + X('x') + "∧" + Y('x') + ")")))
        elif categorias[i] == 'd2':
            print "Hay un determinante: ", words2[i]
            traducciones.append(\
            lambda X:(lambda Y:("∀x (" + X('x') + "→" + Y('x')  + ")")))


    # Revisar si hay un "d" y si esta seguido de un "nc" y avisar si no
    for j in range(0, len(categorias) - 1):
        if categorias[j] == 'd1':
            if categorias[j + 1] == 'nc':
                print len(traducciones)
                aux = []
                contador = 0
                for k in range(len(traducciones) - 1):
                    if k != j:
                        aux.append(traducciones[contador])
                        contador += 1
                    else:
                        aux.append(traducciones[j](traducciones[j + 1]))
                        contador += 2
                traducciones = aux
                print len(traducciones)
            else:
                print "No puedo computar esta frase (no hay sustantivo despues de determinante)"

        if categorias[j] == 'd2':
            if categorias[j + 1] == 'nc':
                aux = []
                contador = 0
                for k in range(len(traducciones) - 1):
                    if k != j:
                        aux.append(traducciones[contador])
                        contador += 1
                    else:
                        aux.append(traducciones[j](traducciones[j + 1]))
                        contador += 2
                traducciones = aux
            else:
                print "No puedo computar esta frase (no hay sustantivo despues de determinante)"
# Operar con las palabras de derecha a izquierda, aplicando la función lambda
# para integrar una expresión en otra
    n = len(traducciones)
    formula = traducciones[n - 1]
    for i in range(0, n-1):
        j = (n - 2) - i
        formula = traducciones[j](formula)

    print "La formula en primer orden es: ",
    print formula

print("©Maria Jose & Javier")

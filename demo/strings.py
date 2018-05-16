
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
np = ["pedro", "maria", "juan"]


words = raw_input("Ingrese su frase: ")
words1 = words.lower()
words2 = words1.split(' ')

# pasar todas las palabras a minusculas
# revisar que no queden as
# Decir que la frase no sirve si hay palabras por fuera del rango

print "La lista de palabras es ", words2

# crear una lista de categorias con base en word2
categorias = []

for w in words2:
    if w in np:
        categorias.append('np')
    elif w in vi:
        categorias.append('vi')
    # faltan las otras categorias


print "La lista de categorias es: ", categorias

# crear un diccionario de categorias ???????

traducciones = []
for i in range(len(words2)):
    if categorias[i] == 'np':
        inicial = words2[i][0].lower()
        traducciones.append(lambda X: X(inicial))
    elif categorias[i] == 'vi':
        print "El verbo es: ", words2[i]
        infini = infinitivo(words2[i])
        print "El infinitivo es: ", infini
        traducciones.append(lambda x: str(infini) + "(" + str(x) + ")")
        # traducciones.append(lambda x: "(" + str(x) + ")")

formula = ''


formula = traducciones[0](traducciones[1])

print "La formula en primer orden es: ",
print formula



print("©Maria Jose & Javier")

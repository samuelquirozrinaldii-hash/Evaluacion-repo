#biblioteca random
"""Generar números enteros: la función randint()
La función randint(a, b) genera un número entero entre a y b, 
ambos incluidos. a debe ser inferior o igual a b."""
import random

print(random.randint(10, 20))


"""Generar números enteros: la función randrange()
La función randrange(a, b, c) genera un número entero entre 
los valores generados por range(a, b, c). Como ocurre con 
range(), la función randrange() admite uno, dos o tres argumentos."""
import random

print(random.randrange(10, 110, 10))


"""Generar números decimales: la función random()
La función random() genera un número decimal entre 0 y 1 
(puede generar 0, pero no 1)."""
import random

print(random.random())


"""Generar números decimales: la función uniform()
La función uniform(a, b) genera un número decimal 
entre a y b (puede generar a y b, debido a la forma de 
redondear de Python, puede que genere b o no)."""
import random

print(random.uniform(5, 8))

"""Seleccionar un elemento al azar: la función choice()
La función choice(secuencia) elige un valor al azar en un 
conjunto de elementos. Cualquier tipo de datos enumerable 
(tupla, lista, cadena, range) puede utilizarse como conjunto 
de elementos."""
#ej1
import random

print(random.choice((14, 15, 20, 150)))

#ej2
import random

print(random.choice(["alfa", "beta", "gamma"]))

#ej3
import random

print(random.choice("AEIOU"))

#ej4
import random

print(random.choice(range(10)))

#nota: En el caso de conjuntos y diccionarios 
#(que en Python 3 no son elementos iterables, sino iteradores), 
# no se puede utilizar la función choice().
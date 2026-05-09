# Crear diccionario Python
# Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. 
# Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value. 
# En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.

d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(d1)
#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

# Acceder y modificar elementos
# Se puede acceder a sus elementos con [] o también con la función get()

print(d1['Nombre'])     #Sara
print(d1.get('Nombre')) #Sara
# Para modificar un elemento basta con usar [] con el nombre del key y asignar el valor que queremos.

d1['Nombre'] = "Laura"
print(d1)
#{'Nombre': Laura', 'Edad': 27, 'Documento': 1003882}
# Si el key al que accedemos no existe, se añade automáticamente.

d1['Direccion'] = "Calle 123"
print(d1)
#{'Nombre': 'Laura', 'Edad': 27, 'Documento': 1003882, 'Direccion': 'Calle 123'}

# Iterar diccionario
# Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos. Para imprimir los key.

# Imprime los key del diccionario
for x in d1:
    print(x)
#Nombre
#Edad
#Documento
#Direccion

# Se puede imprimir también solo el value.

# Impre los value del diccionario
for x in d1:
    print(d1[x])
#Laura
#27
#1003882
#Calle 123

# O si queremos imprimir el key y el value a la vez.

# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)
#Nombre Laura
#Edad 27
#Documento 1003882
#Direccion Calle 123
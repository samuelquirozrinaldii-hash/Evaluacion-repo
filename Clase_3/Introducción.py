
# Variables; es un espacio de memoria ram para almacenar datos

# Forma de declarar variables
nombre_persona = "Mateo"
nombre_persona= "Juan" 
_nombre_persona = "Mario"

# Formas Incorrectas
# -personas, 4personas, nombres personas

# imprimir
print(nombre_persona)
# Tipos de Variables
# (enteros, decimal, caracter)
# Entero como int = negativos y positivos (NO DECIMALES)

numeroEntero1 = 12
numeroEntero2 = -45

print(numeroEntero1)
print(numeroEntero2)
print(type(numeroEntero1))

# Decimales (float)
numeroDecimal = 3.5
print("numero decimal: "),numeroDecimal
print(type(numeroDecimal))

# Complejos (complex)
numeroImaginarios = 3 + 5J
print("numero imaginario: ",numeroImaginarios)
print (type(numeroImaginarios))

# String (str)
nombreCliente = "Jose"
print("nombre Cliente: ",nombreCliente)
print(type(nombreCliente))

# Booleanos (bool)
cuentaFacebook = True
correoElectronico = False
print("Booleanos: ",nombreCliente)
print(type(cuentaFacebook))

# Listas ([List])
lista = [1,"Arturo",1.3, -500]
print(lista)
print (lista[3])
print(type(lista))

# Poner un campo nuevo
lista.insert(1,"Gonzales")
print (lista)

# Remover un campo
lista.remove(-500)
print(lista)

# Tupla 
tupla = (1,2,3,4,5)
print(tupla)
print(type(tupla))

print(tupla[1])

# Diccionario
estudiante = {
    "nombre" : "juan",
    "edad":19,
    "genero" : "m",
    "nota":3.5,
    "estadoMatricula":True
}

print(estudiante)
print(type(estudiante))

estudiante["nombre"] = "carlos"
print(estudiante.items())

# set{}
conjunto = {1,2,2,3,3,4,4,3,7,5,6,5}
print(conjunto)
print(type(conjunto))

print (4 in conjunto)
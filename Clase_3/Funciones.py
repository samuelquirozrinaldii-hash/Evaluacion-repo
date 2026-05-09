def saludo():
    print("hola mundo")

saludo()
saludo()


def saludo2(nombre):
    print("hola", nombre)

saludo2("Juan")
saludo2("Pedro")
saludo2("Maria")


def suma(a,b):
    print(a+b)

suma(2,3)


# Funcion retorno
def resta(a,b):
    return a-b

resultado1 = resta(10,5)
resultado2 = resta(100,47)
print("la resta 1 es {}, la resta 2 es {}".format(resultado1,resultado2))

# Retorno de valores vacio
def operacio(a=None, b=None):
    if a is None:
        return "no se puede realizar la operacion"
    else:
        return a+b
    


# Ejercicio de conversion de grados
def conversion_celcius(temp,unidad):
    if unidad == "K" or "k":
        c = temp + 273.15
    elif unidad == "F" or "f":
        c = (temp - 32) * 5/9
    else:
        print("debes seleccionar una unidad que sea F o K")
    return c

print("la temperatura en celcius es: ", conversion_celcius(31,"k"))


# Guardar una tupla
def guardar(cad, v=2, *algomas):
    print(cad * v)
    for i in algomas:
        print(i)

guardar("hola", 3, "adios", "chau", "perrito")

# Actividad 
#1. Investigar 3 ejemplos complejos de funciones

# Función con validaciones y múltiples retornos
def calcular_promedio(numeros):
    if not numeros:
        return "La lista está vacía"
    
    if not all(isinstance(n, (int, float)) for n in numeros):
        return "Todos los elementos deben ser números"
    
    promedio = sum(numeros) / len(numeros)
    
    if promedio >= 3:
        return f"Aprobado con promedio {promedio}"
    else:
        return f"Reprobado con promedio {promedio}"

print(calcular_promedio([4, 3, 5]))

# Función que usa funciones internas (función anidada)
def potencia(base, exponente):
    
    def multiplicar(a, b):
        return a * b
    
    resultado = 1
    for _ in range(exponente):
        resultado = multiplicar(resultado, base)
    
    return resultado

print(potencia(2, 4))

# Función con argumentos variables y diccionario
def crear_usuario(nombre, edad, **datos_extra):
    usuario = {
        "nombre": nombre,
        "edad": edad
    }
    
    for clave, valor in datos_extra.items():
        usuario[clave] = valor
    
    return usuario

usuario1 = crear_usuario(
    "Juan", 
    25, 
    ciudad="Medellín", 
    profesion="Ingeniero"
)

print(usuario1)

# Función con validaciones y múltiples retornos

# if not numeros: verifica si la lista está vacía
# all(...): revisa que todos los elementos sean números
# sum() y len(): calculan el promedio
# Tiene varios return, dependiendo del caso

# Función que usa funciones internas (función anidada)
# multiplicar() está definida dentro de potencia()
# Solo se puede usar dentro de esa función
# Se usa un ciclo for para repetir la multiplicación

# Función con argumentos variables y diccionario
# **datos_extra: permite enviar muchos datos adicionales
# Se guardan en forma de diccionario
# Se agregan dinámicamente al usuario


# Ficheros read, write, append
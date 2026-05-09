#-----------yield from --------------
#---ejemplo basico
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas=devuelve_ciudades("medellin","bogota","cali","cartagena")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#---subelementos
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento

ciudades_devueltas=devuelve_ciudades("medellin","bogota","cali","cartagena")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))



#ejercicios numero 1 con yield
# Funcion 1: numeros del 0 al 9
def numeros1():
    for i in range(0, 10):
        yield i

# Funcion 2: numeros del 10 al 20
def numeros2():
    for i in range(10, 21):
        yield i

# Funcion 3: une las dos funciones
def unir():
    yield from numeros1()
    yield from numeros2()

# Uso con for
print("Recorrido con for:")
for num in unir():
    print(num)

# Uso con next (3 datos)
print("\n3 datos con next:")
gen = unir()
print(next(gen))
print(next(gen))
print(next(gen))


#ejercicios yield 2
def ejemp2():
    import random

    def generador_aleatorios():
        for _ in range(7):
            yield random.randint(1, 100)

    # Mostrar los números
    print("Numeros aleatorios:")
    for num in generador_aleatorios():
        print(num)
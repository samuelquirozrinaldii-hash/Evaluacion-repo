# Range: Es una lista de números enteros en sucesion aritmetica

for n in range(10):
    print(n)
    
    
for x in range(20):
    if x % 2 == 0:
     print(x)
else:
    print("Impar")
    
    
# Iterar una lista
x = [0,4,3,6,7]
for num in x:
    print(num)
    
print("Comienzo")
for i in [1,1,1]:
    print("Hola",end=" ")
print()



# Funcion len(): Devuelve la longitud de una cadena

print(len(x))
x = [9,4,6,8,1,3]
for num in range(len(x)):
        print(x[num])
        
# Ejemplo texto y operaciones
print("Comienzo Ejemplo 1")
for i in [3,4,5]:
    print(f"Hola, hora i vale {i} y su cuadrado es: {i ** 2}")
    print("Final")
print("Comienzo Ejemplo 2")
for i in ["Marcela","Esteban",47]:
    print(f"Hola, ahora i vale {i}")
    print("Final")
    
    
# Lista y Potencia
print("Comienzo Ejemplo 2")
for i in [0,1,2,3,4]:
    print(f"{num} * {num} = {num * 2}")
    print("Final")
    
# Mostrar Caracteristicas
for i in "MANSO":
    print(f"Dame una {i}")
print("!CACORRO!")



#------------------- EJERCICIO -------------------
# 1. Cuenta cuántas veces aparece la letra "a" en (Anastacia)
# 2. Sumar todas los números 
# 3. Tabla del 5 (1 al 10)

# 1. Cuenta cuántas veces aparece la letra "a" en (Anastacia)

# Ejercicio 1: Contar la letra "a"
palabra = "Anastacia"
conteo = palabra.lower().count("a")
print(f"La letra 'a' aparece {conteo} veces en '{palabra}'")

# Ejercicio 2: Sumar todos los números
num= [0,1,2,3,4,5,6,7,8,9,10]
conteo= sum(num)
print(conteo)

# Ejercicio 3: Tabla del 5 (1 al 10)
for i in range(1, 10):
    resultado = num * i
    print(f"{num} x {i} = {resultado}") 
    
def ejercicio():
# Ejemplo dado con función random
    import random
    print("Comienzo")
    sacaste_cinco = False
    for i in range(3):
        dado = random.randrange(1,7)
        print(dado)
        
    
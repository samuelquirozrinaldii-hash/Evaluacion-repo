# Ejercicio 1:

precio_normal = 3.49
descuento = 0.60
pan = int(input("Numero de pan viejo: "))
precio_descuento = precio_normal * (1 - descuento)
total = pan * precio_descuento
print("Precio Normal:", precio_normal, "€")
print("Descuento:", descuento * 100, "%")
print("Precio por el pan viejo:", round(precio_descuento, 2), "€")
print("Total:", round(total, 2), "€")


# Ejercicio 2: 
palabra = input("Introduce una palabra: ")
for i in range(10):
    print(palabra)
    

# Ejercicio 3:
edad = int(input("Introduce tu edad: "))
for i in range(1, edad + 1):
    print(i)
    

# Ejercicio 4:
numero = int(input("Introduce un número: "))
for i in range(1, numero + 1):
    print("*" * i)
    
# Ejercicio 5: 
for i in range(0, 11, 2):                
    print(i)

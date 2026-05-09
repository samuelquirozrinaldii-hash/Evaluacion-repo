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
palabra = input("Ingrese una palabra: ")
for i in range(10):
    print(palabra)
    

# Ejercicio 3:
edad = int(input("Ingrese su edad: "))
for i in range(1, edad + 1):
    print(i)
    

# Ejercicio 4:
numero = int(input("Ingresa un numero: "))
for i in range(1, numero + 1):
    print("*" * i)
    
# Ejercicio 5: 
for i in range(2, 102, 2):
    print(i)
    
# Ejercicio 6: 
def verificar_contrasena():
    contra = "ChurreneVSChochi"      
    while True:                    
        intento = input("Introduce la contraseña: ")   
        if intento == contra:  
            print("¡Contraseña correcta! Acceso concedido.")
            break                  
        else:
            print("Contraseña incorrecta. Intenta de nuevo.")          
verificar_contrasena()

# Ejercicio 7:
def positivo_o_negativo():
    num = None
    while num != 0:
        num = int(input("Introduce un numero (0 para salir): "))
        if num > 0:
            print(f"{num} Es positivo")
        elif num < 0:
            print(f"{num} Es negativo")
        else:
            print("Bueno Chao.")
positivo_o_negativo()

# Ejercicio 8:
def corta_o_larga():
    palabra = input("Escriba una palabra: ")
    if len(palabra) <= 4:
        print(f'"{palabra}" es una palabra CORTA ({len(palabra)} letras).')
    else:
        print(f'"{palabra}" es una palabra LARGA ({len(palabra)} letras).')
corta_o_larga()

# Ejercicio 9:
def cuenta_regresiva():
    print("Iniciando cuenta regresiva para el despegue...")
    for i in range(10, 0, -1):
        print(i)
    print("¡DESPEGUE!")
cuenta_regresiva()

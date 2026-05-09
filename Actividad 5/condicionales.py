# if condicional

# numero=int(input("Escriba un número positivo: "))
# if numero < 0:
#     print("Su numero es negativo")
# if numero ==0:
#     print("Su numero es cero")
# if numero>0:
#     print("Su numero es positivo")
# print(f"Ha escrito el numero {numero}")


# if else

# print("=================================")
# edad = int(input("¿Cuantos años tienes?: "))
# if edad>=18:
#     print(f"Tienes {edad}, puedes ingresar. Eres mayor de 18 años.")
# else:
#     print(f"Tienes {edad}, no puedes entrar. Debes ser mayor de 18 años.")
# print("=================================")
# print("ALGORITMO TERMINADO")



#Número par o impar: "Dado un numero entero, informar si el mismo es par o impar"
# numero = int(input("Escriba un número entero: "))
# res=numero%2
# if res!=0:
#     print(f"El número {numero} es impar")
# else: 
#     print(f"el numero {numero} es par.")



#Aprobacion examen: "Un estudiante aprueba si su nota es mayor o igual a 10.5."
# nota=float(input("Ingrese su nota: "))
# if nota>=10.5:
#     print("Usted aprobó el módulo")
# else: 
#     print("Usted reprobó el módulo.")
    

#Condiciones anidadas
# print("Este programa mezcla dos colores. (r) Rojo. (a) Azul.")
# primera=input("Elija un color. (r) ó (a)")
# if primera=="r":
#     print("(a) Azul. (v) Verde.")
#     segunda=input("Escoja uno, (a) ó (v)")
#     if segunda=="a":
#         print("La mezcla entre azul y rojo da morado.")
#     else:
#         print("La mezcla entre Rojo y verde da Café.")
# else:
#     print("(r) rojo. (v) Verde.")
#     segunda=input("Escoja uno, (r) ó (v)")
#     if segunda=="r":
#         print("La mezcla entre rojo y azul da morado .")
#     else:
#         print("La mezcla entre azul y verde da azul verdoso.")
         

#Cajero Automático (Simulación de PIN)
# Enunciado: El programa debe pedir una clave de acceso (ej: 1234).
# Si la clave es correcta: Pregunta cuánto dinero quiere retirar.
# Si el monto es menor o igual al saldo disponible (pon un saldo fijo de $500): Imprime "Retiro exitoso".
# Si es mayor al saldo: Imprime "Saldo insuficiente".
# Si la clave es incorrecta: Imprime "Acceso denegado".

# print("=============================")
# print("CAJERO AUTOMATICO")
# print("=============================")
# clave=1607
# clavein=int(input("Escriba su clave: "))
# if clavein==clave:
#     print("========ACCESO ACEPTADO========")
#     saldo=500
#     print(f"Su saldo es de {saldo}$")
#     retiro=int(input("Cuando deseas retirar?: "))
#     if retiro<=saldo:
#         saldo=saldo-retiro
#         print(f"========= RETIRO EXITOSO; USTED RETIRÓ: {retiro}$ =========")
#         print(f"SU SALDO RESTANTE ES DE {saldo}$")
#     else: 
#         print("========== FONDOS INSUFICIENTES ==========")
# else:
#     print("========ACCESO DENEGADO========");



# Escribe un algoritmo que solicite al usuario tres números enteros distintos y los 
# muestre en pantalla ordenados de mayor a menor. Debes utilizar condiciones anidadas para comparar los números entre sí

# num1=int(input("Escriba el primer numero: "))
# num2=int(input("Escriba el segundo numero: "))
# num3=int(input("Escriba el tercer numero: "))

# if num1>num2>num3:
#     print(num1, num2, num3)

# if num2>num3>num1:
#     print(num2, num3, num1)
    
# if num3>num1>num2:
#     print(num3, num1, num2)
    
# if num2>num1>num3:
#     print(num2, num1, num3)
    
# if num1>num3>num2:
#     print(num1, num3, num2) 
    
# if num3>num2>num1:
#     print(num3, num2, num1)


#EJERCICIO 1
# horasTotales =int(input("Cuantas horas: "))
# semanas=int(horasTotales/168)
# horasRest=horasTotales%168
# dias=horasRest/24
# horas=horasRest%24
# print(f"{horasTotales} horas son equivalentes a {semanas} semanas, {dias} dias, {horas} horas.")


#EJERCICIO 2
# descuento= 0.2
# compra=float(input("Cuanto gastaste en total en Mega Plaza hoy?: "))

# if compra>=300:
#     dto=compra*descuento
#     total=compra-dto
#     print(f"SUBTOTAL: {compra}$ -20%dto: TOTAL: {total}$")
# else:
#     print(f"Tus compras de {compra}$ no suman el mínimo de 300$ para aplicar el descuento.")


#EJERCICIO 3
# horas=int(input("Cuantas horas trabajaste esta semana?:"))
# horasExtras=horas-40
# if horas<= 40:
#     total=horas*16
#     print(f"Esta semana trabajaste {horas} horas, no hiciste más de 40 horas, entonces tu salario es de {total}$")
# else:
#     total=((horas-horasExtras)*16)+(horasExtras*20)
#     print(f"Si trabajaste {horas}, significa que hiciste {horasExtras} horas extras; por lo que tu salario fue de {total}$")
    
    
    
#EJERCICIO 5
print("=========================")
numero=int(input("Escriba un numero entre 0 y 99999: "))
if numero<10:
    print(f"{numero} tiene 1 cifra")
elif numero<100:
    print(f"{numero} tiene 2 cifras")
elif numero<1000:
    print(f"{numero} tiene 3 cifras")
elif numero<10000:
    print(f"{numero} tiene 4 cifras")
elif numero<100000:
    print(f"{numero} tiene 5 cifras")
else:
    print("El numero debe de estar entre 0 y 99999")
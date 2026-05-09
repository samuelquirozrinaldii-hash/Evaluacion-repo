# Operaciones Logicos
# + - * / % **
# Jerarquía de operaciones
# (), ** raíz, */, *-

print(34*45+3/(34**7))

# Operadores Relacionados
# >, <, ==, >=, <=, !=
print(12<3)
print(12>3)
print(12==3)
print(12>=3)
print(12!=3)

# Operadores Logicos
# And Or Not

resultado1 = 4>3 and 10<20
print(resultado1)

resultado1 = 4>3 or 10>20
print(resultado1)

resultado1 = not 3>4
print(resultado1)

año = 2026
mes = "Febrero"

resultado1 = año == 2020 and mes == "Febrero"
print(resultado1)

resultado1 = año == 2020 or mes == "Febrero"
print(resultado1)

# Entre Datos

nombre = input("Ingresa Nombre")
genero = input("Ingresa 'M' de Masculino o 'F' de Femenino")
edad = int(input("Ingresar Edad:"))

if(edad>18 and genero == "F"):
    print(f"Usted {nombre} Puede Ingresar Al Bar!!")
    print(f"Su Edad Es {edad} Y Su Género {genero}")
    
    
else:
    print("Usted No Puede Ingresar.")
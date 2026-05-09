# ============================================================
# Taller de Python – Ciclos y Condicionales (10 ejercicios)
# ============================================================

# ----------------------------
# 1. Contar números múltiplos de 5
# ----------------------------
print("=" * 40)
print("1. Contar múltiplos de 5")
print("=" * 40)

contador = 0
for i in range(10):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    if numero % 5 == 0:
        contador += 1

print(f"Cantidad de múltiplos de 5: {contador}")


# ----------------------------
# 2. Suma de números impares
# ----------------------------
print("\n" + "=" * 40)
print("2. Suma de números impares")
print("=" * 40)

N = int(input("Ingresa un número N: "))
suma = 0
for i in range(1, N + 1):
    if i % 2 != 0:
        suma += i

print(f"Suma de impares del 1 al {N}: {suma}")


# ----------------------------
# 3. Cajero automático simple
# ----------------------------
print("\n" + "=" * 40)
print("3. Cajero automático")
print("=" * 40)

saldo = 1000

while True:
    print("\n--- Menú ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    elif opcion == "2":
        monto = float(input("¿Cuánto deseas retirar? $"))
        if monto > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Saldo restante: ${saldo}")
    elif opcion == "3":
        monto = float(input("¿Cuánto deseas depositar? $"))
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
    elif opcion == "4":
        print("Hasta luego. ¡Que tengas un buen día!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")


# ----------------------------
# 4. Número primo
# ----------------------------
print("\n" + "=" * 40)
print("4. Número primo")
print("=" * 40)

numero = int(input("Ingresa un número: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} ES un número primo.")
else:
    print(f"{numero} NO es un número primo.")


# ----------------------------
# 5. Contar dígitos de un número
# ----------------------------
print("\n" + "=" * 40)
print("5. Contar dígitos")
print("=" * 40)

numero = input("Ingresa un número entero: ")
# Ignoramos el signo negativo si lo hay
digitos = len(numero.replace("-", ""))
print(f"El número {numero} tiene {digitos} dígito(s).")


# ----------------------------
# 6. Serie de números descendente
# ----------------------------
print("\n" + "=" * 40)
print("6. Serie descendente")
print("=" * 40)

N = int(input("Ingresa un número N: "))
for i in range(N, 0, -1):
    print(i)


# ----------------------------
# 7. Sumar números positivos
# ----------------------------
print("\n" + "=" * 40)
print("7. Suma de positivos")
print("=" * 40)

suma_positivos = 0
for i in range(8):
    num = float(input(f"Número {i + 1}: "))
    if num > 0:
        suma_positivos += num

print(f"Suma de los números positivos: {suma_positivos}")


# ----------------------------
# 8. Contar letras en una frase
# ----------------------------
print("\n" + "=" * 40)
print("8. Contar letras sin espacios")
print("=" * 40)

frase = input("Ingresa una frase: ")
letras = len(frase.replace(" ", ""))
print(f"La frase tiene {letras} letra(s) (sin contar espacios).")


# ----------------------------
# 9. Número mayor ingresado
# ----------------------------
print("\n" + "=" * 40)
print("9. Número mayor ingresado")
print("=" * 40)

mayor = None
print("Ingresa números (escribe -1 para terminar):")

while True:
    num = int(input("Número: "))
    if num == -1:
        break
    if mayor is None or num > mayor:
        mayor = num

if mayor is not None:
    print(f"El número mayor ingresado fue: {mayor}")
else:
    print("No ingresaste ningún número.")


# ----------------------------
# 10. Patrón de asteriscos
# ----------------------------
print("\n" + "=" * 40)
print("10. Patrón de asteriscos")
print("=" * 40)

N = int(input("Ingresa un número N: "))
for i in range(1, N + 1):
    print("*" * i)
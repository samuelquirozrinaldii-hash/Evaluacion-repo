c1 = float(input("Ingrese Su Nota 1: "))
c2 = float(input("Ingrese Su Nota 2: "))
c3 = float(input("Ingrese Su Nota 3: "))
print("Suma:", c1 + c2 + c3)


nom = str(input("Digite su nombre: "))
horasSemanales = float(input("Ingrese las horas semanales trabajadas: "))
vaHora = int(input("Ingrese el valor ganado por horas: "))
salario = horasSemanales * vaHora
print("El trabajador",nom,"gana semanal",salario)



dolarQuiroz = float(input("ingrese el N de dolares de Quirozz: "))
dolarMonti = dolarQuiroz / 2
dolarMurillo = (dolarQuiroz + dolarMonti)/2
total = dolarQuiroz + dolarMonti + dolarMurillo
print("\nQuiroz tiene $ ",dolarQuiroz," \nMonti tiene $ ",dolarMonti," \nMurillo tiene $ ",dolarMurillo," \ntotal entre los tres 4 $",total)

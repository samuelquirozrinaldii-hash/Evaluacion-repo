# BIBLIOTECA DEL POETA

ARCHIVO = "biblioteca.txt"

# AÑADIR POEMA

def añadir_poema():
    try:
        titulo = input("Título del poema: ")
        autor = input("Autor del poema: ")

        print("Escribe el poema (FIN para terminar):")
        contenido = []

        while True:
            linea = input()
            if linea.upper() == "FIN":
                break
            contenido.append(linea)

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"TITULO: {titulo}\n")
            archivo.write(f"AUTOR: {autor}\n")
            archivo.write("CONTENIDO:\n")

            for linea in contenido:
                archivo.write(linea + "\n")

            archivo.write("---\n")

        print("✅ Poema guardado correctamente\n")

    except Exception as e:
        print("❌ Error:", e)



# LISTAR TITULOS

def listar_titulos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            print("\n📚 LISTA DE TÍTULOS:\n")

            for linea in archivo:
                if linea.startswith("TITULO:"):
                    print(linea.replace("TITULO:", "").strip())

            print()

    except FileNotFoundError:
        print("❌ No existe el archivo biblioteca.txt\n")



# BUSCAR POR AUTOR

def buscar_por_autor():
    try:
        autor_buscar = input("Ingrese el autor: ").lower()
        encontrado = False

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            poemas = archivo.read().split("---\n")

            for poema in poemas:
                if autor_buscar in poema.lower():
                    print("\n📖 POEMA ENCONTRADO:\n")
                    print(poema)
                    encontrado = True

        if not encontrado:
            print("❌ No se encontraron poemas de ese autor\n")

    except FileNotFoundError:
        print("❌ No existe el archivo biblioteca.txt\n")


# CONTADOR DE VERSOS

def contar_versos():
    try:
        max_versos = 0

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            poemas = archivo.read().split("---\n")

            for poema in poemas:
                lineas = poema.strip().split("\n")

                contar = False
                versos = 0

                for linea in lineas:
                    if linea == "CONTENIDO:":
                        contar = True
                        continue

                    if contar and linea.strip() != "":
                        versos += 1

                if versos > max_versos:
                    max_versos = versos

        print(f"📏 El poema más largo tiene {max_versos} versos\n")

    except FileNotFoundError:
        print("❌ No existe el archivo biblioteca.txt\n")

# MENU PRINCIPAL

def menu():
    while True:
        print("====== BIBLIOTECA DEL POETA ======")
        print("1. Añadir poema")
        print("2. Listar títulos")
        print("3. Buscar por autor")
        print("4. Contador de versos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            añadir_poema()
        elif opcion == "2":
            listar_titulos()
        elif opcion == "3":
            buscar_por_autor()
        elif opcion == "4":
            contar_versos()
        elif opcion == "5":
            print("👋 Programa finalizado")
            break
        else:
            print("❌ Opción inválida\n")


# EJECUCION
menu()
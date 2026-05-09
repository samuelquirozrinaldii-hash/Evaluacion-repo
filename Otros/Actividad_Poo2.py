# Punto 1 y 3: Clase Padre con validación en altura
class Padre:
    def __init__(self, color_ojos, forma_cara, altura):
        # Atributos protegidos (uso de _)
        self._color_ojos = color_ojos
        self._forma_cara = forma_cara
        
        # Validación de datos (Punto 3)
        if altura > 0:
            self._altura = altura
        else:
            self._altura = 1.60

    # Punto 2: Método de identidad
    def presentar_rasgos(self):
        print(f"Color de ojos: {self._color_ojos}")
        print(f"Forma de cara: {self._forma_cara}")
        print(f"Altura: {self._altura}")

# Punto 2: Clase Hija con herencia y sobrescritura
class Hija(Padre):
    def __init__(self, color_ojos, forma_cara, altura, talento):
        # Inicializa los atributos del padre
        super().__init__(color_ojos, forma_cara, altura)
        # Atributo propio de la hija
        self._talento = talento

    # Sobrescritura del método
    def presentar_rasgos(self):
        super().presentar_rasgos()
        print(f"Talento: {self._talento}")

# --- Pruebas del Punto 3 ---

print("--- Caso con altura inválida (-5) ---")
# Se intenta pasar -5, el sistema debería corregirlo a 1.60 automáticamente
persona_hija2 = Hija("Verdes", "Redonda", -5, "Cantar")
persona_hija2.presentar_rasgos()
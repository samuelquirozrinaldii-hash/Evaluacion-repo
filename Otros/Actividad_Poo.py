# Razgos del padre
class Padre:
    def __init__(self, color_ojos, forma_cara, altura):
        self._color_ojos = color_ojos
        self._forma_cara = forma_cara
        
        # Para determinar la altura
        if altura > 0:
            self._altura = altura
        else:
            self._altura = 1.60

    def presentar_rasgos(self):
        print("Color de ojos:", self._color_ojos)
        print("Forma de cara:", self._forma_cara)
        print("Altura:", self._altura)


# Para la hija (Razgos heredados del padre)
class Hija(Padre):
    
    def __init__(self, color_ojos, forma_cara, altura, talento):
        super().__init__(color_ojos, forma_cara, altura)
        self.talento = talento

    # Sobrescritura del método
    def presentar_rasgos(self):
        super().presentar_rasgos()
        print("Talento:", self.talento)


# Resultado

print("---- Caso normal ----")
persona_hija = Hija("Azules", "Ovalada", 1.70, "Tocar el piano")
persona_hija.presentar_rasgos()

print("\n---- Caso con altura inválida ----")
persona_hija2 = Hija("Verdes", "Redonda", -5, "Cantar")
persona_hija2.presentar_rasgos()
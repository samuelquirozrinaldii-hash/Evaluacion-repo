class Vehiculos():
    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__enMarcha = False 
        self.__acelera = False
        self.__frenos = False
    
    def arrancar(self):
        self.__enMarcha = True
    def arrancar(self):
        self.__acelera = True
    def arrancar(self):
        self.__frenos = True
    def estado(self):
        print("Marca: ", self.__marca, "\nModelo: ", self.__modelo,
        "\nEn Marcha: ", self.__enMarcha, "\nAcelerando: ", self.__acelera,
        "\nFrenando: ", self.__frenos) 
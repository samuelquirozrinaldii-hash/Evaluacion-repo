class Coche():# clase (Fabrica de objetos)   
    def __init__(self,largoChasis,anchoChasis,ruedas,enMarcha): # constructor inicial
    # atributos o propiedades
       self.__largoChasis = largoChasis
       self.__anchoChasis = anchoChasis
       self.__ruedas = ruedas
        # estado
       self.__enMarcha = enMarcha
   
    def arrancar(self):
       # pass #no haga nada
       self.enMarcha = True
    def estado(self):
       if(self.enMarcha):
           return "El coche esta en marcha chasis"
       else:
           return "El coche esta parado"
    
     

# instancia 
# miCoche1 = Coche() # objeto

# print("el largo del coche es: ",miCoche1.largoChasis)
# print("el coche tiene ",miCoche1.ruedas," ruedas")
# # comportamiento
# miCoche1.arrancar() #metodo
# print(miCoche1.estado())

# print("------otra instancia o objecto---------")

# miCoche2 = Coche()
# miCoche2.largoChasis = 300
# print("el largo del coche 1 es: ",miCoche1.largoChasis)
# print("el largo del coche 2 es: ",miCoche2.largoChasis)

print("------otra instancia o objecto---------")

miCoche3 = Coche(200,100,3,True)
# print("el largo del coche 3 es: ",miCoche3.largoChasis)
# print("el coche tiene ",miCoche3.ruedas," ruedas")
miCoche3.enMarcha = True
print(miCoche3.estado())
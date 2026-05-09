# Método load(),carga de los datos del fichero binario anterior

#---serializacion volcar datos
import pickle

lista_nombres=["pedro","ana","maria","isabel"]

fichero_binario=open("lista_nombre","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()
#del fichero_binario#eliminar fichero del espacio de memoria

#---serializacion Carga de datos
#rescatamos La informacion por medio de python
fichero = open("lista_nombre","rb")

lista=pickle.load(fichero)

print(lista)
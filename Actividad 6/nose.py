#----------------------------DICCIONARIO PARA EMPRESAS----------------------------
empresa_carga = {
    "conductores": Conductores,
    "coteros": Coteros
}
Conductores= [
    {"Nombre": "John Porkynsom","Identificación": "1001", "Licencia": "C2", "Vehiculo": "Camión"},
    {"Nombre": "Arnol Suaseneger","Identificación": "1002", "Licencia": "B2", "Vehiculo": "Tractomula"},
    {"Nombre": "Padre Mis Amores","Identificación": "1003", "Licencia": "C1", "Vehiculo": "Camioneta"},
    {"Nombre": "Quim Yon Un","Identificación": "1004", "Licencia": "B1", "Vehiculo": "Camión"},
    {"Nombre": "Martin Aguirre","Identificación": "1005", "Licencia": "B3", "Vehiculo": "Camioneta"},
    {"Nombre": "Manso Cacorro","Identificación": "1006", "Licencia": "C4", "Vehiculo": "Tractomula"},
    {"Nombre": "Nicolas Jackson","Identificación": "1007", "Licencia": "C2", "Vehiculo": "Camión"},
    {"Nombre": "Esteban Quito","Identificación": "1008", "Licencia": "B2", "Vehiculo": "Tractomula"},
    {"Nombre": "Angel Avid","Identificación": "1009", "Licencia": "A1", "Vehiculo": "Camioneta"},
    {"Nombre": "Hector Vespussy","Identificación": "1010", "Licencia": "B1", "Vehiculo": "Camión"},

],
Coteros= [
    {"Nombre": "Enzo Petuccini","Identificación": "1001", "Turno": "C2", "kg_capacidad": 496},
    {"Nombre": "Esteban Nano","Identificación": "1002", "Turno": "B2", "kg_capacidad": 853},
    {"Nombre": "Myke Hawk","Identificación": "1003", "Turno": "C1", "kg_capacidad": 430},
    {"Nombre": "CR7","Identificación": "1004", "Turno": "B1", "kg_capacidad": 670},
    {"Nombre": "Messi","Identificación": "1005", "Turno": "B3", "kg_capacidad": 889},
],

# Mostrar conductores
print("=" * 50)
print("           CONDUCTORES DE LA EMPRESA")
print("=" * 50)
for conductor in empresa_carga['conductores']:
    print(f"Nombre: {conductor['nombre']} | Cédula: {conductor['cedula']} | "
          f"Licencia: {conductor['licencia']} | Vehículo: {conductor['vehiculo']}")

# Mostrar coteros
print("\n" + "=" * 50)
print("            COTEROS DE LA EMPRESA")
print("=" * 50)
for cotero in empresa_carga['coteros']:
    print(f"Nombre: {cotero['nombre']} | Cédula: {cotero['cedula']} | "
          f"Turno: {cotero['turno']} | Capacidad: {cotero['kg_capacidad']} kg")

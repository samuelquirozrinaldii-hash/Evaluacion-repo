# -------- Empresa de Carga - Diccionario con FOR --------

empresa_carga = {
    'conductores': [
        {"nombre": "Carlos Pérez",    "cedula": "1001", "licencia": "C2", "vehiculo": "Camión"},
        {"nombre": "Andrés Gómez",    "cedula": "1002", "licencia": "C1", "vehiculo": "Tractomula"},
        {"nombre": "Luis Martínez",   "cedula": "1003", "licencia": "C2", "vehiculo": "Camión"},
        {"nombre": "Jorge Ramírez",   "cedula": "1004", "licencia": "B3", "vehiculo": "Camioneta"},
        {"nombre": "Ricardo Torres",  "cedula": "1005", "licencia": "C2", "vehiculo": "Camión"},
        {"nombre": "Mario Herrera",   "cedula": "1006", "licencia": "C1", "vehiculo": "Tractomula"},
        {"nombre": "Pedro Castillo",  "cedula": "1007", "licencia": "C2", "vehiculo": "Camión"},
        {"nombre": "Juan Vargas",     "cedula": "1008", "licencia": "B3", "vehiculo": "Camioneta"},
        {"nombre": "Fabio Morales",   "cedula": "1009", "licencia": "C1", "vehiculo": "Tractomula"},
        {"nombre": "Sergio Díaz",     "cedula": "1010", "licencia": "C2", "vehiculo": "Camión"},
    ],
    'coteros': [
        {"nombre": "Edwin Ríos",      "cedula": "2001", "turno": "Mañana",  "kg_capacidad": 80},
        {"nombre": "Camilo Suárez",   "cedula": "2002", "turno": "Tarde",   "kg_capacidad": 75},
        {"nombre": "Nelson Pardo",    "cedula": "2003", "turno": "Mañana",  "kg_capacidad": 90},
        {"nombre": "Iván Ospina",     "cedula": "2004", "turno": "Noche",   "kg_capacidad": 85},
        {"nombre": "Brayan Lozano",   "cedula": "2005", "turno": "Tarde",   "kg_capacidad": 78},
    ]
}

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
# diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Gema Guadamud",
    "Edad": 32,
    "Ciudad": "Santodomingo de los sachilas",
    "Profesion": "Venta en vive wow"
}

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["Telefono"] = "0939884530"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal:")
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")
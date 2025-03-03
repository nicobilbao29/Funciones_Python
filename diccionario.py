# Crear un diccionario
persona = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Santiago',
    'profesion': 'Ingeniero'
}

# Acceder a un valor por clave
print(persona['nombre'])  # Juan
print(persona['edad'])    # 30

# Modificar un valor en el diccionario
persona['edad'] = 31

# Agregar un nuevo par clave-valor
persona['pais'] = 'Chile'

# Eliminar un par clave-valor
del persona['ciudad']

# Imprimir el diccionario modificado
print(persona)  
# {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero', 'pais': 'Chile'}

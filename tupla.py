# Crear una tupla
frutas = ('manzana', 'plátano', 'cereza', 'naranja')

# Acceder a elementos de la tupla (por índice)
print(frutas[0])  # manzana
print(frutas[2])  # cereza

# Intentar modificar una tupla (esto dará error porque las tuplas son inmutables)
# frutas[1] = 'kiwi'  # Esto causará un error

# Convertir una tupla a lista para modificarla
frutas_lista = list(frutas)
frutas_lista[1] = 'kiwi'
frutas = tuple(frutas_lista)

# Imprimir la tupla modificada
print(frutas)  # ('manzana', 'kiwi', 'cereza', 'naranja')

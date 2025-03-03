def contar_palabras(texto):
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

# Ejemplo de uso
texto_ejemplo = "Este es un ejemplo de texto para contar palabras."
resultado = contar_palabras(texto_ejemplo)
print(f"Cantidad de palabras: {resultado}")

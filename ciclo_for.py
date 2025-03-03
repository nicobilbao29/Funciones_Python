# Pedir al usuario cuántos datos quiere ingresar
n = int(input("¿Cuántos datos quieres ingresar? "))

# Lista para almacenar los datos ingresados
datos = []

# Bucle for para ingresar datos
for i in range(n):
    dato = input(f"Ingrese el dato {i+1}: ")
    datos.append(dato)

# Mostrar los datos ingresados
print("Los datos ingresados son:", datos)

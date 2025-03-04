import pandas as pd
import matplotlib.pyplot as plt

# 📌 Ruta del archivo
archivo_excel = r"D:\FLASK\Funciones_Python\mis_productos.xlsx"

# 📌 Leer el archivo Excel
df = pd.read_excel(archivo_excel, engine="openpyxl")

# 📌 Convertir nombres de columnas a minúsculas y quitar espacios
df.columns = df.columns.str.lower().str.strip()

# 📌 Mostrar las primeras filas y tipos de datos
print("Columnas disponibles:", df.columns)
print(df.head())
print(df.dtypes)  # Verifica los tipos de datos

# 📌 Convertir la columna 'monto' a numérico (por si hay errores en los datos)
df["monto"] = pd.to_numeric(df["monto"], errors="coerce")

# 📌 Verificar los tipos de datos después de la conversión
print(df.dtypes)

# 📌 Agrupar por categoría y sumar los montos
df_agrupado = df.groupby("categoria")["monto"].sum().reset_index()

# 📌 Ver los datos agrupados antes de graficar
print(df_agrupado)

# 📌 Crear el gráfico solo si hay datos válidos
if not df_agrupado.empty:
    plt.figure(figsize=(10, 6))
    
    # 📌 Cambiar el color a verde
    plt.bar(df_agrupado["categoria"], df_agrupado["monto"], color="green")

    # 📌 Personalizar el gráfico
    plt.xlabel("Categoría")
    plt.ylabel("Monto Total")
    plt.title("Monto Total por Categoría")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # 📌 Mostrar valores en las barras
    for i, valor in enumerate(df_agrupado["monto"]):
        plt.text(i, valor, f"{valor:.2f}", ha="center", va="bottom", fontsize=10)

    # 📌 Guardar el gráfico como una imagen PNG
    plt.savefig(r"D:\FLASK\Funciones_Python\grafico_categoria_monto.png")

    # 📌 Mostrar el gráfico
    plt.show()
else:
    print("No hay datos para graficar.")

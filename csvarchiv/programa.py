#creadores Julio Leonel Rubio Ramirez, brayan josue flores gonzalez, 
#carlos ernesto valadez beristain, jose de jesus araiza rogrigez


import csv
import matplotlib.pyplot as plt

archivo_mujeres = 'mujeres.csv'  # Ruta del archivo CSV de mujeres
archivo_hombres = 'hombres.csv'  # Ruta del archivo CSV de hombres
archivo_nombres = 'nombres.csv'  # Ruta del archivo CSV con nombres mezclados

# Diccionarios para almacenar nombres de hombres y mujeres
nombres_hombres = {}
nombres_mujeres = {}

# Contadores para hombres y mujeres
hombres = 0
mujeres = 0

# Leer archivo de hombres
with open(archivo_hombres, 'r') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # Omitir la primera fila si contiene encabezados

    for fila in lector_csv:
        nombre = fila[0].lower()  # Suponemos que el nombre está en la primera columna

        if nombre not in nombres_hombres:
            nombres_hombres[nombre] = True

# Leer archivo de mujeres
with open(archivo_mujeres, 'r') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # Omitir la primera fila si contiene encabezados

    for fila in lector_csv:
        nombre = fila[0].lower()  # Suponemos que el nombre está en la primera columna

        if nombre not in nombres_mujeres:
            nombres_mujeres[nombre] = True

# Leer archivo de nombres mezclados
with open(archivo_nombres, 'r') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)  # Omitir la primera fila si contiene encabezados

    for fila in lector_csv:
        nombre = fila[0].lower()  # Suponemos que el nombre está en la primera columna

        if nombre in nombres_hombres:
            hombres += 1
        elif nombre in nombres_mujeres:
            mujeres += 1
            

etiquetas = ['Hombres', 'Mujeres']
valores = [hombres, mujeres]

# Crear gráfico de barras
plt.bar(etiquetas, valores)

# Configurar el título y etiquetas de los ejes
plt.title('Cantidad de Hombres y Mujeres')
plt.xlabel('Género')
plt.ylabel('Cantidad')

# Mostrar el gráfico
plt.show()

print(f"Cantidad de hombres: {hombres}")
print(f"Cantidad de mujeres: {mujeres}")
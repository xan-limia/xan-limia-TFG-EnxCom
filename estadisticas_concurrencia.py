import numpy as np
import matplotlib.pyplot as plt

clientes = 5
peticiones = 50
pruebas = 5

carpeta = f'./resultados/concurrencia_medium/{clientes}clientes'

def leer_numeros(ruta):
    with open(ruta, 'r') as archivo:
        numeros = [float(linea.strip()) for linea in archivo]
    return numeros

def estadisticas(numeros):
    valor_minimo = min(numeros)
    valor_maximo = max(numeros)
    valor_medio = sum(numeros) / len(numeros)
    return valor_minimo, valor_medio, valor_maximo

def calcular_medias_estadisticas():
    minimos = []
    medios = []
    maximos = []
    numeros_totales = []  

    for i in range(1, pruebas+1):
        ruta = f'{carpeta}/test{clientes}x{peticiones}_{i}.txt'
        numeros = leer_numeros(ruta)
        if numeros:
            valor_minimo, valor_medio, valor_maximo = estadisticas(numeros)
            minimos.append(valor_minimo)
            medios.append(valor_medio)
            maximos.append(valor_maximo)
            numeros_totales.extend(numeros)  
        else:
            print(f"{ruta} no tiene numeros")

    # Calcular las medias de los valores mínimos, medios y máximos
    media_minimos = np.mean(minimos)
    media_medios = np.mean(medios)
    media_maximos = np.mean(maximos)

    # Calcular las desviaciones estándar
    std_minimos = np.std(minimos)
    std_medios = np.std(medios)
    std_maximos = np.std(maximos)

    return (media_minimos, std_minimos), (media_medios, std_medios), (media_maximos, std_maximos), numeros_totales

def diagrama_cajas_percentiles(numeros):
    # Calcular percentiles
    percentiles = [50, 75, 90, 95, 99]
    valores_percentiles = np.percentile(numeros, percentiles)

    # Percentiles
    print("\n--- Percentiles ---")
    for p, valor in zip(percentiles, valores_percentiles):
        print(f"{p} percentil: {valor}")

    # Diagrama de cajas
    boxplot = plt.boxplot(numeros, vert=False, patch_artist=True)

    # Color de la caja
    for box in boxplot['boxes']:
        box.set(facecolor='lightblue')

    # Lineas de percentiles
    colores_percentiles = ['red', 'green', 'blue', 'purple', 'cyan']
    for p, valor, color in zip(percentiles, valores_percentiles, colores_percentiles):
        plt.axvline(x=valor, color=color, linestyle='--', label=f'{p} percentil: {valor:.2f}')
    
    plt.legend(loc='upper right')
    plt.title(f"{clientes} clientes")
    plt.xlabel("Segundos")

    plt.show()

def main():

    (media_minimos, std_minimos), (media_medios, std_medios), (media_maximos, std_maximos), todos_los_numeros = calcular_medias_estadisticas()

    print("\n--- Media ± Desviación Estándar ---")
    print(f"Mínimos: {media_minimos} ± {std_minimos}")
    print(f"Medios: {media_medios} ± {std_medios}")
    print(f"Máximos: {media_maximos} ± {std_maximos}")

    diagrama_cajas_percentiles(todos_los_numeros)

if __name__ == "__main__":
    main()

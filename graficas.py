import matplotlib.pyplot as plt
import numpy as np

# Grafica de barras resumen del tiempo minimo, maximo y medio con la desviacion estandar

def grafica_barras(clientes, minimos, medios, maximos, desviacion_min, desviacion_med, desviacion_max):
    ancho_barras = 0.25
    
    posiciones_clientes = np.arange(len(clientes))
    
    plt.figure(figsize=(10, 6))
    
    # Barras para el valor mínimo con desviación
    plt.bar(posiciones_clientes - ancho_barras, minimos, width=ancho_barras, color='lightcoral', 
            yerr=desviacion_min, capsize=5, label='Mínimo')
    
    # Barras para el valor medio con desviación
    plt.bar(posiciones_clientes, medios, width=ancho_barras, color='skyblue', 
            yerr=desviacion_med, capsize=5, label='Medio')
    
    # Barras para el valor máximo con desviación
    plt.bar(posiciones_clientes + ancho_barras, maximos, width=ancho_barras, color='lightgreen', 
            yerr=desviacion_max, capsize=5, label='Máximo')
    
    # Ajustar los ticks del eje X para que solo muestre los valores de clientes
    plt.xticks(posiciones_clientes, clientes)
    
    plt.xlabel('Número de clientes')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo de espera por petición: mínimo, medio y máximo')
    plt.legend()
    
    plt.show()

clientes = [1, 2, 5, 10, 15, 20]

minimos = [0.575, 0.598, 0.560, 0.551, 0.576, 0.554]  
medios = [0.674, 0.941, 0.977, 1.092, 1.679, 1.721]  
maximos = [0.930, 2.040, 3.036, 4.605, 7.005, 8.437]

desviacion_min = [0.011, 0.017, 0.009, 0.008, 0.016, 0.006]  
desviacion_med = [0.014, 0.115, 0.040, 0.090, 0.308, 0.242] 
desviacion_max = [0.261, 1.003, 1.400, 0.218, 0.469, 0.429]  

grafica_barras(clientes, minimos, medios, maximos, desviacion_min, desviacion_med, desviacion_max)

# Grafica de puntos con el tiempo de cada petición

clientes = 5

markersize = 3

with open(f'./resultados/contexto/testContexto{clientes}x100_cliente1.txt', 'r') as file:
    numeros = [float(line.strip()) for line in file]

plt.plot(numeros, marker='o', linestyle='', color='b', markersize = markersize, label='Cliente 1')

with open(f'./resultados/contexto/testContexto{clientes}x100_cliente2.txt', 'r') as file:
    numeros = [float(line.strip()) for line in file]

plt.plot(numeros, marker='o', linestyle='', color='r', markersize = markersize, label='Cliente 2')

with open(f'./resultados/contexto/testContexto{clientes}x100_cliente3.txt', 'r') as file:
    numeros = [float(line.strip()) for line in file]

plt.plot(numeros, marker='o', linestyle='', color='g', markersize = markersize, label='Cliente 3')

with open(f'./resultados/contexto/testContexto{clientes}x100_cliente4.txt', 'r') as file:
    numeros = [float(line.strip()) for line in file]

plt.plot(numeros, marker='o', linestyle='', color='cyan', markersize = markersize, label='Cliente 4')

with open(f'./resultados/contexto/testContexto{clientes}x100_cliente5.txt', 'r') as file:
    numeros = [float(line.strip()) for line in file]

plt.plot(numeros, marker='o', linestyle='', color='purple', markersize = markersize, label='Cliente 5')

plt.title(f'Evolución del tiempo de petición: {clientes} clientes')
plt.xlabel('Nº Petición')
plt.ylabel('Tiempo (segundos)')
plt.legend()

plt.show()

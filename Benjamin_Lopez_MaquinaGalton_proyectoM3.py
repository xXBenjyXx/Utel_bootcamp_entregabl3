import random as rd #importamos random con el alias de rd
import matplotlib.pyplot as plt #importamos pyplot de matplotlib con el alias de plt

# Función para simular la máquina de Galton y contar la cantidad de canicas en cada contenedor.
def maquina_galton(n_canicas, n_niveles):
    # Inicializar una lista llamada "contenedores" con ceros, que representa la cantidad de canicas en cada contenedor.
    contenedores = [0] * (n_niveles + 1) 

    # Ciclo para simular el recorrido de cada canica.
    for i in range(n_canicas):
        # Inicializar la posición de la canica en el nivel 0 (primer contenedor).
        posicion = 0
        
        # Ciclo para determinar el recorrido vertical de la canica, si cae a la derecha, baja un nivel.
        for nivel in range(n_niveles):
            lado = rd.choice(["Izq", "Der"])  # Escoge aleatoriamente si cae a la izquierda o a la derecha.
            if lado == "Der":
                posicion += 1  # Si cae a la derecha, baja un nivel.
        
        # Incrementar el contador del contenedor correspondiente a la posición final de la canica.
        contenedores[posicion] += 1
    
    return contenedores

# Función para graficar el histograma que muestra la cantidad de canicas en cada contenedor.
def grafica_histograma(datos):
    n_contenedores = len(datos)
    x = list(range(n_contenedores))
    plt.bar(x, datos) #Creacion del histograma para la simulacion de la maquina de galton
    plt.xlabel("numero de Contenedor") #en las siguientes 3 lineas se colocan las etiquetas para interpretar el histograma
    plt.ylabel("Cantidad de Canicas")
    plt.title("Histograma de Galton")
    plt.xticks(x) # numera los contenedores del 0 al 12
    plt.grid(True)  # Mostrar una cuadrícula en el fondo del gráfico.
    plt.show()


# Configuramos la maquina de galton para que simule con 3000 canicas y 12 contenedores
n_canicas = 3000
n_niveles = 12

# Realizar la simulación de la máquina de Galton y obtener los resultados.
resultados = maquina_galton(n_canicas, n_niveles)

# Graficar el histograma de los resultados obtenidos.
grafica_histograma(resultados)

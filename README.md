# Utel_bootcamp_entregabl3


Este código simula la famosa "máquina de Galton" y grafica el resultado en un histograma. La máquina de Galton es un dispositivo que ilustra la distribución binomial y muestra cómo un gran número de eventos aleatorios se agrupan alrededor de un valor medio. La máquina consta de una serie de clavos dispuestos en niveles, y las canicas caen desde la parte superior y rebotan aleatoriamente hasta llegar a uno de los contenedores en la parte inferior. La cantidad de canicas que caen en cada contenedor sigue una distribución binomial.

Veamos el código línea por línea:

import random as rd: Importa la librería random con el alias rd. Esta librería proporciona funciones para trabajar con números aleatorios.

import matplotlib.pyplot as plt: Importa la librería pyplot de matplotlib con el alias plt. Esta librería se utilizará para graficar los resultados.

Se define la función maquina_galton(n_canicas, n_niveles) para simular la máquina de Galton y contar la cantidad de canicas en cada contenedor. Esta función recibe dos parámetros: n_canicas (número de canicas que se lanzarán) y n_niveles (número de niveles o contenedores).

Se inicializa una lista llamada contenedores con ceros, que representa la cantidad de canicas en cada contenedor. El número de elementos en la lista será igual a n_niveles + 1 para tener en cuenta el contenedor en la posición 0.

Se realiza un bucle for i in range(n_canicas): para simular el recorrido de cada canica.

Se inicializa la variable posicion en 0, que representa el nivel inicial de la canica (primer contenedor).

Se realiza otro bucle for nivel in range(n_niveles): para determinar el recorrido vertical de la canica. En cada iteración, se elige aleatoriamente si la canica cae a la izquierda o a la derecha mediante lado = rd.choice(["Izq", "Der"]).

Si la canica cae a la derecha (lado == "Der"), se incrementa la variable posicion en 1, lo que significa que la canica baja un nivel en la máquina.

Después de recorrer todos los niveles, se incrementa el contador del contenedor correspondiente a la posición final de la canica. Es decir, se aumenta contenedores[posicion] en 1, ya que posicion representa el nivel donde terminó la canica.

Se retorna la lista contenedores, que contiene la cantidad de canicas en cada contenedor después de realizar todas las simulaciones.

Se define la función grafica_histograma(datos) para graficar el histograma que muestra la cantidad de canicas en cada contenedor. Esta función recibe una lista datos que contiene la cantidad de canicas en cada contenedor.

Se obtiene el número de contenedores utilizando n_contenedores = len(datos).

Se crea una lista x que contiene los índices de los contenedores, que se utilizarán como etiquetas del eje x en el gráfico.

Se utiliza plt.bar(x, datos) para crear el gráfico de barras. Los valores de x representan las posiciones en el eje x, y los valores de datos son las alturas de las barras.

Se agregan etiquetas a los ejes y se establece el título del gráfico.

plt.xticks(x) se utiliza para numerar los contenedores del 0 al 12 en el eje x.

plt.grid(True) muestra una cuadrícula en el fondo del gráfico.

plt.show() muestra el gráfico resultante.

Se configura la simulación de la máquina de Galton con 3000 canicas y 12 contenedores utilizando n_canicas = 3000 y n_niveles = 12.

Se realiza la simulación llamando a la función maquina_galton(n_canicas, n_niveles) y se guardan los resultados en la variable resultados.

Finalmente, se grafican los resultados llamando a la función grafica_histograma(resultados) para mostrar el histograma que representa la cantidad de canicas en cada contenedor

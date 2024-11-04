#!/usr/bin/env pyhton3

import numpy as np # Biblioteca para calculos matematicos
import matplotlib.pyplot as plt # Biblioteca para crear gáficos

puntos_x = np.linspace( 0, 10, 10 ) # puntos en eje x de [0-a=10]
puntos_y = np.linspace( 0, 20, 20 ) # puntos en eje y de [0-b=20]

X_2D, Y_2D = np.meshgrid( puntos_x, puntos_y ) # convierte estos vectores de 1D a 2D para ver cada punto en el espacio como una grilla en el eje cartesiano

def temperaturas( x, y, c, t): # Diferencias finitas para calcular la temperatura en cada punto
    dx = x[1] - x [0]
    dy = y[1] - y[0]
    
    return Ti

fourier_t = np.fft.fft(temperaturas( ), norm = "forward" ) # optimizamos el calculo usando transformadas de fourier para evaluar la temperatura en cada punto de la grilla

fig = plt.figure() # Inicializa la figura

grafico = fig.add_subplot( 121 ) # Genera una figura en en la parte izquierda

grafico.imshow( temperaturas() , cmap="copper", extent=[ X_2D[0], X_2D[1], Y_2D[0], Y_2D[1] ], ) # Crea un gráfico en 2D para visualizar las temperaturas en distintas posiciones del espacio con colores copper y con limites iguales a los de "x" y "y"  
 
grafico = fig.add_subplot( 122, projection = "3d" ) # Crea otra figura al lado derecho en 3D

grafico.plot_surface(X, Y, temperaturas(), cmap="copper") # Crea la gráfica 3d de superficie de calor

plt.show() # Muestra las 2 gráficas subploteadas

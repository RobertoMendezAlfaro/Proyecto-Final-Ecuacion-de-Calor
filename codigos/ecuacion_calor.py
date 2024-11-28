#!/usr/bin/env python

import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para analizar la evolución temporal de una placa con temperatura inicial temp_init a
# la que se le aplica una temperatura de temp_sup en el borde superior y una de temp_lat en el
# borde izquierdo. ancho y alto definien el tamaño de la grilla, omega es un parámetro del método
# utilizado y frames es la cantidad de imágenes que deseamos guardar del sistema
def temperaturas(temp_sup, temp_lat, temp_init, ancho, alto, omega, frames):

    phi = np.zeros((ancho + 1, alto + 1), dtype=float) # Grilla bidimensional

    phi[:, :] = temp_init # Condición inicial en el interior del sistema

    phi[0, :] = temp_sup # Condición inical en borde superior de grilla

    phi[:, 0] = temp_lat # Condición inical en borde izquierdo de grilla

    phi[0, 0] = (temp_sup + temp_lat) / 2 # Condición inicial en la esquina

    phi_copy = phi.copy() # Para comparar el error con la nueva grilla

    animation = np.zeros((frames, ancho, alto))# Para almacenar copias del sistema para animar

    iterations = 0 # Contador para las iteraciones

    iterations_per_frame = 20 # Cada cuantas iteraciones se desea guarda una copia del sistema

    frame_counter = 0 # Contador para los fotogramas guardados

    delta = 1 # Tolerancia de precisión

    while delta > 1e-7:
        # Método Gauss Seidel para aproximar el cambio de T en el espacio con el tiempo
        for i in range(1, ancho):

            for j in range(1, alto):

                phi[i,j] = (1 + omega) * 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1]) - omega * phi[i, j]

        # Se guarda una copia del estado del sistema para crear la animación
        if frame_counter < frames:
            if (iterations % iterations_per_frame) == 0:

                animation[frame_counter, :, :] = phi[:-1, :-1]

                frame_counter += 1


        delta = np.max(np.abs(phi - phi_copy))

        iterations += 1

        phi_copy = phi.copy() # Ponemos la nueva grilla como la antigua para compararla
                              # con la  nueva en la siguiente iteración

    #print(iterations)  # Este print se debe habilitar para conocer la cantida de iteraciones
                        # para ajustar la animación dependiendo de las condiciones iniciales

    return animation



total_frames = 50 # Cantidad de fotogramas que se desea que muestre la animación

# Implementación de la animación

# Se guardan los resultados de la función iterativa
heatmap = temperaturas(100, 200, 20, 50, 100, 0, total_frames)

fig, ax = plt.subplots()

# Se crea el fotograma inicial, aquí se escoge el esquema de colores con cmap
animation = ax.imshow(heatmap[0,:,:], cmap="inferno")

# Se crea la función que va pasando los fotogramas
def animate(frame):
    new_frame = heatmap[frame,:,:]
    animation.set_data(new_frame)
    return animation


anim = FuncAnimation(fig, animate, frames=total_frames)
plt.show()

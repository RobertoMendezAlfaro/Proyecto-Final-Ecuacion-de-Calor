#!/usr/bin/env python

import numpy as np # Biblioteca para calculos matematicos
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
#import matplotlib.cm as cm # Biblioteca para crear gáficos

def temperaturas(temp_sup, temp_lat, temp_init, ancho, alto, omega, frames):

    phi = np.zeros((ancho + 1, alto + 1), dtype=float) # Grilla bidimensional

    phi[:, :] = temp_init # Condición inicial en el interior del sistema

    phi[0, :] = temp_sup # Condición inical en borde superior de grilla

    phi[:, 0] = temp_lat # Condición inical en borde izquierdo de grilla

    phi[0, 0] = (temp_sup + temp_lat) / 2 # Condición inicial en la esquina

    phi_copy = phi.copy() # Para comparar el error con la nueva grilla

    animation = np.zeros((frames, ancho, alto))

    iterations = 0 # Contador para las iteraciones

    iterations_per_frame = 13 # Cada cuantas iteraciones se desea guarda una copia del sistema

    frame_counter = 0

    delta = 1

    while delta > 1e-5: #
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
        phi_copy = phi.copy() # Ponemos la nueva grilla como la antigua para compararlo con la  nueva en la siguiente iteración
    print(iterations)
    return animation



total_frames = 50 # Cantidad de fotogramas que se desea que muestre la animación

# Implementación de la animación

# Se guardan los resultados de la función iterativa
heatmap = temperaturas(100, 200, 20, 40, 80, 0, total_frames)

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
#video = anim.to_html5_video()
#html = display.HTML(video)
#display.display(html)
#plt.close()


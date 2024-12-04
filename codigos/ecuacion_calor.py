#!/usr/bin/env python

import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def temperaturas(temp_sup, temp_lat, temp_init, ancho, alto, omega, frames):
    """
    Analiza la evolución temporal de la temperatura en una grilla, utilizando el método de Gauss-Seidel para la aproximación en el espacio y tiempo. Los resultados se guardan en una animación de fotogramas para su visualización.

    Parametros
    ----------
    temp_sup : float
        Temperatura en el borde superior.
    temp_lat : float
        Temperatura en el borde izquierdo.
    temp_init : float
        Temperatura inicial.
    ancho : int
        Número de celdas en la drección horizontal de la grilla.
    alto : int
        Número de celdas en la dirección vertical de la grilla.
    omega : float
        Parámetro de relajación del método de Gauss-Seidel.
    frames : int
        Número de fotogramas que se desean para la animación.

    Returns
    -------
    numpy.ndarray
        Una matriz que contiene las diferentes distribuciones de temperatura para cada fotograma.

    Examples
    --------
    >>> temperaturas(100, 200, 20, 50, 100, 0.5, 50)
    Devuelve una matriz que representa la evolución de las temperaturas en la placa durante 50 fotogramas.
    """

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
    """
    Actualiza el fotograma actual en la animación.

    Parametros
    ----------
    frame : int
        Índice del fotograma a actualizar.

    Returns
    -------
    animation : matplotlib.image.AxesImage
        El objeto de imagen actualizado con el nuevo fotograma.
    """
    new_frame = heatmap[frame,:,:]
    animation.set_data(new_frame)
    return animation


anim = FuncAnimation(fig, animate, frames=total_frames)
plt.show()

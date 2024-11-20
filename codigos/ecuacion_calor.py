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

    iterations = -1 # Contador para las iteraciones

    iterations_per_frame = 200 # Cada cuantas iteraciones se desea guarda una copia del sistema

    frame_counter = 0

    delta = 1

    while delta > 1e-5: #
        iterations += 1
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

        phi_copy = phi.copy() # Ponemos la nueva grilla como la antigua para compararlo con la  nueva en la siguiente iteración
    print(iterations)
    return animation


#heatmap = temperaturas(100, 200, 20, 40, 80, 0, 10)

#fig = plt.figure()
#line, = plt.plot([])

#def animate(frame):
 #   images = heatmap[frame, :, :]
  #  line.set_data(images)

#anim = FuncAnimation(fig, animate, frames = 10)
#video = anim.to_html5_video()
#html = display.HTML(video)
#display.display(html)
#plt.close()




#print(temperaturas(100, 200, 20, 40, 80, 0, 10))


plt.imshow(temperaturas(100, 200, 20, 40, 80 ,0, 10)[9, :, :], cmap="inferno")
plt.show()


#writer = FFMpegWriter(fps=15)

#fig, ax = plt.subplots()

#with writer.saving(fig, "heatmap.mp4", 100):
#    for frame in range(30): # Range = numbers of frames used for animation



#        heatmap = temperaturas(100, 10, 20, 0, 10 ,20, 30)

 #       ax.plot(heatmap[frame])

  #      writer.grab_frame()
#        plt.cla()




#temperaturas(100, 40, 80, 0, 10, 2600)

#fig = plt.figure()
#line, = plt.plot([])
#plt.xlabel(r'$x$')
#plt.ylabel(r'$\phi(x,t)$')
#plt.xlim(0.0, 1.0)
#plt.ylim(-0.05, 0.05)

#anim = FuncAnimation(fig, temperaturas(100, 40, 80, 0, 10, 2600, 30), frames = 30, interval = 10)
#video = anim.to_html5_video()
#html = display.HTML(video)
#display.display(html)
#plt.close()


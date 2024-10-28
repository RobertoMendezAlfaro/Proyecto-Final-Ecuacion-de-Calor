#!/usr/bin/env python
import numpy as np

#Evitar variables globales

x_Length = 1
# El delta_x lo escogemos nosotros, escoger uno con el que la gráfica no tenga muchos números
delta_x = 0.25

y_Length = 1
# Igual que el delta_x
delta_y = 0.25

#c = 1  para simplificar
c = 1

# Valor final de t
t_fin = 1
# delta t se escoge tal q:
# delta_t < (delta_x**2 + delta_y**2)/8
delta_t = 0.015

#cantidad de subdivisiones
t_subdivions_count = (t_fin // delta_t) + 1
x_subdivions_count = (x_Length // delta_x) + 1
y_subdivions_count = (y_Length // delta_y) + 1

# Arreglo inicializado con ceros
T = np.zeroes(x_subdivions_count, y_subdivions_count, t_subdivions_count)

# Condiciones iniciales:

# Para T(0,y,t)
for i in x_subdivions_count:
    #
    T[0, y_subdivions_count, t_subdivions_count] = 100


T(x,y,t+1) = T(x,y,t) + ((c**2)*(delta_t / delta_x**2) * (T(x+1,y,t) - 2*T(x,y,t) + T(x-1,y,t)) + ((c**2) * (delta_t / delta_y**2) * (T(x,y+1,t) - 2*T(x,y,t) + T(x,y,t-1))

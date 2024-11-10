#!/usr/bin/env pyhton3

import numpy as np # Biblioteca para calculos matematicos
import matplotlib.cm as cm # Biblioteca para crear gáficos

def temperaturas(cond_inicial):
    
    phi = np.zeros((101, 201), dtype=float) # grilla bidimensional 100 x 200
    
    phi[0,:] = cond_inicial # condicion inical en borde derecho de grilla
    
    phi_copy = phi.copy() # Para comparar el error con la nueva grilla
    delta = 1.0 # Diferencia entre phi inicial y el modificado con los valores de T

    while delta > 1e-5: # Verifica que el error sea sumamente pequeño
        for i in range(101):
            for j in range(201):
                
                if i == 0 or i == M or j == 0 or j == M: # Condición de frontera: T = 280 K en bordes
                    phi[i, j] = 280 
                
                else: # Método Gauss Seidel para aproximar el cambio de T en el espacio con el tiempo

                    phi[i,j] = (1 + omega) * 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1]
        
        delta = np.max(np.abs(phi - phi_copy)) # Estimamos la diferencia

        phi_copy = phi.copy() # Ponemos la nueva grilla como la antigua para compararlo con la nueva en la siguiente iteración
        
    return phi

# Condión Inicial 1: Ti = 0
fourier_t = np.fft.fft(temperaturas(0), norm = "forward" ) # optimizamos el cálculo usando transformadas de fourier para evaluar la temperatura en cada punto de la grilla

plt.imshow(fourier_t)
plt.gray()
plt.show()

# Condión Inicial 2: Ti = 50 K
fourier_t = np.fft.fft(temperaturas(50), norm = "forward" ) 

plt.imshow(fourier_t)
plt.gray()
plt.show()

# Condión Inicial 3: Ti = 170 K
fourier_t = np.fft.fft(temperaturas(170), norm = "forward" ) 

plt.imshow(fourier_t)
plt.gray()
plt.show()
~       

# Condión Inicial 4: Ti = 300 K
fourier_t = np.fft.fft(temperaturas(300), norm = "forward" ) 

plt.imshow(fourier_t)
plt.gray()
plt.show()
~            


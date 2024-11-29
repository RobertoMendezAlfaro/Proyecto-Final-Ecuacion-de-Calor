#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include "ecuacion_calor.hpp"
#include <omp.h>


// Función para resolver la ecuación de calor en 2D usando el método de Gauss-Seidel
void temperaturas(int ancho, int alto, double temp_sup, double temp_lat, double temp_init, 
                  double omega, int frames, int iterations_per_frame) {
    // Crear grilla bidimensional (inicializada con la temperatura inicial)
    std::vector<std::vector<double>> phi(ancho + 1, std::vector<double>(alto + 1, temp_init));
    std::vector<std::vector<double>> phi_copy = phi; // Para comparar cambios

    // condiciones de frontera

    for (int j = 0; j <= alto; ++j) {
        phi[0][j] = temp_sup; // Borde superior
    }
    for (int i = 0; i <= ancho; ++i) {
        phi[i][0] = temp_lat; // Borde izquierdo
    }
    phi[0][0] = (temp_sup + temp_lat) / 2.0; // Esquina superior izquierda

    // Almacenamiento de frames para análisis
    std::vector<std::vector<std::vector<double>>> animation(frames, std::vector<std::vector<double>>(ancho, std::vector<double>(alto)));

    int iterations = 0; // Contador de iteraciones
    int frame_counter = 0; // Contador para los frames
    double delta = 1.0; // Cambios iniciales

    // Iteración hasta que el cambio sea pequeño o se alcance el máximo 
    while (delta > 1e-5) {
        delta = 0.0; // Reinicia el cambio máximo
		     
	#pragma omp parallel //inicio de region en paralelo
        {
            #pragma omp for reduction(max: delta) //paralelizacion de for i con reduction en delta ya que los hilos la accesan de modo concurrente	  
        for (int i = 1; i < ancho; ++i) {
            for (int j = 1; j < alto; ++j) {
                // Aplicar fórmula de Gauss-Seidel con sobrerrelajación
                double nuevo_valor = (1 + omega) * 0.25 * (phi[i + 1][j] + phi[i - 1][j] + phi[i][j + 1] + phi[i][j - 1])
                                     - omega * phi[i][j];
                delta = std::max(delta, std::fabs(nuevo_valor - phi[i][j])); // Actualizar el cambio máximo
                phi[i][j] = nuevo_valor; // Actualizar temperatura
            }
        }
	}
        // Guardar el estado de la grilla para los frames si es necesario
        if (iterations % iterations_per_frame == 0 && frame_counter < frames) {
            for (int i = 0; i < ancho; ++i) {
                for (int j = 0; j < alto; ++j) {
                    animation[frame_counter][i][j] = phi[i][j];
                }
            }
            ++frame_counter;
        }

        ++iterations;
    }

    // Imprimir resultados finales
    std::cout << "Convergencia alcanzada en " << iterations << " iteraciones.\n";
    std::cout << "Estado final de la grilla:\n";
    for (int i = 0; i <= ancho; ++i) {
        for (int j = 0; j <= alto; ++j) {
            std::cout << phi[i][j] << " ";
        }
        std::cout << "\n";
    }
}



//Constructor por defecto

EcuacionCalor::EcuacionCalor(){}




//Constructor copia





//Operador de asignacion en caso de usarse




//Destructor

EcuacionCalor::~EcuacionCalor(){}


//Funciones y sobrecargas


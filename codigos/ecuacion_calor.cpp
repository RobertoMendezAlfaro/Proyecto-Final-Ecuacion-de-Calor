#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include "ecuacion_calor.hpp"

// Constructor por defecto
EcuacionCalor::EcuacionCalor() : omega(0.0), ancho(40), alto(80) {}

// Constructor con parámetros
EcuacionCalor::EcuacionCalor(double omega, int ancho, int alto)
    : omega(omega), ancho(ancho), alto(alto) {}

// Constructor copia
EcuacionCalor::EcuacionCalor(const EcuacionCalor &obj)
    : omega(obj.omega), ancho(obj.ancho), alto(obj.alto) {}

// Operador de asignación
EcuacionCalor &EcuacionCalor::operator=(const EcuacionCalor &obj) {
    if (this != &obj) {
        omega = obj.omega;
        ancho = obj.ancho;
        alto = obj.alto;
    }
    return *this;
}

// Destructor
EcuacionCalor::~EcuacionCalor() {}

// Método para calcular las temperaturas
void EcuacionCalor::temperaturas(double temp_sup, double temp_lat, double temp_init) {
    std::vector<std::vector<double>> phi(alto + 1, std::vector<double>(ancho + 1, temp_init));
    std::vector<std::vector<double>> phi_copy = phi;

    // Condiciones de frontera
    for (int j = 0; j <= ancho; ++j) {
        phi[0][j] = temp_sup; // Borde superior
    }
    for (int i = 0; i <= alto; ++i) {
        phi[i][0] = temp_lat; // Borde izquierdo
    }
    phi[0][0] = (temp_sup + temp_lat) / 2.0; // Esquina superior izquierda

    int iterations = 0;
    double delta = 1.0;

    while (delta > 1e-7) {
        delta = 0.0;

        #pragma omp parallel //inicio de region en paralelo
        {
            #pragma omp for reduction(max: delta) //paralelizacion de for i con reduction en delta ya que los hilos las accesan de modo concurrente
            for (int i = 1; i < alto; ++i) {
                for (int j = 1; j < ancho; ++j) {
                    double nuevo_valor = (1 + omega) * 0.25 * (phi[i + 1][j] + phi[i - 1][j] + phi[i][j + 1] + phi[i][j - 1]) - omega * phi[i][j];
                    delta = std::max(delta, std::fabs(nuevo_valor - phi[i][j]));
                    phi[i][j] = nuevo_valor;
                }
            }
        }
        ++iterations;
    }

    std::cout << "Convergencia alcanzada en " << iterations << " iteraciones.\n";
    std::cout << "Estado final de la grilla:\n";
    for (int i = 0; i <= alto; ++i) {
        for (int j = 0; j <= ancho; ++j) {
            std::cout << phi[i][j] << "  ";
        }
        std::cout << "\n";
    }
}


#include <iostream>
#include "ecuacion_calor.hpp"

int main() {
    // Parámetros de entrada
    double temp_sup = 100.0;
    double temp_lat = 200.0;
    double temp_init = 20.0;
    int ancho = 40;
    int alto = 80;
    double omega = 0.0;
    int frames = 10;
    int iterations_per_frame = 200;

    // Crear objeto de la clase EcuacionCalor utilizando el constructor con parámetros
    EcuacionCalor ec(omega, frames, ancho, alto);

    // Llamar a la función para calcular temperaturas
    std::cout << "A continuación se resuelve la ecuación de calor:.\n";
    ec.temperaturas(temp_sup, temp_lat, temp_init, iterations_per_frame);

    return 0;
}


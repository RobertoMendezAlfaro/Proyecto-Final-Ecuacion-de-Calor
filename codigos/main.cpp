#include <iostream>
#include "ecuacion_calor.hpp"

int main() {
    /* Parámetros utilizados
    temp_sup = 100.0
    temp_lat = 200.0
    temp_init = 20.0
    ancho = 100
    alto = 50
    omega = 0.0 */
    
    // Crear objeto de la clase EcuacionCalor utilizando el constructor con parámetros
    EcuacionCalor ec(0.0, 100, 50);

    // Llamar a la función para calcular temperaturas
    std::cout << "A continuación se resuelve la ecuación de calor:.\n";
    ec.temperaturas(100.0, 200.0, 20.0);

    return 0;
}


#ifndef ECUACIONCALOR_HPP
#define ECUACIONCALOR_HPP

#include <vector>

class EcuacionCalor {
  private:
    double omega;   // Sobrerrelajación
    int frames;     // Número de frames para la animación
    int ancho;      // Ancho de la grilla
    int alto;       // Alto de la grilla

  public:
    EcuacionCalor(); // Constructor por defecto
    EcuacionCalor(double omega, int frames, int ancho, int alto); // Constructor con parámetros
    EcuacionCalor(const EcuacionCalor &obj); // Constructor copia
    EcuacionCalor &operator=(const EcuacionCalor &obj); // Operador de asignación
    ~EcuacionCalor(); // Destructor

    // Método para calcular las temperaturas
    void temperaturas(double temp_sup, double temp_lat, double temp_init, int iterations_per_frame);
};

#endif


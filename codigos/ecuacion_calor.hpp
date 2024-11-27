#ifndef ECUACIONCALOR_HPP
#define ECUACIONCALOR_HPP
#include <vector>

class EcuacionCalor {
  private:

  public:
    EcuacionCalor(); //Constructor por defecto
    EcuacionCalor(const EcuacionCalor &obj); //Constructor copia
    EcuacionCalor &operator=(const EcuacionCalor &obj); //Operador Asignación
    ~EcuacionCalor(); //Destructor

};

//Declarar la funcion temperaturas para poder compilar main.cpp

void temperaturas(int ancho, int alto, double temp_sup, double temp_lat, double temp_init, double omega, int frames, int iterations_per_frame, int &iterations_out);

#endif

#include <iostream>
#include "ecuacion_calor.hpp"

int main(){

  //Parámetros de entrada
  double temp_sup = 100.0;
  double temp_lat = 200.0;
  double temp_init = 20.0;
  int ancho = 40;
  int alto = 80;
  double omega = 0.0;
  int frames = 10;
  int interations_per_frame = 200;

  //LLamar a la funcion para calcular temperaturas

  std::cout << "A continuación se resuelve la ecuación de calor:.\n"
  temperaturas(ancho, alto, temp_sup, temp_lat, temp_init, omega, frames, iterations_per_frame);
  
  return 0;
}

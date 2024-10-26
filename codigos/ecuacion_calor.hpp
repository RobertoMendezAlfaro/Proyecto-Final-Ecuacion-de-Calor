#ifndef ECUACIONCALOR_HPP
#define ECUACIONCALOR_HPP

class EcuacionCalor {
  private:

  public:
    EcuacionCalor(); //Constructor por defecto
    EcuacionCalor(const EcuacionCalor &obj); //Constructor copia
    EcuacionCalor &operator=(const EcuacionCalor &obj); //Operador Asignación
    ~EcuacionCalor(); //Destructor

};

#endif

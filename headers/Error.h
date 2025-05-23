#ifndef ERROR
#define ERROR

#include <iostream>
#include "NodoSimple.h"

class Error : public NodoSimple {
   private:
      int id;
      std::string tipo;
      std::string origen;
      std::string descripcion;
   public:
      // Constructores
      Error();
      Error(int id_, std::string tipo_,std::string origen_, std::string descripcion);

      // Getters
      int getId();
      std::string getTipo();
      std::string getOrigen();
      std::string getDescripcion();

      // Setters
      void setId(int id_);
      void setTipo(std::string tipo_);
      void setOrigen(std::string origen_);
      void setDescripcion(std::string descripcion_);
};

#endif //ERROR
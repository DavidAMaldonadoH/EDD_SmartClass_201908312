#ifndef TAREA
#define TAREA

#include <iostream>
#include "NodoDoble.h"

class Tarea : public NodoDoble{
   private:
      int id;
      std::string carne;
      std::string nombre;
      std::string descripcion;
      std::string materia;
      std::string fecha;
      std::string hora;
      std::string estado;
   public:
      // Constructores
      Tarea();
      Tarea(std::string carne_, std::string nombre_, std::string descripcion_, 
      std::string materia_, std::string fecha_, std::string hora_, std::string estado_);

      // Getters
      int getId();
      std::string getCarne();
      std::string getNombre();
      std::string getDescripcion();
      std::string getMateria();
      std::string getFecha();
      std::string getHora();
      std::string getEstado();

      // Setters
      void setId(int id_);
      void setCarne(std::string carne_);
      void setNombre(std::string nombre_);
      void setDescripcion(std::string descripcion_);
      void setMateria(std::string materia_);
      void setFecha(std::string fecha_);
      void setHora(std::string hora_);
      void setEstado(std::string estado_);

      friend Tarea operator==(Tarea& tarea_, Tarea& tarea2_);
};

#endif //TAREA
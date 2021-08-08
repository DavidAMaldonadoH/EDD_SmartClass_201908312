#ifndef ESTUDIANTE
#define ESTUDIANTE

#include <iostream>
#include "NodoDoble.h"
#include "Cola.h"

class Estudiante : public NodoDoble {
   private:
      std::string carne;
      std::string DPI;
      std::string nombre;
      std::string carrera;
      std::string password;
      std::string correo;
      int creditos;
      int edad;
   public:
      // Constructores
      Estudiante();
      Estudiante(std::string carne_, std::string DPI_, std::string nombre_, 
      std::string carrera_, std::string password_, std::string correo_, int creditos_, int edad_);

      // Getters
      std::string getCarne();  
      std::string getDPI();  
      std::string getNombre();  
      std::string getCarrera();  
      std::string getPassword();
      std::string getCorreo();
      int getCreditos();
      int getEdad();

      //Setters
      void setCarne(std::string carne_);
      void setDPI(std::string DPI_);
      void setNombre(std::string nombre_);
      void setCarrera(std::string carrera_);
      void setPassword(std::string password_);
      void setCorreo(std::string correo_);
      void setCreditos(int creditos_);
      void setEdad(int edad_);

      bool isEqual(Estudiante *estudiante_);
      void printInfo();
      void checkErrors(Cola *colaErrores);
};

#endif
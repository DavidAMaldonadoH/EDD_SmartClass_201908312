#include <iostream>
#include "../headers/Error.h"

using namespace std;

// Constructores
Error::Error() {
   this->setType("Error");
}

Error::Error(int id_, string tipo_, string origen_, string descripcion_) {
   this->setType(descripcion_);
   this->id = id_;
   this->tipo = tipo_;
   this->origen = origen_;
   this->descripcion = descripcion_;
}
// Getters
int Error::getId() {
   return this->id;
}

string Error::getTipo() {
   return this->tipo;
}

string Error::getOrigen() {
   return this->origen;
}

string Error::getDescripcion() {
   return this->descripcion;
}

// Setters
void Error::setId(int id_) {
   this->id = id_;
}

void Error::setTipo(string tipo_) {
   this->tipo = tipo_;
}

void Error::setOrigen(string origen_) {
   this->origen = origen_;
}

void Error::setDescripcion(string descripcion_){
   this->descripcion = descripcion_;
}

#include <iostream>
#include "../headers/Tarea.h"

using namespace std;

// Constructores
Tarea::Tarea() {
   this->setType("Tarea");
}

Tarea::Tarea(string carne_, string nombre_, string descripcion_, 
string materia_, string fecha_, string hora_, string estado_) {
   this->setType("Tarea");
   this->carne = carne_;
   this->nombre = nombre_;
   this->descripcion = descripcion_;
   this->materia = materia_;
   this->fecha = fecha_;
   this->hora = hora_;
   this->estado = estado_;
}

// Getters
int Tarea::getId() {
   return this->id;
}

string Tarea::getCarne() {
   return this->carne;
}

string Tarea::getNombre() {
   return this->nombre;
}

string Tarea::getDescripcion() {
   return this->descripcion;
}

string Tarea::getMateria() {
   return this->materia;
}

string Tarea::getFecha() {
   return this->fecha;
}

string Tarea::getHora() {
   return this->hora;
}

string Tarea::getEstado() {
   return this->estado;
}

// Setters
void Tarea::setId(int id_) {
   this->id = id_;
}

void Tarea::setCarne(std::string carne_) {
   this->carne = carne_;
}

void Tarea::setNombre(std::string nombre_) {
   this->nombre = nombre_;
}

void Tarea::setDescripcion(std::string descripcion_) {
   this->descripcion = descripcion_;
}

void Tarea::setMateria(std::string materia_) {
   this->materia = materia_;
}

void Tarea::setFecha(std::string fecha_) {
   this->fecha = fecha_;
}

void Tarea::setHora(string hora_) {
   this->hora = hora_;
}

void Tarea::setEstado(string estado_) {   
   this->estado = estado_;
}

bool operator==(Tarea tarea_, Tarea tarea2_) {
   return tarea_.getId() == tarea2_.getId();
}
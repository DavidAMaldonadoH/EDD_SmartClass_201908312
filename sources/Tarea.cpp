#include <iostream>
#include <regex>
#include "../headers/Tarea.h"
#include "../headers/ListaDC.h"
#include "../headers/Cola.h"
#include "../headers/Estudiante.h"
#include "../headers/Error.h"

using namespace std;

// Constructores
Tarea::Tarea() {
   this->setType("Tarea");
}

Tarea::Tarea(string carne_, string nombre_, string descripcion_, 
string materia_, string fecha_, string hora_, string estado_) {
   this->setType("");
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
   this->setType(to_string(id_));
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

bool Tarea::isEqual(Tarea *tarea_) {
   return this->id = tarea_->getId();
}

void Tarea::printInfo() {
   cout << "Tarea con: " << endl;
   cout << '\t' << "ID: " << this->id << endl;
   cout << '\t' << "Carnet: " << this->carne << endl;
   cout << '\t' << "Nombre: " << this->nombre << endl;
   cout << '\t' << "Descripcion: " << this->descripcion << endl;
   cout << '\t' << "Materia: " << this->materia << endl;
   cout << '\t' << "Fecha: " << this->fecha << endl;
   cout << '\t' << "Hora: " << this->hora << ":00" << endl;
   cout << '\t' << "Estado: " << this->estado << endl;
}

void Tarea::checkErrors(Cola *colaErrores) {
   regex regFecha("^\\d{4}\\/(0[7-9]{1}|1(0|1))\\/((0[1-9]{1})|((1|2)\\d{1})|30)$");
   if (!regex_search(this->fecha, regFecha)) {
      string descripcion = "La Fecha no posee el formato debido.";
      Error *err = new Error(colaErrores->getSize(), "Tarea", to_string(this->id), descripcion);
      colaErrores->add(err);
   }
   if (stoi(this->hora) > 16 | stoi(this->hora) < 8) {
      string descripcion = "La Hora esta fuera del rango especificado.";
      Error *err = new Error(colaErrores->getSize(), "Tarea", to_string(this->id), descripcion);
      colaErrores->add(err);
   }
}

bool Tarea::inEstudiantes(ListaDC *listaEstudiantes) {
   bool estado = false;
   for (int i = 0; i < listaEstudiantes->getSize(); i++) {
      NodoDoble *tmp = listaEstudiantes->get(i);
      if (this->carne == ((Estudiante*)(tmp))->getCarne()) {
         estado = true;
         break;
      }
   }
   return estado;
}
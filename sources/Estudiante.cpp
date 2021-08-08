#include <iostream>
#include <iomanip>
#include <regex>
#include "../headers/Estudiante.h"
#include "../headers/NodoDoble.h"
#include "../headers/Cola.h"
#include "../headers/Error.h"

using namespace std;

// Constructores
Estudiante::Estudiante() : NodoDoble() {
   this->setType("Estudiante");
}

Estudiante::Estudiante(string carne_, string DPI_, string nombre_, string carrera_, 
string password_, string correo_, int creditos_, int edad_) : NodoDoble() {
   this->setType(DPI_);
   this->carne = carne_;
   this->DPI = DPI_;
   this->nombre = nombre_;
   this->carrera = carrera_;
   this->password = password_;
   this->correo = correo_;
   this->creditos = creditos_;
   this->edad = edad_;
}

// Getters
string Estudiante::getCarne(){
   return this->carne;
}

string Estudiante::getDPI() {
   return this->DPI;
}

string Estudiante::getNombre() {
   return this->nombre;
}

string Estudiante::getCarrera() {
   return this->carrera;
}

string Estudiante::getPassword() {
   return this->password;
}

string Estudiante::getCorreo() {
   return this->correo;
}

int Estudiante::getCreditos() {
   return this->creditos;
}

int Estudiante::getEdad() {
   return this->edad;
}

//Setters
void Estudiante::setCarne(string carne_) {
   this->carne = carne_;
}

void Estudiante::setDPI(string DPI_) {
   this->DPI = DPI_;
}

void Estudiante::setNombre(string nombre_) {
   this->nombre = nombre_;
}

void Estudiante::setCarrera(string carrera_) {
   this->carrera = carrera_;
}

void Estudiante::setPassword(string password_) {
   this->password = password_;
}

void Estudiante::setCorreo(string correo_) {
   this->correo = correo_;
}

void Estudiante::setCreditos(int creditos_) {
   this->creditos = creditos_;
}

void Estudiante::setEdad(int edad_) {
   this->edad = edad_;
}

bool Estudiante::isEqual(Estudiante *estudiante_) {
   return this->DPI == estudiante_->getDPI();
}

void Estudiante::printInfo() {
   cout << "Estudiante con: " << endl;
   cout << '\t' << "Carnet: " << this->carne << endl;
   cout << '\t' << "DPI: " << this->DPI << endl;
   cout << '\t' << "Nombre: " << this->nombre << endl;
   cout << '\t' << "Carrera: " << this->carrera << endl;
   cout << '\t' << "Contraseña: " << this->password << endl;
   cout << '\t' << "Creditos: " << this->creditos << endl;
   cout << '\t' << "Edad: " << this->edad << endl;
   cout << '\t' << "Correo: " << this->correo << endl;
}

void Estudiante::checkErrors(Cola *colaErrores) {
   regex regDPI("^[0-9]{13}$");
   regex regCarnet("^[0-9]{9}$");
   regex regCorreo("^\\w+([\\.-]?\\w+)*@[a-z]+[.](com|es|org)+$");
   if (!regex_search(this->carne, regCarnet)) {
      string descripcion = "El Carnet del Estdudiante no presenta el formato debido.";
      Error *err = new Error(colaErrores->getSize(), "Estudiante", this->DPI, descripcion);
      colaErrores->add(err);
   }
   if (!regex_search(this->DPI, regDPI)) {
      string descripcion = "El DPI del Estudiante no presenta el formato debido.";
      Error *err = new Error(colaErrores->getSize(), "Estudiante", this->DPI, descripcion);
      colaErrores->add(err);
   }
   if (!regex_search(this->correo, regCorreo)) {
      string descripcion = "El Correo del Estudiante no presenta el formato debido.";
      Error *err = new Error(colaErrores->getSize(), "Estudiante", this->DPI, descripcion);
      colaErrores->add(err);
   }
}
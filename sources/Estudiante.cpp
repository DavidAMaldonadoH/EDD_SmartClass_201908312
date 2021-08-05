#include <iostream>
#include <iomanip>
#include "../headers/Estudiante.h"
#include "../headers/NodoDoble.h"

using namespace std;

// Constructores
Estudiante::Estudiante() : NodoDoble() {
   this->setType("Estudiante");
}

Estudiante::Estudiante(string carne_, string DPI_, string nombre_, 
string carrera_, string password_, int creditos_, int edad_) : NodoDoble() {
   this->setType(DPI_);
   this->carne = carne_;
   this->DPI = DPI_;
   this->nombre = nombre_;
   this->carrera = carrera_;
   this->password = password_;
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
}
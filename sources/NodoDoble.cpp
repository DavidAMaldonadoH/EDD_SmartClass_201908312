#include <iostream>
#include "../headers/NodoDoble.h"

using namespace std;

// Constructors
NodoDoble::NodoDoble() {
   this->type = "Nodo Doble";
   this->next = NULL;
   this->previous = NULL;
}

NodoDoble::NodoDoble(string type_) {
   this->type = type_;
   this->next = NULL;
   this->previous = NULL;
}

// Setters
void NodoDoble::setType(string type_) {
   this->type = type_;
}

void NodoDoble::setNext(NodoDoble *nodo_) {
   this->next = nodo_;
}

void NodoDoble::setPrevious(NodoDoble *nodo_) {
   this->previous = nodo_;
}

// Getters
string NodoDoble::getType() {
   return this->type;
}

NodoDoble *NodoDoble::getNext() {
   return this->next;
}

NodoDoble *NodoDoble::getPrevious() {
   return this->previous;
}

bool NodoDoble::isEqual(NodoDoble *nodo_) {
   return this->type == nodo_->getType();
}

void NodoDoble::printInfo() {
   cout << this->type;
}
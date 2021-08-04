#include <iostream>
#include "../headers/NodoSimple.h"

using namespace std;

// Constructors
NodoSimple::NodoSimple() {
   this->type = "Nodo Simple";
   this->next = NULL;
}

NodoSimple::NodoSimple(string type_) {
   this->type = type_;
   this->next = NULL;
}

// Setters
void NodoSimple::setType(string type_) {
   this->type = type_;
}

void NodoSimple::setNext(NodoSimple *nodo_) {
   this->next = nodo_;
}

// Getters
string NodoSimple::getType() {
   return this->type;
}

NodoSimple *NodoSimple::getNext() {
   return this->next;
}
#include <iostream>
#include "../headers/Cola.h"
#include "../headers/NodoSimple.h"

using namespace std;

Cola::Cola() {
   this->cabeza = NULL;
   this->size = 0;
}

bool Cola::isEmpty() {
   return this->cabeza == NULL;
}

int Cola::getSize() {
   return size;
}

NodoSimple *Cola::peek() {
   return this->cabeza;
}

NodoSimple *Cola::remove() {
   if (this->cabeza == NULL) {
      cout << "La Cola esta vacia!" << endl;
      return NULL;
   } else {
      NodoSimple *tmp = this->cabeza;
      this->cabeza = this->cabeza->getNext();
      this->size--;
      return tmp;
      delete tmp;
   }
}

void Cola::add(NodoSimple *nodo_) {
   if (this->cabeza == NULL) {
      this->cabeza = nodo_;
      this->size++;
   } else {
      NodoSimple *tmp = this->cabeza;
      while (tmp->getNext() != NULL) {
         tmp = tmp->getNext();
      }
      tmp->setNext(nodo_);
      this->size++;
   }
}

void Cola::printCola() {
   if (this->cabeza == NULL) {
      cout << "La cola esta vacia!" << endl;
   } else {
      NodoSimple *tmp = this->cabeza;
      while(tmp != NULL) {
         cout << tmp->getType() << "<-";
         tmp = tmp->getNext();
      }
   }
}
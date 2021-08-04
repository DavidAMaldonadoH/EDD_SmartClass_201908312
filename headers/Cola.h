#ifndef COLA
#define COLA

#include <iostream>
#include "NodoSimple.h"

class Cola {
   private:
      NodoSimple *cabeza;
      int size;

   public:
      Cola();
      bool isEmpty();
      int getSize();
      NodoSimple *peek();
      NodoSimple *remove();
      void add(NodoSimple *nodo_);
      void printCola();
};

#endif //COLA
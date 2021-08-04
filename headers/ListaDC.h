#ifndef LISTADC
#define LISTADC

#include <iostream>
#include "NodoDoble.h"

class ListaDC {
   private:
      NodoDoble *cabeza;
      int size;
   public:
      ListaDC();
      bool isEmpty();
      int getSize();
      NodoDoble *find(NodoDoble *nodo_);
      NodoDoble *get(int i);
      void add(NodoDoble *nodo_);
      void remove(NodoDoble *nodo_);
      void printLista();
   };

#endif // LISTADC
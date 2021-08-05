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
      NodoDoble *find(std::string id_);
      NodoDoble *get(int i);
      void add(NodoDoble *nodo_);
      void remove(std::string id_);
      void printLista();
   };

#endif // LISTADC
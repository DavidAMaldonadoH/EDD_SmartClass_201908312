#ifndef LISTADOBLE
#define LISTADOBLE

#include <iostream>
#include "NodoDoble.h"

class ListaDoble {
   private:
      NodoDoble *cabeza;
      int size;

   public:
      ListaDoble();
      bool isEmpty();
      int getSize();
      NodoDoble *find(NodoDoble *nodo_);
      NodoDoble *get(int i);
      void add(NodoDoble *nodo_);
      void remove(NodoDoble *nodo_);
      void printLista();
};

#endif //LISTADOBLE
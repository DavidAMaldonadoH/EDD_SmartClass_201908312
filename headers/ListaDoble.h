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
      NodoDoble *find(std::string id_);
      NodoDoble *get(int i);
      void add(NodoDoble *nodo_);
      void remove(std::string id_);
      void printLista();
};

#endif //LISTADOBLE
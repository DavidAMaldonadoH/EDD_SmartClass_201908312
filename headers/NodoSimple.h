#ifndef NODOSIMPLE
#define NODOSIMPLE

#include <iostream>

class NodoSimple {
private:
   std::string type;
   NodoSimple *next;
public:
   // Constructors
   NodoSimple();
   NodoSimple(std::string type_);

   // Setters
   void setNext(NodoSimple *nodo_);
   void setType(std::string type_);

   // Getters
   std::string getType();
   NodoSimple *getNext();
};

#endif
#ifndef NODODOBLE
#define NODODOBLE

#include <iostream>

class NodoDoble {
   private:
      std::string type;
      NodoDoble *next;
      NodoDoble *previous;
   public:
      // Constructors
      NodoDoble();
      NodoDoble(std::string type_);

      //Setters
      void setType(std::string type_);
      void setNext(NodoDoble *next_);
      void setPrevious(NodoDoble *previous_);

      //Getters
      std::string getType();
      NodoDoble *getNext();
      NodoDoble *getPrevious();

      //Operator Overloading
      friend NodoDoble operator==(NodoDoble& nodo_, NodoDoble& nodo2_);
};

#endif
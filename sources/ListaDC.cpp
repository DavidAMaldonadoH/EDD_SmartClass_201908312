#include <iostream>
#include "../headers/ListaDC.h"
#include "../headers/NodoDoble.h"

using namespace std;

ListaDC::ListaDC() {
   this->cabeza = NULL;
   this->size = 0;
}

bool ListaDC::isEmpty() {
   return this->cabeza == NULL;
}

int ListaDC::getSize() {
   return this->size;
}

NodoDoble *ListaDC::find(string id_) {
   if (this->cabeza == NULL) {
      cout << "La Lista esta vacia!" << endl;
      return NULL;
   } else {
      for (int i = 0; i < this->size; i++) {
         NodoDoble *tmp = get(i);
         if (id_ == tmp->getType()) {
            return tmp;
         }
      }
      return 0;
   }
}

NodoDoble *ListaDC::get(int i) {
   if (i > this->size || i < 0) {
      cout << "El valor a buscar es mayor al tamanio de la lista!" << endl;
      return NULL;
   }
   if (this->cabeza == NULL) {
      cout << "La lista esta vacia!" << endl;
      return NULL;
   } else {
      int indice = 0;
      NodoDoble *tmp = this->cabeza;
      while (indice != i) {
         tmp = tmp->getNext();
         indice++;
      }
      return tmp;
   }
}

void ListaDC::add(NodoDoble *nodo_) {
   if (this->cabeza == NULL) {
      this->cabeza = nodo_;
      this->cabeza->setNext(this->cabeza);
      this->cabeza->setPrevious(this->cabeza);
   } else {
      NodoDoble *tmp = this->cabeza;
      while(tmp->getNext() != this->cabeza) {
         tmp = tmp->getNext();
      }
      tmp->setNext(nodo_);
      nodo_->setPrevious(tmp);
      nodo_->setNext(this->cabeza);
      this->cabeza->setPrevious(nodo_);
   }
   this->size++;
}

void ListaDC::remove(string id_) {
   if (this->cabeza == NULL) {
      cout << "La Lista esta vacia!" << endl;
   } else {
      NodoDoble *toDelete = this->find(id_);
      if (toDelete == this->cabeza) {
         if (this->size != 1) {
            NodoDoble *tmp1 = this->cabeza->getPrevious();
            NodoDoble *tmp2 = this->cabeza->getNext();
            this->cabeza = tmp2;
            tmp2->setPrevious(tmp1);
            tmp1->setNext(tmp2);
         } else {
            this->cabeza = NULL;
         }
         this->size--;
      } else if (toDelete->getNext() == this->cabeza) {
         NodoDoble *tmp = toDelete->getPrevious();
         tmp->setNext(this->cabeza);
         this->cabeza->setPrevious(tmp);
         toDelete->setPrevious(NULL);
         this->size--;
      } else {
         NodoDoble *tmp1 = toDelete->getPrevious();
         NodoDoble *tmp2 = toDelete->getNext();
         tmp1->setNext(tmp2);
         tmp2->setPrevious(tmp1);
         this->size--;
      }
   }
}

void ListaDC::printLista() {
   if (this->cabeza == NULL) {
      cout << "La Lista esta vacia!" << endl;
   } else {
      for (int i = 0; i < this->size; i++) {
         NodoDoble *tmp = this->get(i);
         //cout << tmp->getType() << endl;
         cout << tmp->getPrevious()->getType() << " <- " << tmp->getType() << " -> " << tmp->getNext()->getType() << endl;
      }
   }
}
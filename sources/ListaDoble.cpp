#include <iostream>
#include "../headers/ListaDoble.h"
#include "../headers/NodoDoble.h"

using namespace std;

ListaDoble::ListaDoble() {
   this->cabeza = NULL;
   this->size = 0;
}

bool ListaDoble::isEmpty() {
   return this->cabeza == NULL;
}

int ListaDoble::getSize() {
   return this->size;
}

NodoDoble *ListaDoble::find(NodoDoble *nodo_) {
   if (this->cabeza == NULL) {
      cout << "La Lista esta vacia!" << endl;
      return NULL;
   } else {
      NodoDoble *tmp = this->cabeza;
      while(tmp != NULL) {
         if (nodo_ == tmp ) {
            return tmp;
         } else {
            tmp = tmp->getNext();
         }
      }
      return 0;
   }
}

NodoDoble *ListaDoble::get(int i) {
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

void ListaDoble::add(NodoDoble *nodo_) {
   if (this->cabeza == NULL) {
      this->cabeza = nodo_;
      this->size++;
   } else {
      NodoDoble *tmp = this->cabeza;
      while (tmp->getNext() != NULL) {
         tmp = tmp->getNext();
      }
      tmp->setNext(nodo_);
      nodo_->setPrevious(tmp);
      this->size++;
   }
}

void ListaDoble::remove(NodoDoble *nodo_){
   if (this->cabeza == NULL) {
      cout << "La Lista esta vacia!" << endl;
   } else {
      NodoDoble *toDelete = this->find(nodo_);
      if (toDelete == this->cabeza) {
         if (this->size != 1) {
            NodoDoble *tmp = this->cabeza->getNext();
            tmp->setPrevious(NULL);
            this->cabeza = tmp;
         } else {
            this->cabeza = NULL;
         }
         this->size--;
      } else if (toDelete->getNext() == NULL) {
         NodoDoble *tmp = toDelete->getPrevious();
         tmp->setNext(NULL);
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

void ListaDoble::printLista() {
   if (this->cabeza == NULL) {
      cout << "La Lista esta vacia!" << endl;
   } else {
      for (int i = 0; i < this->size; i++) {
         NodoDoble *tmp = this->get(i);
         if (i == 0) {
            if (tmp->getNext() == NULL) {
               cout << "Nulo <- " << tmp->getType() << " -> Nulo" << endl;
            } else {
               cout << "Nulo <- " << tmp->getType() << " -> " << tmp->getNext()->getType()  << endl;
            }
         } else if (i+1 == this->size) {
            cout << tmp->getPrevious()->getType() << " <- " << tmp->getType() << " -> Nulo" << endl;
         } else {
            cout << tmp->getPrevious()->getType() << " <- " << tmp->getType() << " -> " << tmp->getNext()->getType() << endl;
         }
      }
   }
}
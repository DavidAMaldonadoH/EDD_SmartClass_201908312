#include <iostream>
#include <iomanip>
#include <limits>
#include "headers/functions.h"   

using namespace std;

int main() {
   bool menu = true;

   while (menu) {
      int opcion;
      printMenu();
      cout << "Ingrese la opcion que desee: " << endl;
      try {
         cin >> opcion;
         if (opcion == 1) {
            cargaUsuarios();
         } else if (opcion == 2) {
            cargaTareas();
         } else if (opcion == 3) {
            ingresoManual();
         } else if (opcion == 4) {
            reportes();
         } else if (opcion == 5) {
            menu = false;
         } else {
            cin.clear(); //Limpiar la entrada
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); //Descartar entrada
            throw -1;
         }
      } catch(int x) {
         cout << "Entrada invalida; por favor ingrese de nuevo una opcion!" << endl;
      }
   }

   return 0;
}
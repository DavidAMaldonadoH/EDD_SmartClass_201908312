#include <iostream>
#include <iomanip>
#include <limits>
#include <locale.h>
#include <windows.h>
#include "headers/functions.h"   
#include "headers/ListaDC.h"
#include "headers/Estudiante.h"
#include "headers/Cola.h"
#include "headers/Error.h"

using namespace std;

int main() {
	SetConsoleOutputCP(CP_UTF8);
   bool menu = true;
   ListaDC *listaEstudiantes = new ListaDC();
   Cola *colaErrores = new Cola();
   while (menu) {
      int opcion;
      printMenu();
      printf("Ingrese la opción que desee: ");
      try {
         cin >> opcion;
         if (opcion == 1) {
            cargaUsuarios(listaEstudiantes, colaErrores);
         } else if (opcion == 2) {
            cargaTareas();
         } else if (opcion == 3) {
            ingresoManual(listaEstudiantes);
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
         cout << "Entrada inválida; por favor ingrese de nuevo una opción!" << endl;
      }
   }

   return 0;
}
// g++ -o main.exe main.cpp sources/functions.cpp sources/ListaDC.cpp sources/Cola.cpp sources/NodoDoble.cpp sources/NodoSimple.cpp sources/Estudiante.cpp sources/Error.cpp
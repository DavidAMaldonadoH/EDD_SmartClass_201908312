#include <iostream>
#include <iomanip>
#include <limits>
#include <locale.h>
#include <windows.h>
#include "headers/functions.h"   
#include "headers/ListaDC.h"
#include "headers/ListaDoble.h"
#include "headers/Tarea.h"
#include "headers/Cola.h"

using namespace std;

int main() {
	SetConsoleOutputCP(CP_UTF8);
   setlocale(LC_ALL, "es_ES");
   bool menu = true;
   ListaDC *listaEstudiantes = new ListaDC();
   ListaDoble *listaTareas = new ListaDoble();
   Cola *colaErrores = new Cola();
   while (menu) {
      int opcion;
      printMenu();
      printf("> Ingrese una opción: ");
      try {
         cin >> opcion;
         if (opcion == 1) {
            cargaUsuarios(listaEstudiantes, colaErrores);
         } else if (opcion == 2) {
            cargaTareas(listaTareas, listaEstudiantes, colaErrores);
         } else if (opcion == 3) {
            ingresoManual(listaEstudiantes, listaTareas, colaErrores);
         } else if (opcion == 4) {
            reportes(listaEstudiantes, listaTareas, colaErrores);
         } else if (opcion == 5) {
            solucionarErrores(listaEstudiantes, listaTareas, colaErrores);
         } else if (opcion == 6) {
            menu = false;
         } else {
            cin.clear(); //Limpiar la entrada
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); //Descartar entrada
            throw -1;
         }
      } catch(int x) {
         cout << "> Entrada inválida; por favor ingrese de nuevo una opción!" << endl;
      }
   }

   return 0;
}
//g++ -o main.exe main.cpp sources/functions.cpp sources/ListaDC.cpp sources/ListaDoble.cpp sources/Cola.cpp sources/NodoDoble.cpp sources/NodoSimple.cpp sources/Estudiante.cpp sources/Tarea.cpp sources/Error.cpp
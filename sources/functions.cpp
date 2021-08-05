#include <iostream>
#include <iomanip>
#include <limits>
#include "../headers/functions.h"
#include "../headers/ListaDC.h"
#include "../headers/Estudiante.h"

using namespace std;

// Menu Principal
void printMenu() {
   string menuOptions[5] = {"1. Carga de Usuarios", "2. Carga de Tareas",
   "3. Ingreso Manual", "4. Reportes", "5. Salir"};
   cout << endl;
   cout << setfill('-') << setw(36) << "Smart Class" << setw(25) << setfill('-')  << '\n';
   for (string s : menuOptions) {
      cout << s << endl;
   }
}

// Carga de Usuarios
void cargaUsuarios() {
   cout << '\n' << "Cargando Usuarios" << endl;
}

// Carga de Tareas
void cargaTareas() {
   cout << '\n' << "Cargando Tareas" << endl;
}

// Ingreso Manual
void menuManual() {
   string menuOptions[3] = {"1. Usuarios", "2. Tareas", "3. Salir"};
   cout << endl;
   cout << setfill('-') << setw(38) << "Ingreso Manual" << setw(23) << setfill('-')  << '\n';
   for (string s : menuOptions) {
      cout << s << endl;
   }
}

void menuUsuarios(ListaDC *listaEstudiantes) {
   bool menu = true;
   while(menu) {
      int opcion;
      string menuOptions[4] = {"1. Ingresar", "2. Modificar", "3. Eliminar", "4. Salir"};
      cout << endl;
      cout << setfill('-') << setw(37) << "Menu Usuarios" << setw(24) << setfill('-')  << '\n';
      for (string s : menuOptions) {
         cout << s << endl;
      }
      cout << '\n' <<  "Ingrese la opcion que desee: " << endl;
      try {
         cin >> opcion;
         if (opcion == 1) {
            string carne, DPI, nombre, carrera, password;
            int creditos, edad;
            printf("Carnet: ");
            cin >> carne;
            printf("DPI: ");
            cin >> DPI;
            printf("Nombre: ");
            cin.ignore();
            getline(cin, nombre);
            cin.clear();
            cin.sync();
            printf("Carrera: ");
            getline(cin, carrera);
            printf("Contraseña: "); 
            cin >> password;
            printf("Créditos: ");
            cin >> creditos;
            printf("Edad: ");
            cin >> edad;
            Estudiante *est = new Estudiante(carne, DPI, nombre, carrera, password,
            creditos, edad);
            listaEstudiantes->add(est);
            listaEstudiantes->printLista();
         } else if (opcion == 2) {
            cout << "modificar" << endl;
         } else if (opcion == 3) {
            string id_;
            int eliminar;
            cout << "Ingrese el DPI del estudiante a eliminar: " << endl;
            cin >> id_;
            NodoDoble *tmp = listaEstudiantes->find(id_);
            if (tmp != NULL) {
               cout << "Esta seguro de eliminar a: " << endl;
               tmp->printInfo();
               cout << "Ingrese el numero:\n1. Si\n2. No\n";
               cin >> eliminar;
               if (eliminar == 1) {
                  listaEstudiantes->remove(tmp->getType());
                  cout << "Estudiante eliminado con exito!" << endl;
               } else {
                  cout << "No se ha eliminado al estudiante!" << endl;
               }
               listaEstudiantes->printLista();
            } else {
               cout << "El carnet ingresado no se encuentra en la lista de Estudiantes!\n";
            }
         } else if (opcion == 4) {   
            menu = false;
         } else {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            throw -1;
         }
      } catch (int x) {
         cout << "Entrada invalida; por favor ingrese de nuevo una opcion!" << endl;
      }
   }
}

void menuTareas() {
   bool menu = true;
   while(menu) {
      int opcion;
      string menuOptions[4] = {"1. Ingresar", "2. Modificar", "3. Eliminar", "4. Salir"};
      cout << endl;
      cout << setfill('-') << setw(36) << "Menu Tareas" << setw(25) << setfill('-')  << '\n';
      for (string s : menuOptions) {
         cout << s << endl;
      }
      cout << '\n' <<  "Ingrese la opcion que desee: " << endl;
      try {
         cin >> opcion;
         if (opcion == 1) {
            cout << "ingreso" << endl;
         } else if (opcion == 2) {
            cout << "modificar" << endl;
         } else if (opcion == 3) {
            cout << "eliminar" << endl;
         } else if (opcion == 4) {   
            menu = false;
         } else {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            throw -1;
         }
      } catch (int x) {
         cout << "Entrada invalida; por favor ingrese de nuevo una opcion!" << endl;
      }
   }
}

void ingresoManual(ListaDC *listaEstudiantes) {
   bool menu = true;
   while(true) {
      int opcion;
      menuManual();
      cout << '\n' <<  "Ingrese la opcion que desee: " << endl;
      try {
         cin >> opcion;
         switch (opcion) {
         case 1:
            menuUsuarios(listaEstudiantes);
            break;
         case 2:
            menuTareas();
            break;
         case 3: 
            menu = false;
            return;
            break;
         default:
            cin.clear(); //Limpiar la entrada
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); //Descartar entrada
            throw -1;
            break;
         }
      } catch (int x) {
         cout << "Entrada invalida; por favor ingrese de nuevo una opcion!" << endl;
      }
   }
}

// Reportes
void menuReportes() {
   string menuOptions[3] = {"1. Lista Usuarios", "2. Linealizacion Tareas", "3. Salir"};
   cout << endl;
   cout << setfill('-') << setw(34) << "Reportes" << setw(27) << setfill('-')  << '\n';
   for (string s : menuOptions) {
      cout << s << endl;
   }
}

void reportes() {
   bool menu = true;
   while(menu) {
      int opcion;
      menuReportes();
      cout << '\n' <<  "Ingrese la opcion que desee: " << endl;
      try {
         cin >> opcion;
         switch (opcion)
         {
         case 1:
            cout << "Lista Ususarios" << endl;
            break;
         case 2:
            cout << "Linealizacion Tareas" << endl;
            break;
         case 3:
            menu = false;
            return;
            break;
         default:
            cin.clear(); //Limpiar la entrada
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); //Descartar entrada
            throw -1;
            break;
         }
      } catch(int x) {
         cout << "Entrada invalida; por favor ingrese de nuevo una opcion!" << endl;
      }
   }
}
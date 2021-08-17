#include <iostream>
#include <iomanip>
#include <limits>
#include <fstream>
#include <stdlib.h>
#include "../headers/functions.h"
#include "../headers/ListaDC.h"
#include "../headers/Estudiante.h"
#include "../headers/ListaDoble.h"
#include "../headers/Tarea.h"
#include "../headers/Cola.h"
#include "../headers/Error.h"
using namespace std;

// Menu Principal
void printMenu() {
   string menuOptions[6] = {"1. Carga de Usuarios", "2. Carga de Tareas",
   "3. Ingreso Manual", "4. Reportes", "5. Solucionar Errores", "6. Salir"};
   cout << endl;
   cout << setfill('-') << setw(36) << "Smart Class" << setw(25) << setfill('-')  << '\n';
   for (string s : menuOptions) {
      cout << s << endl;
   }
}

// Carga de Usuarios
void cargaUsuarios(ListaDC *listaEstudiantes, Cola *colaErrores) {
   ifstream file;
   string line, filePath;
   printf("> Ingrese la dirección del archivo: ");
   cin >> filePath;
   file.open(filePath);
   if (!file.fail()) {
      while (getline(file, line)) {
         string datos[8], tmp;
         int comas = 0;
         if (line != "Carnet,DPI,Nombre,Carrera,Password,Creditos,Edad,Correo") {
            for (int i = 0; i < (int)line.size(); i++) {
               if (line[i] != ',') {
                  tmp+=line[i];
               } else {
                  tmp = "";
                  comas++;
               }               
               datos[comas] = tmp;
            }
            Estudiante *est = new Estudiante(datos[0], datos[1], datos[2], datos[3], datos[4], datos[7], stoi(datos[5]), stoi(datos[6]));
            listaEstudiantes->add(est);
            est->checkErrors(colaErrores);
         }
      }
      cout << "\n> Archivo cargado con éxito!\n";
   } else {
      cout << "\n> La dirección ingresada es inválida!\n";
   }
   file.close();
}

// Carga de Tareas
void cargaTareas(ListaDoble *listaTareas, ListaDC *listaEstudiantes, Cola *colaErrores) {
   //Iniciacion de los elementos del array 3d
   int meses = 5, dias = 30, horas = 9;
   Tarea *calendario[meses][dias][horas];
   for (int i = 0; i < meses; i++) {
      for (int j = 0; j < dias; j++) {
         for (int k = 0; k < horas; k++) {
            Tarea *tmp = new Tarea();
            tmp->setId(k+horas*(j+dias*i));
            tmp->setNombre("-1");
            calendario[i][j][k] = tmp;
         }
      }
   }
   ifstream file;
   string line, filePath;
   printf("> Ingrese la dirección del archivo: ");
   cin >> filePath;
   file.open(filePath, ios::in);
   if (!file.fail()) {
      while (getline(file, line)) {
         string datos[9], tmp;
         int comas = 0;
         if (line != "Mes,Dia,Hora,Carnet,Nombre,Descripcion,Materia,Fecha,Estado") {
            for (int i = 0; i < (int)line.size(); i++) {
               if (line[i] != ',') {
                  tmp+=line[i];
               } else {
                  tmp = "";
                  comas++;
               }               
               datos[comas] = tmp;
            }
            Tarea *nuevaTarea = new Tarea(datos[3], datos[4], datos[5], datos[6], datos[7], datos[2], datos[8]);
            nuevaTarea->setId((stoi(datos[2])-8)+horas*((stoi(datos[1])-1)+dias*(stoi(datos[0])-7)));
            nuevaTarea->checkErrors(colaErrores);
            bool existsEst = nuevaTarea->inEstudiantes(listaEstudiantes);
            if (existsEst) {
               calendario[stoi(datos[0])-7][stoi(datos[1])-1][stoi(datos[2])-8] = nuevaTarea;
            } else {
               int agregar = 0;
               cout << "\nEl carnet " << datos[3] << " ingresado en la tarea no corresponde a ningun estudiante previamente ingresado\n";
               cout << "> Desea agregar un nuevo Estudiante con el carnet para la Tarea:\n1. Si\n2. No\n"; 
               cin >> agregar;
               if (agregar == 1) {
                  agregarEstudiante(listaEstudiantes, colaErrores);
                  calendario[stoi(datos[0])-7][stoi(datos[1])-1][stoi(datos[2])-8] = nuevaTarea;
               }
            }
         }
      }
      cout << "\n> Archivo cargado con éxito!\n";
   } else {
      cout << "\n> La dirección del archivo ingresado es inválida!\n";
   }
   file.close();
   //Linealizacion
   for (int i = 0; i < meses; i++) {
      for (int j = 0; j < dias; j++) {
         for (int k = 0; k < horas; k++) {
            listaTareas->add(calendario[i][j][k]);
         }
      }
   }
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

void modificarEstudiante(ListaDC *listaEstudiantes, Cola *colaErrores, string id_ = "") {
   string id = id_ ;
   int modificar;
   if (id_ == ""){
      cout << "> Ingrese el DPI del estudiante a modificar: ";
      cin >> id;
   }
   NodoDoble *tmp = listaEstudiantes->find(id);
   if (tmp != NULL) {
      string entradaS;
      int entradaI;
      tmp->printInfo();
      printf("Que desea modificar:\n1.Carné\n2.DPI\n3.Nombre\n4.Carrera\n5.Contraseña\n6.Créditos\n7.Edad\n8.Correo\n");
      cin >> modificar;
      switch (modificar) {
         case 1:
            printf("Ingrese el nuevo carné: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Estudiante*)(tmp))->setCarne(entradaS); 
            break;
         case 2:
            printf("Ingrese el nuevo DPI: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Estudiante*)(tmp))->setDPI(entradaS); 
            tmp->setType(entradaS);
            break;
         case 3:
            printf("Ingrese el nuevo nombre: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Estudiante*)(tmp))->setNombre(entradaS); 
            break;
         case 4:
            printf("Ingrese la nueva carrera: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Estudiante*)(tmp))->setCarrera(entradaS); 
            break;
         case 5:
            printf("Ingrese la nueva contraseña: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Estudiante*)(tmp))->setPassword(entradaS); 
            break;
         case 6:
            printf("Ingrese los créditos: ");
            cin.ignore();
            cin >> entradaI;
            ((Estudiante*)(tmp))->setCreditos(entradaI); 
            break;
         case 7:
            printf("Ingrese la nueva edad: ");
            cin.ignore();
            cin >> entradaI;
            ((Estudiante*)(tmp))->setEdad(entradaI); 
            break;
         case 8:
            printf("Ingrese el nuevo correo: ");
            cin.ignore();
            cin >> entradaS;
            ((Estudiante*)(tmp))->setCorreo(entradaS); 
            break;
         default:
            break;
      }
      ((Estudiante*)(tmp))->checkErrors(colaErrores);
      cout << "\n> Estudiante modificado con éxito!\n";
   } else {
      cout << "\n> El DPI ingresado no se encuentra en la lista de Estudiantes!\n";
   }
}

void agregarEstudiante(ListaDC *listaEstudiantes, Cola *colaErrores) {
   string carne, DPI, nombre, carrera, password, correo;
   int creditos, edad;
   printf("Carné: ");
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
   printf("Correo: ");
   cin >> correo;
   Estudiante *est = new Estudiante(carne, DPI, nombre, carrera, password, correo, creditos, edad);
   listaEstudiantes->add(est);
   est->checkErrors(colaErrores);
   cout << "\n> Estudiante agregado con éxito!\n";
}

void eliminarEstudiante(ListaDC *listaEstudiantes) {
   string id_;
   int eliminar;
   cout << "\n> Ingrese el DPI del estudiante a eliminar: ";
   cin >> id_;
   NodoDoble *tmp = listaEstudiantes->find(id_);
   if (tmp != NULL) {
      cout << "Esta seguro de eliminar al ";
      tmp->printInfo();
      cout << "> Ingrese una opción:\n1. Si\n2. No\n";
      cin >> eliminar;
      if (eliminar == 1) {
         listaEstudiantes->remove(tmp->getType());
         cout << "> Estudiante eliminado con exito!" << endl;
      } else {
         cout << "> No se ha eliminado al estudiante!" << endl;
      }
   } else {
      cout << "\n> El DPI ingresado no se encuentra en la lista de Estudiantes!\n";
   }
}

void menuUsuarios(ListaDC *listaEstudiantes, Cola *colaErrores) {
   bool menu = true;
   while(menu) {
      int opcion;
      string menuOptions[4] = {"1. Ingresar", "2. Modificar", "3. Eliminar", "4. Salir"};
      cout << endl;
      cout << setfill('-') << setw(37) << "Menu Usuarios" << setw(24) << setfill('-')  << '\n';
      for (string s : menuOptions) {
         cout << s << endl;
      }
      cout << "\n> Ingrese una opción: ";
      try {
         cin >> opcion;
         if (opcion == 1) {
            agregarEstudiante(listaEstudiantes, colaErrores);
         } else if (opcion == 2) {
            modificarEstudiante(listaEstudiantes, colaErrores);
         } else if (opcion == 3) {
            eliminarEstudiante(listaEstudiantes);
         } else if (opcion == 4) {   
            menu = false;
         } else {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            throw -1;
         }
      } catch (int x) {
         cout << "> Entrada inválida; por favor ingrese de nuevo una opción!" << endl;
      }
   }
}

void modificarTarea(ListaDoble *listaTareas, Cola *colaErrores, string id_ = "") {
   string id = id_;
   int modificar, mes, dia, hora;
   if (id_ == "") {
      cout << "\n> Ingrese el Mes de la tarea que desea modificar: ";
      cin >> mes;
      cout << "\n> Ingrese el Dia de la tarea que desea modificar: ";
      cin >> dia;
      cout << "\n> Ingrese la Hora de la tarea que desea modificar: ";
      cin >> hora;
      id = to_string((hora-8)+9*((dia-1)+30*(mes-7)));
   }
   NodoDoble *tmp = listaTareas->find(id);
   if (tmp != NULL) {
      string entradaS;
      tmp->printInfo();
      printf("Que desea modificar:\n1.Carné\n2.Nombre\n3.Descripción\n4.Materia\n5.Fecha\n6.Hora\n7.Estado\n");
      cin >> modificar;
      switch (modificar) {
         case 1:
            printf("Ingrese el nuevo carné: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Tarea*)(tmp))->setCarne(entradaS); 
            break;
         case 2:
            printf("Ingrese el nuevo nombre: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Tarea*)(tmp))->setNombre(entradaS); 
            tmp->setType(entradaS);
            break;
         case 3:
            printf("Ingrese la nueva descripción: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Tarea*)(tmp))->setDescripcion(entradaS); 
            break;
         case 4:
            printf("Ingrese la nueva materia: ");
            cin.ignore();
            getline(cin, entradaS);
            ((Tarea*)(tmp))->setMateria(entradaS); 
            break;
         case 5:
            printf("Ingrese la nueva fecha (YYYY/MM/DD): ");
            cin.ignore();
            getline(cin, entradaS);
            ((Tarea*)(tmp))->setFecha(entradaS); 
            break;
         case 6:
            printf("Ingrese la hora: ");
            cin.ignore();
            cin >> entradaS;
            ((Tarea*)(tmp))->setHora(entradaS); 
            break;
         case 7:
            printf("Ingrese el nuevo estado: ");
            cin.ignore();
            cin >> entradaS;
            ((Tarea*)(tmp))->setEstado(entradaS); 
            break;
         default:
            break;
      }
      ((Tarea*)(tmp))->checkErrors(colaErrores);
      cout << "\n> Tarea modificada con éxito!\n";
   } else {
      cout << "> El id ingresado no se encuentra en la lista de Tareas!\n";
   }
}

void agregarTarea(ListaDoble *listaTareas, Cola *colaErrores) {
   int mes, dia, hora;
   cout << "\n> Ingrese el Mes de la tarea que desea agregar: ";
   cin >> mes;
   cout << "\n> Ingrese el Dia de la tarea que desea agregar: ";
   cin >> dia;
   cout << "\n> Ingrese la Hora de la tarea que desea agregar: ";
   cin >> hora;
   string carne, nombre, descripcion, materia, fecha, estado;
   string id_ = to_string((hora-8)+9*((dia-1)+30*(mes-7)));
   NodoDoble *tmp = listaTareas->find(id_);
   if (((Tarea*)(tmp))->getNombre() == "-1") {
      printf("Carné: ");
      cin >> carne;
      printf("Nombre: ");
      cin.ignore();
      cin.clear(); cin.sync();
      getline(cin, nombre);
      printf("Descripcion: ");
      getline(cin, descripcion);
      printf("Materia: ");
      getline(cin, materia);
      printf("Fecha (YYYY/MM/DD): ");
      cin >> fecha;
      printf("Estado: ");
      cin >> estado;
      ((Tarea*)(tmp))->setCarne(carne);
      ((Tarea*)(tmp))->setNombre(nombre);
      ((Tarea*)(tmp))->setDescripcion(descripcion);
      ((Tarea*)(tmp))->setMateria(materia);
      ((Tarea*)(tmp))->setFecha(fecha);
      ((Tarea*)(tmp))->setHora(to_string(hora));
      ((Tarea*)(tmp))->setEstado(estado);
      ((Tarea*)(tmp))->checkErrors(colaErrores);
      cout << "\n> Tarea agregada con éxito!\n";
   } else {
      cout << "\n> La fecha y hora ingresada ya posee una tarea!\n";
   }
}

void eliminarTarea(ListaDoble *listaTareas) {
   int eliminar;
   int mes, dia, hora;
   cout << "\n> Ingrese el Mes de la tarea que desea eliminar: ";
   cin >> mes;
   cout << "\n> Ingrese el Dia de la tarea que desea eliminar: ";
   cin >> dia;
   cout << "\n> Ingrese la Hora de la tarea que desea eliminar: ";
   cin >> hora;
   string id_ = to_string((hora-8)+9*((dia-1)+30*(mes-7)));
   NodoDoble *tmp = listaTareas->find(id_);
   if (tmp != NULL) {
      cout << "Esta seguro de eliminar la ";
      tmp->printInfo();
      cout << "> Ingrese una opción:\n1. Si\n2. No\n";
      cin >> eliminar;
      if (eliminar == 1) {
         listaTareas->remove(tmp->getType());
         cout << "> Tarea eliminada con exito!" << endl;
      } else {
         cout << "> No se ha eliminado la tarea!" << endl;
      }
   } else {
      cout << "\n> El id ingresado no se encuentra en la lista de Tareas!\n";
   }
}

void menuTareas(ListaDoble *listaTareas, Cola *colaErrores) {
   bool menu = true;
   while(menu) {
      int opcion;
      string menuOptions[4] = {"1. Ingresar", "2. Modificar", "3. Eliminar", "4. Salir"};
      cout << endl;
      cout << setfill('-') << setw(36) << "Menu Tareas" << setw(25) << setfill('-')  << '\n';
      for (string s : menuOptions) {
         cout << s << endl;
      }
      cout << "> Ingrese una opción: ";
      try {
         cin >> opcion;
         if (opcion == 1) {
            agregarTarea(listaTareas, colaErrores);
         } else if (opcion == 2) {
            modificarTarea(listaTareas, colaErrores);
         } else if (opcion == 3) {
            eliminarTarea(listaTareas);
         } else if (opcion == 4) {   
            menu = false;
         } else {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            throw -1;
         }
      } catch (int x) {
         cout << "\n> Entrada inválida; por favor ingrese de nuevo una opción!" << endl;
      }
   }
}

void ingresoManual(ListaDC *listaEstudiantes, ListaDoble *listaTareas, Cola *colaErrores) {
   bool menu = true;
   while(true) {
      int opcion;
      menuManual();
      cout << "> Ingrese una opción: ";
      try {
         cin >> opcion;
         switch (opcion) {
         case 1:
            menuUsuarios(listaEstudiantes, colaErrores);
            break;
         case 2:
            menuTareas(listaTareas, colaErrores);
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
         cout << "\n> Entrada inválida; por favor ingrese de nuevo una opción!" << endl;
      }
   }
}

// Reportes
void menuReportes() {
   string menuOptions[7] = {"1. Lista Usuarios", "2. Linealización Tareas", "3. Búsqueda en estructura linealizada",
   "4. Búsqueda de posición en lista linealizada", "5. Cola de Errores", "6. Código de salida", "7. Salir"};
   cout << endl;
   cout << setfill('-') << setw(34) << "Reportes" << setw(27) << setfill('-')  << '\n';
   for (string s : menuOptions) {
      cout << s << endl;
   }
}

void visualizarEst(ListaDC *listaEstudiantes) {
   ofstream file("archivo.dot", ios::out);//abrir un archivo en forma de escritura
   if (file.is_open()) {
      //escribir en dot 
      file << "digraph estudiantes {\n";
      file << "rankdir=\"LR\";";
      file << "\nbgcolor = \"#cbf3f0\";\nfontcolor = \"#293241\";\nlabelloc=t;\nlabel = \"Lista Estudiantes\";\nedge[color=\"#ff9f1c\"];";
      file << "\nfontname = \"Arial\";\nfontsize = \"24.0\";";
      file << "\nnode[shape=\"rect\" color=\"#ff9f1c\" fillcolor=\"#2ec4b6\" style=\"filled\"]";
      for (int i = 0; i < listaEstudiantes->getSize(); i++) {
         NodoDoble *tmp = listaEstudiantes->get(i);
         Estudiante *aux = ((Estudiante*)(tmp));
         if (i == 0) {
            file << "\nnodo" << i << " -> nodo" << i+1;
            file << "\nnodo" << i << " -> nodo" << listaEstudiantes->getSize()-1;
            file << "\nnodo" << i << "[label=\"DPI:" << aux->getDPI() <<"\\nCarnet:" << aux->getCarne() << "\\nNombre:" << aux->getNombre();
            file << "\\nCarrera: " << aux->getCarrera() << "\\nCorreo: " << aux->getCorreo() << "\\nContraseña: " << aux->getPassword();
            file << "\\nCréditos: " << aux->getCreditos() << "\\nEdad: " << aux->getEdad() << "\"]";
         } else if (i == listaEstudiantes->getSize()-1) {
            file << "\nnodo" << i << " -> nodo" << i-1;
            file << "\nnodo" << i << " -> nodo" << 0;
            file << "\nnodo" << i << "[label=\"DPI:" << aux->getDPI() <<"\\nCarnet:" << aux->getCarne() << "\\nNombre:" << aux->getNombre();
            file << "\\nCarrera: " << aux->getCarrera() << "\\nCorreo: " << aux->getCorreo() << "\\nContraseña: " << aux->getPassword();
            file << "\\nCréditos: " << aux->getCreditos() << "\\nEdad: " << aux->getEdad() << "\"]";
         } else {
            file << "\nnodo" << i << " -> nodo" << i+1;
            file << "\nnodo" << i << " -> nodo" << i-1;
            file << "\nnodo" << i << "[label=\"DPI:" << aux->getDPI() <<"\\nCarnet:" << aux->getCarne() << "\\nNombre:" << aux->getNombre();
            file << "\\nCarrera: " << aux->getCarrera() << "\\nCorreo: " << aux->getCorreo() << "\\nContraseña: " << aux->getPassword();
            file << "\\nCréditos: " << aux->getCreditos() << "\\nEdad: " << aux->getEdad() << "\"]";
         }
      }
      file << "\n}";
      file.close();
      int x = rand() % 100 + 1; 
      string cadena = "dot -Nfontname=Arial -Tsvg archivo.dot -o Img/estudiantes_" + to_string(x) + ".svg";
      const char *command = cadena.c_str();
      system(command);
      cout << "\n> Archivo generado exitosamente!\n";
   } else {
      cout << "\n> Algo salió mal!";
   }
}

void visualizarTareas(ListaDoble *listaTareas) {
   ofstream file("archivo.dot", ios::out);//abrir un archivo en forma de escritura
   if (file.is_open()) {
      //escribir en dot 
      file << "digraph tareas {\n";
      file << "rankdir=\"LR\";\n";
      file << "bgcolor = \"#caf0f8\";\nfontcolor = \"#03045e\";\nlabelloc=t;\nlabel = \"Lista Tareas\";\nedge[color=\"#03045e\"];";
      file << "\nfontname = \"Arial\";\nfontsize = \"24.0\";";
      file << "\nnode[shape=\"rect\" color=\"#03045e\" fillcolor=\"#48cae4\" style=\"filled\"]";
      for (int i = 0; i < listaTareas->getSize(); i++) {
         NodoDoble *tmp = listaTareas->get(i);
         Tarea *aux = ((Tarea*)(tmp));
         if (i == 0) {
            file << "\nnodo" << i << " -> nodo" << i+1;
            file << "\nnodo" << i << "[label=\"ID:" << aux->getId() <<"\\nCarnet:" << aux->getCarne() << "\\nNombre:" << aux->getNombre();
            file << "\\nDescripción: " << aux->getDescripcion() << "\\nMateria: " << aux->getMateria() << "\\nFecha: " << aux->getFecha();
            file << "\\nHora: " << aux->getHora() << ":00\\nEstado: " << aux->getEstado() << "\"]";
         } else if (i == listaTareas->getSize()-1) {
            file << "\nnodo" << i << " -> nodo" << i-1;
            file << "\nnodo" << i << "[label=\"ID:" << aux->getId() <<"\\nCarnet:" << aux->getCarne() << "\\nNombre:" << aux->getNombre();
            file << "\\nDescripción: " << aux->getDescripcion() << "\\nMateria: " << aux->getMateria() << "\\nFecha: " << aux->getFecha();
            file << "\\nHora: " << aux->getHora() << ":00\\nEstado: " << aux->getEstado() << "'\"]";
         } else {
            file << "\nnodo" << i << " -> nodo" << i+1;
            file << "\nnodo" << i << " -> nodo" << i-1;
            file << "\nnodo" << i << "[label=\"ID:" << aux->getId() <<"\\nCarnet:" << aux->getCarne() << "\\nNombre:" << aux->getNombre();
            file << "\\nDescripción: " << aux->getDescripcion() << "\\nMateria: " << aux->getMateria() << "\\nFecha: " << aux->getFecha();
            file << "\\nHora: " << aux->getHora() << ":00\\nEstado: " << aux->getEstado() << "\"]";
         }
      }
      file << "\n}";
      file.close();
      int x = rand() % 100 + 1; 
      string cadena = "dot -Nfontname=Arial -Tsvg archivo.dot -o Img/tareas_" + to_string(x) + ".svg";
      const char *command = cadena.c_str();
      system(command);
      cout << "\n> Archivo generado exitosamente!\n";
   } else {
      cout << "\n> Algo salió mal!";
   }
}

void visualizarErrores(Cola *colaErrores) {
   ofstream file("archivo.dot", ios::out);//abrir un archivo en forma de escritura
   if (file.is_open()) {
      //escribir en dot 
      file << "digraph estudiantes {\n";
      file << "rankdir=\"LR\";";
      file << "\nbgcolor = \"#ffccd5\";\nfontcolor = \"#293241\";\nlabelloc=t;\nlabel = \"Cola Errores\";\nedge[color=\"#800f2f\"];";
      file << "\nfontname = \"Arial\";\nfontsize = \"24.0\";";
      file << "\nnode[shape=\"rect\" color=\"#800f2f\" fillcolor=\"#ff6b6b\" style=\"filled\"]";
      NodoSimple *tmp = colaErrores->peek();
      file << "nodo0 -> Salida";
      for (int i = 0; i < colaErrores->getSize(); i++) {
         Error *aux = ((Error*)(tmp));
         if (i == colaErrores->getSize()-1) {
            file << "\nnodo" << i << "[label=\"ID: " << aux->getId()+1 <<"\\nTipo: " << aux->getTipo() << "\\nOrigen: " << aux->getOrigen();
            file << "\\nDescripción: " << aux->getDescripcion() << "\"]";
            file << "Entrada -> nodo" << i;
         } else {
            file << "\nnodo" << i + 1 << " -> nodo" << i;
            file << "\nnodo" << i << "[label=\"ID: " << aux->getId()+1 <<"\\nTipo: " << aux->getTipo() << "\\nOrigen: " << aux->getOrigen();
            file << "\\nDescripción: " << aux->getDescripcion() << "\"]";
         }
         tmp = tmp->getNext();
      }
      file << "\n}";
      file.close();
      int x = rand() % 100 + 1; 
      string cadena = "dot -Nfontname=Arial -Tsvg archivo.dot -o Img/errores_" + to_string(x) + ".svg";
      const char *command = cadena.c_str();
      system(command);
      cout << "\n> Archivo generado exitosamente!\n";
   } else {
      cout << "\n> Algo salió mal!";
   }
}

void buscarLista(ListaDoble *listaTareas) {
   int mes, dia, hora;
   cout << "\n> Ingrese el Mes de la tarea que desea modificar: ";
   cin >> mes;
   cout << "\n> Ingrese el Dia de la tarea que desea modificar: ";
   cin >> dia;
   cout << "\n> Ingrese la Hora de la tarea que desea modificar: ";
   cin >> hora;
   int id_ = (hora-8)+9*((dia-1)+30*(mes-7));
   NodoDoble *tmp = listaTareas->find(to_string(id_));
   if (tmp != NULL) 
      tmp->printInfo();
   else 
      cout << "> El id ingresado no se encuentra en la lista de Tareas!\n";
}

void calcularPosicion() {
   int mes, dia, hora;
   cout << "\n> Ingrese el Mes de la posición que desea buscar: ";
   cin >> mes;
   cout << "\n> Ingrese el Dia de la posición que desea buscar: ";
   cin >> dia;
   cout << "\n> Ingrese la Hora de la posición que desea buscar: ";
   cin >> hora;
   int posicion = (hora-8)+9*((dia-1)+30*(mes-7)); 
   cout << "La posición en la estructura linealizada sería: " << posicion << endl;
}

void generarSalida(ListaDC *listaEstudiantes, ListaDoble *listaTareas, Cola *colaErrores) {
   if (colaErrores->isEmpty()) {
      ofstream file("salida.txt", ios::out);//abrir un archivo en forma de escritura
      if (file.is_open()) { 
         file << "¿Elements?\n";
         for (int i = 0; i < listaEstudiantes->getSize(); i++) {
            NodoDoble *tmp = listaEstudiantes->get(i);
            Estudiante *aux = ((Estudiante*)(tmp));
            file << "\t¿element type=\"user\"?\n";
            file << "\t\t¿item Carnet = \"" << aux->getCarne() << "\"$?\n";
            file << "\t\t¿item DPI = \"" << aux->getDPI() << "\"$?\n";
            file << "\t\t¿item Nombre = \"" << aux->getNombre() << "\"$?\n";
            file << "\t\t¿item Carrera = \"" << aux->getCarrera() << "\"$?\n";
            file << "\t\t¿item Password = \"" << aux->getPassword() << "\"$?\n";
            file << "\t\t¿item Creditos = "<< aux->getCreditos() << " $?\n";
            file << "\t\t¿item Edad = " << aux->getEdad() << " $?\n";
            file << "\t¿$element?\n";
         }
         for (int i = 0; i < listaTareas->getSize(); i++) {
            NodoDoble *tmp = listaTareas->get(i);
            Tarea *aux = ((Tarea*)(tmp));
            if (aux->getNombre() != "-1")
            {
               file << "\t¿element type=\"task\"?\n";
               file << "\t\t¿item Carnet = \"" << aux->getCarne() << "\" $?\n";
               file << "\t\t¿item Nombre = \"" << aux->getNombre() << "\" $?\n";
               file << "\t\t¿item Descripcion = \"" << aux->getDescripcion() << "\" $?\n";
               file << "\t\t¿item Materia = \"" << aux->getMateria() << "\" $?\n";
               file << "\t\t¿item Fecha = \"" << aux->getFecha() << "\" $?\n";
               file << "\t\t¿item Hora = \"" << aux->getHora() << ":00\" $?\n";
               file << "\t\t¿item Estado = \"" << aux->getEstado() << "\" $?\n";
               file << "\t¿$element?\n";
            }
         }
         file << "¿$Elements?";
         file.close();
         cout << "\n> Archivo generado exitosamente!\n";
      } else {
      cout << "\n> Algo salió mal!";
   }
   } else {
      cout << "\nLos datos ingresados aun poseen erroes, corrijalos antes de generar el archivo!.\n";
   }
}

void reportes(ListaDC *listaEstudiantes, ListaDoble *listaTareas, Cola *colaErrores) {
   bool menu = true;
   while(menu) {
      int opcion;
      menuReportes();
      cout << "> Ingrese una opción: ";
      try {
         cin >> opcion;
         switch (opcion)
         {
         case 1://Lista de Usuarios
            visualizarEst(listaEstudiantes);
            break;
         case 2://Lista de Tareas
            visualizarTareas(listaTareas);
            break;
         case 3://Busqueda en lista doblemente enlazada
            buscarLista(listaTareas);
            break;
         case 4://Calculo de posicion segun mes dia y hora
            calcularPosicion();
            break;
         case 5://Cola de Errores
            visualizarErrores(colaErrores);
            break;
         case 6://Archivo de salida
            generarSalida(listaEstudiantes, listaTareas, colaErrores);
            break;
         case 7:
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
         cout << "\n> Entrada inválida; por favor ingrese de nuevo una opción!" << endl;
      }
   }
}

//Errores
void solucionarErrores(ListaDC *listaEstudiantes, ListaDoble *listaTareas, Cola *colaErrores) {
   bool solucionar = true, continuar = true;
   int vueltas = 0, x;
   while (solucionar) {
      if (vueltas != 0) {
         cout << "\n> Desea continuar:\n1. Si\n2. No ";
         cin >> x;
         if (x == 2)
            continuar = false;
      }
      if (colaErrores->isEmpty() | !continuar) {
         solucionar = false;
         break;
      }
      NodoSimple *tmpError = colaErrores->remove();
      cout << "\n> Descripción: " << ((Error*)(tmpError))->getDescripcion() << '\n';
      if (((Error*)(tmpError))->getTipo() == "Estudiante") {
         modificarEstudiante(listaEstudiantes, colaErrores, ((Error*)(tmpError))->getOrigen());
      } else {
         modificarTarea(listaTareas, colaErrores, ((Error*)(tmpError))->getOrigen());
      }
      vueltas++;
   }
}
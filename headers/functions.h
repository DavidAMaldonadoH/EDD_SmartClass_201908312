#ifndef FUNCTIONS
#define FUNCTIONS

#include "ListaDC.h"

// Menu Principal
void printMenu();

// Carga de Usuarios
void cargaUsuarios();

// Carga de Tareas
void cargaTareas();

// Ingreso Manual
void menuManual();
void menuUsuarios(ListaDC *listaEstudiantes);
void menuTareas();
void ingresoManual(ListaDC *listaEstudiantes);

// Reportes
void menuReportes();
void reportes();

#endif
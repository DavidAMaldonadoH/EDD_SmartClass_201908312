#ifndef FUNCTIONS
#define FUNCTIONS

#include "ListaDC.h"
#include "Cola.h"

// Menu Principal
void printMenu();

// Carga de Usuarios
void cargaUsuarios(ListaDC *listaEstudiantes, Cola *colaErrores);

// Carga de Tareas
void cargaTareas();

// Ingreso Manual
void menuManual();
void modificarEstudiante(ListaDC *listaEstudiantes);
void agregarEstudiante(ListaDC *listaEstudiantes);
void eliminarEstudiante(ListaDC *listaEstudiantes);
void menuUsuarios(ListaDC *listaEstudiantes);
void menuTareas();
void ingresoManual(ListaDC *listaEstudiantes);

// Reportes
void menuReportes();
void reportes();

#endif
#ifndef FUNCTIONS
#define FUNCTIONS

#include "ListaDC.h"
#include "ListaDoble.h"
#include "Tarea.h"
#include "Cola.h"

// Menu Principal
void printMenu();

// Carga de Usuarios
void cargaUsuarios(ListaDC *listaEstudiantes, Cola *colaErrores);

// Carga de Tareas
void cargaTareas(ListaDoble *listaTareas, ListaDC *listaEstudiantes, Cola *colaErrores);

// Ingreso Manual
void menuManual();
void modificarEstudiante(ListaDC *listaEstudiantes, Cola *colaErrores);
void agregarEstudiante(ListaDC *listaEstudiantes, Cola *colaErrores);
void eliminarEstudiante(ListaDC *listaEstudiantes);
void menuUsuarios(ListaDC *listaEstudiantes, Cola *colaErrores);
void modificarTarea(ListaDoble *listaTareas, Cola *colaErrores);
void agregarTarea(ListaDoble *listaTareas, Cola *colaErrores);
void eliminarTarea(ListaDoble *listaTareas);
void menuTareas(ListaDoble *listaTareas, Cola *colaErrores);
void ingresoManual(ListaDC *listaEstudiantes, ListaDoble *listaTareas, Cola *colaErrores);

// Reportes
void menuReportes();
void reportes();

#endif
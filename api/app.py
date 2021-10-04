import sys
import os
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
if(sys.path.__contains__(parentDir)):
    pass
else:
    sys.path.append(parentDir)

from flask import Flask, url_for, request, Response, jsonify
from flask_cors import CORS

import json

from TDAs.AVLTree import AVLTree
from TDAs.Estudiante import Estudiante
from TDAs.Tarea import Tarea
from TDAs.Year import Year
from TDAs.Semestre import Semestre
from TDAs.Mes import Mes
from TDAs.SimpleList import SimpleList
from TDAs.BTree import BTree
from TDAs.Curso import Curso
from Analyzer.parser import parser, elementos
from api.functions import cargarArchivo, genGraphAVL, genGraphMatriz, genGraphTareas, genGraphB

app = Flask(__name__)
CORS(app)

estudiantes = AVLTree()
cursosP = BTree()

#Rutas
@app.route('/', methods=['GET'])
def index():
    return "Estas en el index"

@app.route('/carga', methods=['POST'])
def carga():
    data = request.json
    tipo = data['tipo']
    path = data['path']
    file = cargarArchivo(path)
    if file:
        if (tipo == 'estudiante') | (tipo == 'recordatorio'):
            mensaje = file.read()
            parser.parse(mensaje)
            for elemento in elementos:
                if elemento['type'] == 'user':
                    est = Estudiante(int(elemento['carnet']), elemento['dpi'], elemento['nombre'], elemento['carrera'],
                    elemento['correo'], elemento['password'], elemento['creditos'], elemento['edad'])
                    estudiantes.add(est)
                else:
                    est = estudiantes.get(int(elemento['carnet']))
                    if est:
                        fecha = elemento['fecha'].split('/')
                        listaAn = est.getListaA()
                        listaAn.add(Year(int(fecha[2])))
                        year = listaAn.find(int(fecha[2]))
                        mesData = int(fecha[1][1]) if (fecha[1][0] == '0') else int(fecha[1])
                        diaData = int(fecha[0][1]) if (fecha[0][0] == '0') else int(fecha[0])
                        horaData = elemento['hora'].split(':')
                        if mesData <= 6:
                            year.getSemestres().add(Semestre(1))
                        elif mesData >= 7:
                            year.getSemestres().add(Semestre(2))
                        year.getMeses().add(Mes(mesData))
                        mes = year.getMeses().find(mesData)
                        tareasM = mes.getTareas()
                        if not tareasM.get(int(horaData[0]), diaData):
                            listaT = SimpleList()
                            tareasM.add(int(horaData[0]), int(diaData), listaT)
                        task = Tarea(
                            tareasM.get(int(horaData[0]), diaData).getTareas().getSize(), elemento['carnet'], elemento['nombre'],
                            elemento['descripcion'], elemento['materia'],
                            elemento['fecha'], elemento['hora'], elemento['estado']
                        )
                        tareasM.get(int(horaData[0]), diaData).getTareas().add(task)
        else:
            data = json.loads(file.read())
            for estudiante in data['Estudiantes']:
                est = estudiantes.get(int(estudiante['Carnet']))
                years = est.getListaA()
                for y in estudiante['Años']:
                    if years.find(int(y['Año'])) is None:
                        years.add(Year(int(y['Año'])))
                    cy = years.find(int(y['Año']))
                    sems = cy.getSemestres()
                    for sem in y['Semestres']:
                        if not sems.find(int(sem['Semestre'])):
                            sems.add(Semestre(int(sem['Semestre'])))
                        csem = sems.find(int(sem['Semestre'])).getCursos()
                        for item in sem['Cursos']:
                            csem.add(Curso(int(item['Codigo']), item['Nombre'], item['Creditos'], item['Prerequisitos'], item['Obligatorio']))

        file.close()
    return "Carga masiva realizada con éxito!"

@app.route('/reporte', methods=['GET'])
def reporte():
    data = request.json
    if data['tipo'] == 0:
        genGraphAVL(estudiantes)
        return 'Reporte de Estudiantes generado con éxito!'
    elif data['tipo'] == 1:
        est = estudiantes.get(int(data['carnet']))
        year = est.getListaA().find(int(data['año']))
        mes = year.getMeses().find(int(data['mes']))
        genGraphMatriz(mes.getTareas())
        return 'Reporte de Matriz de Tareas generado con éxito!'
    elif data['tipo'] == 2:
        est = estudiantes.get(int(data['carnet']))
        print(est)
        year = est.getListaA().find(int(data['año']))
        mes = year.getMeses().find(int(data['mes']))
        tareas = mes.getTareas().get(data['hora'], data['dia'])
        genGraphTareas(tareas.getTareas())
        return 'Reporte de Lista de Tareas generado con éxito!'
    elif data['tipo'] == 3:
        genGraphB(cursosP, 'Pensum')
        return 'Reporte de Pensum generado con éxito!'
    else:
        est = estudiantes.get(int(data['carnet']))
        year = est.getListaA().find(int(data['año']))
        semestre = year.getSemestres().find(int(data['semestre']))
        genGraphB(semestre.getCursos(), 'Estudiante')
        return f'Reporte de Cursos del estudiante generado con éxito!'

@app.route('/estudiante', methods=['GET', 'POST', 'PUT', 'DELETE'])
def estudiante():
    data = request.json
    if request.method == 'GET':
        print(data['carnet'])
        est = estudiantes.get(int(data['carnet']))
        resp = {
            'carnet': est.getCarnet(), 'DPI': est.getDPI(), 'nombre': est.getNombre(),
            'carrera': est.getCarrera(), 'correo': est.getCorreo(), 'password': est.getPassword(),
            'creditos': est.getCreditos(), 'edad': est.getEdad()
            }
        return jsonify(resp)
    elif request.method == 'POST':
        est = Estudiante(
            int(data['carnet']), data['DPI'], data['nombre'], data['carrera'], data['correo'],
            data['password'], data['creditos'], data['edad']
        )
        estudiantes.add(est)
        return f'Estudiante con carnet: {est.getCarnet()} agregado con éxito!'
    elif request.method == 'PUT':
        est = estudiantes.get(int(data['carnet']))
        est.setDPI(data['DPI'])
        est.setNombre(data['nombre'])
        est.setCarrera(data['carrera'])
        est.setCorreo(data['correo'])
        est.setPassword(data['password'])
        est.setCreditos(data['creditos'])
        est.setEdad(data['edad'])
        return f"Estudiante con carnet: {data['carnet']} actualizado con éxito!"
    else:
        estudiantes.delete(int(data['carnet']))
        return f"Estudiante con carnet: {data['carnet']} eliminado con éxito!"

@app.route('/recordatorios', methods=['GET', 'POST', 'PUT', 'DELETE'])
def recordatorios():
    data = request.json
    est = estudiantes.get(int(data['carnet']))
    fecha = data['fecha'].split('/')
    mesData = int(fecha[1][1]) if (fecha[1][0] == '0') else int(fecha[1])
    diaData = int(fecha[0][1]) if (fecha[0][0] == '0') else int(fecha[0])
    hora = data['hora'].split(':')
    if not est.getListaA().find(int(fecha[2])):
        est.getListaA().add(Year(int(fecha[2])))
    year = est.getListaA().find(int(fecha[2]))
    if mesData <= 6:
        year.getSemestres().add(Semestre(1))
    elif mesData >= 7:
        year.getSemestres().add(Semestre(2))
    if not year.getMeses().find(mesData):
        year.getMeses().add(Mes(mesData))
    mes = year.getMeses().find(mesData)
    tareasM = mes.getTareas()
    if not tareasM.get(int(hora[0]), diaData):
        listaT = SimpleList()
        tareasM.add(int(hora[0]), int(diaData), listaT)
    ltareas = tareasM.get(int(hora[0]), diaData).getTareas()
    if request.method == 'GET':
        tarea = ltareas.get(data['posicion'])
        if tarea:
            resp = {
                'carnet': tarea.getCarnet(), 'nombre': tarea.getNombre(), 'descripcion': tarea.getDescripcion(),
                'materia': tarea.getMateria(), 'fecha': tarea.getFecha(), 'hora': tarea.getHora(), 'estado': tarea.getEstado()
            }
            return jsonify(resp)
        return 'Rescordatorio no encontrado!'
    elif request.method == 'POST':
        task = Tarea (
            ltareas.getSize(), data['carnet'], data['nombre'], data['descripcion'], data['materia'], data['fecha'], 
            data['hora'], data['estado']
        )
        ltareas.add(task)
        return "Recordatorio agregado con éxito!"
    elif request.method == 'PUT':
        tarea = ltareas.get(data['posicion'])
        if tarea:
            tarea.setNombre(data['nombre'])
            tarea.setDescripcion(data['descripcion'])
            tarea.setEstado(data['estado'])
            tarea.setMateria(data['materia'])
            return "Rescordatorio actualizado con éxito!"
        return 'Rescordatorio no encontrado!'
    else:
        tarea = ltareas.get(data['posicion'])
        if tarea:
            ltareas.delete(data['posicion'])
            return "Rescordatorio eliminado con éxito!"
        return 'Rescordatorio no encontrado!'

@app.route('/cursosEstudiante', methods=['POST'])
def cursosEstudiante():
    data = request.json
    path = data['path']
    file = cargarArchivo(path)
    if file:
        data = json.loads(file.read())
        for estudiante in data['Estudiantes']:
            est = estudiantes.get(int(estudiante['Carnet']))
            years = est.getListaA()
            for y in estudiante['Años']:
                if years.find(int(y['Año'])) is None:
                    years.add(Year(int(y['Año'])))
                cy = years.find(int(y['Año']))
                sems = cy.getSemestres()
                for sem in y['Semestres']:
                    if not sems.find(int(sem['Semestre'])):
                        sems.add(Semestre(int(sem['Semestre'])))
                    csem = sems.find(int(sem['Semestre'])).getCursos()
                    for item in sem['Cursos']:
                        csem.add(Curso(int(item['Codigo']), item['Nombre'], item['Creditos'], item['Prerequisitos'], item['Obligatorio']))
        file.close()
    return 'Cursos del estudiante cargados con éxito!'

@app.route('/cursosPensum', methods=['POST'])
def cursosPensum():
    data = request.json
    path = data['path']
    file = cargarArchivo(path)
    if file:
        data = json.loads(file.read())
        for item in data['Cursos']:
            cursosP.add(Curso(int(item['Codigo']), item['Nombre'], item['Creditos'], item['Prerequisitos'], item['Obligatorio']))
        file.close()
    return 'Cursos de Pensum cargados con éxito!'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)
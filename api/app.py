import sys
import os

myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
if sys.path.__contains__(parentDir):
    pass
else:
    sys.path.append(parentDir)

from flask import Flask, url_for, request, Response, jsonify
from flask_cors import CORS
from cryptography.fernet import Fernet

import json
import hashlib

from TDAs.AVLTree import AVLTree
from TDAs.Estudiante import Estudiante
from TDAs.Tarea import Tarea
from TDAs.Year import Year
from TDAs.Semestre import Semestre
from TDAs.Mes import Mes
from TDAs.SimpleList import SimpleList
from TDAs.BTree import BTree
from TDAs.Curso import Curso
from TDAs.Apunte import Apunte
from TDAs.HashTable import HashTable
from TDAs.HashNode import HashNode
from Analyzer.parser import parser, elementos
from api.functions import (
    analizarCurso,
    cargarArchivo,
    genGraphAVL,
    genGraphMatriz,
    genGraphTareas,
    genGraphB,
    genGraphHashTable,
    genStringAVL,
    genStringAVL2,
    genStringBTree,
    genStringGraph,
    genStringHash,
)

app = Flask(__name__)
CORS(app)

estudiantes = AVLTree()
cursosP = BTree()
apuntesTable = HashTable()

# Rutas
@app.route("/", methods=["GET"])
def index():
    return "Estas en el index"


@app.route("/carga", methods=["POST"])
def carga():
    data = request.json
    tipo = data["tipo"]
    path = data["path"]
    file = cargarArchivo(path)
    if file:
        if (tipo == "estudiante") | (tipo == "recordatorio"):
            mensaje = file.read()
            parser.parse(mensaje)
            for elemento in elementos:
                if elemento["type"] == "user":
                    est = Estudiante(
                        int(elemento["carnet"]),
                        elemento["dpi"],
                        elemento["nombre"],
                        elemento["carrera"],
                        elemento["correo"],
                        elemento["password"],
                        elemento["creditos"],
                        elemento["edad"],
                    )
                    estudiantes.add(est)
                else:
                    est = estudiantes.get(int(elemento["carnet"]))
                    if est:
                        fecha = elemento["fecha"].split("/")
                        listaAn = est.getListaA()
                        listaAn.add(Year(int(fecha[2])))
                        year = listaAn.find(int(fecha[2]))
                        mesData = (
                            int(fecha[1][1]) if (fecha[1][0] == "0") else int(fecha[1])
                        )
                        diaData = (
                            int(fecha[0][1]) if (fecha[0][0] == "0") else int(fecha[0])
                        )
                        horaData = elemento["hora"].split(":")
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
                            tareasM.get(int(horaData[0]), diaData)
                            .getTareas()
                            .getSize(),
                            elemento["carnet"],
                            elemento["nombre"],
                            elemento["descripcion"],
                            elemento["materia"],
                            elemento["fecha"],
                            elemento["hora"],
                            elemento["estado"],
                        )
                        tareasM.get(int(horaData[0]), diaData).getTareas().add(task)
        else:
            data = json.loads(file.read())
            for estudiante in data["Estudiantes"]:
                est = estudiantes.get(int(estudiante["Carnet"]))
                years = est.getListaA()
                for y in estudiante["Años"]:
                    if years.find(int(y["Año"])) is None:
                        years.add(Year(int(y["Año"])))
                    cy = years.find(int(y["Año"]))
                    sems = cy.getSemestres()
                    for sem in y["Semestres"]:
                        if not sems.find(int(sem["Semestre"])):
                            sems.add(Semestre(int(sem["Semestre"])))
                        csem = sems.find(int(sem["Semestre"])).getCursos()
                        for item in sem["Cursos"]:
                            csem.add(
                                Curso(
                                    int(item["Codigo"]),
                                    item["Nombre"],
                                    item["Creditos"],
                                    item["Prerequisitos"],
                                    item["Obligatorio"],
                                )
                            )

        file.close()
    return "Carga masiva realizada con éxito!"


@app.route("/reporte", methods=["GET"])
def reporte():
    data = request.json
    if data["tipo"] == 0:
        genGraphAVL(estudiantes)
        return "Reporte de Estudiantes generado con éxito!"
    elif data["tipo"] == 1:
        est = estudiantes.get(int(data["carnet"]))
        year = est.getListaA().find(int(data["año"]))
        mes = year.getMeses().find(int(data["mes"]))
        genGraphMatriz(mes.getTareas())
        return "Reporte de Matriz de Tareas generado con éxito!"
    elif data["tipo"] == 2:
        est = estudiantes.get(int(data["carnet"]))
        year = est.getListaA().find(int(data["año"]))
        mes = year.getMeses().find(int(data["mes"]))
        tareas = mes.getTareas().get(data["hora"], data["dia"])
        genGraphTareas(tareas.getTareas())
        return "Reporte de Lista de Tareas generado con éxito!"
    elif data["tipo"] == 3:
        genGraphB(cursosP, "Pensum")
        return "Reporte de Pensum generado con éxito!"
    else:
        est = estudiantes.get(int(data["carnet"]))
        year = est.getListaA().find(int(data["año"]))
        semestre = year.getSemestres().find(int(data["semestre"]))
        genGraphB(semestre.getCursos(), "Estudiante")
        return f"Reporte de Cursos del estudiante generado con éxito!"


@app.route("/estudiante", methods=["GET", "POST", "PUT", "DELETE"])
def estudiante():
    data = request.json
    if request.method == "GET":
        est = estudiantes.get(int(data["carnet"]))
        resp = {
            "carnet": est.getCarnet(),
            "DPI": est.getDPI(),
            "nombre": est.getNombre(),
            "carrera": est.getCarrera(),
            "correo": est.getCorreo(),
            "password": est.getPassword(),
            "creditos": est.getCreditos(),
            "edad": est.getEdad(),
        }
        return jsonify(resp)
    elif request.method == "POST":
        if estudiantes.key:
            contra = hashlib.sha256(data["password"].encode())
            est = Estudiante(
                int(data["carnet"]),
                Fernet(estudiantes.key).encrypt(str(data["carnet"]).encode()),
                Fernet(estudiantes.key).encrypt(str(data["DPI"]).encode()),
                Fernet(estudiantes.key).encrypt(data["nombre"].encode()),
                data["carrera"],
                Fernet(estudiantes.key).encrypt(data["correo"].encode()),
                Fernet(estudiantes.key).encrypt(contra.hexdigest().encode()),
                str(data["creditos"]),
                Fernet(estudiantes.key).encrypt(str(data["edad"]).encode()),
            )
            estudiantes.add(est)
            return jsonify({"msg": "Estudiante agredado con exito"})
        return jsonify(msg="No hay llave, no se puede guardar la informacion")
    elif request.method == "PUT":
        est = estudiantes.get(int(data["carnet"]))
        est.setDPI(data["DPI"])
        est.setNombre(data["nombre"])
        est.setCarrera(data["carrera"])
        est.setCorreo(data["correo"])
        est.setPassword(data["password"])
        est.setCreditos(data["creditos"])
        est.setEdad(data["edad"])
        return f"Estudiante con carnet: {data['carnet']} actualizado con éxito!"
    else:
        estudiantes.delete(int(data["carnet"]))
        return f"Estudiante con carnet: {data['carnet']} eliminado con éxito!"


@app.route("/recordatorios", methods=["GET", "POST", "PUT", "DELETE"])
def recordatorios():
    data = request.json
    est = estudiantes.get(int(data["carnet"]))
    fecha = data["fecha"].split("/")
    mesData = int(fecha[1][1]) if (fecha[1][0] == "0") else int(fecha[1])
    diaData = int(fecha[0][1]) if (fecha[0][0] == "0") else int(fecha[0])
    hora = data["hora"].split(":")
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
    if request.method == "GET":
        tarea = ltareas.get(data["posicion"])
        if tarea:
            resp = {
                "carnet": tarea.getCarnet(),
                "nombre": tarea.getNombre(),
                "descripcion": tarea.getDescripcion(),
                "materia": tarea.getMateria(),
                "fecha": tarea.getFecha(),
                "hora": tarea.getHora(),
                "estado": tarea.getEstado(),
            }
            return jsonify(resp)
        return "Rescordatorio no encontrado!"
    elif request.method == "POST":
        task = Tarea(
            ltareas.getSize(),
            data["carnet"],
            data["nombre"],
            data["descripcion"],
            data["materia"],
            data["fecha"],
            data["hora"],
            data["estado"],
        )
        ltareas.add(task)
        return "Recordatorio agregado con éxito!"
    elif request.method == "PUT":
        tarea = ltareas.get(data["posicion"])
        if tarea:
            tarea.setNombre(data["nombre"])
            tarea.setDescripcion(data["descripcion"])
            tarea.setEstado(data["estado"])
            tarea.setMateria(data["materia"])
            return "Rescordatorio actualizado con éxito!"
        return "Rescordatorio no encontrado!"
    else:
        tarea = ltareas.get(data["posicion"])
        if tarea:
            ltareas.delete(data["posicion"])
            return "Rescordatorio eliminado con éxito!"
        return "Rescordatorio no encontrado!"


@app.route("/cursosEstudiante", methods=["POST"])
def cursosEstudiante():
    data = request.json
    for estudiante in data["Estudiantes"]:
        est = estudiantes.get(int(estudiante["Carnet"]))
        years = est.getListaA()
        for y in estudiante["Años"]:
            if years.find(int(y["Año"])) is None:
                years.add(Year(int(y["Año"])))
            cy = years.find(int(y["Año"]))
            sems = cy.getSemestres()
            for sem in y["Semestres"]:
                if not sems.find(int(sem["Semestre"])):
                    sems.add(Semestre(int(sem["Semestre"])))
                csem = sems.find(int(sem["Semestre"])).getCursos()
                for item in sem["Cursos"]:
                    csem.add(
                        Curso(
                            int(item["Codigo"]),
                            item["Nombre"],
                            item["Creditos"],
                            item["Prerequisitos"],
                            item["Obligatorio"],
                        )
                    )
    return jsonify(msg="Cursos del estudiante cargados con éxito!")


@app.route("/cursosPensum", methods=["POST"])
def cursosPensum():
    data = request.json
    for curso in data["Cursos"]:
        cursosP.add(
            Curso(
                int(curso["Codigo"]),
                curso["Nombre"],
                curso["Creditos"],
                curso["Prerequisitos"],
                curso["Obligatorio"],
            )
        )
    return jsonify(msg="Cursos de Pensum cargados con éxito!")


@app.route("/adminKey", methods=["GET"])
def getAdminKey():
    if not estudiantes.key:
        key = Fernet.generate_key()
        estudiantes.key = key
        return jsonify({"adminKey": key.decode()})
    return jsonify({"adminKey": estudiantes.key.decode()})


@app.route("/user/<string:carnet>/<string:password>", methods=["GET"])
def user(carnet, password):
    est = estudiantes.get(int(carnet))
    contrain = hashlib.sha256(password.encode()).hexdigest()
    contra = Fernet(estudiantes.key).decrypt(est.getPassword()).decode()
    if est:
        if contrain == contra:
            return jsonify(
                msg="log",
                carnet=Fernet(estudiantes.key).decrypt(est.getCarnet()).decode(),
                DPI=Fernet(estudiantes.key).decrypt(est.getDPI()).decode(),
                nombre=Fernet(estudiantes.key).decrypt(est.getNombre()).decode(),
                carrera=est.getCarrera(),
                correo=Fernet(estudiantes.key).decrypt(est.getCorreo()).decode(),
                password=Fernet(estudiantes.key).decrypt(est.getPassword()).decode(),
                creditos=est.getCreditos(),
                edad=Fernet(estudiantes.key).decrypt(est.getEdad()).decode(),
            )
        return jsonify(msg="Contraseña incorrecta!")
    return jsonify(msg="El estudiante no exite!")


@app.route("/users", methods=["POST"])
def users():
    data = request.json
    for estudiante in data["estudiantes"]:
        if estudiantes.key:
            contra = hashlib.sha256(estudiante["password"].encode())
            est = Estudiante(
                int(estudiante["carnet"]),
                Fernet(estudiantes.key).encrypt(str(estudiante["carnet"]).encode()),
                Fernet(estudiantes.key).encrypt(str(estudiante["DPI"]).encode()),
                Fernet(estudiantes.key).encrypt(estudiante["nombre"].encode()),
                estudiante["carrera"],
                Fernet(estudiantes.key).encrypt(estudiante["correo"].encode()),
                Fernet(estudiantes.key).encrypt(contra.hexdigest().encode()),
                str(estudiante["creditos"]),
                Fernet(estudiantes.key).encrypt(str(estudiante["edad"]).encode()),
            )
            estudiantes.add(est)
    if estudiantes.key:
        return jsonify(msg="Estudiantes agregados con exito!")
    return jsonify(
        msg="No se pudieron agregar los estudiantes no se ha generado aun clave de seguridad!"
    )


@app.route("/apuntes", methods=["POST"])
def apuntes():
    data = request.json
    for user in data["usuarios"]:
        apunteNode = HashNode(int(user["carnet"]))
        for i, apunte in enumerate(user["apuntes"]):
            apunteNode.addNote(
                Apunte(i, user["carnet"], apunte["titulo"], apunte["contenido"])
            )
        apuntesTable.insert(apunteNode)
    return jsonify(msg="Apuntes cargados con éxito!")


@app.route("/apuntes_usuario/<string:carnet>", methods=["GET", "POST"])
def apuntes_usuario(carnet):
    if request.method == "POST":
        data = request.json
        notes = apuntesTable.find(int(carnet))
        if not notes:
            apunteNode = HashNode(int(carnet))
            apunteNode.addNote(
                Apunte(
                    apunteNode.getNotesSize(),
                    int(carnet),
                    data["titulo"],
                    data["contenido"],
                )
            )
            apuntesTable.insert(apunteNode)
        else:
            notes.addNote(
                Apunte(
                    notes.getNotesSize() + 1,
                    int(carnet),
                    data["titulo"],
                    data["contenido"],
                )
            )
        return jsonify(msg="Apunte agregado con éxito!")
    else:
        notes = apuntesTable.find(int(carnet))
        resp = []
        for i in range(notes.getNotes().getSize()):
            resp.append(
                {
                    "ID": notes.getNotes().get(i).data,
                    "Titulo": notes.getNotes().get(i).titulo,
                    "Contenido": notes.getNotes().get(i).contenido,
                }
            )
        return jsonify({"apuntes": resp})


@app.route("/redcursos/<string:codigo>", methods=["GET"])
def redcursos(codigo):
    codigoCurso = int(codigo)
    tablaAdy = list()
    curso = cursosP.get(codigoCurso)
    analizarCurso(tablaAdy, curso, cursosP)
    cadena = genStringGraph(tablaAdy)
    return jsonify(dotSrc=cadena)


@app.route("/asignarcurso/<string:carnet>/<string:codigo>", methods=["GET"])
def asignarcurso(carnet, codigo):
    codigoCurso = int(codigo)
    curso = cursosP.get(codigoCurso)
    est = estudiantes.get(int(carnet))
    years = est.getListaA()
    if years.find(2021) is None:
        years.add(Year(2021))
    cy = years.find(2021)
    sems = cy.getSemestres()
    if sems.find(2) is None:
        sems.add(Semestre(2))
    csem = sems.find(2).getCursos()
    csem.add(curso)
    return jsonify(msg=f"Curso con codigo: {codigo}, asignado con exito a: {carnet}")


@app.route(
    "/cursos/ver/<string:carnet>/<string:year>/<string:semestre>", methods=["GET"]
)
def vercursos(carnet, year, semestre):
    est = estudiantes.get(int(carnet))
    anio = est.getListaA().find(int(year))
    sems = anio.getSemestres().find(int(semestre))
    cadena = genStringBTree(sems.getCursos())
    return jsonify(dotSrc=cadena)

@app.route("/redcurriculum/", methods=['GET'])
def redcurriculum():
    tablaAdy = list()
    cursosP.toListaAdy(tablaAdy)
    cadena = genStringGraph(tablaAdy)
    return jsonify(dotSrc=cadena)

@app.route("/reporteapuntes/", methods=['GET'])
def reporteapuntes():
    cadena = genStringHash(apuntesTable)
    return jsonify(dotSrc=cadena)

@app.route("/reporteavl1/", methods=['GET'])
def reporteavl1():
    cadena = genStringAVL(estudiantes)
    return jsonify(dotSrc=cadena)

@app.route("/reporteavl2/", methods=['GET'])
def reporteavl2():
    cadena = genStringAVL2(estudiantes)
    return jsonify(dotSrc=cadena)

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)

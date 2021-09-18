from typing import DefaultDict
from flask import Flask, url_for, request, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Rutas
@app.route('/', methods=['GET'])
def index():
    return "Estas en el index"

@app.route('/carga', methods=['POST'])
def carga():
    return "Carga Masiva"

@app.route('/reporte', methods=['GET'])
def reporte():
    return 'Reporte'

@app.route('/estudiante/', methods=['POST'], defaults={'carnet':None})
@app.route('/estudiante/<string:carnet>', methods=['GET', 'PUT', 'DELETE'])
def estudiante(carnet):
    if request.method == 'GET':
        return f"Obteniedo estudiante con carnet: {carnet}"
    elif request.method == 'POST':
        return f"Ingresando estudiante"
    elif request.method == 'PUT':
        return f"Actualizando estudiante con carnet: {carnet}"
    else:
        return f"Eliminando estudiante con carnet: {carnet}"

@app.route('/recordatorios', methods=['GET', 'POST', 'PUT', 'DELETE'])
def recordatorios():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    else:
        pass

@app.route('/cursosEstudiante', methods=['POST'])
def cursosEstudiante():
    pass

@app.route('/cursosPensum', methods=['POST'])
def cursosPensum():
    pass

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)

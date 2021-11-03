import os

def cargarArchivo(filename):
    if filename != "":
        file = open(filename, "r", encoding="utf-8")
    else:
        file = None
    return file

def genGraphYears(years):
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph anios {\npad=0.35\n")
    f.write('rankdir="LR"\nbgcolor = "#c7f9cc";\nfontcolor = "#22577a";\nlabelloc=t;\nlabel = "Años";\nedge[color="#22577a"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="folder" color="#22577a" fillcolor="#80ed99" style="filled" fontcolor = "#22577a" fontname = "Arial"]')
    for i in range(years.getSize()):
        year = years.get(i)
        if i == 0:
            f.write(f"\nnodo{i} -> nodo{i+1}")
        elif i == years.getSize() - 1:
            f.write(f"\nnodo{i} -> nodo{i-1}")
        else:
            f.write(f"\nnodo{i} -> nodo{i+1}")
            f.write(f"\nnodo{i} -> nodo{i-1}")
        f.write(f'\nnodo{i}[label="Año: {year.getData()}\\nSemestres *\\nMeses *"]')
    f.write("\n}")
    f.close()
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/Years.svg")
    print("\n> Grafico de años generado exitosamente!")

def genGraphMeses(meses):
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph meses {\npad=0.35\n")
    f.write('rankdir="LR"\nbgcolor = "#ff9b54";\nfontcolor = "#4f000b";\nlabelloc=t;\nlabel = "Meses";\nedge[color="#720026"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="component" color="#720026" fillcolor="#ce4257" style="filled" fontcolor = "#4f000b" fontname = "Arial"]')
    for i in range(meses.getSize()):
        mes = meses.get(i)
        if i == 0:
            f.write(f"\nnodo{i} -> nodo{i+1}")
        elif i == meses.getSize() - 1:
            f.write(f"\nnodo{i} -> nodo{i-1}")
        else:
            f.write(f"\nnodo{i} -> nodo{i+1}")
            f.write(f"\nnodo{i} -> nodo{i-1}")
        f.write(f'\nnodo{i}[label="Mes: {mes.getData()}\\nTareas *"]')
    f.write("\n}")
    f.close()
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/Meses.svg")
    print("\n> Grafico de meses generado exitosamente!")

def genGraphSemestres(semestres):
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph semestres {\npad=0.35\n")
    f.write('rankdir="LR"\nbgcolor = "#ffe66d";\nfontcolor = "#1a535c";\nlabelloc=t;\nlabel = "Semestres";\nedge[color="#1a535c"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="tab" color="#1a535c" fillcolor="#4ecdc4" style="filled" fontcolor = "#1a535c" fontname = "Arial"]')
    for i in range(semestres.getSize()):
        semestre = semestres.get(i)
        if i == semestres.getSize() - 1:
            f.write(f'\nnodo{i}[label="Semestre: {semestre.getData()}\\nCursos *"]')
        else:
            f.write(f"\nnodo{i} -> nodo{i+1}")
            f.write(f'\nnodo{i}[label="Semestre: {semestre.getData()}\\nCursos *"]')
    f.write("\n}")
    f.close()
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/Semestres.svg")
    print("\n> Grafico de semestres generado exitosamente!")

def genGraphTareas(tareas):
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph tareas {\npad=0.35\n")
    f.write('rankdir="LR"\nbgcolor = "#75dddd";\nfontcolor = "#172a3a";\nlabelloc=t;\nlabel = "Tareas";\nedge[color="#004346"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="note" color="#004346" fillcolor="#09bc8a" style="filled" fontcolor = "#172a3a" fontname = "Arial"]')
    for i in range(tareas.getSize()):
        tarea = tareas.get(i)
        if i == tareas.getSize() - 1:
            f.write(f'\nnodo{i}[label="ID: {tarea.getId()}\\nCarnet: {tarea.getCarnet()}\\nNombre: {tarea.getNombre()}')
            f.write(f'\\nDescripción: {tarea.getDescripcion()}\\nMateria: {tarea.getMateria()}\\nFecha: {tarea.getFecha()}')
            f.write(f'\\nHora: {tarea.getHora()}\\nEstado: {tarea.getEstado()}"]')
        else:
            f.write(f"\nnodo{i} -> nodo{i+1}")
            f.write(f'\nnodo{i}[label="ID: {tarea.getId()}\\nCarnet: {tarea.getCarnet()}\\nNombre: {tarea.getNombre()}')
            f.write(f'\\nDescripción: {tarea.getDescripcion()}\\nMateria: {tarea.getMateria()}\\nFecha: {tarea.getFecha()}')
            f.write(f'\\nHora: {tarea.getHora()}\\nEstado: {tarea.getEstado()}"]')
    f.write("\n}")
    f.close()
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/Tareas.svg")
    print("\n> Grafico de tareas generado exitosamente!")

def genGraphMatriz(matriz):
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph tareas {\npad=0.35\n")
    f.write('splines=false;\nbgcolor = "#b7efc5";\nfontcolor = "#10451d";\nlabelloc=t;\nlabel = "Tareas";\nedge[color="#10451d"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="box3d" width = 1.5 color="#10451d" fillcolor="#4ad66d" style="filled" fontcolor = "#10451d" fontname = "Arial"]')
    #Encabezados dias (columnas)
    for j in range(matriz.dias.getSize()):
        dia = matriz.dias.get(j)
        if j == 0:
            if matriz.dias.get(j+1):
                f.write(f"\nnodoC{j} -> nodoC{j+1}")
            else:
                f.write(f"\nnodoC{j}")
        elif j == matriz.dias.getSize() - 1:
            f.write(f"\nnodoC{j} -> nodoC{j-1}")
        else:
            f.write(f"\nnodoC{j} -> nodoC{j+1}")
            f.write(f"\nnodoC{j} -> nodoC{j-1}")
        f.write(f'\nnodoC{j} -> nodo{dia.getAccessNode().getRow()}_{dia.getAccessNode().getColumn()}')
        f.write(f'\nnodoC{j}[label="Día: {dia.getData()}" width = 1.5 color="#f25c54" fillcolor="#f7b267" style="filled" shape="rect" pos="{(j+1)*2},0!"]')
    #Encabezados horas (filas)
    for i in range(matriz.horas.getSize()):
        horaV = matriz.horas.get(i).getData()
        hora = matriz.horas.get(i)
        if i == 0:
            if matriz.horas.get(i+1):
                f.write(f"\nnodoF{i} -> nodoF{i+1}")
            else:
                f.write(f"\nnodoF{i}")
        elif i == matriz.horas.getSize() - 1:
            f.write(f"\nnodoF{i} -> nodoF{i-1}")
        else:
            f.write(f"\nnodoF{i} -> nodoF{i-1}")
            f.write(f"\nnodoF{i} -> nodoF{i+1}")
        f.write(f'\nnodoF{i} -> nodo{hora.getAccessNode().getRow()}_{hora.getAccessNode().getColumn()}')
        f.write(f'\nnodoF{i}[label="Hora: {hora.getData()}" width = 1.5 color="#f25c54" fillcolor="#f7b267" style="filled" shape="rect" pos="0,{(i*-1)-1}!"]')
        for j in range(matriz.dias.getSize()):
            diaV = matriz.dias.get(j).getData()
            tareas = matriz.get(horaV, diaV)
            if tareas is not None:
                if (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#1
                    pass
                elif (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#2
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                elif (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#3
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                elif (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is not None):#4
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#5
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#6  
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#7
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is not None) & (tareas.getPrev() is not None):#8
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#9
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#10
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#11
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is not None):#12
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#13
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#14  
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is not None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#15
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                else:
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()};')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()};')
                f.write(f'\nnodo{horaV}_{diaV}[label = "{tareas.getTareas().getSize()}" pos="{(j+1)*2}, {(i*-1)-1}!"]')
    f.write('\n}')
    f.close()
    os.system(f"neato -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/MatrizTareas.svg")
    print("\n> Grafico de matriz generado exitosamente!")

def genGraphAVL(AVLtree):
    cadenas = []
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph avltree {\npad=0.35\n")
    f.write('rankdir="TB"\nbgcolor = "#ff9e00";\nfontcolor = "#240046";\nlabelloc=t;\nlabel = "Árbol AVL Estudiantes";\nedge[color="#240046"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="record" color="#240046" fillcolor="#9d4edd" style="filled" fontcolor = "#240046" fontname = "Arial"]')
    AVLtree.toGviz(cadenas)
    for cadena in cadenas:
        f.write(cadena)
    f.write("\n}")
    f.close()
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/AvlEstudiantes.svg")
    print("\n> Grafico de arbol AVL generado exitosamente!")

def genGraphB(Btree, tipo):
    cadenas = []
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph btree {\npad=0.35\n")
    f.write('rankdir="TB"\nbgcolor = "#ffb3ae";\nfontcolor = "#0e606b";\nlabelloc=t;\nlabel = "Árbol B Cursos";\nedge[color="#0e606b"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="record" color="#0e606b" fillcolor="#f47068" style="filled" fontcolor = "#0e606b" fontname = "Arial"]')
    Btree.toGviz(cadenas)
    for cadena in cadenas:
        f.write(cadena)
    f.write("\n}")
    f.close()
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/{tipo}_btree.svg")
    print("\n> Grafico de arbol B generado exitosamente!")

def genGraphHashTable(hashtable):
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph hashtable {\npad=0.35\n")
    f.write('rankdir="TB"\nbgcolor = "#edf6f9";\nfontcolor = "#0e606b";\nlabelloc=t;\nlabel = "Tabla Hash";\nedge[color="#0e606b"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="record" color="#e29578" fillcolor="#ffddd2" style="filled" fontcolor = "#e29578" fontname = "Arial"]')
    for i, key in enumerate(hashtable.keys):
        f.write(f'\nnodoK{i}[label="{key.getData()}" width = 1.5 height = 1 pos="0, {i*-1}!"]')
        if key.getData() != -1:
            f.write(f'\nnodoK{i} -> nodo{i}{0}')
            for j in range(key.getNotes().getSize()):
                apunte = key.getNotes().get(j)
                if j != key.getNotes().getSize() - 1:
                    f.write(f'\nnodo{i}{j}->nodo{i}{j+1}')
                f.write(f'\nnodo{i}{j}[label="Titulo: {apunte.titulo}" pos="{(j+1)*4}, {i*-1}!" height = 0.75 ')
                f.write(f'shape="oval" color="#006d77" fillcolor="#83c5be" fontcolor="#006d77"]')
            
    f.write("\n}")
    f.close()
    os.system(f"neato -Nfontname=Arial -Tsvg archivo.dot -o Reportes_F2/hashtable.svg")
    print("\n> Grafico de Tabla Hash generado exitosamente!")

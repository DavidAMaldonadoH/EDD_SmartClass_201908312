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
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Img/years.svg")
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
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Img/meses.svg")
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
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Img/semestres.svg")
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
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Img/tareas.svg")
    print("\n> Grafico de tareas generado exitosamente!")

def genGraphMatriz(matriz):
    f = open("archivo.dot", "w", encoding="utf-8")
    f.write("digraph tareas {\npad=0.35\n")
    f.write('splines=false;\nbgcolor = "#b7efc5";\nfontcolor = "#10451d";\nlabelloc=t;\nlabel = "Tareas";\nedge[color="#10451d"];')
    f.write('\nfontname = "Arial";\nfontsize = "24.0";')
    f.write('\nnode[shape="box3d" width = 1.5 color="#10451d" fillcolor="#4ad66d" style="filled" fontcolor = "#10451d" fontname = "Arial"]')
    f.write('\nMt[ label = "Matrix" width = 1.5 color="#0d47a1" fillcolor="#42a5f5" style="filled" shape="rect" group=1]')
    #Encabezados dias (columnas)
    columna = 'Mt'
    for j in range(matriz.dias.getSize()):
        dia = matriz.dias.get(j)
        if j == 0:
            f.write(f"\nnodoC{j} -> nodoC{j+1} [constraint=false]")
        elif j == matriz.dias.getSize() - 1:
            f.write(f"\nnodoC{j} -> nodoC{j-1} [constraint=false]")
        else:
            f.write(f"\nnodoC{j} -> nodoC{j+1} [constraint=false]")
            f.write(f"\nnodoC{j} -> nodoC{j-1} [constraint=false]")
        f.write(f'\nnodoC{j} -> nodo{dia.getAccessNode().getRow()}_{dia.getAccessNode().getColumn()}')
        f.write(f'\nnodoC{j}[label="Día: {dia.getData()}" width = 1.5 color="#f25c54" fillcolor="#f7b267" style="filled" shape="rect" group={2+j}]')
        columna+=f' -> nodoC{j}'
    f.write('\nrank = same { ' + columna +' [style = invis]} ')
    #Encabezados horas (filas)
    for i in range(matriz.horas.getSize()):
        horaV = matriz.horas.get(i).getData()
        hora = matriz.horas.get(i)
        if i == 0:
            f.write(f"\nnodoF{i} -> nodoF{i+1}")
        elif i == matriz.horas.getSize() - 1:
            f.write(f"\nnodoF{i} -> nodoF{i-1}")
        else:
            f.write(f"\nnodoF{i} -> nodoF{i-1}")
            f.write(f"\nnodoF{i} -> nodoF{i+1}")
        f.write(f'\nnodoF{i} -> nodo{hora.getAccessNode().getRow()}_{hora.getAccessNode().getColumn()} [constraint=false];')
        f.write(f'\nnodoF{i}[label="Hora: {hora.getData()}" width = 1.5 color="#f25c54" fillcolor="#f7b267" style="filled" shape="rect" group=1]')
        fila = f'nodoF{i}'
        for j in range(matriz.dias.getSize()):
            diaV = matriz.dias.get(j).getData()
            tareas = matriz.get(horaV, diaV)
            if tareas is not None:
                if (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#1
                    pass
                elif (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#2
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                elif (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#3
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                elif (tareas.getTop() is None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is not None):#4
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#5
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#6  
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#7
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                elif (tareas.getTop() is None) & (tareas.getBottom() is not None) & (tareas.getNext() is not None) & (tareas.getPrev() is not None):#8
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#9
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#10
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#11
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is None) & (tareas.getNext() is not None) & (tareas.getPrev() is not None):#12
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is None):#13
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is not None) & (tareas.getNext() is None) & (tareas.getPrev() is not None):#14  
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                elif (tareas.getTop() is not None) & (tareas.getBottom() is not None) & (tareas.getNext() is not None) & (tareas.getPrev() is None):#15
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                else:
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getTop().getRow()}_{tareas.getTop().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getBottom().getRow()}_{tareas.getBottom().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getNext().getRow()}_{tareas.getNext().getColumn()} [constraint=false];')
                    f.write(f'\nnodo{horaV}_{diaV} -> nodo{tareas.getPrev().getRow()}_{tareas.getPrev().getColumn()} [constraint=false];')
                f.write(f'\nnodo{horaV}_{diaV}[label = "{tareas.getTareas()}" group={2+j}]')
                fila+=f' -> nodo{horaV}_{diaV}'
        f.write('\nrank = same{ ' + fila +' [style=invis] }')
    f.write('\nMt -> nodoF0;\nMt -> nodoC0;')
    f.write('\n}')
    f.close()
    os.system(f"dot -Nfontname=Arial -Tsvg archivo.dot -o Img/matriz.svg")
    print("\n> Grafico de matriz generado exitosamente!")
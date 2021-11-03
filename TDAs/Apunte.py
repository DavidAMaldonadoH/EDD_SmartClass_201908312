from TDAs.SimpleNode import SimpleNode


class Apunte(SimpleNode):
    def __init__(self, data, carnet, titulo, contenido):
        super().__init__(data)
        self.carnet = carnet
        self.titulo = titulo
        self.contenido = contenido

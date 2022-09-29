class proyecto:
    def __init__(self, nombre_usuario="", repositorio="", fecha="", leng="", likes=float(0), tags=(), url=""):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.fecha_actualizacion = fecha
        self.lenguaje = leng
        self.likes = likes
        self.tags = tags
        self.url = url


def to_string(software):
    res = "Nombre de usuario: "+str(software.nombre_usuario)+" | Repositorio: "+str(software.repositorio) +\
          " | Fecha de actualizacion: "+software.fecha_actualizacion+" | Lenguaje: "+software.lenguaje +\
          " | Likes: "+str(software.likes)+"K"+" | Tags: "+str(software.tags)+" | URL: "+str(software.url)

    return res



class Software:
    def __init__(self, nombre_usuario="", repositorio="", descripcion="", fecha="", leng="", likes="", tags=(), url=""):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.descripcion = descripcion
        self.fecha_actualizacion = fecha
        self.lenguaje = leng
        self.likes = likes
        self.tags = tags
        self.url = url


def to_string(software):
    res = "Nombre de usuario: "+str(software.nombre_usuario)+" | Repositorio: "+str(software.repositorio) +\
          " | Descripcion: "+software.descripcion +\
          " | Fecha de actualizacion: "+software.fecha_actualizacion+" | Lenguaje: "+software.lenguaje +\
          " | Likes: "+str(software.likes) + " | Tags: "+str(software.tags)+" | URL: "+str(software.url)

    return res


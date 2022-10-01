class Proyecto:
    def __init__(self, nombre_usuario="", repositorio="", fecha="", leng="", likes=float(0), tags=(), url=""):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.fecha_actualizacion = fecha
        self.lenguaje = leng
        self.likes = likes
        self.tags = tags
        self.url = url


class Resumen:
    def __init__(self, mes, estrellas, cantidad):
        self.mes = mes
        self.estrellas = estrellas
        self.cantidad = cantidad


def to_string(software):
    res = "Nombre de usuario: "+str(software.nombre_usuario)+" | Repositorio: "+str(software.repositorio) +\
          " | Fecha de actualizacion: "+str(software.fecha_actualizacion)+" | Lenguaje: "+str(software.lenguaje) +\
          " | Likes: "+str(software.likes)+"K"+" | Tags: "+str(software.tags)+" | URL: "+str(software.url)

    return res


def conver_estrellas(software):
    rangos = (0, 10, 20, 30, 40)
    estrellas = 0
    for i in range(len(rangos)):
        if software.likes > 40:
            estrellas = 5
            break
        if software.likes <= rangos[i] and software.likes > rangos[i-1]:
            estrellas = i

    return estrellas


def to_string_acotado(software):
    estrellas = conver_estrellas(software)
    res = "Repositorio: "+str(software.repositorio) +\
          " | Fecha de actualizacion: "+software.fecha_actualizacion+" | Estrellas: "+str(estrellas)

    return res

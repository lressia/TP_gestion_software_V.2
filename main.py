from clase import*
import os.path
import pickle
#FUNCIONES BASICAS


#Carga y extencion de arrenglo de n registros
def carga(v):
    if not os.path.exists("proyectos.csv"):
        print("No existe un archivo a procesar\n")
    else:
        m = open("proyectos.csv", "rt", encoding="utf8")
        largo = os.path.getsize("proyectos.csv")
        primera_linea = False
        while m.tell() < largo:
            proyecto = pickle.load(m)
            if primera_linea:
                # nombre_us = proyecto.nombre_usuario
                # repositorio = proyecto.repositorio
                # descripcion = proyecto.descripcion
                # fecha = proyecto.fecha_actualizacion
                # lenguaje = proyecto.lenguaje
                # likes = proyecto.likes
                # tags = proyecto.tags
                # url = proyecto.url
                # sof = Software(nombre_us, repositorio, descripcion, fecha, lenguaje, likes, tags, url)
                # v.append(proyecto.split("|"))
                sof = Software(proyecto.split("|"))
                v.append(sof)
            else:
                primera_linea = True


#Mostrar el menu de opciones y validar la seleccion de una opcion
def menu():
    print()
    print("PROGRAMA GESTOR DE PROYECTOS DE SOFTWARE\n")
    print("1 - cargar proyectos\n2 - filtrar por tag\n3 - resumen por lenguaje\n4 - popularidad\n\
    5 - buscar proyecto y actualizarlo\n6 - guardar populares\n7 - mostrar archivo\n0 - salir del programa\n")
    print("ingrese una de las opciones")
    seleccion = validate()
    print()
    while seleccion < 0 or seleccion > 7:
        print("debe ingresar una opcion valida")
        seleccion = validate()
    return seleccion


#Gestionar el programa
def principal():
    s = None
    registros = []
    while s != 0:
        s = menu()
        if s == 1:
            carga(registros)
        else:
            if s == 2:
                mostrar(registros)
            elif s == 3:
                pass
            elif s == 4:
                pass
            elif s == 5:
                pass
            elif s == 6:
                pass
            elif s == 7:
                pass
        if s == 0:
            print("hasta luego")


if __name__ == '__main__':
    principal()

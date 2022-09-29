from clase import*
import os.path


#Carga y extencion de arrenglo de n registros
def carga(v):
    if not os.path.exists("proyectos.csv"):
        print("No existe un archivo a procesar\n")
    else:
        m = open("proyectos.csv", "rt", encoding="utf8")
        largo = os.path.getsize("proyectos.csv")
        repetidos = []
        deleteados = 0
        cargados = 0
        primera_linea = False
        while m.tell() < largo:
            atr = m.readline()
            atr = atr.split("|")
            if primera_linea:
                if not atr == "" and not atr[4] == "":
                    if not atr[1] in repetidos:
                        crear_registro(atr, v)
                        repetidos.append(atr[1])
                        cargados += 1
                    else:
                        deleteados += 1
                else:
                    deleteados += 1
            else:
                primera_linea = True
        m.close()


def crear_registro(lista, v):
    nombre_us = lista[0]
    repositorio = lista[1]
    fecha = lista[3]
    lenguaje = lista[4]

    li = lista[5].split("k")
    likes = float(li[0])

    tags = lista[6]
    url = lista[7]
    sof = proyecto(nombre_us, repositorio, fecha, lenguaje, likes, tags, url)
    v.append(sof)


def mostrar(v):
    for i in range(len(v)):
        print(to_string(v[i]))


#Validar numero positivo
def validate():
    n = int(input('llene el campo: '))
    print()
    while n <= 0:
        print("no se permiten numeros negativos")
        n = int(input('llene el campo: '))
        print()
    return n


#Mostrar el menu de opciones y validar la seleccion de una opcion
def menu():
    print()
    print("PROGRAMA GESTOR DE PROYECTOS DE SOFTWARE\n")
    print("1 - cargar proyectos\n2 - filtrar por tag\n3 - resumen por lenguaje\n4 - popularidad\n" +\
          "5 - buscar proyecto y actualizarlo\n6 - guardar populares\n7 - mostrar archivo\n0 - salir del programa\n")
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



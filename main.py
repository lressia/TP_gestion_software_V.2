from clase import*
import os.path
import datetime


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
        print("cantidad de elementos cargados: "+str(cargados))
        print("cantidad de elementos eliminado: "+str(deleteados))


def crear_registro(lista, v):
    nombre_us = lista[0]
    repositorio = lista[1]
    fecha = lista[3]
    lenguaje = lista[4]

    li = lista[5].split("k")
    likes = float(li[0])

    tags = lista[6]
    url = lista[7]
    sof = Proyecto(nombre_us, repositorio, fecha, lenguaje, likes, tags, url)
    add_in_order(v, sof)


def mostrar(v):
    for i in range(len(v)):
        print(to_string(v[i]))


def mostrar_acotados(v):
    for i in range(len(v)):
        print(to_string_acotado(v[i]))


def validate():
    n = int(input('llene el campo: '))
    print()
    while n <= 0:
        print("no se permiten numeros negativos")
        n = int(input('llene el campo: '))
        print()
    return n


def add_in_order(vec, reg):
    n = len(vec)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].repositorio == reg.repositorio:
            pos = c
            break
        if reg.repositorio < vec[c].repositorio:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def buscar_tag(v, cad):
    encontrados = []
    for i in v:
        lista = i.tags.split(",")
        for j in lista:
            if j == cad:
                encontrados.append(i)
                break
    return encontrados


def busqueda_bin(vec, ref):
    n = len(vec)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].repositorio == ref:
            print("Se encontro el proyecto")
            print(to_string(vec[c]))
            return c
        if ref < vec[c].repositorio:
            der = c - 1
        else:
            izq = c + 1
    print("No se encontro ningun proyecto con el repositorio ", ref)


def act_url_fecha(vec, pos):
    url = input("Ingrese una nueva url para este proyecto\n")
    vec[pos].url, vec[pos].fecha_actualizacion = url, str(datetime.datetime.utcnow()).split(" ")[0]
    print(to_string(vec[pos]))


def crear_archivo(v):
    if len(v) == 0:
        print('Disculpa, no se encontraron datos guardados. Ingrese datos o comuníquese con su administrador')
        return
    m = open('filtrados.csv', 'w')
    linea_1 = "nombre_usuario|repositorio|fecha_actualizacion|lenguaje|estrellas|tags|url"
    m.write(linea_1)
    for proyecto in v:
        m.write(to_string(proyecto))
    m.close()


def to_month(reg):
    fecha = reg.fecha_actualizacion.split("-")
    mes = int(fecha[1])
    return mes


def generar_matriz(v):
    filas, columnas = 12, 5
    matrix = [[0] * columnas for i in range(filas)]
    for i in v:
        mes = to_month(i)
        estrellas = conver_estrellas(i)
        matrix[mes-1][estrellas-1] += 1

    return matrix


def mostrar_matriz(matriz):
    mes = 0
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
             "Octubre", "Noviembre", "Diciembre")
    print("{:<13}".format("Estrellas")+"1   "+"2   "+"3   "+"4   "+"5   ")
    print("-"*32)
    for i in matriz:
        print("{:<11}".format(meses[mes])+"| "+"{:<4}".format(i[0])+"{:<4}".format(i[1])+"{:<4}".format(i[2]) +
              "{:<4}".format(i[3])+"{:<4}".format(i[4]))
        mes += 1
    print("\n\n")


def menu():
    print()
    print("PROGRAMA GESTOR DE PROYECTOS DE SOFTWARE\n")
    print("1 - cargar proyectos\n2 - filtrar por tag\n3 - resumen por lenguaje\n4 - popularidad\n" +
          "5 - buscar proyecto y actualizarlo\n6 - guardar populares\n7 - mostrar archivo\n0 - salir del programa\n")
    print("ingrese una de las opciones")
    seleccion = validate()
    print()
    while seleccion < 0 or seleccion > 7:
        print("debe ingresar una opcion valida")
        seleccion = validate()
    return seleccion


def principal():
    s = None
    bandera_carga = False
    registros = []
    while s != 0:
        s = menu()
        if s == 1:
            if bandera_carga:
                print("Ya se cargo el arreglo de registros, no puede cargar otro\n")
            else:
                carga(registros)
                bandera_carga = True

        elif bandera_carga:
            if s == 2:
                cad = input("Ingrese el tag que desea buscar")
                encontrados = buscar_tag(registros, cad)
                mostrar_acotados(encontrados)
                print('¿Desea guardar este listado en un archivo?')
                print('Ingrese 1 para continuar')
                op = validate()
                if op == 1:
                    crear_archivo(encontrados)
            elif s == 3:
                pass

            elif s == 4:
                total = 0
                matriz = generar_matriz(registros)
                mostrar_matriz(matriz)
                print("ingrese el numero de mes que desea resumir")
                m = validate()
                while m > 12:
                    print("ingrese un mes valido")
                    m = validate()
                    print()
                for i in matriz[m-1]:
                    total += i
                print("el total de proyectos actualizados en el mes ", m, " es: ", total)

            elif s == 5:
                rep = input("Ingrese el repositorio del proyecto que desea buscar")
                pos = busqueda_bin(registros, rep)
                act_url_fecha(registros, pos)
            elif s == 6:
                pass
            elif s == 7:
                pass
        else:
            print("Debe cargar el arreglo en la opcion 1 para acceder a las demas opciones\n")
        if s == 0:
            print("hasta luego")


if __name__ == '__main__':
    principal()



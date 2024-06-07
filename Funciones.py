from random import randint, choice
from os import system


def mapear_lista(funcion, lista:list)->list:
    """_summary_

    Args:
        funcion (_type_): Funcion para mapear
        lista (list): Lista que se va a mapear

    Returns:
        list: Se creara una lista con los datos de la lista que ingresaste y con lo que especifiques en la funcion,
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno

def filtrar_lista(funcion, lista:list)->list:
    """_summary_

    Args:
        funcion (_type_): Funcion para filtrar
        lista (list): Lista que se va a filtrar

    Returns:
        list: Se creara una lista con los datos de la lista que ingresaste luego de ser filtrados en base a tu funcion
    """
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno

def for_each_lista(funcion, lista:list)->None:
    """_summary_

    Args:
        funcion (_type_): Funcion para cada elemento
        lista (list): Lista que se va a iterar/recorrer
    """
    for el in lista:
        funcion(el)

def mostrar_heroe(un_heroe:dict)->str:
    """_summary_

    Args:
        un_heroe (dict): Diccionario con los datos del heroe

    Raises:
        ValueError: No se habria ingresado un diccionario

    Returns:
        str: Retorna la lista con los datos del heroe
    """
    if isinstance(un_heroe,dict):
        print(f"Nombre: {un_heroe["nombre"]}\n Identidad: {un_heroe["identidad"]}\n Empresa: {un_heroe["empresa"]}\n Altura: {un_heroe["altura"]}\n Peso: {un_heroe["peso"]}\n Genero: {un_heroe["genero"]}\n Color de ojos: {un_heroe["color_ojos"]}\n Color de pelo: {un_heroe["color_pelo"]}\n Fuerza: {un_heroe["fuerza"]}\n Ingeligencia: {un_heroe["inteligencia"]}\n")
    else:
        raise ValueError("No se ingreso ningun diccionario")

def mostrar_dato(un_heroe:list)->str:
    """_summary_

    Args:
        un_heroe (list): Lista con los datos del heroe

    Raises:
        ValueError: No se habria ingresado un diccionario

    Returns:
        str: Printea los datos del heroe por linea
    """
    if isinstance(un_heroe,list):
        for el in un_heroe:
            print(el)
    else:
        raise ValueError("No se ingreso ningun diccionario")

def swap_lista(lista:list, valor1, valor2):
    """_summary_

    Args:
        lista (list): lista a swapear
        valor1 (_type_): primer valor a swapear
        valor2 (_type_): segundo valor a swapear
    """
    aux = lista[valor1]
    lista[valor1] = lista[valor2]
    lista[valor2] = aux

def ordenar_lista(criterio, lista)->None:
    """_summary_

    Args:
        criterio (_type_): criterio sobre como se debe ordenar
        lista (_type_): lista que se desea ordenar
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if criterio(lista[i], lista[j]):
                swap_lista(lista, i, j)

def mostrar_heroe_fila(un_heroe: dict)->str:
    """_summary_

    Args:
        un_heroe (dict): lista de datos del heroe

    Returns:
        str: Los datos del heroe sobre una fila
    """
    print(f"{un_heroe["nombre"]} {un_heroe["identidad"]:<8} {un_heroe["empresa"]:<10} {un_heroe["altura"]} {un_heroe["peso"]:2} {un_heroe["genero"]:<18} {un_heroe["color_ojos"]:<12} {un_heroe["color_pelo"]:<12} {un_heroe["fuerza"]:<12} {un_heroe["inteligencia"]:<20}")

def mostrar_heroes(heroes:list)->None:
    """_summary_

    Args:
        heroes (list): Lista de superheroes

    Raises:
        ValueError: No se habria ingresado ninguna lista
    """
    if isinstance(heroes,list):
        cant = len(heroes)
        print("                             ***Lista de Heroes***")
        print("  Nombre Identidad Empresa Altura Peso Genero ColorOjos ColorPelo Fuerza Ingeligencia")
        print("-----------------------------------------------------------------------------------------------------------------------")
        for i in range(cant):
            mostrar_heroe_fila(heroes[i])
        print()
    else:
        raise ValueError("Eso no es una lista")

def definir_campo(campo:str)->str:
    """_summary_

    Args:
        campo (str): Valores: n = nombre ; i = identidad ; e = empresa ; a = altura ; p = peso ; f = fuerza ; int = inteligencia; g = genero

    Raises:
        ValueError: No se ingreso un valor valido

    Returns:
        str: La palabra completa
    """
    match campo:
        case "n":
            retorno = "nombre"
        case "id":
            retorno = "id_bike"
        case "tipe":
            retorno = "tipo"
        case "time":
            retorno = "tiempo"
        case _: raise ValueError("No es un campo valido")
    return retorno

def ordenar_campo(lista:list, campo:str, asc:bool = True):
    """_summary_

    Args:
        heroes (list): Lista de heroes
        campo (str): Campo a ordenar
        asc (bool, optional): True = Ascendente, False = Descendente. Defaults to True.

    Raises:
        ValueError: No se habria ingresado ninguna lista
    """
    if isinstance(lista,list):
        atributo = definir_campo(campo)
        tam = len(lista)
        for i in range(tam - 1):
            for j in range(i + 1, tam):
                if lista[i][atributo] > lista[j][atributo] if asc else lista[i][atributo] < lista[j][atributo]:
                    swap_lista(lista, i, j)  
    else:
        raise ValueError("No se ingreso ninguna lista") 

def altura_float(lista):
    """_summary_

    Args:
        lista (_type_): Lista de alturas para pasar a float
    """
    for i in lista:
        i["altura"] = float(i["altura"])

def peso_float(lista):
    """_summary_

    Args:
        lista (_type_): Lista de pesos a pasar a float
    """
    for i in lista:
        i["peso"] = float(i["peso"])

def no_inteligencia(lista):
    """_summary_

    Args:
        lista (_type_): Lista de pesos a pasar a float
    """
    for i in lista:
        if i["inteligencia"] == "":
            i["inteligencia"] = "no tiene"

def igualar_max(max, lista,campo):
    """_summary_

    Args:
        max (_type_): valor maximo
        lista (_type_): lista a iterar/recorrer
        campo (_type_): campo a igualar con el max

    Returns:
        _type_: el valor del campo igualado a max
    """
    for i in lista:
        if max == i[definir_campo(campo)]:
            return i["nombre"]

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu()->str:
    """_summary_

    Returns:
        str: Menu de stark
    """
    limpiar_pantalla()
    print("      BikeCarrer Menu")
    print("1-Cargar Archivo.CSV")
    print("2-Imprimir lista")
    print("3-Asignar tiempos")
    print("4-Informar ganador")
    print("5-Filtrar por tipo")
    print("6-Informar promedio por tipo")
    print("7-Mostrar posiciones")
    print("8-Guardar posiciones(Archivo JSON)")
    print("9-Salir")
    return  input("Ingrese opcion: ")

def contador_lista(lista,campo):
    """_summary_

    Args:
        lista (_type_): lista a iterar/recorrer
        campo (_type_): campo que  se itera/recorre

    Returns:
        _type_: Diccionario con la cantidad de propietarios a cada uno
    """
    campo = {}
    for el in lista:
        campo[el] = 0
    
    for el in lista:
        for i in campo:
            if el == i:
                campo[el] += 1
    
    return campo

def totalizar_lista(lista:list)->int:
    """_summary_

    Args:
        lista (list): lista a sumar

    Raises:
        ValueError: No se habria ingresado una lista

    Returns:
        int: Suma todos sus elementos
    """
    if isinstance(lista, list):
        total = 0
        for el in lista:
            total += int(el)
        return total
    raise ValueError("Eso no es una lista")

def calcular_promedio(lista:list)->float:
    """_summary_

    Args:
        lista (list): lista a calcular promedio

    Raises:
        ValueError: La lista habria estado vacia
        ValueError: No se habria ingresado una lista

    Returns:
        float: El promedio del total de la lista
    """
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("No esta definido el promedio de una lista vacia")
        return totalizar_lista(lista) / cant
    raise ValueError("Eso no es una lista")

def calcular_mayor(lista:list)->int:
    """_summary_

    Args:
        lista (list): lista a calcular mayor

    Raises:
        ValueError: La lista habria estado vacia
        ValueError: No se habria ingresado una lista

    Returns:
        int: Devuelve el mayor numero de la lista
    """
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("La lista esta vacia")
        mayor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor
    raise ValueError ("No es una lista")

def calcular_menor(lista:list)->int:
    """_summary_

    Args:
        lista (list): lista a calcular mayor

    Raises:
        ValueError: La lista habria estado vacia
        ValueError: No se habria ingresado una lista

    Returns:
        int: Devuelve el mayor numero de la lista
    """
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("La lista esta vacia")
        menor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] < menor:
                menor = lista[i]
        return menor
    raise ValueError ("No es una lista")

def enlistar(lista:list, campo1, campo_agrupar):
    """_summary_

    Args:
        lista (list): lista a iterar/recorrer
        campo1 (_type_): campo dato principal
        campo_agrupar (_type_): campo a clasificar

    Returns:
        _type_: diccionario con los clasificados en sus lugares
    """
    campo = {}
    for el in mapear_lista(lambda hero:hero[campo1], lista):
        campo[el] = ""
    for i in lista:   
        for j in campo.keys():
            if i[campo1] == j:
                campo[j] += f" {i[campo_agrupar]},"
    
    return campo

def get_path_actual(nombre_archivo):
    """_summary_

    Args:
        nombre_archivo (_type_): Nombre del archivo actual

    Returns:
        _type_: la ubicacion del archivo en el que se trabaja
    """
    import os
    ubi = os.path.dirname(__file__)
    
    return os.path.join(ubi, nombre_archivo)

def import_json_file(archivo_datos:str):
    """_summary_

    Args:
        archivo_datos (str): nombre del archivo .json a importar
    """
    import json
    with open(get_path_actual(archivo_datos), "r", encoding="utf-8") as archivo:
        dato = json.load(archivo)

def export_json_file(archivo_destino:str):
    import json
    with open(get_path_actual(archivo_destino), "w", encoding="utf-8") as archivo:
        json.dump("****dato****", archivo, indent=2)

def cargar_archivo_csv(nombre_archivo_data:str, lista):
    """_summary_

    Args:
        nombre_archivo_data (str): Nombre del archivo de donde se obtendra la informacion
    """
    with open(get_path_actual(nombre_archivo_data), "r", encoding="utf-8") as archivo:
         encabezado = archivo.readline().strip("\n").split(",")
    
         for linea in archivo.readlines():
            bicicleta = {}
            linea = linea.strip("\n").split(",")
            id_bike, nombre, tipo, tiempo = linea
            bicicleta["id_bike"] = int(id_bike)
            bicicleta["nombre"] = nombre
            bicicleta["tipo"] = tipo
            bicicleta["tiempo"] = tiempo
            
            lista.append(bicicleta)
            
def asignar_tiempo(lista, ini,fin):
    """_summary_

    Args:
        lista (_type_): lista a iterar/recorrer
        ini (_type_): tiempo minimo
        fin (_type_): tiempo maximo

    Returns:
        _type_: _description_
    """
    tiempos = mapear_lista(lambda bici:bici["tiempo"] ,lista)
    for i in range(len(tiempos)):
        tiempos[i] = randint(ini,fin)
    for i in range(len(lista)):
        lista[i]["tiempo"] = tiempos[i]

    return lista
        
def asignar_ganador(lista:list):
    """_summary_

    Args:
        lista (list): lista a iterar/recorrer

    Returns:
        _type_: retorna el/los diccionario/s del ganador/es
    """
    winner = []
    ordenar_campo(lista, "time", True)
    for i in lista:
        if i["tiempo"] == lista[0]["tiempo"]:
            winner.append(i)
    return winner

def crear_archivo_tipo(lista:list):
    """_summary_

    Args:
        lista (list): lista con datos para crear archivo
    """
    tipe_bike = input("Ingrese el tipo de bicicleta: ")
    while tipe_bike != "BMX" and tipe_bike != "PLAYERA" and tipe_bike != "MTB" and tipe_bike != "PASEO":
        tipe_bike = input("Ingrese un tipo de bicicleta valido: ")
    lista_tipo = (filtrar_lista(lambda bike: bike["tipo"] == tipe_bike, lista))
    
    with open(get_path_actual(tipe_bike + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_tipo)):
            l = ",".join(lista_tipo[i]) + "\n"
    
        for persona in lista_tipo:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)

def ordenar_lista_doble(lista, campo1, campo2):
    if isinstance(lista,list):
            atributo = definir_campo(campo1)
            atributo2 = definir_campo(campo2)
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i][atributo] == lista[j][atributo]:
                        if lista[i][atributo2] > lista[j][atributo2]:
                            swap_lista(lista, i, j)  
                    elif lista[i][atributo] > lista[j][atributo]:
                        swap_lista(lista,i,j)
    else:
        raise ValueError("No se ingreso ninguna lista") 










from Funciones import *
import json
from random import randint
lista = []
flag_file = True
    
while True:
        match menu():
            case "1":
                  limpiar_pantalla()
                  cargar_archivo_csv("BicicletasData.csv", lista)
                  print("Archivo importado!")
                  flag_file = False
            case "2":
                  limpiar_pantalla()
                  if flag_file == False:
                        mostrar_dato(lista)
                  else:
                        print("Primero debe ingresar archivo csv")
            case "3":
                  limpiar_pantalla()
                  if flag_file == False:
                        mostrar_dato((asignar_tiempo(lista, 50, 120)))
                  else:
                        print("Primero debe ingresar archivo csv")
            case "4":
                  limpiar_pantalla()
                  if flag_file == False:
                        print("El/los ganador/es de la carrera es/son:")
                        mostrar_dato(asignar_ganador(lista))
                  else:
                        print("Primero debe ingresar archivo csv")
            case "5":
                  limpiar_pantalla()
                  if flag_file == False:
                        crear_archivo_tipo(lista)
                        print("Archivo CSV creado")
                  else:
                        print("Primero debe ingresar archivo csv")
            case "6":
                limpiar_pantalla()
                if flag_file == False:
                        lista_tipos = ["BMX", "PASEO", "MTB", "PLAYERA"]
                        for i in lista_tipos:
                            print(f"El promedio de las bicicletas {i} es: {calcular_promedio(mapear_lista(lambda bike:bike["tiempo"],filtrar_lista(lambda tipe:tipe["tipo"] == i, lista)))}")
                else:
                    print("Primero debe ingresar archivo csv")
            case "7":
                  limpiar_pantalla()
                  if flag_file == False:
                        ordenar_lista(lista,"tipe", "time")
                        mostrar_dato(lista)
                  else:
                        print("Primero debe ingresar archivo csv")
            case "8":
                limpiar_pantalla()
                if flag_file == False:
                        with open(get_path_actual("Posiciones_tipo_bicicleta.json"), "w", encoding="utf-8") as archivo:
                            json.dump(lista, archivo, indent=2)
                        print("Archivo JSON creado")
                else:
                    print("Primero debe ingresar archivo csv")
            case "9":
                  limpiar_pantalla()
                  print("Nos vemos!!")
                  break
            case _:
                  limpiar_pantalla()
                  print("Debe ingresar un numero valido!")
        pausar()
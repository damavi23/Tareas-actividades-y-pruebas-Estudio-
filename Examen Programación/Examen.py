import os
import time

import funciones

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]


while True:
    print("*********************")
    print("[1] Asignar sueldos aleatorios")
    print("[2] Clasificar sueldos")
    print("[3] Ver estadisticas")
    print("[4] Reporte de sueldos")
    print("[5] Salir del programa")
    opc = int(input("Ingrese una opcion: "))
    while True:
        if opc == 1:
            funciones.asignar_sueldos(trabajadores)
            time.sleep(2)
            os.system("cls")
            break
            
        elif opc == 2:
            funciones.clasificar_sueldos(trabajadores)
            time.sleep(8)
            os.system("cls")
            break
        elif opc == 3:
            funciones.ver_estadisticas(trabajadores)
            time.sleep(8)
            os.system("cls")
            break
        elif opc == 4:
            funciones.reporte_de_sueldos(trabajadores)
            time.sleep(3)
            os.system("cls")
            break
        elif opc == 5:
            print("Finalizando programa...")
            print("Desarrollado por Daniel Maldonado")
            print("RUT 21.419.107.5")
            os._exit(0)


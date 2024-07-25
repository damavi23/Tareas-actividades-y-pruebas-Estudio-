import random
import random
import math



trabajadores = [
    "Juan Pérez",
    "María García",
    "Carlos López",
    "Ana Martínez",
    "Pedro Rodríguez",
    "Laura Hernández",
    "Miguel Sánchez",
    "Isabel Gómez",
    "Francisco Díaz",
    "Elena Fernández"
    ]

def asignar_sueldos(trabajadores):
    import random
    for i in range(len(trabajadores)):
        
        trabajadores[i] = (trabajadores[i], random.randint(300000, 2500000))
    print("\nSueldos asignados correctamente\n")
    
    return trabajadores

def clasificar_sueldos(trabajadores):
   
    sueldos_menor_800000 = []
    sueldos_entre_800000_2000000 = []
    sueldos_mayor_2000000 = []

    for trabajador, sueldo in trabajadores:
        if sueldo < 800000:
            sueldos_menor_800000.append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            sueldos_entre_800000_2000000.append((trabajador, sueldo))
        else:
            sueldos_mayor_2000000.append((trabajador, sueldo))

    print("\nSueldos menores a 800000: ", len(sueldos_menor_800000))
    for trabajador, sueldo in sueldos_menor_800000:
        print(f"{trabajador}: {sueldo}")

    print("\nSueldos entre 800000 y 2000000: ", len(sueldos_entre_800000_2000000))
    for trabajador, sueldo in sueldos_entre_800000_2000000:
        print(f"{trabajador}: {sueldo}")

    print("\nSueldos mayores a 2000000: ", len(sueldos_mayor_2000000))
    for trabajador, sueldo in sueldos_mayor_2000000:
        print(f"{trabajador}: {sueldo}")

    total_sueldos = sum(sueldo for _, sueldo in trabajadores)
    print(f"\nTotal de sueldos de todos los empleado5s: {total_sueldos}\n")
    
def ver_estadisticas(trabajadores):
    sueldos = [sueldo for _, sueldo in trabajadores]
    sueldos.sort()
    print("*********************")
    print("\nEstadísticas de sueldos")
    print(f"\nSueldo más bajo: {sueldos[0]}")
    print(f"\nSueldo más alto: {sueldos[-1]}")
    print(f"\nPromedio de sueldos: {sum(sueldos) / len(sueldos)}")
    print(f"\nMedia geométrica de sueldos: {math.prod(sueldos) ** (1 / len(sueldos))}")
    
    return sueldos

#Funcion que crea un archivo csv con el nombre de trabajadores, sus sueldos,descuento de salud (0.7%), descuento de AFP (12%) y sueldo líquido. Todo esto debe quedar indentado en el archivo.
def reporte_de_sueldos(trabajadores):

    with open("reporte_sueldos.csv", "w") as f:
        f.write("Nombre, Sueldo, Descuento Salud, Descuento AFP, Sueldo líquido\n")
        for trabajador, sueldo in trabajadores:
            descuento_salud = round((sueldo * 0.07),0)
            descuento_afp = round((sueldo * 0.12),0)
            sueldo_liquido = round((sueldo - descuento_salud - descuento_afp),0)
            f.write(f"{trabajador}, {sueldo}, {descuento_salud}, {descuento_afp}, {sueldo_liquido}\n")
    print("\nReporte de sueldos generado correctamente\n")





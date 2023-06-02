import sys

if len(sys.argv) == 2:
    import datetime
    import os

    hora = datetime.datetime.now()
    hora = int(datetime.datetime.timestamp(hora))

    lluvia = sys.argv[1]
    temperatura = input("Ingrese la temperatura en grados centígrados")
    humedad = input("Ingrese la humedad en porcentaje")

    texto = f"{str(hora)},{humedad},{temperatura},{lluvia}"

    archivo = open("C:/Users/dmon2/OneDrive/Desktop/Python-Prep/M10_manejodearchivos/clase09_ej2.csv","a")
    archivo.write(texto+"\n")
    archivo.close()
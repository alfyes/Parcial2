# -*- coding: utf-8 -*-

import shutil
import time

import os

from CmdAJAR import ejecutar_comando


def ejecutar_pruebas(dirapk):
    # Ejecución de calabash
    dirbase = "C:\\AJAR\\Pruebas Auto\\Parcial 2"
    dircalabash = "calabash"
    nombre_salida = "salida.txt"
    nombre_apk = os.path.basename(dirapk)

    # region Se fija directorio de trabajo base general
    os.chdir(dirbase)
    # endregion

    # region Se borrar si existe un arhivo con el mismo nombre.
    if os.path.exists(os.path.join(dirbase, dircalabash, nombre_apk)):
        os.remove(os.path.join(dirbase, dircalabash, nombre_apk))
    # endregion

    # region Se copia el apk al directorio de trabajo.
    shutil.copyfile(dirapk, os.path.join(dircalabash, nombre_apk))
    # endregion

    # region Se fija directorio de trabajo para calabash.
    os.chdir(os.path.join(dirbase, dircalabash))
    # endregion

    # region Se borrar archivo de salida.
    if os.path.exists(nombre_salida):
        os.remove(nombre_salida)
    # endregion

    # region Ejecución de las prubas de calabash.
    resultado = ejecutar_comando(["calabash-android", "run", "me.kuehle.carreport_69.apk"])
    # endregion

    # region Guarda resultado en salida.
    file_salida = open(nombre_salida, "a")
    file_salida.write(resultado['salida'])
    file_salida.write("Error")
    file_salida.write(resultado['error'])
    file_salida.close()
    # endregion

    # region Se fija  nuevamente directorio base
    os.chdir(dirbase)
    # endregion

    
    print "Resultado ejecución para {0}: {1}".format(dirapk, resultado)

    print "Ejecución pruebas calabash finalizada"


if __name__ == "__main__":
    ejecutar_pruebas(".\\oraculo\\me.kuehle.carreport_69.apk")

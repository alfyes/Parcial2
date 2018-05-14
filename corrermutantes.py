# -*- coding: utf-8 -*-
import os

from corrercalabash import ejecutar_pruebas
from correrresemble import correr_vrt
from utilidades import mover_archivos


def correr_mutantes():
    print "Inicia proceso de pruebas en mutantes"

    for dirname in os.listdir("./apks")[:20]:
        ejecutar_pruebas(".\\apks\\{0}\\signed-carreport.apk".format(dirname))
        mover_archivos("./datos_mutantes/{0}/".format(dirname))
        correr_vrt(".\\datos_mutantes\\{0}\\".format(dirname))


if __name__ == "__main__":
    correr_mutantes()

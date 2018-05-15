# -*- coding: utf-8 -*-

import shutil
import time

import os

from CmdAJAR import ejecutar_comando


def firmar_apks():
    # Se fija directorio base.
    os.chdir("/Users/ingridjulietteardila/AJAR/Parcial2/")

    print "Inicia proceso de volver a firmar apk"

    for dirname in os.listdir("./apks"):
        if dirname.startswith('apk'):
            # Se fina como directorio base donde se encuentra el apk.
            os.chdir("/Users/ingridjulietteardila/AJAR/Parcial2/apks/" + dirname)
            print dirname
            # Se ejecuta el comando que vuelve a firmar el apk.
            print ejecutar_comando(["calabash-android", "resign", "signed-carreport.apk"])

    print "Proceso ce firmar finalizado"


if __name__ == "__main__":
    firmar_apks()

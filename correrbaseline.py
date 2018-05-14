# -*- coding: utf-8 -*-
from corrercalabash import ejecutar_pruebas
from utilidades import mover_archivos


def correr_baseline():

    ejecutar_pruebas(".\\oraculo\\me.kuehle.carreport_69.apk")
    mover_archivos("./datos_baseline/")


if __name__ == "__main__":
    correr_baseline()

# -*- coding: utf-8 -*-
import os

from CmdAJAR import ejecutar_comando


def correr_vrt(directorio):

    for img_name in os.listdir(directorio):
        if img_name == "salida.txt":
            continue
        img_base = ".\\datos_baseline\\" + img_name
        img_mutante = directorio + img_name
        img_comparacion = directorio + "cpm_" + img_name

        # region Ejecuta comparación imagen
        res_resemble = ejecutar_comando(["node", "./AppNode/appResemble.js", img_base, img_mutante, img_comparacion])
        # endregion

        # region Guarda resultado en salida.
        file_salida = open(directorio + "cmp_res{0}.txt".format(img_name[0:-4]), "a")
        file_salida.write(res_resemble['salida'])
        file_salida.write("Error")
        file_salida.write(res_resemble['error'])
        file_salida.close()
        # endregion

        print res_resemble['salida']


if __name__ == "__main__":
    correr_vrt(".\\datos_mutantes\\apk114\\")

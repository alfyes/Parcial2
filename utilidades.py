import os
import shutil


def mover_archivos(directorio):
    if os.path.exists(directorio):
        shutil.rmtree(directorio)

    shutil.copytree("./process_images/", directorio)
    shutil.move("./calabash/salida.txt", directorio + 'salida.txt')


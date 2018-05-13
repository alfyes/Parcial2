import subprocess


def ejecutar_comando(cmd):
    my_process = subprocess.Popen(cmd,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, shell=True)
    out, error = my_process.communicate()

    return {'salida': out, 'error': error}

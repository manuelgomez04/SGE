from ufos import *
import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter, defaultdict

Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentarios')
fichero = "../data/ovnis.csv"

# Test de la función lee_avistamientos


def lee_avistamientos(fichero):
    res = []
    with open (fichero, encoding = "utf-8") as csvfile:
        lector = csv.reader(csvfile)
        for x in lector:
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistamiento(fechahora,ciudad,estado,forma,duracion,comentarios,latitud,longitud)
            res.append(tupla)
        return res



#Test de la función duracion_total

    
# Test de la función comentario_mas_largo



# Test de la función avistamientos_fechas



# Test de la función hora_mas_avistamientos










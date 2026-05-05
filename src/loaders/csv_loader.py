import csv
from pyDatalog import pyDatalog

#------------------------------------
#----- Cargar Conexiones/Hechos -----
#------------------------------------

# Carga conexiones desde CSV como hechos pyDatalog: conexion(origen, destino, distancia, tipo).
def load_roads_from_csv(filepath: str):

    with open(filepath, 'r', encoding='utf-8') as f:

        reader = csv.DictReader(f)

        for row in reader:
            
            pyDatalog.assert_fact(
                'conexion',
                row['origen'],
                row['destino'],
                float(row['distancia_km']),
                row['tipo_sendero']
            )

    print(f"[CSV] - Rutas cargadas desde {filepath}")
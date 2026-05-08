import csv
from pyDatalog import pyDatalog

#------------------------------------
#----- Cargar Conexiones/Hechos -----
#------------------------------------

def load_roads_from_csv(filepath: str):

    with open(filepath, 'r', encoding='utf-8') as f:

        reader = csv.DictReader(f)

        for row in reader:
            
            pyDatalog.load(f"""
            + conexion('{row['origen']}', '{row['destino']}', {float(row['distancia_km'])}, '{row['tipo_sendero']}')
            """)

    print(f"[CSV] - Rutas cargadas...")
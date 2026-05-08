import json
from pyDatalog import pyDatalog

#----------------------------------
#----- Cargar Rutas Inundadas -----
#----------------------------------

def load_weather_from_json(filepath: str):
    
    with open(filepath, 'r', encoding='utf-8') as f: data = json.load(f)
    
    for ruta in data['alertas']['rutas_cerradas_por_crecida']:

        origen, destino = ruta.split('-')

        pyDatalog.load(f"""
        + inundado('{origen}', '{destino}')
        """)
    
    print(f"[JSON] - Se encontraron {len(data['alertas']['rutas_cerradas_por_crecida'])} rutas bloqueadas...")
    return data['timestamp']
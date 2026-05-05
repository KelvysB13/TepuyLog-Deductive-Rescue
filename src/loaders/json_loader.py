import json
from pyDatalog import pyDatalog

#----------------------------------
#----- Cargar Rutas Inundadas -----
#----------------------------------

def load_weather_from_json(filepath: str):
    """Carga rutas inundadas desde JSON como hechos: inundado(origen, destino)"""
    with open(filepath, 'r', encoding='utf-8') as f: data = json.load(f)
    
    for ruta in data['alertas']['rutas_cerradas_por_crecida']:
        
        origen, destino = ruta.split('-')
        pyDatalog.assert_fact('inundado', origen, destino)
    
    print(f"[JSON] Cargadas {len(data['alertas']['rutas_cerradas_por_crecida'])} rutas bloqueadas")
    return data['timestamp']
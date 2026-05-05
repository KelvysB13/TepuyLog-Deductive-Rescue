#------------------------------------------
#----- Importar Funciones Principales -----
#------------------------------------------

from src.loaders.csv_loader import load_roads_from_csv
from src.loaders.json_loader import load_weather_from_json
from src.loaders.db_loader import (
    load_personal_info,
    registrar_bitacora,
    get_suministros_en_campamento
)

#------------------------------------
#----- Control de Importaciones -----
#------------------------------------

__all__ = [
    'load_roads_from_csv',
    'load_weather_from_json',
    'load_personal_info',
    'registrar_bitacora',
    'get_suministros_en_campamento'
]

print("[loaders] - Módulo de carga de datos listo para operación")
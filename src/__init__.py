#-------------------------------
#----- Versión del Paquete -----
#-------------------------------

__version__ = "1.0.0"
__author__ = "Kelvys Concepcion"
__status__ = "Operacional"

#--------------------------------------------------
#----- Exportación de Componentes Principales -----
#--------------------------------------------------

from src.engine import verificar_acceso, obtener_ruta_completa

#------------------------------------
#----- Control de Importaciones -----
#------------------------------------

from .engine import verificar_acceso, obtener_ruta_completa

__all__ = [
    'verificar_acceso',
    'obtener_ruta_completa',
    'loaders'
]

print("[src] - Paquete TepuyLog inicializado correctamente")
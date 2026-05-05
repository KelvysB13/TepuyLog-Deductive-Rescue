from pyDatalog import pyDatalog

# pylint: disable=undefined-variable
# pyright: reportUndefinedVariable=false

#-----------------------------------------
#----- Definición de Hechos/Términos -----
#-----------------------------------------

pyDatalog.create_terms('X, Y, Z, Dist, Tipo, conexion, inundado, acceso')

#----------------------------------------
#----- Definición de Reglas Lógicas -----
#----------------------------------------

def setup_rules():
     
pyDatalog.load('''acceso(X, Y) <= conexion(X, Y, Dist, Tipo) & ~inundado(X, Y)''') # Regla Base: Acceso directo si hay conexión y no está inundada.
pyDatalog.load('''acceso(X, Z) <= conexion(X, Y, Dist, Tipo) & ~inundado(X, Y) & acceso(Y, Z)''') # Regla Recursiva: Acceso indirecto.

#--------------------------------------------------------
#----- Función para Verificar si existe ruta segura -----
#--------------------------------------------------------

def verificar_acceso(origen, destino):

    try:

        setup_rules()
        resultados = pyDatalog.ask(acceso(origen, destino))
        
        if resultados:
            print(f"\n✅ Ruta segura encontrada: {origen} -> {destino}")
            return True
        
        else:
            print(f"\n❌ No hay ruta segura: {origen} -> {destino}")
            return False
        
    except Exception as e:
            
            print(f"\n⚠️ Error en consulta: {e}")
            return False
    
#----------------------------------------------
#----- Función para Obtener Ruta Completa -----
#----------------------------------------------

def obtener_ruta_completa(origen, destino):

    if verificar_acceso(origen, destino):

        return [origen, destino]
    
    return None
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

def verificar_acceso(origen, destino, imprimir=True):

    try:

        setup_rules()

        consulta = f"acceso('{origen}', '{destino}')"
        resultados = pyDatalog.ask(consulta)
    
        if resultados and imprimir:
            print(f"✅ Ruta segura encontrada: {origen} → {destino}")

        elif not resultados and imprimir:
            print(f"❌ No hay ruta segura: {origen} → {destino}")

        return bool(resultados)
        
    except Exception as e:
        print(f"⚠️ Error en consulta: {e}")
        return False
    
#----------------------------------------------
#----- Función para Obtener Ruta Completa -----
#----------------------------------------------

def obtener_ruta_completa(origen, destino):

    if verificar_acceso(origen, destino, imprimir=False):
        return [origen, destino]
    
    return None
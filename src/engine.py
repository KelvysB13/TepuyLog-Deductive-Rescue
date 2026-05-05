# pylint: disable=undefined-variable
# pyright: reportUndefinedVariable=false

from pyDatalog import pyDatalog

#-----------------------------------------
#----- Definición de Hechos/Términos -----
#-----------------------------------------

pyDatalog.create_terms('X, Y, Z, Dist, Tipo, conexion, inundado, acceso, ruta_segura')

#----------------------------------------
#----- Definición de Reglas Lógicas -----
#----------------------------------------

acceso(X, Y) <= (conexion(X, Y, Dist, Tipo) & ~inundado(X, Y)) # Regla Base: Acceso directo si hay conexión y no está inundada.
acceso(X, Z) <= (conexion(X, Y, Dist, Tipo) & ~inundado(X, Y) & acceso(Y, Z)) # Regla Recursiva: Acceso indirecto.

# Regla para encontrar ruta completa (opcional, muestra el camino).
ruta_segura(X, Y, [X, Y]) <= (conexion(X, Y, Dist, Tipo) & ~inundado(X, Y))
ruta_segura(X, Z, [X | Resto]) <= (conexion(X, Y, Dist, Tipo) & ~inundado(X, Y) & ruta_segura(Y, Z, Resto))

#--------------------------------------------------------
#----- Función para Verificar si existe ruta segura -----
#--------------------------------------------------------

def verificar_acceso(origen, destino):

    try:
        
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

    try:
        
        resultados = pyDatalog.ask(ruta_segura(origen, destino, ['X']))
        
        if resultados and resultados.answers:

            for sol in resultados.answers:
                if len(sol) > 2:
                    return sol[2]
            
        return None

    except Exception as e:
        print(f"⚠️ Error obteniendo ruta: {e}")
        return None
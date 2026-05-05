import os

from engine import verificar_acceso, obtener_ruta_completa
from loaders import *

def print_banner():
    """Imprime el banner de la misión"""
    print("=" * 60)
    print("🚁 OPERACIÓN TEPUY-LOG | SISTEMA DEDUCTIVO DE RESCATE")
    print("=" * 60)
    print("📍 Misión: Rescatar a la Dra. Massiel en Campamento Paraitepuy")
    print("⏰ Tiempo límite: 72 horas")
    print("=" * 60)


def print_grafo_conexiones():

    print("\n🗺️ GRAFO DE CONEXIONES (Campamentos):")

    print("""
        BASE
        /  \\
    KAVAK  MISION
     |      |
   RAPIDOS  ARUY
     |      |
    PARAITEPUY
    """)

    print("📌 Leyenda: BASE → KAVAK → RAPIDOS → PARAITEPUY (ruta bloqueada por inundación)")
    print("📌 Leyenda: BASE → MISION → ARUY → PARAITEPUY (ruta alternativa)")

#-----------------------------
#----- Función Principal -----
#-----------------------------

def main():

    print_banner()
    
#---------------------------------------
#----- Cargar Datos desde Archivos -----
#---------------------------------------

    print("\n[1] CARGANDO DATOS DE TERRENO...")
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Cargar rutas desde CSV.
    csv_path = os.path.join(base_path, "data", "roads.csv")
    load_roads_from_csv(csv_path)
    
    # Cargar clima desde JSON.
    json_path = os.path.join(base_path, "data", "weather.json")
    timestamp = load_weather_from_json(json_path)
    print(f"    📅 Clima registrado: {timestamp}")
    
    # Mostrar grafo.
    print_grafo_conexiones()
    
#---------------------------------------------------
#----- Consultar Personal Atrapado en Database -----
#---------------------------------------------------

    print("\n[2] CONSULTANDO BASE DE DATOS DE PERSONAL...")
    atrapados = load_personal_info()
    
    if not atrapados:
        print("    ✅ No hay personal atrapado. Misión completada.")
        return
    
    print(f"    🆘 Personal atrapado detectado: {len(atrapados)} persona(s)")
    
#------------------------------------
#----- Evaluar Rutas de Rescate -----
#------------------------------------

    print("\n[3] EVALUANDO RUTAS DE RESCATE CON LÓGICA DEDUCTIVA...")
    print("    🔍 Regla recursiva: acceso(X,Z) ← conexion(X,Y) ∧ ¬inundado(X,Y) ∧ acceso(Y,Z)")
    
    origen_base = "BASE"
    rutas_exitosas = 0
    
    for atrapado in atrapados:

        nombre = atrapado[0]
        rol = atrapado[1]
        destino = atrapado[2]
        edad = atrapado[3]
        estado = atrapado[4]
        
        print(f"\n" + "-" * 40)
        print(f"🎯 RESCATANDO A: {nombre}")
        print(f"   📋 Rol: {rol} | Edad: {edad} | Ubicación: {destino}")
        print(f"   🏁 Punto de partida: {origen_base}")
        
        hay_acceso = verificar_acceso(origen_base, destino)
        
        if hay_acceso:
            # Obtener ruta completa
            ruta = obtener_ruta_completa(origen_base, destino)
            
            if ruta:
                ruta_str = " → ".join(ruta)
                print(f"   🗺️ Ruta de extracción: {ruta_str}")
                print(f"   ✅ VEREDICTO: RESCATE POSIBLE")
                registrar_bitacora(ruta_str, origen_base, destino)
                rutas_exitosas += 1
            else:
                print(f"   ✅ VEREDICTO: RESCATE POSIBLE (ruta existente)")
                registrar_bitacora("Ruta segura existente", origen_base, destino)
                rutas_exitosas += 1
        else:
            print(f"   🚫 RUTAS BLOQUEADAS")
            print(f"   ❌ VEREDICTO: RESCATE IMPOSIBLE VÍA TERRESTRE")
            registrar_bitacora("SIN RUTA SEGURA - EVALUAR RESCATE AÉREO", origen_base, destino)
    
#----------------------------
#----- Reportes Finales -----
#----------------------------

    print("\n" + "=" * 60)
    print("📊 INFORME FINAL DE LA MISIÓN")
    print("=" * 60)
    
    print(f"   👥 Total de personas atrapadas: {len(atrapados)}")
    print(f"   ✅ Rescates posibles por tierra: {rutas_exitosas}")
    print(f"   ❌ Rescates que requieren helicóptero: {len(atrapados) - rutas_exitosas}")
    
    if rutas_exitosas == len(atrapados):
        print("\n   🎉 ¡TODAS LAS RUTAS SON TRANSITABLES!")
        print("   🚁 ACTIVANDO EQUIPO DE RESCATE TERRESTRE")

    elif rutas_exitosas > 0:
        print("\n   ⚠️ ALGUNAS RUTAS ESTÁN BLOQUEADAS POR INUNDACIONES")
        print("   🚁 ACTIVANDO RESCATE COMBINADO (TERRESTRE + AÉREO)")
        
    else:
        print("\n   🚨 EMERGENCIA MÁXIMA - SIN ACCESO TERRESTRE")
        print("   🚁 SOLICITANDO HELICÓPTERO DE RESCATE URGENTE")
    
    print("\n" + "=" * 60)
    print("🏁 MISIÓN TEPUY-LOG FINALIZADA.")
    print("=" * 60)

if __name__ == "__main__":
    main()
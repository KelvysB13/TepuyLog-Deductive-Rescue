import os
import time

from os import system
from engine import verificar_acceso, obtener_ruta_completa
from loaders import load_roads_from_csv, load_weather_from_json, load_personal_info, registrar_bitacora

# ----- Dibuja las "conexiones" mediante un grafo -----
def print_grafo_conexiones():

    print("".center(124, "—"))
    print("🗺️ GRAFO DE CONEXIONES (Campamentos)".center(123))
    print("".center(124, "—"))

    print("\n")
    grafo = """
                                                                BASE
                                                                /  \\
                                                            KAVAK  MISION
                                                              |      |
                                                           RAPIDOS  ARUY
                                                              |      |
                                                             PARAITEPUY
    """

    print(grafo.center(123))

    print("\n")
    print("📌 Leyenda: BASE → KAVAK → RAPIDOS → PARAITEPUY (ruta bloqueada por inundación)")
    print("📌 Leyenda: BASE → MISION → ARUY → PARAITEPUY (ruta alternativa)")

    input("\n\nPulsar Enter Volver al Menú Principal...")
    system("cls")

    menu()

#--------------------------
#----- Menú Principal -----
#--------------------------

def menu():

    print(" ≫ ★ ≪ ".center(124, "—"))
    print("🚁 OPERACIÓN TEPUY-LOG | SISTEMA DEDUCTIVO DE RESCATE".center(123))

    print("📍 Misión: Rescatar al personal atrapado en Campamento Paraitepuy".center(123))
    print("⏰ Tiempo límite: 72 horas".center(123))
    print("".center(124, "—"))

    print("\n")
    print("[1] - Iniciar Misión".ljust(31).center(124))
    print("[2] - Grafo de Conexiones".ljust(31).center(124))
    print("[3] - Informe Final de la Misión".ljust(31).center(124))
    print("[4] - Creditos".ljust(31).center(124))
    print("[0] - Salir".ljust(31).center(124))

    print("\n")
    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            system("cls")
            cargar_datos()
            return
            
        case 2:
            system("cls")
            print_grafo_conexiones()
            return
            
        case 3:
            system("cls")
            generar_informe_final([], 0)
            return
            
        case 4:
            system("cls")
            print(" ≫ ★ ≪ ".center(124, "—"))
            print("Créditos:".center(124))
            print("".center(124, "—"))

            print("\n")
            print("Developed by: Kelvys Concepcion".ljust(31).center(124))
            print("Version: 1.1.0".ljust(31).center(124))
            print("Status: Operacional".ljust(31).center(124))

            input("\n\nPulsar Enter Volver al Menú Principal...")
            system("cls")
            return
            
        case 0:
            system("cls")
            exit()

        case _:
            print("\nOpción no válida. Por favor, seleccione una opción del menú.")
            return

#-----------------------------
#----- Función Principal -----
#-----------------------------

def main():

    menu()

#---------------------------------------
#----- Cargar Datos desde Archivos -----
#---------------------------------------

def cargar_datos():

    #----- Cargar Datos de Terreno -----
        print("".center(124, "—"))
        print("[1] DATOS DE TERRENO".center(123))
        print("".center(124, "—"))
        print("\n")

        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Cargar rutas desde CSV.
        csv_path = os.path.join(base_path, "data", "roads_data.csv")
        load_roads_from_csv(csv_path)
        
        # Cargar clima desde JSON.
        json_path = os.path.join(base_path, "data", "weather_data.json")
        timestamp = load_weather_from_json(json_path)
        print(f"    📅 Clima registrado: {timestamp}")
    
    #----- Cargar Información de Personal -----
        print("\n")
        print("".center(124, "—"))
        print("[2] INFORMACIÓN DE PERSONAL".center(123))
        print("".center(124, "—"))
        atrapados = load_personal_info()
        
        if not atrapados:
            print("    ✅ No hay personal atrapado. Misión completada.")
            return
        
        print(f"    🆘 Personal atrapado detectado: {len(atrapados)} persona(s)")

        input("\n\nPulsar Enter para evaluar rutas de rescate...")
        system("cls")

        evaluar_rutas(atrapados)

#------------------------------------
#----- Evaluar Rutas de Rescate -----
#------------------------------------

def evaluar_rutas(atrapados):

        print("".center(124, "—"))
        print("[3] RUTAS DE RESCATE CON LÓGICA DEDUCTIVA".center(123))
        print("".center(124, "—"))
        
        origen_base = "BASE"
        rutas_exitosas = 0
        
        for atrapado in atrapados:

            nombre = atrapado[0]
            rol = atrapado[1]
            destino = atrapado[2]
            edad = atrapado[3]
            estado = atrapado[4]
            
            print("\n")
            print(f"🎯 RESCATANDO A: {nombre}")
            print(f"   📋 Rol: {rol} | Edad: {edad} | Ubicación: {destino}")
            print(f"   🏁 Punto de partida: {origen_base}")
            print("\n")
            
            hay_acceso = verificar_acceso(origen_base, destino)
            
            if hay_acceso:

                ruta = obtener_ruta_completa(origen_base, destino)
                
                if ruta:
                    ruta_str = " → ".join(ruta)

                    print(f"    🗺️ Ruta de extracción: {ruta_str}")
                    print(f"    ✅ VEREDICTO: RESCATE POSIBLE")

                    registrar_bitacora(ruta_str, origen_base, destino)
                    rutas_exitosas += 1

                else:
                    print(f"   ✅ VEREDICTO: RESCATE POSIBLE (ruta existente)")

                    registrar_bitacora("Ruta segura existente", origen_base, destino)
                    rutas_exitosas += 1

            else:
                print(f"    🚫 RUTAS BLOQUEADAS")
                print(f"    ❌ VEREDICTO: RESCATE IMPOSIBLE VÍA TERRESTRE")

                registrar_bitacora("SIN RUTA SEGURA - EVALUAR RESCATE AÉREO", origen_base, destino)

        input("\n\nPulsar Enter para generar informe final...")
        system("cls")

        generar_informe_final(atrapados, rutas_exitosas)

#-----------------------------------------
#----- Imprimir Informe Final en TXT -----
#-----------------------------------------

def imprimir_informe_txt(atrapados, rutas_exitosas):

    print("".center(124, "—"))
    print("📊 INFORME FINAL DE LA MISIÓN".center(123))
    print("".center(124, "—"))

    # Crear carpeta 'logs' si no existe
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_dir = os.path.join(base_path, "logs")
    
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        print(f"   📁 Carpeta creada: {logs_dir}")
    
    # Buscar archivos de informe existentes
    import re
    archivos_existentes = []
    patron = re.compile(r'Informe_(\d+)\.txt')
    
    for archivo in os.listdir(logs_dir):
        match = patron.match(archivo)
        if match:
            archivos_existentes.append(int(match.group(1)))
    
    # Determinar el siguiente número
    siguiente_numero = max(archivos_existentes) + 1 if archivos_existentes else 1
    
    # Nombre del archivo
    nombre_archivo = f"Informe_{siguiente_numero}.txt"
    ruta_completa = os.path.join(logs_dir, nombre_archivo)
    
    # Generar contenido del informe
    contenido = []
    contenido.append("".center(124, "—"))
    contenido.append("📊 INFORME FINAL DE LA MISIÓN".center(123))
    contenido.append("".center(124, "—"))
    contenido.append("")
    contenido.append(f"📅 Fecha y hora del informe: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    contenido.append(f"📄 Número de informe: {siguiente_numero}")
    contenido.append("")
    contenido.append("".center(124, "—"))
    contenido.append("📈 ESTADÍSTICAS GENERALES".center(123))
    contenido.append("".center(124, "—"))
    contenido.append("")
    contenido.append(f"👥 Total de personas atrapadas: {len(atrapados)}")
    contenido.append(f"✅ Rescates posibles por tierra: {rutas_exitosas}")
    contenido.append(f"❌ Rescates que requieren helicóptero: {len(atrapados) - rutas_exitosas}")
    contenido.append("")
    
    # Agregar detalle de cada persona (opcional)
    contenido.append("")
    contenido.append("".center(124, "—"))
    contenido.append("📋 DETALLE DEL PERSONAL".center(123))
    contenido.append("".center(124, "—"))
    contenido.append("")
    
    for i, atrapado in enumerate(atrapados, 1):
        nombre, rol, destino, edad, estado = atrapado
        contenido.append(f"{i}. {nombre} - {rol} - {edad} años - Ubicación: {destino} - Estado: {estado}")
    
    # Escribir archivo
    try:
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write("\n".join(contenido))
        
        print("")
        print(f"\n✅ Informe generado exitosamente:")
        print(f"        📄 Archivo: {nombre_archivo}")
        print(f"        📂 Ubicación: {logs_dir}")
        print(f"        📊 Total de informes: {siguiente_numero}")

        input("\n\nPulsar Enter para volver al Menú Principal...")
        system("cls")
        menu()
        return True
        
    except Exception as e:
        print(f"\n   ❌ Error al generar el informe: {e}")
        return False
    
#----------------------------
#----- Reportes Finales -----
#----------------------------

def generar_informe_final(atrapados, rutas_exitosas):

        print("".center(124, "—"))
        print("📊 INFORME FINAL DE LA MISIÓN".center(123))
        print("".center(124, "—"))

        print("\n")
        print(f"👥 Total de personas atrapadas: {len(atrapados)}")
        print(f"✅ Rescates posibles por tierra: {rutas_exitosas}")
        print(f"❌ Rescates que requieren helicóptero: {len(atrapados) - rutas_exitosas}")
        
        if rutas_exitosas == len(atrapados):
            print("\n🎉 ¡TODAS LAS RUTAS SON TRANSITABLES!")
            print("🚁 ACTIVANDO EQUIPO DE RESCATE TERRESTRE...")

        elif rutas_exitosas > 0:
            print("\n⚠️ ¡ALGUNAS RUTAS ESTÁN BLOQUEADAS POR INUNDACIONES!")
            print("🚁 ACTIVANDO RESCATE COMBINADO (TERRESTRE + AÉREO)...")
            
        else:
            print("\n🚨 ¡EMERGENCIA MÁXIMA - SIN ACCESO TERRESTRE!")
            print("🚁 SOLICITANDO HELICÓPTERO DE RESCATE URGENTE...")

        print("\n")
        print("[1] - Imprimir Informe Final".ljust(31).center(123))
        print("[0] - Volver al Menú Principal".ljust(31).center(123))
        print("\n")

        opcion = int(input("\nSelecciona una opción: "))


        match opcion:
            case 1:
                system("cls")
                imprimir_informe_txt(atrapados, rutas_exitosas)
            case 0:
                system("cls")
                menu()

if __name__ == "__main__":
        main()
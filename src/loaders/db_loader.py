import psycopg2
from psycopg2.extras import RealDictCursor


#-----------------------------------------
#----- Conexión con la base de datos -----
#-----------------------------------------

def get_db_connection():
    
    return psycopg2.connect(

        host="localhost",
        database="TepuyLog",
        user="Support",
        password="12345678",
        port=5432
    )

#------------------------------------------
#----- Consultas en la tabla personal -----
#------------------------------------------

def load_personal_info():

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute("""
        SELECT nombre, rol, campamento_actual, edad, estado
        FROM personal
        WHERE estado = 'ATRAPADO'
    """)
    
    atrapados = cur.fetchall()
    cur.close()
    conn.close()
    
    print("\n[PostgreSQL] - Personal atrapado:")

    for p in atrapados:
        
        print(f"  - {p['nombre']} ({p['rol']}) en {p['campamento_actual']}")
    
    return atrapados

#------------------------------------------
#----- Registrar rescates en bitácora -----
#------------------------------------------

def registrar_bitacora(ruta_encontrada, origen, destino):
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO bitacora_rescate (evento, responsable, ruta_evaluada)
        VALUES (%s, %s, %s)
    """, (
        f"Evaluación de ruta {origen} -> {destino}", ruta_encontrada
    ))

    conn.commit()
    cur.close()
    conn.close()

    print("[PostgreSQL] - Evento registrado en bitácora")
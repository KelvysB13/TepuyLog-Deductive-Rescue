#----------------------------------------------
#----- Base de datos logística de rescate -----
#----------------------------------------------

--- Crear base de datos ---
CREATE DATABASE TepuyLog;

\c TepuyLog;

--- Crear tablas iniciales ---
CREATE TABLE campamentos (
    id VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    latitud NUMERIC(10,6),
    longitud NUMERIC(10,6),
    tipo VARCHAR(20) CHECK (tipo IN ('BASE', 'INTERMEDIO', 'REFUGIO', 'PELIGRO'))
);

CREATE TABLE personal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    rol VARCHAR(50),
    campamento_actual VARCHAR(20) REFERENCES campamentos(id),
    edad INT,
    estado VARCHAR(20) CHECK (estado IN ('ATRAPADO', 'SEGURO', 'EN_RESCATE', 'EVACUADO'))
);

CREATE TABLE suministros (
    id SERIAL PRIMARY KEY,
    campamento_id VARCHAR(20) REFERENCES campamentos(id),
    tipo_recurso VARCHAR(50),
    cantidad INT,
    unidad VARCHAR(20)
);

CREATE TABLE bitacora_rescate (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT NOW(),
    evento TEXT,
    responsable VARCHAR(100),
    ruta_evaluada TEXT[]
);

--- Insertar datos iniciales ---
INSERT INTO campamentos VALUES
('BASE', 'Campamento Base', 6.1234, -62.5678, 'BASE'),
('PARAITEPUY', 'Campamento Paraitepuy', 5.9876, -61.2345, 'PELIGRO'),
('KAVAK', 'Kavak', 5.7654, -61.4321, 'INTERMEDIO'),
('RAPIDOS', 'Rápidos del Tepuy', 5.6543, -61.8765, 'INTERMEDIO'),
('MISION', 'Misión Santa Elena', 6.2345, -61.9876, 'REFUGIO'),
('ARUY', 'Mirador Aruy', 5.8765, -62.3456, 'INTERMEDIO');

INSERT INTO personal (nombre, rol, campamento_actual, edad, estado) VALUES
('Dra. Massiel', 'Bióloga Jefe', 'PARAITEPUY', 70, 'ATRAPADO'),
('Exploradora Jefe', 'Coordinadora Logística', 'BASE', 58, 'SEGURO'),
('Luis Rivas', 'Rescatista', 'BASE', 34, 'EN_RESCATE'),
('Ana Karina', 'Médico', 'MISION', 42, 'SEGURO');

INSERT INTO suministros (campamento_id, tipo_recurso, cantidad, unidad) VALUES
('BASE', 'Botiquín avanzado', 3, 'unidades'),
('BASE', 'Radio satelital', 2, 'unidades'),
('MISION', 'Agua potable', 200, 'litros'),
('PARAITEPUY', 'Comida de emergencia', 1, 'raciones/dia');
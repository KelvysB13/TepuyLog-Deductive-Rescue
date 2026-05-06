# 🚁 Operación Tepuy-Log | Sistema Deductivo de Rescate

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14.4-blue?logo=python)
![pyDatalog](https://img.shields.io/badge/pyDatalog-0.17.4-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue?logo=postgresql)
![Status](https://img.shields.io/badge/Status-Operacional-brightgreen)

**Sistema de planificación de rutas de rescate basado en lógica deductiva**

</div>

---

## 📖 Descripción

**Operación Tepuy-Log** es un sistema de apoyo logístico para misiones de rescate en zonas de difícil acceso. Utiliza **programación lógica deductiva (pyDatalog) básica** para modelar el terreno y determinar rutas seguras de evacuación, combinando datos topográficos estáticos con información meteorológica en tiempo real.

### 📜 Contexto de la Misión

Una expedición científica quedó aislada en la **Gran Sabana** debido a fuertes precipitaciones que bloquearon las rutas tradicionales. El sistema debe:

1. **Mapear conexiones** entre campamentos (hechos).
2. **Evaluar rutas seguras** usando reglas recursivas.
3. **Determinar viabilidad** del rescate terrestre.

---

## 🏗️ Arquitectura del Sistema

![Descripción del GIF](https://ejemplo.com/imagen.gif)

<iframe src="https://assets.pinterest.com/ext/embed.html?id=682154674784982645" height="700" width="600" frameborder="0" scrolling="no" ></iframe>
---

## 🗂️ Estructura del Proyecto

```text
TepuyLog-Deductive-Rescue/
│
├── 📁 data/ # Datos de entrada
│ ├── 📄 roads_data.csv # Conexiones topográficas
│ └── 📄 weather_data.json # Estado climático y rutas bloqueadas
│
├── 📁 docs/ # Documentación adicional
│
├── 📁 src/ # Código fuente
│ ├── init.py # Paquete principal
│ ├── engine.py # Reglas deductivas (pyDatalog)
│ ├── main.py # Orquestador principal
│ └── 📁 loaders/ # Módulo de carga de datos
│    ├── init.py
│    ├── csv_loader.py # Lector CSV
│    ├── json_loader.py # Lector JSON
│    └── db_loader.py # Conexión PostgreSQL
│
├── 📁 sql/ # Esquemas de base de datos
│ └── 📄 schema.sql # Tablas y datos iniciales
│
├── 📁 .git/ # Configuración de Git
│ ├── 📄 .gitattributes # Estadísticas de lenguaje
│ └── 📄 .gitignore # Archivos ignorados
│
├── 📄 LICENSE # Licencia MIT
├── 📄 README.md
└── 📄 requirements.txt # Dependencias Necesarias
```
# 🚁 Operación Tepuy-Log | Sistema Deductivo de Rescate

<div align="center">

![Diagrama del grafo](./docs/images/TepuyLog-Banner.png)

<a href="https://www.python.org/downloads/release/python-3144/">
    <img src="https://img.shields.io/badge/Python-3.14.4-blue?logo=python" alt="Python 3.14.4">
</a>
<a href="https://pypi.org/project/pyDatalog/">
    <img src="https://img.shields.io/badge/pyDatalog-0.17.4-green" alt="pyDatalog 0.17.4">
</a>
<a href="https://www.postgresql.org/docs/17/index.html">
    <img src="https://img.shields.io/badge/PostgreSQL-17-blue?logo=postgresql" alt="PostgreSQL 17">
</a>
<a href="#">
    <img src="https://img.shields.io/badge/Status-Operacional-brightgreen" alt="Estado: Operacional">
</a>

**Sistema de Planificación de Rutas de Rescate Basado en Lógica Deductiva**

</div>

---

## 📖 Descripción

**Tepuy-Log Deductive Rescue** es un sistema de apoyo logístico para misiones de rescate en zonas de difícil acceso en la Gran Sabana. Utiliza **programación lógica deductiva básica, utilizando reglas y hechos manejados en pyDatalog** para modelar el terreno y determinar rutas seguras de evacuación, combinando datos topográficos estáticos con información meteorológica en tiempo real.

### 📜 Contexto de la Misión

Una expedición científica quedó aislada en la **Gran Sabana** debido a fuertes precipitaciones que bloquearon las rutas tradicionales. El sistema debe:

1. **Mapear conexiones** entre campamentos (hechos).
2. **Evaluar rutas seguras** usando reglas recursivas.
3. **Determinar viabilidad** del rescate terrestre.

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
│ ├── Planteamiento del Problema.pdf
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
# 🚁 Operación Tepuy-Log | Sistema Deductivo de Rescate

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![pyDatalog](https://img.shields.io/badge/pyDatalog-0.17.4-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![Status](https://img.shields.io/badge/Status-Operacional-brightgreen)

**Sistema de planificación de rutas de rescate basado en lógica deductiva**

</div>

---

## 📖 Descripción

**Operación Tepuy-Log** es un sistema de apoyo logístico para misiones de rescate en zonas de difícil acceso. Utiliza **programación lógica deductiva (pyDatalog)** para modelar el terreno y determinar rutas seguras de evacuación, combinando datos topográficos estáticos con información meteorológica en tiempo real.

### Contexto de la Misión

Una expedición científica quedó aislada en la **Gran Sabana** debido a fuertes precipitaciones que bloquearon las rutas tradicionales. El sistema debe:

1. **Mapear conexiones** entre campamentos (hechos)
2. **Evaluar rutas seguras** usando reglas recursivas
3. **Determinar viabilidad** del rescate terrestre

---

## 🏗️ Arquitectura del Sistema


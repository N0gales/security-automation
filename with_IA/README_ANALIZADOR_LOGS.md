# 🔍 ANALIZADOR_LOGS.py  
## Automatización de Análisis de Logs SSH para Detección de Actividad Sospechosa

Este script forma parte de mi repositorio de **Security Automation**, donde desarrollo herramientas orientadas a automatizar tareas reales dentro de un SOC (Security Operations Center), como el análisis de eventos de autenticación y la detección temprana de comportamientos anómalos.

Actualmente no dispongo de conocimientos avanzados en programación, pero eso no me impide identificar necesidades técnicas y construir herramientas funcionales para abordarlas.

Este proyecto nace precisamente de esa premisa:

> No es necesario saberlo todo para empezar a automatizar procesos.  
> Tener una necesidad clara es suficiente para empezar a crear soluciones.

---

## 🎯 Objetivo del Proyecto

Desarrollar una herramienta capaz de:

- Analizar logs de autenticación SSH.
- Detectar patrones de comportamiento sospechosos.
- Identificar posibles intentos de acceso no autorizados.
- Generar informes estructurados para su posterior análisis.
- Visualizar actividad potencialmente maliciosa.

Todo ello mediante automatización con Python aplicada a escenarios reales de monitorización de seguridad.

---

## ⚙️ Funcionamiento

El script:

- Localiza automáticamente el archivo de logs dentro del proyecto.
- Procesa cada línea del archivo.
- Extrae direcciones IP, usuarios y hora de acceso.
- Analiza intentos de autenticación fallidos y exitosos.
- Detecta posibles patrones de ataque como:
  - Múltiples intentos fallidos desde una misma IP.
  - Ataques de password spraying.
  - Accesos fuera de horario habitual.
  - Enumeración de usuarios desde una misma IP.

---

## 📁 Estructura del Proyecto


security-automation/
├── data/

│ └── logs_ssh.txt

└── with_IA/

└── ANALIZADOR_LOGS.py


La carpeta `data/` contiene los archivos de logs que serán analizados por las herramientas desarrolladas en el repositorio.

---

## 🚀 Uso

Desde la carpeta donde se encuentra el script:

```bash
py ANALIZADOR_LOGS.py logs_ssh.txt
```
## 📊 Salida Generada

Al ejecutarse, el script genera:

- `report.csv` → Resumen de intentos fallidos por IP y usuario.
- `failed_attempts.png` → Visualización gráfica de IPs con actividad sospechosa.
- Alertas en consola indicando actividad sospechosa.

---

## 🔎 Tipos de Detección Implementados

- 🔐 IP sospechosa: cuando supera un umbral de intentos fallidos.
- 🎯 Password spraying: cuando múltiples IPs atacan al mismo usuario.
- ⏰ Login fuera de horario: accesos antes de las 06:00.
- 👥 Enumeración de usuarios: una IP intentando múltiples cuentas.

Los umbrales pueden modificarse en:

```python
THRESHOLD_IP = 3
THRESHOLD_USER = 3
```

## 🧠 Enfoque de Aprendizaje
Este proyecto refleja mi forma de aprendizaje:

- Detectar una necesidad.
- Plantear una solución.
- Construir una herramienta funcional.
- Comprender progresivamente la lógica detrás del desarrollo.

Aunque aún estoy desarrollando mis habilidades en programación, eso no me impide comenzar a automatizar tareas y experimentar con herramientas que simulan procesos reales de análisis en ciberseguridad.

La idea no es esperar a saber programar para empezar a crear, sino aprender programando mientras creo.

Autora:N0gales

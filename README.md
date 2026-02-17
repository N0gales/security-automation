# 🛡️ Security Automation Repository

Este repositorio recoge mi proceso de aprendizaje en **automatización aplicada a ciberseguridad**, mediante el desarrollo de herramientas en Python orientadas a tareas comunes dentro de un SOC (Security Operations Center).

Aunque actualmente no dispongo de conocimientos avanzados en programación, esto no me impide trabajar sobre ideas interesantes relacionadas con la automatización de análisis de datos, logs y eventos de seguridad.

Para ello, estoy utilizando dos enfoques paralelos:

- Desarrollo asistido con Inteligencia Artificial  
- Desarrollo manual paso a paso  

El objetivo es poder llevar a cabo proyectos funcionales mientras desarrollo progresivamente mis propias habilidades como programadora en Python aplicada a ciberseguridad.

---

## 📁 Estructura del Repositorio
```
security-automation/
├── data/
│ └──logs.txt
│ └──logs_ssh.txt
│
├── with_IA/
│ └──ANALIZADOR_LOGS.py
│ └──WORDLIST_PASS_ef_v1.py
└── without_IA/
  └──login_anomaly_detector.py
  └──login_anomaly_detector_file.py
```

---

## 📊 Carpeta `data/`

La carpeta `data/` está destinada al almacenamiento de:

- Archivos de logs (`.txt`, `.log`, etc.)
- Datos de entrada para análisis
- Ficheros utilizados por las distintas herramientas del repositorio

Aquí se almacenarán todos los archivos que posteriormente serán procesados por los scripts desarrollados en las carpetas `with_IA` y `without_IA`.

Esta separación permite trabajar con distintos datasets sin modificar la lógica de análisis de las herramientas.

---

## 🤖 Carpeta `with_IA/`

En esta carpeta se incluyen proyectos desarrollados con la asistencia de Inteligencia Artificial.

El objetivo de estos proyectos es:

- Explorar ideas de automatización de forma más ágil
- Comprender la lógica detrás de herramientas de análisis de seguridad
- Aprender a utilizar la IA como herramienta de apoyo en el desarrollo técnico

Estos proyectos me permiten implementar soluciones funcionales incluso mientras continúo desarrollando mis habilidades en programación.

---

## 🧠 Carpeta `without_IA/`

Esta carpeta contiene proyectos desarrollados manualmente, sin asistencia directa de IA.

Aquí se incluyen scripts que voy creando paso a paso conforme avanzo en:

- Python aplicado a ciberseguridad
- Análisis de logs
- Procesamiento de datos
- Automatización de tareas en entornos SOC

El objetivo es reforzar mi comprensión de la lógica de programación y desarrollar mis propias herramientas desde cero.

---

## 🎯 Objetivo General

Este repositorio refleja mi enfoque de aprendizaje basado en:

- Implementar ideas de automatización desde fases tempranas
- Aprovechar la IA como soporte técnico
- Desarrollar paralelamente mis propias capacidades como programadora
- Aplicar estos conocimientos al análisis de eventos de seguridad

A medida que avance en conocimientos, los proyectos evolucionarán en complejidad y autonomía de desarrollo.

Autor: N0gales

# 🔐 Security Automation Projects

Repositorio orientado al desarrollo progresivo de herramientas de automatización en ciberseguridad utilizando Python.

El objetivo es evolucionar desde scripting básico hacia motores de análisis estructurados y modulares alineados con perfiles como:

- Junior Security Engineer  
- SOC / Detection Analyst  
- Security Automation Engineer  
- Pentester técnico orientado a automatización  

Este repositorio refleja aprendizaje práctico, diseño modular y modelado de comportamiento en sistemas de seguridad.

---

# 🧠 Enfoque Técnico

Los proyectos incluidos no se limitan a ejercicios aislados.  
Están diseñados para simular escenarios reales de:

- Procesamiento de logs
- Análisis stateful de eventos
- Modelado de comportamiento por entidad (IP)
- Aplicación de reglas de detección
- Clasificación de riesgo
- Análisis secuencial de eventos

Cada proyecto sigue principios de:
- Separación de responsabilidades
- Modularidad
- Extensibilidad
- Diseño limpio de código

---

# 📂 Estructura del Repositorio

```
security-automation/
│
├── data/
│   └── logs.txt
│
├── login_anomaly_detector.py
├── login_anomaly_detector_file.py
└── README.md
```

---

# 🛡️ Proyecto Principal: Login Anomaly Detector

Motor de detección de anomalías en autenticaciones.

Incluye dos versiones:

### 1️⃣ Versión básica (`login_anomaly_detector.py`)
- Logs simulados en memoria
- Construcción de estado por IP
- Detección de múltiples intentos fallidos
- Clasificación de riesgo

### 2️⃣ Versión con ingestión de archivo (`login_anomaly_detector_file.py`)
- Lectura de logs desde archivo (`data/logs.txt`)
- Modelado stateful por IP
- Detección de:
  - Múltiples intentos fallidos
  - Posible brute force exitoso
  - Patrón secuencial (3 fallos consecutivos + éxito)
- Sistema de scoring (Low / Medium / High)
- Presentación estructurada de resultados

---

# 🏗️ Arquitectura General

El motor está dividido en fases independientes:

1. Construcción de estado (`build_state`)
2. Evaluación de reglas (`evaluate_rules`)
3. Cálculo de riesgo (`risk_score`)
4. Detección secuencial (`detect_sequential_bruteforce`)
5. Orquestación en `main`

Esto permite:

- Añadir nuevas reglas fácilmente
- Implementar motores adicionales
- Separar análisis cuantitativo y secuencial
- Reutilizar funciones en otros contextos

---

# 🎯 Objetivo Profesional

Este repositorio demuestra:

- Modelado stateful con diccionarios anidados
- Pensamiento orientado a detección
- Separación entre datos y lógica
- Diseño modular escalable
- Automatización aplicada a seguridad

Refleja transición de scripting básico hacia ingeniería de detección.

---

Autor: N0gales

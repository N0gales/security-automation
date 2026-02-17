# 🛡️ Login Anomaly Detector

Motor básico de detección de anomalías en intentos de login desarrollado en Python.

Simula un sistema stateful que analiza eventos de autenticación y aplica reglas de detección sobre el estado acumulado por IP.

---

## 🏗️ Arquitectura

El motor está dividido en dos fases principales:

### 1️⃣ Construcción de Estado (`build_state`)
- Procesa los logs línea por línea
- Separa IP y tipo de evento
- Crea un diccionario por IP que almacena:
  - Número de intentos fallidos
  - Número de intentos exitosos
  - Último evento registrado

### 2️⃣ Evaluación de Reglas (`evaluate_rules`)
- Analiza el estado final por IP
- Detecta:
  - IPs con múltiples intentos fallidos
  - Posibles ataques de fuerza bruta (fallos seguidos de éxito)

Esta separación permite modularidad y futura ampliación del sistema.

---

## 📊 Ejemplo de Salida
# 🛡️ Login Anomaly Detector

Motor básico de detección de anomalías en intentos de login desarrollado en Python.

Simula un sistema stateful que analiza eventos de autenticación y aplica reglas de detección sobre el estado acumulado por IP.

---

## 🏗️ Arquitectura

El motor está dividido en dos fases principales:

### 1️⃣ Construcción de Estado (`build_state`)
- Procesa los logs línea por línea
- Separa IP y tipo de evento
- Crea un diccionario por IP que almacena:
  - Número de intentos fallidos
  - Número de intentos exitosos
  - Último evento registrado

### 2️⃣ Evaluación de Reglas (`evaluate_rules`)
- Analiza el estado final por IP
- Detecta:
  - IPs con múltiples intentos fallidos
  - Posibles ataques de fuerza bruta (fallos seguidos de éxito)

Esta separación permite modularidad y futura ampliación del sistema.

---

## 📊 Ejemplo de Salida
192.168.1.25 👀 Suspicious IP due to multiple failed attempts
192.168.1.30 💥 ALERT! BRUTE FORCE DETECTED 💥


---

## 🔎 Lógica de Detección

Reglas actuales:

- ≥ 3 intentos fallidos → IP sospechosa
- ≥ 3 intentos fallidos + último evento exitoso → posible brute force exitoso

---

## 🎯 Objetivo Técnico

Este proyecto demuestra:

- Modelado de estado con diccionarios anidados
- Separación de responsabilidades en funciones
- Diseño modular
- Aplicación de reglas de detección
- Pensamiento orientado a automatización en seguridad


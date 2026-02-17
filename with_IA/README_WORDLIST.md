\# 🔐 Generador de Wordlists Personalizadas



Este script en Python permite generar una wordlist personalizada a partir de información potencialmente asociada a un objetivo, con el fin de simular ataques de fuerza bruta o diccionario en entornos controlados de auditoría de seguridad.



Forma parte de mi repositorio de \*\*Security Automation\*\*, donde desarrollo herramientas orientadas a automatizar tareas relacionadas con análisis ofensivo y defensivo dentro de contextos de ciberseguridad.



---



\## 🎯 Objetivo del Proyecto



El propósito de esta herramienta es:



\- Automatizar la generación de wordlists específicas para un objetivo.

\- Simular escenarios reales de ataques de diccionario.

\- Aplicar técnicas básicas de OSINT en procesos de auditoría.

\- Entender cómo se construyen contraseñas a partir de datos personales.

\- Replicar patrones comunes utilizados por usuarios al crear contraseñas.



---



\## ⚙️ Funcionamiento



El script solicita información relacionada con un posible objetivo, organizada en distintas categorías como:



\- Identidad básica

\- Vínculos emocionales

\- Localización

\- Vida profesional

\- Gustos y aficiones

\- Fechas significativas

\- Datos cotidianos



A partir de estos datos:



\- Se generan distintas combinaciones de palabras.

\- Se extraen números relevantes (años, fechas, etc.).

\- Se aplican variaciones como:

&nbsp; - Mayúsculas y minúsculas.

&nbsp; - Concatenaciones.

&nbsp; - Separadores (`\_`, `-`).

&nbsp; - Sustituciones tipo \*leet\* (ej: `a → 4`, `e → 3`).

&nbsp; - Inclusión de símbolos comunes.



El resultado es una wordlist que simula patrones de contraseñas reales utilizadas por usuarios.



---



\## 📁 Salida Generada



El script genera:



\- `wordlist.txt` → Archivo con todas las combinaciones generadas.



Este archivo se guarda automáticamente en la misma carpeta donde se encuentra el script.



---



\## 🚀 Uso



Desde la carpeta donde se encuentra el script:



```bash

py WORDLIST\_PASS\_ef\_v1.py

```

A continuación, el programa solicitará los distintos datos necesarios para generar la wordlist.

Una vez introducida la información, se generará automáticamente el archivo wordlist.txt.



\## 🧠 Conceptos Aplicados



\- OSINT aplicado a generación de credenciales.  

\- Ingeniería social en entornos controlados.  

\- Automatización de generación de diccionarios.  

\- Técnicas de mutación de contraseñas.  

\- Patrones de construcción de passwords.  



---



\## ⚠️ Uso Ético



Esta herramienta ha sido desarrollada únicamente con fines educativos y para su uso en:



\- Laboratorios.  

\- Entornos de pruebas.  

\- Auditorías autorizadas.  

\- Simulación de ataques en procesos de pentesting.  



El uso indebido de esta herramienta fuera de entornos autorizados puede ser ilegal.



---



\## 📈 Enfoque de Aprendizaje



Este proyecto forma parte de mi proceso de aprendizaje en:



\- Python aplicado a ciberseguridad.  

\- Automatización de tareas ofensivas.  

\- Comprensión de técnicas de ataque basadas en información personal.  



A través del desarrollo de este tipo de herramientas, busco entender cómo pequeñas piezas de información pueden ser utilizadas para comprometer la seguridad de credenciales en sistemas reales.




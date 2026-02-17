# 🔐 Security Automation Projects

This repository contains my security-focused automation projects built with Python.

The goal of this repository is to progressively develop practical tooling aligned with roles such as:

- Junior Security Engineer
- SOC / Detection Analyst
- Security Automation Engineer
- Technical Pentester

Each project focuses on applying Python to model state, analyze events, and implement detection logic.

---

## 📂 Projects

### 🛡️ Login Anomaly Detector
A basic stateful login detection engine that:

- Tracks failed and successful login attempts per IP
- Detects multiple failed attempts
- Identifies potential brute-force attacks (failed attempts followed by success)
- Implements modular structure (state builder + rule evaluator)

> Future improvements:
> - Risk scoring per IP
> - Event sequence modeling
> - Timestamp-based analysis
> - CLI support
> - Log file ingestion

---

## 🎯 Purpose

This repository reflects my progression from basic scripting to structured security tooling.

Rather than focusing only on CTF-style exercises, these projects aim to:

- Model system behavior
- Automate analysis processes
- Apply detection logic
- Develop structured and modular Python code

---

## 🚀 Continuous Development

Projects will evolve over time:
- Refactoring
- Additional detection rules
- Risk scoring engines
- More realistic log simulation
- Real-world log parsing

---

## 🧠 Tech Focus

- Python
- Stateful analysis
- Detection logic
- Security automation concepts
- Modular code design

---

Author: N0gales

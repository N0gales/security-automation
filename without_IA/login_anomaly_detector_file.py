"""
Stateful Login Anomaly Detection Engine

This script processes authentication logs from a file and performs:

- Stateful tracking of login attempts per IP
- Detection of multiple failed login attempts
- Risk scoring classification (Low / Medium / High)
- Sequential brute force detection (3 consecutive failures followed by success)

The engine is modular and separates:
- State construction
- Rule evaluation
- Risk scoring
- Sequential pattern detection

Author: N0gales
"""

def build_state(logs):
    ips = {}
    for line_log in logs:
        ip, login = line_log.split(",")

        if ip not in ips:
            if login == "LOGIN_FAILED":
                ips[ip] = {
                    "failed": 1,
                    "success": 0,
                    "last_event": login,
                    "events": [login]
                }
            else:
                ips[ip] = {
                    "failed": 0,
                    "success": 1,
                    "last_event": login,
                    "events": [login]
                }
        else:
            if login == "LOGIN_FAILED":
                ips[ip]["failed"] += 1
            else:
                ips[ip]["success"] += 1

            ips[ip]["last_event"] = login
            ips[ip]["events"].append(login)

            if len(ips[ip]["events"]) > 4:
                ips[ip]["events"].pop(0)

    return ips

def detect_sequential_bruteforce(ips):
    sequential_alerts = []

    for ip in ips:
        if ips[ip]["events"] == ["LOGIN_FAILED","LOGIN_FAILED","LOGIN_FAILED","LOGIN_SUCCESS"]:
            sequential_alerts.append(ip)

    return sequential_alerts

def evaluate_rules(ips):
    alerts = {}

    for ip in ips:
        ip_alerts = []

        if ips[ip]["failed"] >= 3 and ips[ip]["last_event"] == "LOGIN_SUCCESS":
            ip_alerts.append("💥Brute force detected")

        elif ips[ip]["failed"] >= 3:
            ip_alerts.append("👀Multiple failed attempts")

        if ip_alerts:
            alerts[ip] = ip_alerts

    return alerts

def risk_score(ips):
    risk_report = {}
    for ip in ips:
        failed = ips[ip]["failed"]
        success = ips[ip]["success"]
        last_event = ips[ip]["last_event"]

        score = failed * 2

        if failed >= 3:
            score += 3

        if failed >= 3 and last_event == "LOGIN_SUCCESS":
            score += 5

        if score < 4:
            level = "Low"
        elif score < 9:
            level = "Medium"
        else:
            level = "High"

        risk_report[ip] = {
            "score": score,
            "level": level
        }

    return risk_report

if __name__ == "__main__":

    with open("data/logs.txt", "r") as file:
        lines = file.readlines()

    logs = []
    for line in lines:
        logs.append(line.strip())
    ips = build_state(logs)

    alerts = evaluate_rules(ips)
    sequential = detect_sequential_bruteforce(ips)
    risk = risk_score(ips)

    for ip in ips:
        print(f"\nIP: {ip}")
        print(f"  - Risk Level: {risk[ip]['level']} (Score: {risk[ip]['score']})")

        if ip in alerts:
            for alert in alerts[ip]:
                print(f"  - Alert: {alert}")

        if ip in sequential:
            print("  - Alert: Sequential brute force pattern detected")

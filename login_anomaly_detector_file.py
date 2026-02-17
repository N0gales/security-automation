"""
Basic Stateful Login Detection Engine

This script processes login events and detects:
- Multiple failed login attempts
- Possible brute force attacks (failed attempts followed by success)

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
    return ips

def detect_sequential_bruteforce(ips):
    for ip in ips:
        events = ips[ip]["events"]

        if events == ["LOGIN_FAILED", "LOGIN_FAILED", "LOGIN_FAILED", "LOGIN_SUCCESS"]:
            print(ip, "🔥 Sequential brute force detected")

def evaluate_rules(ips):
    for ip in ips:
        if ips[ip]["failed"] >= 3 and ips[ip]["last_event"] == "LOGIN_SUCCESS":
            print(ip, "💥 ALERT! BRUTE FORCE DETECTED 💥")
        elif ips[ip]["failed"] >= 3:
            print(ip, "👀 Suspicious IP due to multiple failed attempts")


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
    evaluate_rules(ips)
    risk = risk_score(ips)
    detect_sequential_bruteforce(ips)

    for ip in risk:
        print(ip, "→", risk[ip]["level"], "(Score:", risk[ip]["score"], ")")
    
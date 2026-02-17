"""
Basic Stateful Login Detection Engine

This script processes login events and detects:
- Multiple failed login attempts
- Possible brute force attacks (failed attempts followed by success)

Author: N0gales
"""


logs = [
    "192.168.1.10,LOGIN_SUCCESS",
    "192.168.1.12,LOGIN_SUCCESS",
    "192.168.1.15,LOGIN_FAILED",
    "192.168.1.15,LOGIN_SUCCESS",
    "192.168.1.25,LOGIN_FAILED",
    "192.168.1.25,LOGIN_FAILED",
    "192.168.1.25,LOGIN_FAILED",
    "192.168.1.30,LOGIN_FAILED",
    "192.168.1.30,LOGIN_FAILED",
    "192.168.1.30,LOGIN_FAILED",
    "192.168.1.30,LOGIN_SUCCESS",
]
def build_state(logs):
    ips = {}
    for line_log in logs:
        ip, login = line_log.split(",")

        if ip not in ips:
            if login == "LOGIN_FAILED":
                ips[ip] = {
                    "failed": 1,
                    "success": 0,
                    "last_event": login
                }
            else:
                ips[ip] = {
                    "failed": 0,
                    "success": 1,
                    "last_event": login
                }
        else:
            if login == "LOGIN_FAILED":
                ips[ip]["failed"] += 1
            else:
                ips[ip]["success"] += 1
            ips[ip]["last_event"] = login
    return ips

def evaluate_rules(ips):
    for ip in ips:
        if ips[ip]["failed"] >= 3 and ips[ip]["last_event"] == "LOGIN_SUCCESS":
            print(ip, "💥 ALERT! BRUTE FORCE DETECTED 💥")
        elif ips[ip]["failed"] >= 3:
            print(ip, "👀 Suspicious IP due to multiple failed attempts")


if __name__ == "__main__":
    ips = build_state(logs)
    evaluate_rules(ips)
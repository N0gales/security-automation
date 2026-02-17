import re
import time
import csv
from collections import defaultdict
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

THRESHOLD_IP = 3
THRESHOLD_USER = 3
INTERVAL = 60  # segundos entre análisis automáticos


# 🔍 Función para buscar archivo dentro del proyecto
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


# 📍 Detectar rutas del proyecto
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

# 📂 Determinar archivo de log
if len(sys.argv) > 1:
    LOG_FILE = sys.argv[1]

    if not os.path.isfile(LOG_FILE):
        print("[*] Archivo no encontrado en ruta directa. Buscando en el proyecto...")
        found = find_file(LOG_FILE, PROJECT_ROOT)

        if found:
            LOG_FILE = found
            print(f"[+] Archivo encontrado en: {LOG_FILE}")
        else:
            print(f"[!] No se encontró {LOG_FILE} en el proyecto.")
            sys.exit(1)
else:
    LOG_FILE = find_file("logs_ssh.txt", PROJECT_ROOT)

    if LOG_FILE:
        print(f"[+] Usando archivo por defecto: {LOG_FILE}")
    else:
        print("[!] No se encontró logs_ssh.txt en el proyecto.")
        sys.exit(1)


def extract_hour(line):
    try:
        parts = line.split()
        time_part = parts[2]
        hour = int(time_part.split(":")[0])
        return hour
    except:
        return None


def analyze_logs():
    failed_attempts_ip = defaultdict(int)
    failed_attempts_user = defaultdict(int)
    ip_to_users = defaultdict(set)
    user_to_ips = defaultdict(set)
    successful_logins = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            user_match = re.search(r"for (invalid user )?(\w+)", line)

            if not ip_match or not user_match:
                continue

            ip = ip_match.group(1)
            user = user_match.group(2)
            hour = extract_hour(line)

            if "Failed password" in line:
                failed_attempts_ip[ip] += 1
                failed_attempts_user[user] += 1
                ip_to_users[ip].add(user)
                user_to_ips[user].add(ip)

            if "Accepted password" in line:
                successful_logins.append((ip, user, hour))

    generate_csv(failed_attempts_ip, failed_attempts_user)
    generate_graph(failed_attempts_ip)
    generate_alerts(failed_attempts_ip, failed_attempts_user, user_to_ips, ip_to_users, successful_logins)


def generate_csv(failed_ip, failed_user):
    with open("report.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["Type", "Identifier", "Failed Attempts"])

        for ip, count in failed_ip.items():
            writer.writerow(["IP", ip, count])

        for user, count in failed_user.items():
            writer.writerow(["User", user, count])

    print("[+] CSV generado: report.csv")


def generate_graph(failed_ip):
    df = pd.DataFrame(list(failed_ip.items()), columns=["IP", "Failed Attempts"])
    df.plot(kind="bar", x="IP", y="Failed Attempts")
    plt.title("Intentos fallidos por IP")
    plt.tight_layout()
    plt.savefig("failed_attempts.png")
    print("[+] Gráfica guardada como failed_attempts.png")


def generate_alerts(failed_ip, failed_user, user_to_ips, ip_to_users, successful_logins):
    print("\n=== ALERTAS DETECTADAS ===\n")

    for ip, count in failed_ip.items():
        if count >= THRESHOLD_IP:
            print(f"[!] IP sospechosa: {ip} con {count} fallos")

    for user, ips in user_to_ips.items():
        if len(ips) >= 3:
            print(f"[!] Posible password spraying contra {user} desde {len(ips)} IPs")

    for ip, user, hour in successful_logins:
        if hour is not None and hour < 6:
            print(f"[!] Login fuera de horario: {user} desde {ip} a las {hour}:00")

    for ip, users in ip_to_users.items():
        if len(users) >= 3:
            print(f"[!] IP {ip} intentó múltiples usuarios: {', '.join(users)}")


def main():
    print("🔍 Analizando logs...")
    analyze_logs()


if __name__ == "__main__":
    main()

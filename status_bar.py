#!/usr/bin/env python3
import subprocess, psutil, time
from datetime import datetime

while True:
    cpu = str(psutil.cpu_percent(interval=0.25)) + "%"

    m = psutil.virtual_memory()
    ram = str(round(m.used / 1073741824, 1)) + " GiB / " + str(round(m.total / 1073741824, 1)) + " GiB"

    # ⚡ 🔋
    battery_level = open("/sys/class/power_supply/BAT0/capacity", "r").read()[:-1]
    battery_icon = ""
    battery_status = open("/sys/class/power_supply/BAT0/status", "r").read()[:-1]
    if battery_status == "Not charging":
        battery_icon = "🔌"
    elif battery_status == "Discharging":
        battery_icon = "🔋"
    else:
        battery_icon = "⚡"
    
    battery = f"{battery_level}% {battery_icon}"

    wifi_status = subprocess.check_output("nmcli connection show --active | grep wifi | awk '{print $1}'", shell=True).decode()
    wifi = "📶 🚫"
    if wifi_status != "":
        wifi = f"📶 {wifi_status[:-1]}"

    now = datetime.now()
    current_time = datetime.strftime(now, "%B %-d, %Y %-I:%M:%S %p")

    bar = f"{cpu} | {ram} | {wifi} | {battery} | {current_time}"

    print(bar, flush=True)

    time.sleep(0.25)
#!/usr/bin/env python3
import subprocess, psutil, time
from datetime import datetime

while True:
    cpu = str(psutil.cpu_percent(interval=0.25)) + "%"

    m = psutil.virtual_memory()
    ram = str(round(m.used / 1073741824, 1)) + " GiB / " + str(round(m.total / 1073741824, 1)) + " GiB"

    battery_level = open("/sys/class/power_supply/BAT0/capacity", "r").read()[:-1]
    battery_icon = ""
    battery_status = open("/sys/class/power_supply/BAT0/status", "r").read()[:-1]
    battery_level_icon = ""
    # 0/4, 1/4, 2/4, 3/4, 4/4
    # 0-2  2-4  4-6  6-8  8-10
    bl = int(battery_level)
    if bl < 20:
        battery_level_icon = ""
    elif bl < 40:
        battery_level_icon = ""
    elif bl < 60:
        battery_level_icon = ""
    elif bl < 80:
        battery_level_icon = ""
    else:
        battery_level_icon = ""
    if battery_status == "Not charging":
        battery_icon = ""
    elif battery_status == "Discharging":
        battery_icon = battery_level_icon
    else:
        battery_icon = ""
    
    battery = f"{battery_level}% {battery_icon}"

    wifi_status = subprocess.check_output("nmcli connection show --active | grep wifi | awk '{print $1}'", shell=True).decode()
    wifi = ""
    if wifi_status != "":
        wifi = f" {wifi_status[:-1]}"

    brightness = "" + str(round(float(subprocess.check_output("light", shell=True).decode().rstrip("\n")), 0)) + "%"


    now = datetime.now()
    current_time = datetime.strftime(now, "%B %-d, %Y %-I:%M:%S %p")

    bar = f"{cpu} | {ram} | {wifi} | {battery} | {current_time}"

    print(bar, flush=True)

    time.sleep(0.25)
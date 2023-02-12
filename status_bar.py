#!/usr/bin/env python3
import os, psutil, time
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

    now = datetime.now()
    current_time = datetime.strftime(now, "%B %-d, %Y %-I:%M:%S %p")

    bar = f"{cpu} | {ram} | {battery} | {current_time}"

    print(bar, flush=True)

    time.sleep(0.25)
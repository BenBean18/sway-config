#!/usr/bin/env python3
import subprocess, psutil, time, re
from datetime import datetime

avg_power_draw = []
samples = 5
last_energy = 0

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
        battery_icon = "" # plug with bolt should be 

    power_draw = int(open("/sys/class/power_supply/BAT0/power_now", "r").read()[:-1]) / 1000000.0 # Wh/h
    energy_now = int(open("/sys/class/power_supply/BAT0/energy_now", "r").read()[:-1]) / 1000000.0 # Wh

    if energy_now != last_energy:
        last_energy = energy_now
        avg_power_draw = [power_draw] + avg_power_draw
        if len(avg_power_draw) > 5:
            avg_power_draw.pop()

    current_avg = sum(avg_power_draw) / len(avg_power_draw)

    # Wh / (Wh)(h^-1) = h
    time_left = round(energy_now / current_avg, 1) if current_avg != 0 else float("inf")
    battery_time = f"{time_left} hrs"

    power_profile = subprocess.check_output("powerprofilesctl get", shell=True).decode().rstrip("\n ")
    profile_icon = ""
    if power_profile == "power-saver":
        profile_icon = "" # leaf
    elif power_profile == "balanced":
        profile_icon = "" # mid gauge
    else:
        profile_icon = "" # high gauge
    
    battery = f"{battery_level}% {battery_icon}, {battery_time} {profile_icon}"

    try:
        wifi_status = subprocess.check_output("nmcli connection show --active | grep wifi", shell=True).decode().split("  ")
        wifi = " Off"
        if len(wifi_status) >= 1:
            wifi = f" {wifi_status[0]}"
    except:
        wifi = " Off"

    brightness_value = int(float(subprocess.check_output("light", shell=True).decode().rstrip("\n")))
    brightness = f" {brightness_value}%"

    sound_value = subprocess.check_output("amixer sget Master -M", shell=True).decode().splitlines()[-1]
    m = re.search(r'\[\d+%\]', sound_value)
    volume = int(m.group()[1:-2])
    on = "[on]" in sound_value
    sound = ""
    if not on:
        sound = f" {volume}%"
    else:
        if volume < 1:
            sound = f" {volume}%"
        elif volume < 50:
            sound = f" {volume}%"
        else:
            sound = f" {volume}%"
    
    recording = ""
    try:
        subprocess.check_output("pgrep wf-recorder", shell=True).decode()
        recording = " |"
    except:
        recording = ""

    now = datetime.now()
    current_time = datetime.strftime(now, "%A, %B %-d, %Y %-I:%M:%S %p")

    bar = f"{recording} {brightness} | {sound} | {cpu} | {ram} | {wifi} | {battery} | {current_time}"

    print(bar, flush=True)

    time.sleep(0.25)

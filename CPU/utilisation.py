import matplotlib.pyplot as plt
import time
from Lecture_Fichier import Stat, Uptime

import locking


def calcul_utilisation_cpu(stat, uptime, clock_ticks_per_second):
    process_utime_sec = stat.utime / clock_ticks_per_second
    process_stime_sec = stat.stime / clock_ticks_per_second
    process_start_sec = stat.starttime / clock_ticks_per_second

    system_uptime_sec = uptime.total_time

    process_elapsed_sec = system_uptime_sec - process_start_sec
    process_cpu_usage = 100 * ((process_utime_sec + process_stime_sec) / process_elapsed_sec)

    return process_cpu_usage


def plot_cpu_usage(cpu_usage_list, time_list):
    with locking.lock:
        plt.figure()
        plt.plot(time_list, cpu_usage_list)
        plt.xlabel("Temps (s)")
        plt.ylabel("Utilisation du CPU (%)")
        plt.show()

def store_cpu_usage(cpu_usage_list, time_list, pid):
    with locking.lock:
        plt.figure()
        plt.plot(time_list, cpu_usage_list)
        plt.xlabel("Temps (s)")
        plt.ylabel("Utilisation du CPU (%)")
        plt.savefig(f"CPU_{pid}.png")
        plt.close()


def utilisation_cpu(pid, frequence,nbre_points):

    process_info = Stat(pid)
    uptime_info = Uptime()

    temps_debut = int(time.time())

    list_cpu = []
    list_temps = []
    compt = 0
    while compt < nbre_points:
        temps_actuel_ms = int(time.time())

        process_info.read_proc_stat()
        uptime_info.read_proc_uptime()

        list_cpu.append(calcul_utilisation_cpu(process_info, uptime_info, 100))
        list_temps.append(temps_actuel_ms - temps_debut)
        compt += 1

        time.sleep(frequence)

    store_cpu_usage(list_cpu, list_temps)

import matplotlib.pyplot as plt
import time

from Read_File import Stat, Uptime
from shared import locking
from shared import Result


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


def utilisation_cpu(pid, frequence, nbre_points, result):
    process_info = Stat(pid)
    uptime_info = Uptime()

    point_per_sec = 10

    list_cpu = []
    list_temps = []
    compt = 0
    while process_info.read_proc_stat() != -1 and uptime_info.read_proc_uptime() != -1 and compt < nbre_points:

        list_cpu.append(calcul_utilisation_cpu(process_info, uptime_info, 100))
        list_temps.append(compt * frequence)
        compt += 1

        time.sleep(60/point_per_sec)

    result.append(Result("CPU", "Utilisation du cpu (%)", [list_temps, list_cpu]))
    # store_cpu_usage(list_cpu, list_temps, pid)

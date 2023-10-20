# Exemple d'utilisation

from Lecture_Fichier.stat import Stat
from Lecture_Fichier.uptime import Uptime
import time
import matplotlib.pyplot as plt


def calcul_utilisation_cpu(stat, uptime, clock_ticks_per_second):
    process_utime_sec = stat.utime / clock_ticks_per_second
    process_stime_sec = stat.stime / clock_ticks_per_second
    process_start_sec = stat.starttime / clock_ticks_per_second

    system_uptime_sec = uptime.total_time

    process_elapsed_sec = system_uptime_sec - process_start_sec
    process_cpu_usage = 100 * ((process_utime_sec + process_stime_sec) / process_elapsed_sec)

    return process_cpu_usage

def plot_cpu_usage(cpu_usage_list, time_list):

    plt.plot(time_list, cpu_usage_list)
    plt.xlabel("Temps (ms)")
    plt.ylabel("Utilisation du CPU (%)")
    plt.show()

def main():
    pid = 21863  # Remplacez par le PID du processus que vous souhaitez inspecter
    frequence = 0.1  # en seconde

    process_info = Stat(pid)
    uptime_info = Uptime()

    Liste_CPU = []
    Liste_temps = []
    compt = 0
    while compt < 100:
        temps_actuel_ms = int(time.time() * 1000)

        process_info.read_proc_stat(pid)
        uptime_info.read_proc_uptime()

        Liste_CPU.append(calcul_utilisation_cpu(process_info, uptime_info, 100))
        Liste_temps.append(temps_actuel_ms)
        compt += 1

        time.sleep(frequence)

    plot_cpu_usage(Liste_CPU , Liste_temps)


if __name__ == "__main__":
    main()

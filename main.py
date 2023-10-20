# Exemple d'utilisation

from Lecture_Fichier.stat import Stat
from Lecture_Fichier.uptime import Uptime
import time


def calcul_utilisation_cpu(stat, uptime, clock_ticks_per_second):
    process_utime_sec = stat.utime / clock_ticks_per_second
    process_stime_sec = stat.stime / clock_ticks_per_second
    process_start_sec = stat.starttime / clock_ticks_per_second

    system_uptime_sec = uptime.total_time

    process_elapsed_sec = system_uptime_sec - process_start_sec
    process_cpu_usage = 100 * ((process_utime_sec + process_stime_sec) / process_elapsed_sec)

    return process_cpu_usage


def main():
    pid = 21863  # Remplacez par le PID du processus que vous souhaitez inspecter
    process_info = Stat(pid)
    process_info.read_proc_stat(pid)
    process_info.display_info()
    uptime_info = Uptime()
    uptime_info.read_proc_uptime()
    print(f"Utilisation du CPU : {} %")

    Liste_CPU = []
    compt = 0
    while compt < 100:
        current_time = time.localtime()

        # Formattez l'heure comme une chaîne de caractères
        time_str = time.strftime("%H:%M:%S", current_time)

        Liste_CPU.append([calcul_utilisation_cpu(process_info,uptime_info,100),time_str])
        compt += 1
    print(Liste_CPU)



if __name__ == "__main__":
   main()
""" @package CPU
Documentation for CPU module.

More details.
Function for calculating the CPU usage of a process.
"""

import time

from Read_File.PID import Stat as ProcStat
from Read_File.stat import Stat
from Read_File import Uptime
from shared import Result, flags


def calcul_utilisation_cpu(stat, uptime, clock_ticks_per_second):
    """
    Calculate the CPU usage of a process.
    :param stat: Object Stat read from /proc/[pid]/stat
    :param uptime: Object Uptime read from /proc/uptime
    :param clock_ticks_per_second: Number of clock ticks per second
    :return: CPU usage of a process (in %)
    """

    process_utime_sec = stat.utime / clock_ticks_per_second
    process_stime_sec = stat.stime / clock_ticks_per_second
    process_start_sec = stat.starttime / clock_ticks_per_second

    system_uptime_sec = uptime.total_time

    process_elapsed_sec = system_uptime_sec - process_start_sec
    process_cpu_usage = 100 * ((process_utime_sec + process_stime_sec) / process_elapsed_sec)

    return process_cpu_usage


def utilisation_cpu(pid, frequency, interval, result):
    """
    Find the CPU usage of a process in files /proc/[pid]/stat and /proc/uptime.
    :param pid: pid of the process
    :param frequency: point per second wanted
    :param interval: interval of time wanted
    :param result: array for sending the result to the main thread
    :return: status of the function
    """

    process_info = ProcStat(pid)
    uptime_info = Uptime()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_cpu = []
    list_temps = []
    while process_info.read_proc_stat() != -1 and uptime_info.read_proc_uptime() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)
        list_cpu.append(calcul_utilisation_cpu(process_info, uptime_info, 100))
        list_temps.append(now - start)

        time.sleep(frequency / 60)

    result.append(Result("CPU", "Utilisation du cpu (%)", [list_temps, list_cpu]))
    flags.THREAD_CPU_END_FLAG = True
    return 0


def utilisation_cpus(frequency, interval, result):
    """
    Find the CPU usage of a process in files /proc/[pid]/stat and /proc/uptime.
    :param frequency: point per second wanted
    :param interval: interval of time wanted
    :param result: array for sending the result to the main thread
    :return: status of the function
    """

    process_info = Stat()
    uptime_info = Uptime()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_cpu = []
    list_temps = []
    while process_info.read_stat() != -1 and uptime_info.read_proc_uptime() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)
        process_info.cpu_stats.get("cpu").starttime = uptime_info.total_time + uptime_info.idle_time
        list_cpu.append(calcul_utilisation_cpu(process_info.cpu_stats.get("cpu"), uptime_info, 100))
        list_temps.append(now - start)

        time.sleep(frequency / 60)

    result.append(Result("CPU", "Utilisation du cpu (%)", [list_temps, list_cpu]))
    flags.THREAD_CPU_END_FLAG = True
    return 0

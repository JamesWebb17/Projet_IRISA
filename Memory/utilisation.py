""" @package Memory
Documentation for Memory module.

More details.
Function for calculating the Memory usage of a process.
"""

import time

from Read_File.PID import Statm
from Read_File import Uptime
from shared import Result, flags


def utilisation_mem(pid, frequency, interval, result):
    """
    Find the Memory usage of a process in files /proc/[pid]/statm and /proc/uptime.
    :param pid: pid of the process
    :param frequency: frequency of the points
    :param interval: interval of time wanted
    :param result: array for sending the result to the main thread
    :return: status of the function
    """

    process_info = Statm(pid)
    uptime_info = Uptime()

    start = time.clock_gettime(time.CLOCK_REALTIME)
    now = 0

    list_mem = []
    list_temps = []

    while process_info.read_proc_statm() != -1 and uptime_info.read_proc_uptime() != -1 and now - start < interval:
        now = time.clock_gettime(time.CLOCK_REALTIME)

        list_mem.append(process_info.size)
        list_temps.append(now - start)

        time.sleep(frequency / 60)

    result.append(Result("MEM", "Utilisation mémoire (mB)", [list_temps, list_mem]))
    flags.THREAD_MEM_END_FLAG = True
    return 0

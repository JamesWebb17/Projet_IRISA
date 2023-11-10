"""
This is the main file of the project. It is used to launch the program.

More details.

"""

import csv
import threading
from matplotlib import pyplot as plt

import shared
from CPU import utilisation_cpu, utilisation_cpus
from Memory import utilisation_mem
import Arguments
from Power import utilisation_power
from shared import flags
from Read_File.stat import Stat


def main():
    """
    Main function of the program.
    :return: status of the program
    """

    threads = []
    result = []

    args = Arguments.usage()

    if args.verbose:
        flags.VERBOSE_MODE_FLAG = True

    if args.ALL:
        if flags.VERBOSE_MODE_FLAG:
            print("Mode selected is ALL : CPU, MEM, POWER")
        threads.append(threading.Thread(target=utilisation_cpus, args=(args.Frequency, args.Interval, result), name="CPU"))
        #threads.append(threading.Thread(target=utilisation_cpu, args=(args.PID, args.Frequency, args.Interval, result), name="CPU"))
        threads.append(threading.Thread(target=utilisation_mem, args=(args.PID, args.Frequency, args.Interval, result), name="MEM"))
        threads.append(threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result), name="POWER"))

    else:
        if args.CPU:
            if flags.VERBOSE_MODE_FLAG:
                print("Mode selected is CPU")
            threads.append(
                    threading.Thread(target=utilisation_cpu, args=(args.PID, args.Frequency, args.Interval, result), name="CPU"))
        if args.MEM:
            if flags.VERBOSE_MODE_FLAG:
                print("Mode selected is MEM")
            threads.append(
                threading.Thread(target=utilisation_mem, args=(args.PID, args.Frequency, args.Interval, result), name="MEM"))
        if args.POWER:
            if flags.VERBOSE_MODE_FLAG:
                print("Mode selected is POWER")
            threads.append(
                threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result), name="POWER"))

    for t in threads:
        if flags.VERBOSE_MODE_FLAG:
            print(f"Beginning of thread {t.name}")
        t.start()

    for t in threads:
        t.join()
        if flags.VERBOSE_MODE_FLAG:
            print(f"End of thread {t.name}")

    if args.Plot:
        if flags.VERBOSE_MODE_FLAG:
            print("Plotting data...")
        shared.plot_data(result)

    if args.Save:
        if flags.VERBOSE_MODE_FLAG:
            print("Saving data...")
        shared.save_data(args.Save, result)

    return 0


if __name__ == "__main__":
    main()
    stat_info = Stat()
    stat_info.read_stat()

    print("CPU Stats:\n", stat_info)

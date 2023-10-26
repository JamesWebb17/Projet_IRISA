from matplotlib import pyplot as plt

from CPU import utilisation_cpu
from Memoire import utilisation_mem
import Arguments
import shared.config as config

import threading

from shared import locking


def plot_data(data_list, str):
    with locking.lock:
        plt.figure()
        plt.plot(data_list[0], data_list[1])
        plt.xlabel("Temps (s)")
        plt.ylabel(str)
        plt.show()


def main():
    threads = []
    result = []

    args = Arguments.usage()
    pid = args.PID
    frequence = args.Frequence
    nbre_points = args.Nombre

    if args.verbose:
        print("VERBOSE")
        config.activer_mode_verbeux()

    if args.ALL:
        print("ALL")
        threads.append(threading.Thread(target=utilisation_cpu, args=(pid, frequence, nbre_points), name="CPU"))
        threads.append(threading.Thread(target=utilisation_mem, args=(pid, frequence, nbre_points), name="MEM"))

    else:
        if args.CPU:
            print("CPU")
            threads.append(
                threading.Thread(target=utilisation_cpu, args=(pid, frequence, nbre_points, result), name="CPU"))
        if args.MEM:
            print("MEM")
            threads.append(
                threading.Thread(target=utilisation_mem, args=(pid, frequence, nbre_points, result), name="MEM"))

    for t in threads:
        print(f"Début du thread {t.name}")
        t.start()

    for t in threads:
        t.join()

    print(result)

    plot_data(result[0], "Utilisation du cpu (%)")
    plot_data(result[1], "Utilisation de la mémoire (%)")


if __name__ == "__main__":
    main()

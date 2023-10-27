import csv

from matplotlib import pyplot as plt

from CPU import utilisation_cpu
from Memoire import utilisation_mem
import Arguments
import shared.config as config

import threading

from Power import utilisation_power
from shared import Result


def plot_data(data_list: [Result]):
    for i, data in enumerate(data_list):
        plt.figure()
        plt.plot(data.data[0], data.data[1])
        plt.xlabel("Temps (s)")
        plt.ylabel(data.message)
        plt.title(data.name)
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
        threads.append(threading.Thread(target=utilisation_power, args=(frequence, nbre_points, result), name="POWER"))

    else:
        if args.CPU:
            print("CPU")
            threads.append(
                threading.Thread(target=utilisation_cpu, args=(pid, frequence, nbre_points, result), name="CPU"))
        if args.MEM:
            print("MEM")
            threads.append(
                threading.Thread(target=utilisation_mem, args=(pid, frequence, nbre_points, result), name="MEM"))
        if args.POWER:
            print("POWER")
            threads.append(
                threading.Thread(target=utilisation_power, args=(frequence, nbre_points, result), name="POWER"))

    for t in threads:
        print(f"Début du thread {t.name}")
        t.start()

    for t in threads:
        t.join()

    if args.Plot:
        plot_data(result)

    if args.Save:
        save_data(args.Save, result)


def save_data(file_name, data: [Result]):
    with open(file_name, mode='w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)

        # Écrivez la première ligne avec les en-têtes des colonnes
        writer.writerow(data[k].name for k in range(0, len(data)))

        # Écrivez les données ligne par ligne
        for t, c, m in zip(data[0][0], data[0][1], data[1][1]):
            print(t, c, m)
            writer.writerow([t, c, m])


if __name__ == "__main__":
    main()

"""
This is the main file of the project. It is used to launch the program.

More details.

"""

import csv
import threading
from matplotlib import pyplot as plt

from CPU import utilisation_cpu
from Memory import utilisation_mem
import Arguments
import shared.config as config
from Power import utilisation_power
from shared import Result


def plot_data(data_list: [Result]):
    """
    Plot the data in the data_list.
    :param data_list: list of data to plot
    :return:
    """

    for i, data in enumerate(data_list):
        plt.figure()
        plt.plot(data.data[0], data.data[1])
        plt.xlabel("Temps (s)")
        plt.ylabel(data.message)
        plt.title(data.name)
    plt.show()


def main():
    """
    Main function of the program.
    :return: status of the program
    """

    threads = []
    result = []

    args = Arguments.usage()

    if args.verbose:
        print("VERBOSE")
        config.activer_mode_verbeux()

    if args.ALL:
        print("ALL")
        threads.append(threading.Thread(target=utilisation_cpu, args=(args.PID, args.Frequency, args.Interval, result), name="CPU"))
        threads.append(threading.Thread(target=utilisation_mem, args=(args.PID, args.Frequency, args.Interval, result), name="MEM"))
        threads.append(threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result), name="POWER"))

    else:
        if args.CPU:
            print("CPU")
            threads.append(
                    threading.Thread(target=utilisation_cpu, args=(args.PID, args.Frequency, args.Interval, result), name="CPU"))
        if args.MEM:
            print("MEM")
            threads.append(
                threading.Thread(target=utilisation_mem, args=(args.PID, args.Frequency, args.Interval, result), name="MEM"))
        if args.POWER:
            print("POWER")
            threads.append(
                threading.Thread(target=utilisation_power, args=(args.Frequency, args.Interval, result), name="POWER"))

    for t in threads:
        print(f"Début du thread {t.name}")
        t.start()

    for t in threads:
        t.join()

    if args.Plot:
        plot_data(result)

    if args.Save:
        save_data(args.Save, result)

    return 0


def save_data(file_name, data: [Result]):
    """
    Save the data in a csv file.
    :param file_name: name of the file
    :param data: data to save
    :return: status of the function
    """

    for result in data:
        full_csv_file_name = file_name + "_" + result.name + ".csv"
        with open(full_csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Écriture de l'en-tête
            csv_writer.writerow(["Name", "Message", "Temp", "Data"])
            for temp, data in zip(result.data[0], result.data[1]):
                csv_writer.writerow([result.name, result.message, temp, data])

        print(f"Les données de " + result.name + " ont été écrites dans {full_csv_file_name}.")


if __name__ == "__main__":
    main()

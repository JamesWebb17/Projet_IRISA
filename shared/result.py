""" @package shared
Documentation for result module.

More details.
Class for storing the result of a thread.
"""
import csv

from matplotlib import pyplot as plt


class Result:
    def __init__(self, name, message, data):
        """
        The constructor for Result class.
        :param name: name of the result
        :param message: message to print on the graph
        :param data: data of the result
        """

        self.name = name
        self.message = message
        self.data = data

    def plot_data(self):
        """
        Plot the data in result.
        :return: status of the function
        """

        for data in self.data:
            plt.figure()
            plt.plot(data.data[0], data.data[1])
            plt.xlabel("Temps (s)")
            plt.ylabel(self.message)
            plt.title(self.name)
        plt.show()
        return 0

    def save_data(self, file_name):
        """
        Save the data in a csv file.
        :param file_name: name of the file
        :return: status of the function
        """

        full_csv_file_name = file_name + "_" + self.name + ".csv"
        with open(full_csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Écriture de l'en-tête
            csv_writer.writerow(["Name", "Message", "Temp", "Data"])
            for temp, data in zip(self.data[0], self.data[1]):
                csv_writer.writerow([self.name, self.message, temp, data])

        print(f"Les données de {self.name} ont été écrites dans {full_csv_file_name}.")


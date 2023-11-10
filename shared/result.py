""" @package shared
Documentation for result module.

More details.
Class for storing the result of a thread.
"""


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

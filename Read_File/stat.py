""" @package read_file
This file contains the Stat class which is used to read the /proc/stat file
"""


class CPU:
    def __init__(self, system, user, nice, idle):
        self.system = system
        self.user = user
        self.nice = nice
        self.idle = idle

    def __str__(self):
        return (
            f"Time spend in system: {self.system}\n"
            f"Time spend in user: {self.user}\n"
            f"Time spend in nice: {self.nice}\n"
            f"Time spend in idle: {self.idle}\n"
        )


class Stat:
    def __init__(self):
        self.cpu_stats = {}
        self.intr = 0
        self.context_switches = 0
        self.boot_time = 0
        self.processes_created = 0
        self.running_processes = 0
        self.blocked_processes = 0

    def read_stat(self):
        with open('/proc/stat', 'r') as stat_file:
            for line in stat_file:
                parts = line.split()
                if 'cpu' in parts[0]:
                    self.cpu_stats[str(parts[0])] = CPU(int(parts[1]), parts[2], parts[3], parts[4:])
                elif parts[0] == 'intr':
                    self.intr = str(parts[1:])
                elif parts[0] == 'ctxt':
                    self.context_switches = int(parts[1])
                elif parts[0] == 'btime':
                    self.boot_time = int(parts[1])
                elif parts[0] == 'processes':
                    self.processes_created = int(parts[1])
                elif parts[0] == 'procs_running':
                    self.running_processes = int(parts[1])
                elif parts[0] == 'procs_blocked':
                    self.blocked_processes = int(parts[1])

    def __str__(self):
        result_str = ""
        for key, value in self.cpu_stats.items():
            result_str += f"{key}: {value}\n"
        return result_str.strip()


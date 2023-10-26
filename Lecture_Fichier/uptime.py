class Uptime:
    def __init__(self):
        self.total_time = 0
        self.idle_time = 0

    def read_proc_uptime(self):
        #with open('/proc/uptime') as f:
        with open('./Files/uptime') as f:
            data = f.read().split()
            self.total_time = float(data[0])
            self.idle_time = float(data[1])

    def display_info(self):
        print(f"Temps total : {self.total_time}")
        print(f"Temps d'inactivité : {self.idle_time}")

class Hwmon:
    def __init__(self):
        self.name = ""
        self.volts = 0
        self.amps = 0

    def __set_name__(self, hwmon_id, file_id):
        file_label = "/sys/class/hwmon/hwmon" + hwmon_id + "/in" + file_id + "_label"
        with open(file_label, "r") as f:
            self.name = str(f.read())

    def read(self, hwmon_id, file_id):
        file_in = "/sys/class/hwmon/hwmon" + hwmon_id + "/in" + file_id + "_input"
        file_curr = "/sys/class/hwmon/hwmon" + hwmon_id + "/curr" + file_id + "_input"

        with open(file_in, "r") as f:
            self.amps = float(f"{int(f.read()) / 1000:,.3f}")
            #self.amps = int(f.read())

        with open(file_curr, "r") as f:
            #self.volts = float(f"{int(f.read()) / 100:,.2f}")
            self.volts = int(f.read())


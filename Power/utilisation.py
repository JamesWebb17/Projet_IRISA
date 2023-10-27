import time

from Lecture_Fichier import Uptime, Hwmon
from shared import Result


def utilisation_power(frequence, nbre_points, result):
    vdd_gpu_soc = Hwmon()
    vdd_gpu_soc.__set_name__("3", "1")
    vdd_cpu_cv = Hwmon()
    vdd_cpu_cv.__set_name__("3", "2")
    vin_sys_5_v0 = Hwmon()
    vin_sys_5_v0.__set_name__("3", "3")
    vddq_vdd2_1_v8_ao = Hwmon()
    vddq_vdd2_1_v8_ao.__set_name__("4", "2")

    uptime_info = Uptime()

    temps_debut = int(time.time())

    list_power_vdd_gpu_soc = []
    list_power_vdd_cpu_cv = []
    list_power_vin_sys_5_v0 = []
    list_power_vddq_vdd2_1_v8_ao = []

    list_temps = []

    compt = 0
    while compt < nbre_points:
        temps_actuel_ms = int(time.time())

        vdd_gpu_soc.read("3", "1")
        vdd_cpu_cv.read("3", "2")
        vin_sys_5_v0.read("3", "3")
        vddq_vdd2_1_v8_ao.read("4", "2")

        uptime_info.read_proc_uptime()

        list_power_vdd_gpu_soc.append(vdd_gpu_soc.amps * vdd_gpu_soc.volts)
        list_power_vdd_cpu_cv.append(vdd_cpu_cv.amps * vdd_cpu_cv.volts)
        list_power_vin_sys_5_v0.append(vin_sys_5_v0.amps * vin_sys_5_v0.volts)
        list_power_vddq_vdd2_1_v8_ao.append(vddq_vdd2_1_v8_ao.amps * vddq_vdd2_1_v8_ao.volts)

        list_temps.append(temps_actuel_ms - temps_debut)
        compt += 1

        time.sleep(frequence)

    result.append(Result("POWER_"+vdd_gpu_soc.name, "Consomation énergétique (mW)", [list_temps, list_power_vdd_gpu_soc]))
    result.append(Result("POWER_"+vdd_cpu_cv.name, "Consomation énergétique (mW)", [list_temps, list_power_vdd_cpu_cv]))
    result.append(Result("POWER_"+vin_sys_5_v0.name, "Consomation énergétique (mW)", [list_temps, list_power_vin_sys_5_v0]))
    result.append(Result("POWER_"+vddq_vdd2_1_v8_ao.name, "Consomation énergétique (mW)", [list_temps, list_power_vddq_vdd2_1_v8_ao]))
    # store_mem_usage(list_mem, list_temps,pid)

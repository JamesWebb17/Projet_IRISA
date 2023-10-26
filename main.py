from CPU import utilisation_cpu
from Memoire import utilisation_mem
import Arguments

import threading


def main():
    threads = []

    args = Arguments.usage()
    pid = args.PID
    frequence = args.Frequence
    nbre_points = args.Nombre

    if args.ALL:
        print("ALL")
        threads.append(threading.Thread(target=utilisation_cpu, args=(pid, frequence,nbre_points), name="CPU"))
        threads.append(threading.Thread(target=utilisation_mem, args=(pid, frequence,nbre_points), name="MEM"))

    else:
        if args.CPU:
            print("CPU")
            threads.append(threading.Thread(target=utilisation_cpu, args=(pid, frequence,nbre_points), name="CPU"))
        if args.MEM:
            print("MEM")
            threads.append(threading.Thread(target=utilisation_mem, args=(pid, frequence,nbre_points), name="MEM"))

    for t in threads:
        print(f"Début du thread {t.name}")
        t.start()

    for t in threads:
        t.join()





if __name__ == "__main__":
    main()

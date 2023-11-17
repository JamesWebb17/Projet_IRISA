import psutil
import time

def calculate_cpu_usage(core):
    # Utilisation du CPU pour le cœur spécifié depuis le dernier appel
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)[core]
    return cpu_percent

def main():
    target_core = 0  # Remplacez cela par le numéro du cœur que vous souhaitez surveiller

    while True:
        cpu_usage = calculate_cpu_usage(target_core)
        print(f'CPU Usage (Core {target_core}): {cpu_usage}%')
        time.sleep(1)

if __name__ == "__main__":
    main()

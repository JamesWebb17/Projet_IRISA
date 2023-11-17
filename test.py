import psutil
import time

def calculate_cpu_usage():
    # Utilisation du CPU depuis le dernier appel
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def main():
    while True:
        cpu_usage = calculate_cpu_usage()
        print(f'CPU Usage: {cpu_usage}%')
        time.sleep(1)

if __name__ == "__main__":
    main()

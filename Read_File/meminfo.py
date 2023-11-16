class MemInfo:
    def __init__(self):
        self.mem_info = {}

    def read_mem_info(self, file_path='/proc/meminfo'):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split(':')
                    self.mem_info[key.strip()] = int(value.split()[0])
        except FileNotFoundError:
            print(f"Le fichier {file_path} n'a pas été trouvé.")


def main():
    # Exemple d'utilisation
    mem_info = MemInfo()
    mem_info.read_meminfo()

    # Accéder aux informations
    print(f"Total Memory: {mem_info.mem_total} kB")
    print(f"Free Memory: {mem_info.mem_free} kB")
    print(f"Available Memory: {mem_info.mem_available} kB")
    # ... et ainsi de suite pour d'autres informations

if __name__ == "__main__":
    main()
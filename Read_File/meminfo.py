class MemInfo:
    def __init__(self):
        self.mem_total = 0
        self.mem_free = 0
        self.mem_available = 0
        self.buffers = 0
        self.cached = 0
        self.swap_cached = 0
        self.active = 0
        self.inactive = 0
        self.active_anon = 0
        self.inactive_anon = 0
        self.active_file = 0
        self.inactive_file = 0
        self.unevictable = 0
        self.mlocked = 0
        self.swap_total = 0
        self.swap_free = 0
        self.dirty = 0
        self.writeback = 0
        self.anonPages = 0
        self.mapped = 0
        self.shmem = 0
        self.slab = 0
        self.sreclaimable = 0
        self.sunreclaim = 0
        self.kernelstack = 0
        self.pagetables = 0
        self.nfs_unstable = 0
        self.bounce = 0
        self.writebacktmp = 0
        self.commitlimit = 0
        self.committed_as = 0
        self.vmaltotal = 0
        self.vmallocused = 0
        self.vmallocchunk = 0
        self.percpu = 0
        self.hardwarecorrupted = 0
        self.anonhugepages = 0
        self.shmemhugepages = 0
        self.shmempmdmapped = 0
        self.filehugepages = 0
        self.filepmdmapped = 0
        self.cmatotal = 0
        self.cmafree = 0
        self.hugepages_total = 0
        self.hugepages_free = 0
        self.hugepages_rsvd = 0
        self.hugepages_surp = 0
        self.hugetpagesize = 0
        self.hugetlb = 0

    def read_meminfo(self):
        try:
            with open('/proc/meminfo') as f:
                for line in f:
                    key, value = line.split(':', 1)
                    setattr(self, key.strip().lower(), int(value.split()[0]))
        except FileNotFoundError:
            print("Le fichier /proc/meminfo n'existe pas.")


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
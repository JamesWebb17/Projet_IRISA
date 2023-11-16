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
                    if key == 'MemTotal':
                        self.mem_total = int(value.split()[0])
                    elif key == 'MemFree':
                        self.mem_free = int(value.split()[0])
                    elif key == 'MemAvailable':
                        self.mem_available = int(value.split()[0])
                    elif key == 'Buffers':
                        self.buffers = int(value.split()[0])
                    elif key == 'Cached':
                        self.cached = int(value.split()[0])
                    elif key == 'SwapCached':
                        self.swap_cached = int(value.split()[0])
                    elif key == 'Active':
                        self.active = int(value.split()[0])
                    elif key == 'Inactive':
                        self.inactive = int(value.split()[0])
                    elif key == 'Active(anon)':
                        self.active_anon = int(value.split()[0])
                    elif key == 'Inactive(anon)':
                        self.inactive_anon = int(value.split()[0])
                    elif key == 'Active(file)':
                        self.active_file = int(value.split()[0])
                    elif key == 'Inactive(file)':
                        self.inactive_file = int(value.split()[0])
                    elif key == 'Unevictable':
                        self.unevictable = int(value.split()[0])
                    elif key == 'Mlocked':
                        self.mlocked = int(value.split()[0])
                    elif key == 'SwapTotal':
                        self.swap_total = int(value.split()[0])
                    elif key == 'SwapFree':
                        self.swap_free = int(value.split()[0])
                    elif key == 'Dirty':
                        self.dirty = int(value.split()[0])
                    elif key == 'Writeback':
                        self.writeback = int(value.split()[0])
                    elif key == 'AnonPages':
                        self.anonPages = int(value.split()[0])
                    elif key == 'Mapped':
                        self.mapped = int(value.split()[0])
                    elif key == 'Shmem':
                        self.shmem = int(value.split()[0])
                    elif key == 'Slab':
                        self.slab = int(value.split()[0])
                    elif key == 'SReclaimable':
                        self.sreclaimable = int(value.split()[0])
                    elif key == 'SUnreclaim':
                        self.sunreclaim = int(value.split()[0])
                    elif key == 'KernelStack':
                        self.kernelstack = int(value.split()[0])
                    elif key == 'PageTables':
                        self.pagetables = int(value.split()[0])
                    elif key == 'NFS_Unstable':
                        self.nfs_unstable = int(value.split()[0])
                    elif key == 'Bounce':
                        self.bounce = int(value.split()[0])
                    elif key == 'WritebackTmp':
                        self.writebacktmp = int(value.split()[0])
                    elif key == 'CommitLimit':
                        self.commitlimit = int(value.split()[0])
                    elif key == 'Committed_AS':
                        self.committed_as = int(value.split()[0])
                    elif key == 'VmallocTotal':
                        self.vmaltotal = int(value.split()[0])
                    elif key == 'VmallocUsed':
                        self.vmallocused = int(value.split()[0])
                    elif key == 'VmallocChunk':
                        self.vmallocchunk = int(value.split()[0])
                    elif key == 'Percpu':
                        self.percpu = int(value.split()[0])
                    elif key == 'HardwareCorrupted':
                        self.hardwarecorrupted = int(value.split()[0])
                    elif key == 'AnonHugePages':
                        self.anonhugepages = int(value.split()[0])
                    elif key == 'ShmemHugePages':
                        self.shmemhugepages = int(value.split()[0])
                    elif key == 'ShmemPmdMapped':
                        self.shmempmdmapped = int(value.split()[0])
                    elif key == 'FileHugePages':
                        self.filehugepages = int(value.split()[0])
                    elif key == 'FilePmdMapped':
                        self.filepmdmapped = int(value.split()[0])
                    elif key == 'CmaTotal':
                        self.cmatotal = int(value.split()[0])
                    elif key == 'CmaFree':
                        self.cmafree = int(value.split()[0])
                    elif key == 'HugePages_Total':
                        self.hugepages_total = int(value.split()[0])
                    elif key == 'HugePages_Free':
                        self.hugepages_free = int(value.split()[0])
                    elif key == 'HugePages_Rsvd':
                        self.hugepages_rsvd = int(value.split()[0])
                    elif key == 'HugePages_Surp':
                        self.hugepages_surp = int(value.split()[0])
                    elif key == 'Hugepagesize':
                        self.hugetpagesize = int(value.split()[0])
                    elif key == 'Hugetlb':
                        self.hugetlb = int(value.split()[0])
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
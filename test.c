#include <stdio.h>
#include <stdlib.h>

int main() {
    pid_t pid = 11338; // Remplacez 1234 par le PID du processus que vous souhaitez surveiller
    char proc_path[256];
    snprintf(proc_path, sizeof(proc_path), "/proc/%d/stat", pid);

    FILE *file = fopen(proc_path, "r");
    if (file == NULL) {
        perror("Erreur lors de l'ouverture du fichier /proc");
        return 1;
    }

    unsigned long utime, stime, vsize, rss;
    if (fscanf(file, "%*d %*s %*c %*d %*d %*d %*d %*d %*u %*u %*u %*u %*u %*u %lu %lu %*ld %*ld %*ld %*ld %*ld %*ld %lu %lu",
               &utime, &stime, &vsize, &rss) != 4) {
        perror("Erreur lors de la lecture des statistiques du processus");
        fclose(file);
        return 1;
    }

    fclose(file);

    // Utilisation CPU en millisecondes
    printf("CPU user time: %lu ms\n", utime);
    printf("CPU system time: %lu ms\n", stime);

    // Utilisation mémoire en kilo-octets
    printf("Taille de la mémoire virtuelle: %lu KB\n", vsize);
    printf("Taille de la mémoire résidente: %lu KB\n", rss);

    return 0;
}

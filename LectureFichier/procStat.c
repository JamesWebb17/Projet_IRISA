//
// Created by Faucher Simon on 12/10/2023.
//

#include "procStat.h"

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

/**
 * Récupère les informations du fichier /proc/stat
 * @param Procstat
 * @return 0 si tout s'est bien passé, 1 sinon
 */
int rempliproStat( struct procStat * Procstat) {

    char path[256];
    snprintf(path, sizeof(path), "/proc/stat");

    int fd = openat(AT_FDCWD, "/proc/stat", O_RDONLY);
    if (fd == -1) {
        perror("openat");
        return 1;
    }

    char buffer[1024];
    ssize_t bytesRead = read(fd, buffer, sizeof(buffer) - 1);
    if (bytesRead == -1) {
        perror("read");
        close(fd);
        return 1;
    }
    buffer[bytesRead] = '\0'; // Null-terminate the string

    //printf("Contents of /proc/stat:\n%s\n", buffer);

    char *p = strtok(buffer, " ");
    int i = 0;
    int cpuCount = 0;
    while (p != NULL) {
        printf("p : %s\n", p);
        switch (i) {
            case 0:
                Procstat->cpu[cpuCount]->name = p;
                break;
            case 1:
                Procstat->cpu[cpuCount]->user_time = atoi(p);
                break;
            case 2:
                Procstat->cpu[cpuCount]->nice_time = atoi(p);
                break;
            case 3:
                Procstat->cpu[cpuCount]->system_time = atoi(p);
                break;
            case 4:
                Procstat->cpu[cpuCount]->idle_time = atoi(p);
                break;
            case 5:
                Procstat->cpu[cpuCount]->iowait_time = atoi(p);
                break;
            case 6:
                Procstat->cpu[cpuCount]->irq_time = atoi(p);
                break;
            case 7:
                Procstat->cpu[cpuCount]->softirq_time = atoi(p);
                break;
            case 8:
                Procstat->cpu[cpuCount]->steal_time = atoi(p);
                break;
            case 9:
                Procstat->cpu[cpuCount]->guest_time = atoi(p);
                break;
            case 10:
                Procstat->cpu[cpuCount]->guest_nice_time = atoi(p);
                break;
        }
        i++;
        p = strtok(NULL, " ");
    }
    close(fd);
    return 0;
}

/**
 * Affiche le contenu de la structure procStat
 * @param Procstat
 * @return 0 si tout s'est bien passé, 1 sinon
 */
 int printProcStat(struct procStat * Procstat) {

     for (int i = 0 ; i < Procstat->cpuCount ; i++) {

         printf("name : %s\n", Procstat->cpu[i]->name);
         printf("user_time : %d\n", Procstat->cpu[i]->user_time);
         printf("nice_time : %d\n", Procstat->cpu[i]->nice_time);
         printf("system_time : %d\n", Procstat->cpu[i]->system_time);
         printf("idle_time : %d\n", Procstat->cpu[i]->idle_time);
         printf("iowait_time : %d\n", Procstat->cpu[i]->iowait_time);
         printf("irq_time : %d\n", Procstat->cpu[i]->irq_time);
         printf("softirq_time : %d\n", Procstat->cpu[i]->softirq_time);
         printf("steal_time : %d\n", Procstat->cpu[i]->steal_time);
         printf("guest_time : %d\n", Procstat->cpu[i]->guest_time);
         printf("guest_nice_time : %d\n", Procstat->cpu[i]->guest_nice_time);
         printf("\n");
     }
}

void initProcStat(struct procStat * Procstat, int cpuCount) {
    Procstat->cpu = malloc(sizeof(struct procStatCpu*)*cpuCount);
    for (int i = 0 ; i < cpuCount ; i++) {
        Procstat->cpu[i] = malloc(sizeof(struct procStatCpu));
    }
    Procstat->cpuCount = cpuCount;
}

void main() {
    struct procStat Procstat;
    Procstat.cpu = malloc(sizeof(struct procStatCpu*)*12);
    initProcStat(&Procstat, 12);

    rempliproStat(&Procstat);
    printProcStat(&Procstat);
}





int procStat(struct procStat * Procstat) {

    char path[256];
    snprintf(path, sizeof(path), "/proc/stat");

    int fd = openat(AT_FDCWD, path, O_RDONLY);
    if (fd == -1) {
        perror("openat");
        return 1;
    }

    char buffer[1024];
    ssize_t bytesRead = read(fd, buffer, sizeof(buffer) - 1);
    if (bytesRead == -1) {
        perror("read");
        close(fd);
        return 1;
    }
    buffer[bytesRead] = '\0'; // Null-terminate the string

    printf("Contents of /proc/stat:\n%s\n", buffer);

}

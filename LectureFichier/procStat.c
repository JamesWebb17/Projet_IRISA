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
    while (p != NULL) {
        printf("p : %s\n", p);
        switch (i) {
            case 0:
                Procstat->cpu->name = p;
                break;
            case 1:
                Procstat->cpu->user_time = atoi(p);
                break;
            case 2:
                Procstat->cpu->nice_time = atoi(p);
                break;
            case 3:
                Procstat->cpu->system_time = atoi(p);
                break;
            case 4:
                Procstat->cpu->idle_time = atoi(p);
                break;
            case 5:
                Procstat->cpu->iowait_time = atoi(p);
                break;
            case 6:
                Procstat->cpu->irq_time = atoi(p);
                break;
            case 7:
                Procstat->cpu->softirq_time = atoi(p);
                break;
            case 8:
                Procstat->cpu->steal_time = atoi(p);
                break;
            case 9:
                Procstat->cpu->guest_time = atoi(p);
                break;
            case 10:
                Procstat->cpu->guest_nice_time = atoi(p);
                break;
        }
        i++;
        p = strtok(NULL, " ");
    }
    close(fd);
    return 0;
}

void main() {
    struct procStat Procstat;
    rempliproStat(&Procstat);
}

/**
 * Affiche le contenu du fichier /proc/stat
 * @param Procstat
 * @return 0 si tout s'est bien passé, 1 sinon
 */





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

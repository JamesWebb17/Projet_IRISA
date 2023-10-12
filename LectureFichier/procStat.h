//
// Created by Faucher Simon on 12/10/2023.
//

#ifndef PROJET_IRISA_PROCSTAT_H
#define PROJET_IRISA_PROCSTAT_H

#include "procStatCpu.h"

struct procStat {
    struct procStatCpu * cpu ;   // Liste des CPU avec leur informations, 0 étant le total
    int cpuCount ;        // Nombre de CPU
    int * intr ;          // Nombre d'interruptions par type
    int contextSwitches ; // Nombre de changement de contexte
    int btime ;           // Temps en secondes depuis le démarrage du système
    int processes ;       // Nombre de processus créés depuis le démarrage du système
    int procsRunning ;    // Nombre de processus en cours d'exécution
    int procsBlocked ;    // Nombre de processus bloqués
    int * softirq ;       // Nombre d'interruptions logicielles par type
} ;

/**
 * Récupère les informations du fichier /proc/stat
 * @param Procstat
 * @return 0 si tout s'est bien passé, 1 sinon
 */
int rempliproStat( struct procStat * Procstat);

/**
 * Affiche le contenu de la structure procStat
 * @param Procstat
 * @return 0 si tout s'est bien passé, 1 sinon
 */
int printProcStat(struct procStat * Procstat);



#endif //PROJET_IRISA_PROCSTAT_H

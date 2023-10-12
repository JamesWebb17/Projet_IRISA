//
// Created by Faucher Simon on 12/10/2023.
//

#ifndef PROJET_IRISA_PROCSTATCPU_H
#define PROJET_IRISA_PROCSTATCPU_H

struct procStatCpu {
    char  *name;            // Nom du CPU
    int user_time;          // Temps passé en mode utilisateur
    int nice_time;          // Temps passé en mode utilisateur avec priorité faible
    int system_time;        // Temps passé en mode système
    int idle_time;          // Temps passé en mode inactif
    int iowait_time;        // Temps passé en attente d'IO
    int irq_time;           // Temps passé en mode interruption
    int softirq_time;       // Temps passé en mode interruption logiciel
    int steal_time;         // Temps volé
    int guest_time;         // Temps passé en mode utilisateur dans une machine virtuelle
    int guest_nice_time;    // Temps passé en mode utilisateur avec priorité faible dans une machine virtuelle
} procStatCpu ;


#endif //PROJET_IRISA_PROCSTATCPU_H

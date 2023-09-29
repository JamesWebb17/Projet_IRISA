//
// Created by Faucher Simon on 28/09/2023.
//
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "AllocationMemoireHard.h"

void AllocationMemoire () {
    long long int *ptr;
    int i = 0;

    ptr = (long long int *)malloc(1048576); // Allouer 1 Mo (1024 * 1024 octets) de mémoire

    if (ptr == NULL) {
        perror("Erreur d'allocation de mémoire");
    }

    for (i = 0; i < 1024 * 128; i++) {
        ptr[i] = 0; // Accéder à chaque page mémoire pour s'assurer qu'elle est vraiment allouée
    }

    printf("1 Mo de mémoire allouée.\n");

    usleep(500000); // Attendre 0,5 seconde (500 000 microsecondes)

}


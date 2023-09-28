//
// Created by Faucher Simon on 28/09/2023.
//
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    long long int *ptr;
    int i = 0;
    int compt = 1 ;

    printf("mon PID est %d\n", getpid());

    while (compt < 1000) {
        ptr = (long long int *)malloc(1048576); // Allouer 1 Mo (1024 * 1024 octets) de mémoire

        if (ptr == NULL) {
            perror("Erreur d'allocation de mémoire");
            break;
        }

        for (i = 0; i < 1024 * 128; i++) {
            ptr[i] = 0; // Accéder à chaque page mémoire pour s'assurer qu'elle est vraiment allouée
        }

        printf("1 Mo de mémoire allouée. %d\n" , compt);

        usleep(500000); // Attendre 0,5 seconde (500 000 microsecondes)
        compt ++ ;
    }

    return 0;
}


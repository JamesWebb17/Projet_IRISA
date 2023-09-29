//
// Created by Faucher Simon on 28/09/2023.
//
#include "ConsomationCPU.h"

void ConsomationCPU () {
    // Effectuez une opération de calcul intensive (par exemple, une multiplication)
    // pour utiliser le CPU.
    // Vous pouvez augmenter le nombre d'itérations pour consommer plus de CPU.
    int nb = 100000000000;
    int result = 0;

    for (int i = 0; i < nb ; i++) {
        result = i * 2;
    }
    //printf("Résultat de la consommation CPU : %d\n", result);
}


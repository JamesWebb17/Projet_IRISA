//
// Created by Faucher Simon on 28/09/2023.
//
#include <stdio.h>
#include <unistd.h>
#include "./allocationMemoire/AllocationMemoireHard.h"
#include "./consomationCPU/ConsomationCPU.h"

int main() {

    int compt = 1 ;

    printf("Mon PID est : %d\n", getpid());

    while (compt < 1000) {
        AllocationMemoire();
        ConsomationCPU();
        printf("Nombre de fois que le programme a été exécuté : %d\n", compt);
        compt++;
    }
}
cmake_minimum_required(VERSION 3.26)
project(Projet_IRISA C)

set(CMAKE_C_STANDARD 11)

add_executable(Projet_IRISA
        allocationMemoire/AllocationMemoireHard.c
        consomationCPU/ConsomationCPU.c
        main.c)

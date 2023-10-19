#!/bin/bash


# Ddurée du compte à rebours en milisecondes     
frequence=100 #en ms

sudo echo "c"

#sudo tegrastats --readall --logfile ./tegrastat_Data/tegrastat.txt --interval $frequence 

#pcregrep -o '\[\K.*?\]' ./tegrastat.txt > tegrastat_CpuData.txt 

pcregrep -o '(?<=\[)[^\]]+(?=\])' ./tegrastat.txt > ./tegrastat_Data/tegrastat_CpuData.txt 

pcregrep -o1 'EMC_FREQ (\d+%@\d+)' ./tegrastat.txt > ./tegrastat_Data/tegrastat_MemData.txt

pcregrep -o 'VDD_GPU_SOC \K\d+mW/\d+mW' ./tegrastat.txt | sed 's/mW\//;/g; s/mW//g' > ./tegrastat_Data/tegrastat_VDD_GPU_SOC.txt 

pcregrep -o 'VDD_CPU_CV \K\d+mW/\d+mW' ./tegrastat.txt | sed 's/mW\//;/g; s/mW//g' > ./tegrastat_Data/tegrastat_VDD_CPU_CV.txt 

pcregrep -o 'VIN_SYS_5V0 \K\d+mW/\d+mW' ./tegrastat.txt | sed 's/mW\//;/g; s/mW//g' > ./tegrastat_Data/tegrastat_VIN_SYS_5V0.txt 

pcregrep -o 'VDDQ_VDD2_1V8AO \K\d+mW/\d+mW' ./tegrastat.txt | sed 's/mW\//;/g; s/mW//g' > ./tegrastat_Data/tegrastat_VDDQ_VDD2_1V8AO.txt 


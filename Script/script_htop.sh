#!/bin/bash

# Exécute top et redirige la sortie vers un fichier temporaire

# Nom du processus que je souhaite rechercher
process_name="Projet_IRISA"

# Trouve la commande ps pour rechercher le PID du processus

pid=$(ps aux | grep "Projet_IRISA" | head -n 1 | awk '{print $2}')

echo "PID du processus $process_name : $pid"

# Ddurée du compte à rebours en milisecondes
iteration=6000

echo "/Users/simon/CLionProjects/Projet_IRISA/cmake-build-debug/Projet_IRISA"

echo "PID;TIME+;START;ELAPSED;VIRT;RES;MEM%;NCPU%;CPU%;Command" > "./out/file.csv"
#q | htop -C -p "$pid" | aha --line-fix | html2text -width 999 | grep -v "F1Help" | grep -v "xml version="  >  "./out/file.txt"


# Boucle jusqu'à ce que le compte à rebours soit terminé
while [ $iteration -gt 0 ]; do

      # Met à jour le compte à rebours
      iteration=$((iteration - 1))

      echo "Itération restantes : $iteration"

      echo q | htop -C -p "$pid" | aha --line-fix | html2text -width 999 | grep -v "F1Help" | grep -v "xml version="  | tail -n 2 | head -n 1 | awk '{ printf("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n", $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12) }'>> "./out/file.csv"

done

#top -a -s 1 -o power -l 0 -stats  pid,cpu,cpu_me,cpu_others,time,csw,power,mem,purg,vsize,vprvt,kprvt,kshrd, -pid "$pid" > top_data.txt

echo "Données de top exportées vers top_data.txt"

kill $pid

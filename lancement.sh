!/bin/bash

# File to load
file_to_load="production/trainNetwork.jl"

# Fonctions Julia à exécuter
julia_getpid="getpid()"
julia_function_apprentissage="tup = f1_vs_epoch()"

# Ouvrir le premier terminal pour Julia
gnome-terminal --tab --bash "cd ~/Desktop/NOP_DeepLearning; juliadev -t auto -O3; julia -e 'println( getpid() )'" &

# Attendre un court instant pour laisser le premier terminal s'ouvrir
sleep 2

# Récupérer le PID du processus Julia
julia_pid=$(pgrep julia)

# Afficher le PID
echo "PID de Julia : $julia_pid"

# Exécuter la fonction Julia
echo "Exécution de la fonction Julia..."



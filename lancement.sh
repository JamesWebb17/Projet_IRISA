!/bin/bash

# File to load
file_to_load="production/trainNetwork.jl"

# Fonctions Julia à exécuter
julia_getpid="getpid()"
julia_function_apprentissage="tup = f1_vs_epoch()"

# Ouvrir le premier terminal pour Julia
gnome-terminal --tab -- bash -c "cd ~/Desktop/NOP_DeepLearning; juliadev -t auto -O3; julia -e 'println( getpid() )'" &
pid=$!
echo "Le PID du processus Julia est : $pid"


